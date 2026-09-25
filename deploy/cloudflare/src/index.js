import { Container } from "@cloudflare/containers";

/**
 * Durable Object wrapping the Python MCP server container.
 *
 * All configuration the Python server needs is passed as environment
 * variables at container start. Secrets (AJ360_API_KEY, optionally
 * AJ360_REFRESH_TOKEN / AJ360_DASHBOARD_TOKEN) are Worker secrets
 * (`wrangler secret put ...`) forwarded into the container here.
 */
export class AJ360Container extends Container {
  defaultPort = 8080;
  // Keep the instance warm between MCP requests; it sleeps after idle
  // and cold-starts in a few seconds on the next request.
  sleepAfter = "15m";

  constructor(ctx, env) {
    super(ctx, env);
    this.envVars = {
      MCP_TRANSPORT: "streamable-http",
      MCP_PORT: "8080",
      // The standalone dashboard thread is pointless inside the container;
      // the dashboard routes are still served on the main port.
      AJ360_ENABLE_DASHBOARD: "false",
      AJ360_ALLOWED_HOST: env.AJ360_ALLOWED_HOST ?? "",
      AJ360_API_KEY: env.AJ360_API_KEY ?? "",
      AJ360_REFRESH_TOKEN: env.AJ360_REFRESH_TOKEN ?? "",
      AJ360_DASHBOARD_TOKEN: env.AJ360_DASHBOARD_TOKEN ?? "",
      AJ360_ENABLE_SEO_TOOLS: this.seoTools ? "1" : "",
    };
  }

  // Public endpoint: the 10 core discovery tools only.
  get seoTools() { return false; }
}

/**
 * Team endpoint: same server with the 16 SEO/analytics tools enabled.
 * Reached only through /team/<AJ360_TEAM_TOKEN>/mcp, so the heavy tools are
 * not exposed to the public or to directory crawlers.
 */
export class AJ360TeamContainer extends AJ360Container {
  get seoTools() { return true; }
}

// ---------------------------------------------------------------------------
// Usage analytics
//
// The in-container SQLite dashboard resets whenever the container sleeps, so
// usage history never accumulated. The Worker sits in front of every request
// and writes to D1 instead, which persists.
//
// Privacy: no IP addresses and no personal identifiers are stored — only the
// AI client type (self-reported in the MCP handshake), which tool ran, the
// content query, and the coarse country code Cloudflare already provides.
// ---------------------------------------------------------------------------

const MAX_QUERY_LEN = 200;

// Clients driven by a person (AI chat apps, coding assistants). Everything
// else — directory indexers, uptime probes, scanners, scripts — is
// "automated". Unknown new apps land in "automated" until added here, so
// the human numbers stay conservative.
const HUMAN_CLIENTS =
  /claude|opencode|cursor|windsurf|vscode|visual studio code|copilot|chatgpt|openai|gemini|cline|roo-?code|continue|zed|goose|librechat|lm ?studio|msty|raycast|jan\b|warp|kiro|amp\b|perplexity|mistral|le ?chat/i;
const AUTOMATED_HINT = /probe|bot|crawler|indexer|scanner|health|uptime|check|harvest|measure|monitor|watch|meter|index|registry|verif|scraper|collector/i;

/** "human" | "automated" | "team" for one request. */
function classify(ua, clientName, isTeam) {
  if (isTeam) return "team";
  const id = `${clientName || ""} ${ua || ""}`;
  if (AUTOMATED_HINT.test(clientName || "")) return "automated";
  return HUMAN_CLIENTS.test(id) ? "human" : "automated";
}

/** Pick the most descriptive argument of a tool call for the `query` column. */
function summarizeArgs(args) {
  if (!args || typeof args !== "object") return null;
  // View diagnostics reports are capability flags; keep them whole.
  if (args.report) return String(args.report).slice(0, 600);
  for (const key of ["query", "section_id", "sections", "host_name", "genre", "country"]) {
    if (args[key] != null && args[key] !== "") return String(args[key]).slice(0, MAX_QUERY_LEN);
  }
  for (const key of ["video_id", "series_id", "season_id"]) {
    if (args[key] != null) return `${key}=${args[key]}`;
  }
  const first = Object.entries(args)[0];
  return first ? `${first[0]}=${String(first[1]).slice(0, 80)}` : null;
}

