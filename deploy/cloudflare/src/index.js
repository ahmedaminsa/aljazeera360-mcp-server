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
      AJ360_ENABLE_SEO_TOOLS: env.AJ360_ENABLE_SEO_TOOLS ?? "",
    };
  }
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

/** Pick the most descriptive argument of a tool call for the `query` column. */
function summarizeArgs(args) {
  if (!args || typeof args !== "object") return null;
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

async function logEvents(env, request, response, bodyText) {
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

  const stmt = env.ANALYTICS_DB.prepare(
    `INSERT INTO events
       (ts, session_id, method, tool, query, client_name, client_version, country, ua)
     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)`
  );
  try {
    await env.ANALYTICS_DB.batch(
      events.map((e) =>
        stmt.bind(
          ts, sessionId, e.method, e.tool, e.query,
          e.client_name, e.client_version, country, ua
        )
      )
    );
  } catch (err) {
    console.error("analytics write failed:", err.message);
  }
}

/** Aggregate report over the last N days. Token-protected. */
async function usageReport(env, url) {
  const days = Math.min(Math.max(parseInt(url.searchParams.get("days") || "30", 10) || 30, 1), 365);
  const since = new Date(Date.now() - days * 86400_000).toISOString();
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
           COUNT(DISTINCT e.session_id) AS sessions
    FROM events e LEFT JOIN sess s ON e.session_id = s.session_id
    WHERE e.ts >= ?
    GROUP BY client, version
    ORDER BY events DESC LIMIT 20`;

  const q = (sql) => db.prepare(sql).bind(since).all();
  const [totals, clients, tools, queries, countries, daily, sessions] = await Promise.all([
    q(`SELECT COUNT(*) AS events, COUNT(DISTINCT session_id) AS sessions FROM events WHERE ts >= ?`),
    q(clientsSql),
    q(`SELECT tool, COUNT(*) AS calls FROM events WHERE ts >= ? AND tool IS NOT NULL
       GROUP BY tool ORDER BY calls DESC LIMIT 30`),
    q(`SELECT query, tool, COUNT(*) AS n FROM events WHERE ts >= ? AND query IS NOT NULL
       GROUP BY query, tool ORDER BY n DESC LIMIT 30`),
    q(`SELECT COALESCE(country,'??') AS country, COUNT(*) AS events FROM events WHERE ts >= ?
       GROUP BY country ORDER BY events DESC LIMIT 20`),
    q(`SELECT substr(ts,1,10) AS day, COUNT(*) AS events,
              COUNT(DISTINCT session_id) AS sessions
       FROM events WHERE ts >= ? GROUP BY day ORDER BY day DESC LIMIT 60`),
    q(`SELECT session_id, MIN(ts) AS started, COUNT(*) AS events,
              MAX(client_name) AS client
       FROM events WHERE ts >= ? AND session_id IS NOT NULL
       GROUP BY session_id ORDER BY started DESC LIMIT 25`),
  ]);

  return {
    period_days: days,
    since,
    totals: totals.results?.[0] ?? {},
    clients: clients.results ?? [],
    tools: tools.results ?? [],
    top_queries: queries.results ?? [],
    countries: countries.results ?? [],
    daily: daily.results ?? [],
    recent_sessions: sessions.results ?? [],
    note: "No IP addresses or personal identifiers are stored. Client names are self-reported by the AI client in the MCP handshake.",
  };
}

function authorized(request, url, env) {
  const token = env.AJ360_DASHBOARD_TOKEN;
  if (!token) return false; // fail closed when unset
  const header = request.headers.get("authorization") || "";
  const bearer = header.toLowerCase().startsWith("bearer ") ? header.slice(7).trim() : "";
  return bearer === token || url.searchParams.get("token") === token;
}

export default {
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

    // Read the body before forwarding — it can only be consumed once.
    let bodyText = null;
    if (request.method === "POST" && url.pathname === "/mcp") {
      try {
        bodyText = await request.clone().text();
      } catch {
        bodyText = null;
      }
    }

    // Single named instance: MCP streamable-http sessions must keep
    // hitting the same backend, and one container serves this fine.
    const container = env.AJ360_CONTAINER.getByName("mcp");
    const response = await container.fetch(request);

    if (bodyText) ctx.waitUntil(logEvents(env, request, response, bodyText));
    return response;
  },
};
