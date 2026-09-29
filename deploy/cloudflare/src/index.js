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
      // Video index + transcription live in the Worker (D1 + Workers AI);
      // the container reaches them over /internal/* with a shared secret.
      AJ360_INDEX_URL: env.AJ360_ALLOWED_HOST ? `https://${env.AJ360_ALLOWED_HOST}` : "",
      AJ360_INTERNAL_TOKEN: env.AJ360_INTERNAL_TOKEN ?? "",
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

// ---------------------------------------------------------------------------
// Video index (D1) and speech-to-text (Workers AI) for video_intel.py.
// Reached only by the containers, with the AJ360_INTERNAL_TOKEN secret.
// ---------------------------------------------------------------------------

const WHISPER_MODEL = "@cf/openai/whisper-large-v3-turbo";

/** Same rules as video_intel.normalize() in Python. */
function normalizeText(t) {
  return String(t || "")
    .replace(/[\u064B-\u0652\u0670\u0640]/g, "")
    .toLowerCase()
    .replace(/[أإآٱ]/g, "ا").replace(/ى/g, "ي").replace(/ة/g, "ه")
    .replace(/\s+/g, " ").trim();
}

async function handleInternal(request, url, env) {
  if (!env.AJ360_INTERNAL_TOKEN || request.headers.get("x-internal-token") !== env.AJ360_INTERNAL_TOKEN) {
    return Response.json({ error: "Not found" }, { status: 404 });
  }
  const db = env.ANALYTICS_DB;
  try {
    if (url.pathname === "/internal/transcribe" && request.method === "POST") {
      if (!env.AI) return Response.json({ error: "Workers AI binding missing" }, { status: 500 });
      const body = await request.json();
      const result = await env.AI.run(WHISPER_MODEL, {
        audio: body.audio,
        language: body.language || "ar",
        vad_filter: body.vad_filter !== false,
      });
      return Response.json({ result });
    }

    if (url.pathname === "/internal/clip" && request.method === "POST") {
      if (!env.CLIPS) return Response.json({ error: "Clip storage (R2) not configured" }, { status: 500 });
      const name = (url.searchParams.get("name") || "clip.mp4").replace(/[^\w.-]+/g, "-").slice(0, 80);
      const key = `${crypto.randomUUID()}/${name}`;
      await env.CLIPS.put(key, request.body, { httpMetadata: { contentType: "video/mp4" } });
      return Response.json({ url: `${url.origin}/clips/${key}` });
    }

    if (url.pathname === "/internal/index/save" && request.method === "POST") {
      const { video, analysis, kinds = [], moments = [], span = null } = await request.json();
      const id = Number(video?.id);
      if (!id) return Response.json({ error: "video.id required" }, { status: 400 });
      const stmts = [];
      if (analysis) {
        const old = await db.prepare("SELECT data FROM video_analysis WHERE video_id = ?").bind(id).first();
        const merged = { ...(old?.data ? JSON.parse(old.data) : {}), ...analysis };
        stmts.push(db.prepare(
          `INSERT INTO video_analysis (video_id, title, series, duration, watch_url, summary, data, updated_at)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?)
           ON CONFLICT(video_id) DO UPDATE SET title = excluded.title, series = excluded.series,
             duration = excluded.duration, watch_url = excluded.watch_url,
             summary = COALESCE(excluded.summary, video_analysis.summary),
             data = excluded.data, updated_at = excluded.updated_at`
        ).bind(id, video.title ?? null, video.series ?? null, video.duration ?? null,
               video.watch_url ?? null, merged.summary ?? null, JSON.stringify(merged), new Date().toISOString()));
      }
      if (kinds.length) {
        // With a span, only that time range is replaced (long episodes arrive in parts).
        const inSpan = Array.isArray(span) ? " AND t_sec >= ? AND t_sec < ?" : "";
        stmts.push(db.prepare(
          `DELETE FROM video_moments WHERE video_id = ? AND kind IN (${kinds.map(() => "?").join(",")})${inSpan}`
        ).bind(id, ...kinds, ...(inSpan ? [Math.floor(span[0]), Math.ceil(span[1])] : [])));
      }
      // Multi-row inserts: 16 rows × 6 values stays under D1's 100 bound parameters,
      // and an hour of transcript is ~45 statements instead of ~700.
      const ROWS = 16;
      for (let i = 0; i < moments.length; i += ROWS) {
        const part = moments.slice(i, i + ROWS);
        stmts.push(db.prepare(
          `INSERT INTO video_moments (video_id, t_sec, kind, text, norm, words) VALUES ${part.map(() => "(?, ?, ?, ?, ?, ?)").join(", ")}`
        ).bind(...part.flatMap((m) => [id, Math.round(Number(m.t_sec) || 0), String(m.kind), String(m.text),
          normalizeText(m.norm || m.text), m.words?.length ? JSON.stringify(m.words) : null])));
      }
      // D1 batches are transactional; keep each under the statement limit.
      for (let i = 0; i < stmts.length; i += 90) await db.batch(stmts.slice(i, i + 90));
      return Response.json({ saved: true, moments: moments.length });
    }

    if (url.pathname === "/internal/index/get") {
      const id = Number(url.searchParams.get("id")) || 0;
      if (!id) {
        const { results } = await db.prepare(
          `SELECT a.video_id, a.title, a.series, a.updated_at,
             json_extract(a.data, '$.auto_index.status') AS auto_status,
             json_array_length(json_extract(a.data, '$.ad_breaks')) AS ad_breaks,
             (SELECT COUNT(*) FROM video_moments m WHERE m.video_id = a.video_id AND m.kind = 'transcript') AS transcript_segments
           FROM video_analysis a ORDER BY a.updated_at DESC LIMIT 200`).all();
        return Response.json({ videos: results });
      }
      const analysis = await db.prepare("SELECT * FROM video_analysis WHERE video_id = ?").bind(id).first();
      const cols = url.searchParams.get("words") === "1" ? "t_sec, kind, text, words" : "t_sec, kind, text";
      const { results } = await db.prepare(
        `SELECT ${cols} FROM video_moments WHERE video_id = ? ORDER BY kind, t_sec`).bind(id).all();
      return Response.json({ analysis: analysis ?? null, moments: results });
    }

    if (url.pathname === "/internal/index/search") {
      const q = normalizeText(url.searchParams.get("q") || "");
      const kind = url.searchParams.get("kind") || "all";
      const limit = Math.min(Math.max(parseInt(url.searchParams.get("limit") || "40", 10) || 40, 1), 200);
      if (!q) return Response.json({ results: [] });
      const { results } = await db.prepare(
        `SELECT m.video_id, m.t_sec, m.kind, m.text, m.words, a.title, a.series, a.watch_url
         FROM video_moments m LEFT JOIN video_analysis a ON a.video_id = m.video_id
         WHERE m.norm LIKE ?${kind !== "all" ? " AND m.kind = ?" : ""}
         ORDER BY m.video_id, m.t_sec LIMIT ?`
      ).bind(`%${q}%`, ...(kind !== "all" ? [kind] : []), limit).all();
      return Response.json({ results });
    }
    return Response.json({ error: "Not found" }, { status: 404 });
  } catch (err) {
    return Response.json({ error: err.message }, { status: 500 });
  }
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

// ---------------------------------------------------------------------------
// Clips (R2): made by make_clip, public by unguessable link, deleted after 7 days.
// ---------------------------------------------------------------------------
const CLIP_DAYS = 7;

async function serveClip(request, url, env) {
  if (!env.CLIPS) return new Response("Not found", { status: 404 });
  const key = decodeURIComponent(url.pathname.slice("/clips/".length));
  const range = request.headers.get("range");
  const m = range && range.match(/bytes=(\d*)-(\d*)/);
  const opts = m ? { range: m[1] ? { offset: Number(m[1]), ...(m[2] ? { length: Number(m[2]) - Number(m[1]) + 1 } : {}) }
                                   : { suffix: Number(m[2]) } } : {};
  const obj = await env.CLIPS.get(key, opts);
  if (!obj) return new Response("Not found", { status: 404 });
  const headers = new Headers({
    "content-type": "video/mp4", "accept-ranges": "bytes", "cache-control": "private, max-age=3600",
    "content-disposition": `inline; filename="${key.split("/").pop()}"`, "x-robots-tag": "noindex",
  });
  if (m && obj.range) {
    const start = obj.range.offset ?? (obj.size - obj.range.suffix);
    const len = obj.range.length ?? (obj.size - start);
    headers.set("content-range", `bytes ${start}-${start + len - 1}/${obj.size}`);
    headers.set("content-length", String(len));
    return new Response(obj.body, { status: 206, headers });
  }
  headers.set("content-length", String(obj.size));
  return new Response(obj.body, { headers });
}

async function deleteOldClips(env) {
  if (!env.CLIPS) return 0;
  const cutoff = Date.now() - CLIP_DAYS * 86400_000;
  let cursor, removed = 0;
  do {
    const page = await env.CLIPS.list({ cursor, limit: 500 });
    const old = page.objects.filter((o) => o.uploaded.getTime() < cutoff).map((o) => o.key);
    if (old.length) { await env.CLIPS.delete(old); removed += old.length; }
    cursor = page.truncated ? page.cursor : undefined;
  } while (cursor);
  return removed;
}

// ---------------------------------------------------------------------------
// Team studio: /team/<token>/studio — indexed episodes, transcripts, ad breaks.
// ---------------------------------------------------------------------------
const esc = (v) => String(v ?? "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
const ts = (s) => { s = Math.max(0, Math.floor(Number(s) || 0)); const h = Math.floor(s / 3600), m = Math.floor(s % 3600 / 60), x = s % 60;
  return (h ? `${h}:${String(m).padStart(2, "0")}` : String(m).padStart(2, "0")) + ":" + String(x).padStart(2, "0"); };
const srtTs = (s) => { const ms = Math.round(s * 1000); const p = (n, w = 2) => String(n).padStart(w, "0");
  return `${p(Math.floor(ms / 3600000))}:${p(Math.floor(ms % 3600000 / 60000))}:${p(Math.floor(ms % 60000 / 1000))},${p(ms % 1000, 3)}`; };

async function studio(request, url, env, base, rest) {
  const db = env.ANALYTICS_DB;
  const file = rest.match(/^\/(\d+)(\.srt|-ads\.csv)$/);
  if (file) {
    const id = Number(file[1]);
    if (file[2] === ".srt") {
      const { results } = await db.prepare(
        "SELECT t_sec, text, words FROM video_moments WHERE video_id = ? AND kind = 'transcript' ORDER BY t_sec").bind(id).all();
      const cues = results.map((r, i) => {
        const w = r.words ? JSON.parse(r.words) : [];
        const start = w.length ? w[0][0] : r.t_sec;
        const end = w.length ? w[w.length - 1][1] : (results[i + 1]?.t_sec ?? r.t_sec + 5);
        return `${i + 1}\n${srtTs(start)} --> ${srtTs(end)}\n${r.text}`;
      });
      return new Response(cues.join("\n\n") + "\n", { headers: {
        "content-type": "application/x-subrip; charset=utf-8", "content-disposition": `attachment; filename="aj360-${id}.srt"` } });
    }
    const row = await db.prepare("SELECT data FROM video_analysis WHERE video_id = ?").bind(id).first();
    const breaks = row?.data ? (JSON.parse(row.data).ad_breaks || []) : [];
    const csv = ["break,time,seconds,categories,brand_safety",
      ...breaks.map((b) => `${b.break},${b.at},${b.at_sec},"${(b.categories || []).join(" ")}",${b.brand_safety}`)].join("\n");
    return new Response("\ufeff" + csv + "\n", { headers: {
      "content-type": "text/csv; charset=utf-8", "content-disposition": `attachment; filename="aj360-${id}-ad-breaks.csv"` } });
  }
  const { results } = await db.prepare(
    `SELECT a.video_id, a.title, a.series, a.duration, a.watch_url, a.updated_at,
       json_extract(a.data, '$.auto_index.status') AS auto_status,
       json_extract(a.data, '$.ad_breaks') AS ad_breaks,
       (SELECT COUNT(*) FROM video_moments m WHERE m.video_id = a.video_id AND m.kind = 'transcript') AS segs
     FROM video_analysis a ORDER BY a.updated_at DESC LIMIT 150`).all();
  const status = { done: "✅ مفهرسة", protected: "🔒 محمية DRM", failed: "⚠️ فشلت" };
  const rows = results.map((r) => {
    const breaks = r.ad_breaks ? JSON.parse(r.ad_breaks) : [];
    const chips = breaks.map((b) => `<span class="chip ${b.brand_safety === "sensitive" ? "warn" : ""}" title="${esc((b.categories || []).join("، "))}">${esc(b.at)}</span>`).join("");
    return `<tr>
      <td><a href="${esc(r.watch_url)}" target="_blank" rel="noopener">${esc(r.title)}</a><div class="muted">${esc(r.series || "")} · ${esc(r.video_id)}</div></td>
      <td>${r.duration ? ts(r.duration) : ""}</td>
      <td>${r.segs ? `${r.segs} سطر · <a href="${base}/studio/${r.video_id}.srt">SRT</a>` : '<span class="muted">—</span>'}</td>
      <td>${chips || '<span class="muted">—</span>'}${breaks.length ? ` <a href="${base}/studio/${r.video_id}-ads.csv">CSV</a>` : ""}</td>
      <td>${esc(status[r.auto_status] || (r.segs ? "✅ مفرّغة" : "—"))}<div class="muted">${esc((r.updated_at || "").slice(0, 16).replace("T", " "))}</div></td>
    </tr>`;
  }).join("");
  const html = `<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex">
<title>استوديو الجزيرة 360</title>
<style>
:root{--bg:#f3f4f6;--card:#fff;--ink:#16181d;--muted:#5e6470;--line:#e3e5e9;--acc:#3ecf6a;--warn:#e5484d}
@media (prefers-color-scheme:dark){:root{--bg:#0f1115;--card:#171a20;--ink:#eef0f3;--muted:#9aa1ad;--line:#262a33}}
body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.6 system-ui,"Segoe UI",Tahoma,sans-serif}
main{max-width:1100px;margin:0 auto;padding:24px 16px}
h1{margin:0 0 4px;font-size:24px}.muted{color:var(--muted);font-size:13px}
.card{background:var(--card);border:1px solid var(--line);border-radius:14px;overflow-x:auto;margin-top:18px}
table{width:100%;border-collapse:collapse;min-width:720px}th,td{padding:10px 12px;border-bottom:1px solid var(--line);text-align:start;vertical-align:top}
th{font-size:13px;color:var(--muted);font-weight:600}a{color:inherit}
.chip{display:inline-block;padding:1px 8px;margin:2px;border-radius:99px;background:color-mix(in srgb,var(--acc) 18%,transparent);font:12px ui-monospace,monospace}
.chip.warn{background:color-mix(in srgb,var(--warn) 18%,transparent)}
</style></head><body><main>
<h1>استوديو الجزيرة 360</h1>
<div class="muted">الحلقات المفهرسة: التفريغ بالتوقيت، ونقاط الإعلانات المقترحة (الأحمر = محتوى حساس للمعلنين). الحلقات الجديدة تُفهرس تلقائيًا كل ساعة.</div>
<div class="card"><table><thead><tr><th>الحلقة</th><th>المدة</th><th>التفريغ</th><th>نقاط الإعلانات</th><th>الحالة</th></tr></thead>
<tbody>${rows || '<tr><td colspan="5" class="muted">لا توجد حلقات مفهرسة بعد.</td></tr>'}</tbody></table></div>
</main></body></html>`;
  return new Response(html, { headers: { "content-type": "text/html; charset=utf-8", "cache-control": "no-store", "x-robots-tag": "noindex" } });
}

// Retention promised in the privacy policy (/privacy): 180 days.
const RETENTION_DAYS = 180;
const AUTO_INDEX_CRON = "7 * * * *";

export default {
  // Daily cron (wrangler.jsonc "triggers"): delete analytics past retention.
  async scheduled(event, env, ctx) {
    // Hourly: index the newest episodes (transcript + ad breaks) on the team container.
    if (event.cron === AUTO_INDEX_CRON) {
      if (env.AJ360_INTERNAL_TOKEN && env.AJ360_ALLOWED_HOST) {
        ctx.waitUntil(env.AJ360_TEAM_CONTAINER.getByName("mcp-team").fetch(new Request(
          `https://${env.AJ360_ALLOWED_HOST}/jobs/auto-index`,
          { method: "POST", headers: { "x-internal-token": env.AJ360_INTERNAL_TOKEN } }))
          .then((r) => r.text()).then((t) => console.log("auto-index:", t))
          .catch((err) => console.error("auto-index failed:", err.message)));
      }
      return;
    }
    ctx.waitUntil(deleteOldClips(env).then((n) => console.log(`clips: deleted ${n}`))
      .catch((err) => console.error("clip cleanup failed:", err.message)));
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

    if (url.pathname.startsWith("/internal/")) return handleInternal(request, url, env);
    if (url.pathname.startsWith("/clips/") && request.method === "GET") return serveClip(request, url, env);

    // Private team endpoint: /team/<token>/mcp → the full-profile container.
    let isTeam = false;
    const team = url.pathname.match(/^\/team\/([^/]+)(\/.*)?$/);
    if (team) {
      if (!env.AJ360_TEAM_TOKEN || team[1] !== env.AJ360_TEAM_TOKEN) {
        return Response.json({ error: "Not found" }, { status: 404 });
      }
      isTeam = true;
      if ((team[2] || "").startsWith("/studio")) {
        return studio(request, url, env, `/team/${team[1]}`, team[2].slice("/studio".length));
      }
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