/** Turn one JSON-RPC message into a row, or null if it isn't worth logging. */
function toEvent(msg) {
  if (!msg || typeof msg !== "object" || !msg.method) return null;
  const method = msg.method;
  // Notifications are protocol chatter, not usage.
  if (method.startsWith("notifications/")) return null;
  const params = msg.params || {};
  return {
    method,
    tool: method === "tools/call" ? params.name ?? null : null,
    query: method === "tools/call" ? summarizeArgs(params.arguments) : null,
    client_name: params.clientInfo?.name ?? null,
    client_version: params.clientInfo?.version ?? null,
  };
}

async function logEvents(env, request, response, bodyText, isTeam) {
  if (!env.ANALYTICS_DB || !bodyText) return;
  let parsed;
  try {
    parsed = JSON.parse(bodyText);
  } catch {
    return; // not JSON-RPC (SSE resume, GET stream, …)
  }
  const messages = Array.isArray(parsed) ? parsed : [parsed];
  const events = messages.map(toEvent).filter(Boolean);
  if (events.length === 0) return;

  // On `initialize` the session id only exists on the response.
  const sessionId =
    request.headers.get("mcp-session-id") || response.headers.get("mcp-session-id") || null;
  const ts = new Date().toISOString();
  const country = request.cf?.country ?? null;
  const ua = (request.headers.get("user-agent") || "").slice(0, 200) || null;
  const initClient = events.find((e) => e.client_name)?.client_name || null;

  const stmt = env.ANALYTICS_DB.prepare(
    `INSERT INTO events
       (ts, session_id, method, tool, query, client_name, client_version, country, ua, kind)
     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)`
  );
  try {
    await env.ANALYTICS_DB.batch(
      events.map((e) =>
        stmt.bind(
          ts, sessionId, e.method, e.tool, e.query,
          e.client_name, e.client_version, country, ua,
          classify(ua, e.client_name || initClient, isTeam)
        )
      )
    );
  } catch (err) {
    console.error("analytics write failed:", err.message);
  }
}

/**
 * Aggregate report over the last N days. Token-protected.
 * ?kind=human (default) | team | automated | all — which traffic the detail
 * sections cover. The "by_kind" totals always cover everything, so directory
 * crawlers are visible but never mixed into the human numbers.
 */
async function usageReport(env, url) {
  const days = Math.min(Math.max(parseInt(url.searchParams.get("days") || "30", 10) || 30, 1), 365);
  const since = new Date(Date.now() - days * 86400_000).toISOString();
  const kindParam = (url.searchParams.get("kind") || "human").toLowerCase();
  const kinds = kindParam === "all" ? ["human", "team", "automated"]
    : kindParam === "people" ? ["human", "team"] : [kindParam];
  const inKinds = `COALESCE(kind,'automated') IN (${kinds.map(() => "?").join(",")})`;
  const db = env.ANALYTICS_DB;

  // Tool calls carry no clientInfo, so resolve each session's client from its
  // initialize row and join it back onto every event in that session.
  const clientsSql = `
    WITH sess AS (
      SELECT session_id, MAX(client_name) AS client_name, MAX(client_version) AS client_version
      FROM events WHERE client_name IS NOT NULL AND session_id IS NOT NULL
      GROUP BY session_id
    )
    SELECT COALESCE(e.client_name, s.client_name, 'unknown') AS client,
           COALESCE(e.client_version, s.client_version, '')  AS version,
           COUNT(*) AS events,
           COUNT(DISTINCT e.session_id) AS sessions,
           SUM(e.method = 'tools/call') AS tool_calls
    FROM events e LEFT JOIN sess s ON e.session_id = s.session_id
    WHERE e.ts >= ? AND ${inKinds.replace("kind", "e.kind")}
    GROUP BY client, version
    ORDER BY tool_calls DESC, events DESC LIMIT 30`;

  const q = (sql) => db.prepare(sql).bind(since, ...kinds).all();
  const [byKind, totals, clients, tools, queries, countries, daily, sessions, topAutomated] = await Promise.all([
    db.prepare(`SELECT COALESCE(kind,'automated') AS kind, COUNT(*) AS events,
                COUNT(DISTINCT session_id) AS sessions, SUM(method='tools/call') AS tool_calls
                FROM events WHERE ts >= ? GROUP BY 1 ORDER BY events DESC`).bind(since).all(),
    q(`SELECT COUNT(*) AS events, COUNT(DISTINCT session_id) AS sessions,
       SUM(method='tools/call') AS tool_calls FROM events WHERE ts >= ? AND ${inKinds}`),
    q(clientsSql),
    q(`SELECT tool, COUNT(*) AS calls FROM events WHERE ts >= ? AND ${inKinds} AND tool IS NOT NULL
       GROUP BY tool ORDER BY calls DESC LIMIT 30`),
    q(`SELECT query, tool, COUNT(*) AS n FROM events WHERE ts >= ? AND ${inKinds} AND query IS NOT NULL
       AND tool != 'run_diagnostics' GROUP BY query, tool ORDER BY n DESC LIMIT 30`),
    q(`SELECT COALESCE(country,'??') AS country, COUNT(*) AS events FROM events WHERE ts >= ? AND ${inKinds}
       GROUP BY country ORDER BY events DESC LIMIT 20`),
    q(`SELECT substr(ts,1,10) AS day, COUNT(*) AS events, COUNT(DISTINCT session_id) AS sessions,
       SUM(method='tools/call') AS tool_calls
       FROM events WHERE ts >= ? AND ${inKinds} GROUP BY day ORDER BY day DESC LIMIT 60`),
    q(`SELECT session_id, MIN(ts) AS started, COUNT(*) AS events, SUM(method='tools/call') AS tool_calls,
       MAX(client_name) AS client
       FROM events WHERE ts >= ? AND ${inKinds} AND session_id IS NOT NULL
       GROUP BY session_id ORDER BY started DESC LIMIT 25`),
    db.prepare(`SELECT COALESCE(client_name, substr(ua,1,40), 'unknown') AS agent, COUNT(*) AS events,
                SUM(method='tools/call') AS tool_calls
                FROM events WHERE ts >= ? AND COALESCE(kind,'automated') = 'automated'
                GROUP BY agent ORDER BY events DESC LIMIT 15`).bind(since).all(),
  ]);

  return {
    period_days: days,
    since,
    kind: kindParam,
    by_kind: byKind.results ?? [],
    totals: totals.results?.[0] ?? {},
    clients: clients.results ?? [],
    tools: tools.results ?? [],
    top_queries: queries.results ?? [],
    countries: countries.results ?? [],
    daily: daily.results ?? [],
    recent_sessions: sessions.results ?? [],
    top_automated_agents: topAutomated.results ?? [],
    notes: [
      "kind: human = people using AI apps (Claude, ChatGPT, Cursor, …); team = the private team endpoint; automated = directory indexers, probes and scripts.",
      "Country is where the connecting server is: Claude and ChatGPT connect from their own data centres (mostly US), not the user's country.",
      "No IP addresses or personal identifiers are stored. Client names are self-reported in the MCP handshake.",
    ],
  };
}

function isInitialize(bodyText) {
  try {
    const parsed = JSON.parse(bodyText);
    return (Array.isArray(parsed) ? parsed : [parsed]).some((m) => m && m.method === "initialize");
  } catch {
    return false;
  }
}

function authorized(request, url, env) {
  const token = env.AJ360_DASHBOARD_TOKEN;
  if (!token) return false; // fail closed when unset
  const header = request.headers.get("authorization") || "";
  const bearer = header.toLowerCase().startsWith("bearer ") ? header.slice(7).trim() : "";
  return bearer === token || url.searchParams.get("token") === token;
}

// Retention promised in the privacy policy (/privacy): 180 days.
const RETENTION_DAYS = 180;

export default {
  // Daily cron (wrangler.jsonc "triggers"): delete analytics past retention.
  async scheduled(event, env, ctx) {
    if (!env.ANALYTICS_DB) return;
    const cutoff = new Date(Date.now() - RETENTION_DAYS * 86400_000).toISOString();
    ctx.waitUntil(
      env.ANALYTICS_DB.prepare("DELETE FROM events WHERE ts < ?").bind(cutoff).run()
        .then((r) => console.log(`retention: deleted ${r.meta?.changes ?? 0} rows older than ${cutoff}`))
        .catch((err) => console.error("retention failed:", err.message))
    );
  },

  async fetch(request, env, ctx) {
    const url = new URL(request.url);

    // Worker-level usage analytics (persistent; the container's own
    // /api/stats only covers the current container lifetime).
    if (url.pathname === "/api/usage") {
      if (!authorized(request, url, env)) {
        return Response.json({ error: "Unauthorized" }, { status: 403 });
      }
      try {
        return Response.json(await usageReport(env, url));
      } catch (err) {
        return Response.json({ error: err.message }, { status: 500 });
      }
    }

    // Private team endpoint: /team/<token>/mcp → the full-profile container.
    let isTeam = false;
    const team = url.pathname.match(/^\/team\/([^/]+)(\/.*)?$/);
    if (team) {
      if (!env.AJ360_TEAM_TOKEN || team[1] !== env.AJ360_TEAM_TOKEN) {
        return Response.json({ error: "Not found" }, { status: 404 });
      }
      isTeam = true;
      const inner = new URL(request.url);
      inner.pathname = team[2] || "/mcp";
      request = new Request(inner, request);
    }
    const path = new URL(request.url).pathname;

    // Rate limit MCP traffic, per client. The key is the conversation's
    // session id, so a client rotating through IP addresses is still one
    // client, and people on Claude/ChatGPT (who share their provider's IPs)
    // are counted separately. Without a session id, the key is the IP's /24
    // (IPv4) or /48 (IPv6) range. The IP is only used for this in-memory
    // counter and is never stored.
    if (path === "/mcp" && env.MCP_LIMITER) {
      const sid = request.headers.get("mcp-session-id");
      const ip = request.headers.get("cf-connecting-ip") || "unknown";
      const range = ip.includes(":") ? ip.split(":").slice(0, 3).join(":") : ip.split(".").slice(0, 3).join(".");
      const limiter = isTeam ? env.TEAM_LIMITER || env.MCP_LIMITER : env.MCP_LIMITER;
      const { success } = await limiter.limit({ key: sid ? `s:${sid}` : `r:${range}` });
      if (!success) {
        return new Response(JSON.stringify({
          jsonrpc: "2.0", id: null,
          error: { code: -32029, message: "Rate limit exceeded: too many requests. Please retry in a minute." },
        }), { status: 429, headers: { "content-type": "application/json", "retry-after": "60" } });
      }
    }

    // Read the body before forwarding — it can only be consumed once.
    let bodyText = null;
    if (request.method === "POST" && path === "/mcp") {
      try {
        bodyText = await request.clone().text();
      } catch {
        bodyText = null;
      }
    }

    // Single named instance: MCP streamable-http sessions must keep
    // hitting the same backend, and one container serves this fine.
    const container = isTeam
      ? env.AJ360_TEAM_CONTAINER.getByName("mcp-team")
      : env.AJ360_CONTAINER.getByName("mcp");
    let response = await container.fetch(request);

    // The server runs stateless (no mcp-session-id), so a sleeping or
    // redeployed container can never strand a client on a dead session.
    // Analytics still wants to group a conversation's calls, so the Worker
    // hands out its own id on `initialize`; clients echo it back and the
    // stateless server ignores it, so a stale id can never fail a request.
    if (bodyText && !response.headers.get("mcp-session-id") && isInitialize(bodyText)) {
      response = new Response(response.body, response);
      response.headers.set("mcp-session-id", crypto.randomUUID());
    }

    if (bodyText) ctx.waitUntil(logEvents(env, request, response, bodyText, isTeam));
    return response;
  },
};
