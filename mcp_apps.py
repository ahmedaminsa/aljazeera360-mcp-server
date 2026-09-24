"""
MCP Apps (interactive UI) for the Al Jazeera 360 MCP server.

Implements the MCP Apps extension (``io.modelcontextprotocol/ui``, spec
2026-01-26): tools declare a ``ui://`` resource in their ``_meta``, and hosts
that support the extension (Claude, ChatGPT, and others) render that resource
as a sandboxed HTML view next to the tool result. Hosts without support ignore
the metadata and keep using the plain JSON text, so nothing changes for them.

One self-contained single-page view serves every UI-bound tool:

* Catalog  — search results, section rows, trending, latest episodes as
             thumbnail cards with section chips and an in-view search box.
* Series   — poster, description, season tabs, episode list (loads seasons
             on demand through ``tools/call``).
* Video    — details card with play / open-on-site / ask-about-it actions.
* Player   — the official aljazeera360.com player embedded in an iframe.

Why the player embeds the official page instead of a stream URL:
the platform's streams are DRM-protected (Widevine / PlayReady), the stream
token is bound to the IP address that requested it, and the platform API only
allows CORS from aljazeera360.com. A server-side stream URL would therefore
never play in the viewer's browser, and proxying the stream would bypass the
platform's rights controls. Embedding the official page keeps playback, DRM,
sign-in, ads and analytics on Al Jazeera 360's own player. Whether the host
sandbox allows protected playback varies by client, so the view checks for
EME support and always offers "open on aljazeera360.com" as a fallback.
"""

from __future__ import annotations

import os

# ----------------------------------------------------------------------------
# Constants shared with server.py
# ----------------------------------------------------------------------------

UI_ENABLED = os.environ.get("AJ360_ENABLE_UI", "1").strip().lower() not in ("0", "false", "no")

APP_URI = "ui://aljazeera360/app.html"
APP_MIME_TYPE = "text/html;profile=mcp-app"

# Origins the sandboxed view may load from. Everything else is blocked by the
# host-enforced Content Security Policy.
IMAGE_DOMAINS = [
    "https://dve-images.imggaming.com",
    "https://vod-images.onvesper.com",
    "https://static.diceplatform.com",
    "https://img.dge-prod.dicelaboratory.com",  # live-channel thumbnails in search
    # Both CDNs answer some requests with a 307 to Vesper's image resizers
    # (vod-images /prod/i/..., and dve-images sizes not generated yet). CSP
    # applies to redirect targets, so they are allowed too. If a resizer host
    # ever changes, the view falls back to the original image URL.
    "https://y6p2scuk6d.execute-api.eu-west-1.amazonaws.com",
    "https://9mf8d6e75e.execute-api.eu-west-1.amazonaws.com",
]
FRAME_DOMAINS = ["https://www.aljazeera360.com"]

RESOURCE_META = {
    "ui": {
        "csp": {
            "connectDomains": [],
            "resourceDomains": IMAGE_DOMAINS,
            "frameDomains": FRAME_DOMAINS,
        },
        "prefersBorder": True,
    }
}


def tool_meta() -> dict | None:
    """``_meta`` for a UI-bound tool, or None when the UI is disabled.

    Both the nested key (current spec) and the flat ``ui/resourceUri`` key
    (earlier drafts, still read by some hosts) are sent.
    """
    if not UI_ENABLED:
        return None
    return {"ui": {"resourceUri": APP_URI}, "ui/resourceUri": APP_URI}


# ----------------------------------------------------------------------------
# The view
# ----------------------------------------------------------------------------
# Plain HTML + vanilla JS so the server stays a single Python package with no
# build step. The host bridge is the MCP Apps postMessage JSON-RPC protocol;
# a small fallback also supports the ChatGPT Apps SDK ``window.openai`` bridge.

APP_HTML = r"""<!doctype html>
<html lang="ar" dir="rtl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>الجزيرة 360</title>
<style>
:root{
  --bg:#ffffff; --surface:#f4f5f7; --surface-2:#e9ebef; --text:#111418; --muted:#5b6470;
  --accent:#c8962d; --accent-ink:#1a1204; --border:#dde1e6; --lock:#8a5a00; --lock-bg:#fff4dc;
  --radius:12px; --shadow:0 1px 2px rgba(0,0,0,.06),0 4px 14px rgba(0,0,0,.06);
}
:root[data-theme="dark"]{
  --bg:#0f1115; --surface:#191c22; --surface-2:#232730; --text:#eef0f3; --muted:#9aa3ae;
  --accent:#e0ad45; --accent-ink:#1a1204; --border:#2a2f38; --lock:#ffcf73; --lock-bg:#3a2c0e;
  --shadow:0 1px 2px rgba(0,0,0,.4),0 4px 14px rgba(0,0,0,.35);
}
*{box-sizing:border-box}
html,body{margin:0;background:var(--bg);color:var(--text);
  font:15px/1.5 system-ui,-apple-system,"Segoe UI","Noto Sans Arabic",Tahoma,sans-serif}
button{font:inherit;color:inherit;cursor:pointer}
.app{padding:14px 16px 18px}
.top{display:flex;align-items:center;gap:10px;margin-bottom:12px}
.brand{font-weight:700;font-size:16px;white-space:nowrap}
.brand b{color:var(--accent)}
.back{border:1px solid var(--border);background:var(--surface);border-radius:999px;padding:4px 12px;font-size:13px}
.search{flex:1;display:flex;gap:6px;min-width:0}
.search input{flex:1;min-width:0;border:1px solid var(--border);background:var(--surface);color:var(--text);
  border-radius:999px;padding:7px 14px;font:inherit}
.search button{border:0;background:var(--accent);color:var(--accent-ink);border-radius:999px;padding:6px 14px;font-weight:600}
.chips{display:flex;gap:6px;overflow-x:auto;padding-bottom:6px;margin-bottom:10px;scrollbar-width:thin}
.chip{flex:none;border:1px solid var(--border);background:var(--surface);border-radius:999px;padding:4px 12px;font-size:13px}
.chip[aria-pressed="true"]{background:var(--text);color:var(--bg);border-color:var(--text)}
h2{font-size:15px;margin:14px 0 8px}
.row{display:grid;grid-auto-flow:column;grid-auto-columns:minmax(170px,210px);gap:10px;overflow-x:auto;
  padding-bottom:8px;scroll-snap-type:x proximity;scrollbar-width:thin}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(170px,1fr));gap:10px}
.card{scroll-snap-align:start;text-align:start;border:1px solid var(--border);background:var(--surface);
  border-radius:var(--radius);overflow:hidden;padding:0;display:flex;flex-direction:column;box-shadow:var(--shadow)}
.card:hover,.card:focus-visible{outline:2px solid var(--accent);outline-offset:0}
.thumb{position:relative;aspect-ratio:16/9;background:var(--surface-2);overflow:hidden}
.thumb img{width:100%;height:100%;object-fit:cover;display:block}
.thumb .dur{position:absolute;bottom:6px;left:6px;background:rgba(0,0,0,.72);color:#fff;font-size:11px;
  padding:1px 6px;border-radius:6px;direction:ltr}
.thumb .kind{position:absolute;top:6px;right:6px;background:var(--accent);color:var(--accent-ink);font-size:11px;
  font-weight:700;padding:1px 7px;border-radius:6px}
.card .body{padding:8px 10px 10px}
.card .t{font-weight:600;font-size:13.5px;line-height:1.35;display:-webkit-box;-webkit-line-clamp:2;
  -webkit-box-orient:vertical;overflow:hidden}
.card .s{color:var(--muted);font-size:12px;margin-top:3px;display:-webkit-box;-webkit-line-clamp:2;
  -webkit-box-orient:vertical;overflow:hidden}
.lock{display:inline-block;margin-top:5px;font-size:11px;color:var(--lock);background:var(--lock-bg);padding:1px 7px;border-radius:6px}
.hero{display:grid;grid-template-columns:minmax(0,190px) 1fr;gap:14px;align-items:start}
.hero img{width:100%;border-radius:var(--radius);display:block;background:var(--surface-2)}
.hero h1{font-size:19px;margin:0 0 6px}
.meta{color:var(--muted);font-size:13px;display:flex;flex-wrap:wrap;gap:4px 12px;margin-bottom:8px}
.desc{font-size:14px;margin:0 0 10px}
.tags{display:flex;flex-wrap:wrap;gap:6px;margin:6px 0 10px}
.tag{font-size:12px;background:var(--surface-2);padding:2px 9px;border-radius:999px}
.actions{display:flex;flex-wrap:wrap;gap:8px}
.btn{border:1px solid var(--border);background:var(--surface);border-radius:999px;padding:7px 14px;font-weight:600;font-size:13.5px}
.btn.primary{background:var(--accent);border-color:var(--accent);color:var(--accent-ink)}
.tabs{display:flex;gap:6px;overflow-x:auto;margin:14px 0 8px}
.eps{display:flex;flex-direction:column;gap:8px}
.ep{display:grid;grid-template-columns:150px 1fr;gap:10px;align-items:center;border:1px solid var(--border);
  background:var(--surface);border-radius:var(--radius);padding:6px;text-align:start}
.ep:hover,.ep:focus-visible{outline:2px solid var(--accent)}
.ep .thumb{border-radius:8px}
.player{position:relative;aspect-ratio:16/9;background:#000;border-radius:var(--radius);overflow:hidden}
.player iframe{position:absolute;inset:0;width:100%;height:100%;border:0}
.player .poster{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:.45}
.player .overlay{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;
  gap:10px;color:#fff;text-align:center;padding:16px}
.note{color:var(--muted);font-size:12.5px;margin:8px 0 0}
.state{padding:28px 8px;text-align:center;color:var(--muted)}
.spinner{width:26px;height:26px;border:3px solid var(--surface-2);border-top-color:var(--accent);border-radius:50%;
  animation:spin .8s linear infinite;margin:0 auto 10px}
@keyframes spin{to{transform:rotate(360deg)}}
@media (max-width:520px){.hero{grid-template-columns:1fr}.hero img{max-width:220px}.ep{grid-template-columns:120px 1fr}}
</style>
</head>
<body>
<div class="app" id="app"><div class="state"><div class="spinner"></div>جارٍ التحميل…</div></div>
<script>
(() => {
"use strict";
const SITE = "https://www.aljazeera360.com";
const SECTIONS = [
  ["__trending","الرائج"], ["AJ360-Originals","أعمال أصلية"], ["AJA","الجزيرة"], ["AJD","الوثائقية"],
  ["Atheer","أثير"], ["AJ-Plus","AJ+"], ["Podcast","بودكاست"], ["Documentaries","وثائقيات"], ["Talk Show","حوارية"],
  ["Investigative Show","تحقيقية"]
];
const $app = document.getElementById("app");

/* ------------------------------------------------------------------ bridge */
// MCP Apps: JSON-RPC 2.0 over postMessage with the host (window.parent).
let rpcId = 0; const pending = new Map(); let hostCaps = {};
const openai = window.openai || null;           // ChatGPT Apps SDK fallback
function post(msg){ window.parent.postMessage(msg, "*"); }
function request(method, params){
  return new Promise((resolve, reject) => {
    const id = ++rpcId; pending.set(id, {resolve, reject});
    post({jsonrpc:"2.0", id, method, params: params || {}});
    setTimeout(() => { if (pending.has(id)) { pending.delete(id); reject(new Error("timeout: " + method)); } }, 45000);
  });
}
function notify(method, params){ post({jsonrpc:"2.0", method, params: params || {}}); }

window.addEventListener("message", (ev) => {
  const m = ev.data;
  if (!m || m.jsonrpc !== "2.0") return;
  if (m.id != null && pending.has(m.id) && !m.method) {
    const p = pending.get(m.id); pending.delete(m.id);
    m.error ? p.reject(new Error(m.error.message || "error")) : p.resolve(m.result);
    return;
  }
  switch (m.method) {
    case "ui/notifications/tool-input": lastInput = (m.params && m.params.arguments) || {}; break;
    case "ui/notifications/tool-result": onToolResult(m.params); break;
    case "ui/notifications/host-context-changed": applyContext(m.params); break;
    case "ui/notifications/tool-cancelled": renderState("أُلغي الطلب."); break;
    case "ui/resource-teardown": if (m.id != null) post({jsonrpc:"2.0", id:m.id, result:{}}); break;
    default: if (m.id != null && m.method) post({jsonrpc:"2.0", id:m.id, error:{code:-32601, message:"not supported"}});
  }
});

async function callTool(name, args){
  if (openai && openai.callTool) return openai.callTool(name, args);
  return request("tools/call", {name, arguments: args});
}
function openLink(url){
  if (openai && openai.openExternal) return openai.openExternal({href:url});
  request("ui/open-link", {url}).catch(() => window.open(url, "_blank", "noopener"));
}
function sendMessage(text){
  if (openai && openai.sendFollowUpMessage) return openai.sendFollowUpMessage({prompt:text});
  request("ui/message", {role:"user", content:[{type:"text", text}]}).catch(() => {});
}
function tellModel(text){
  // Keeps the model aware of what the user is looking at (like data-llm).
  if (!hostCaps.updateModelContext && !openai) return;
  request("ui/update-model-context", {content:[{type:"text", text}]}).catch(() => {});
}
function requestFullscreen(){
  if (openai && openai.requestDisplayMode) return openai.requestDisplayMode({mode:"fullscreen"});
  request("ui/request-display-mode", {mode:"fullscreen"}).catch(() => {});
}
function applyContext(ctx){
  if (!ctx) return;
  if (ctx.theme) document.documentElement.dataset.theme = ctx.theme;
}
let lastH = 0;
function reportSize(){
  const h = Math.ceil(document.documentElement.getBoundingClientRect().height);
  if (Math.abs(h - lastH) < 2) return; lastH = h;
  if (openai) return;
  notify("ui/notifications/size-changed", {width: Math.ceil(document.documentElement.scrollWidth), height: h});
}
new ResizeObserver(reportSize).observe(document.documentElement);

/* ------------------------------------------------------------ data parsing */
function parseResult(res){
  if (!res) return null;
  const sc = res.structuredContent;
  if (sc && typeof sc === "object") {
    if (typeof sc.result === "string") { try { return JSON.parse(sc.result); } catch(e){} }
    else if (!("result" in sc) || Object.keys(sc).length > 1) return sc;
  }
  const txt = (res.content || []).filter(c => c.type === "text").map(c => c.text).join("");
  try { return JSON.parse(txt); } catch(e){ return txt ? {error: txt} : null; }
}
function thumb(url, w, h){
  if (!url) return "";
  // dve-images supports on-the-fly resizing (/WxH/ path); saves ~90% bytes.
  return url.replace("https://dve-images.imggaming.com/original/", `https://dve-images.imggaming.com/${w}x${h}/`);
}
const isSeries = (t) => /SERIES/i.test(t || "");
const isLive = (t) => /LIVE/i.test(t || "");
const lockText = (a) => a === "GRANTED_ON_SIGN_IN" ? "يتطلب تسجيل الدخول" : (a && a !== "GRANTED" && a !== "UNKNOWN" ? "محتوى مقيّد" : "");
function card(it){
  return {
    kind: isSeries(it.type) ? "series" : isLive(it.type) ? "live" : "video",
    url: it.watch_url || it.url || "",
    id: String(it.id || ""),
    title: it.title || "",
    sub: it.series || it.description || "",
    image: it.thumbnail || it.poster || it.image || "",
    duration: it.duration && it.duration !== "N/A" ? it.duration : "",
    lock: lockText(it.access_level),
  };
}
const cards = (arr) => (arr || []).filter(x => x && x.id).map(card);

/* ------------------------------------------------------------------ render */
function esc(s){ return String(s == null ? "" : s).replace(/[&<>"']/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c])); }
const history = [];      // stack of {tool, args, data}
let current = null, lastInput = {}, activeChip = "", initialTool = null;

function header(){
  const back = history.length ? `<button class="back" data-act="back">→ رجوع</button>` : "";
  return `<div class="top">${back}<div class="brand">الجزيرة <b>360</b></div>
    <form class="search" data-act="search"><input name="q" placeholder="ابحث في الجزيرة 360…" aria-label="بحث">
    <button type="submit">بحث</button></form></div>
    <div class="chips" role="toolbar">${SECTIONS.map(([id,l]) =>
      `<button class="chip" data-act="section" data-id="${esc(id)}" aria-pressed="${activeChip===id}">${esc(l)}</button>`).join("")}</div>`;
}
function cardHTML(c){
  const img = c.image ? `<img loading="lazy" alt="" src="${esc(thumb(c.image,400,225))}" data-orig="${esc(c.image)}">` : "";
  const act = c.kind === "live" ? `data-act="open" data-url="${esc(c.url)}"` : `data-act="${c.kind}" data-id="${esc(c.id)}"`;
  return `<button class="card" ${act} title="${esc(c.title)}">
    <div class="thumb">${img}${c.duration ? `<span class="dur">${esc(c.duration)}</span>` : ""}${c.kind==="series" ? `<span class="kind">برنامج</span>` : c.kind==="live" ? `<span class="kind">مباشر</span>` : ""}</div>
    <div class="body"><div class="t">${esc(c.title)}</div>${c.sub ? `<div class="s">${esc(c.sub)}</div>` : ""}
    ${c.lock ? `<span class="lock">${esc(c.lock)}</span>` : ""}</div></button>`;
}
function rowsHTML(rows, gridIfSingle){
  const rs = rows.filter(r => r.items.length);
  if (!rs.length) return `<div class="state">لا توجد نتائج.</div>`;
  return rs.map(r => `${r.title ? `<h2>${esc(r.title)}</h2>` : ""}
    <div class="${gridIfSingle && rs.length === 1 ? "grid" : "row"}">${r.items.map(cardHTML).join("")}</div>`).join("");
}
function mount(html){
  $app.innerHTML = header() + html;
  $app.querySelectorAll("img[data-orig]").forEach(img => img.addEventListener("error", () => {
    if (img.src !== img.dataset.orig) img.src = img.dataset.orig; else img.remove();
  }, {once:false}));
  reportSize();
}
function renderState(text, spin){ mount(`<div class="state">${spin ? '<div class="spinner"></div>' : ""}${esc(text)}</div>`); }

const views = {
  search_videos(d){
    activeChip = "";
    tellModel(`User is viewing Al Jazeera 360 search results for "${d.query}".`);
    return `<h2>نتائج البحث: «${esc(d.query || "")}»</h2>` + rowsHTML([{title:"", items:cards(d.results)}], true);
  },
  browse_section(d){
    activeChip = d.section_id || activeChip;
    tellModel(`User is browsing the Al Jazeera 360 section "${d.section || d.section_id}".`);
    return `<h2>${esc(d.section || "")}</h2>` + rowsHTML((d.programs || []).map(p => ({title:p.category, items:cards(p.items)})));
  },
  get_trending_content(d){
    activeChip = "__trending";
    tellModel("User is browsing trending content on Al Jazeera 360.");
    return rowsHTML((d.categories || []).map(c => ({title:c.name, items:cards(c.items)})));
  },
  get_latest_episodes(d){
    activeChip = d.section_id || "";
    return `<h2>أحدث الحلقات — ${esc(d.section || "")}</h2>` + rowsHTML([{title:"", items:cards(d.latest_episodes)}], true);
  },
  get_series_details(d){
    tellModel(`User is viewing the series "${d.title}" (series_id ${d.id}).`);
    const seasons = d.seasons || [];
    const img = d.poster || d.cover;
    setTimeout(() => { if (seasons[0]) loadSeason(seasons[0].season_id); }, 0);
    return `<div class="hero">${img ? `<img alt="" src="${esc(thumb(img,300,450))}" data-orig="${esc(img)}">` : "<div></div>"}
      <div><h1>${esc(d.title)}</h1>
      <div class="meta"><span>${seasons.length} ${seasons.length === 1 ? "موسم" : "مواسم"}</span>
        ${seasons.reduce((n,s) => n + (s.episode_count || 0), 0) ? `<span>${seasons.reduce((n,s) => n + (s.episode_count || 0), 0)} حلقة</span>` : ""}</div>
      <p class="desc">${esc(d.description)}</p>
      ${(d.tags || []).length ? `<div class="tags">${d.tags.map(t => `<span class="tag">${esc(t)}</span>`).join("")}</div>` : ""}
      <div class="actions"><button class="btn" data-act="open" data-url="${esc(d.url)}">افتح على الجزيرة 360 ↗</button>
      <button class="btn" data-act="ask" data-text="${esc("لخّص لي برنامج «" + d.title + "» وأهم حلقاته")}">اسأل عن البرنامج</button></div></div></div>
      ${seasons.length > 1 ? `<div class="tabs">${seasons.map((s,i) =>
        `<button class="chip" data-act="season" data-id="${s.season_id}" aria-pressed="${i===0}">${esc(s.title || ("الموسم " + s.season_number))}</button>`).join("")}</div>` : ""}
      <div id="eps"><div class="state"><div class="spinner"></div>جارٍ تحميل الحلقات…</div></div>`;
  },
  get_season_episodes(d){
    return `<h2>${esc(d.series_title || "")}${d.season_title && d.season_title !== d.series_title ? " — " + esc(d.season_title) : ""}</h2>` + episodesHTML(d);
  },
  get_video_details(d){
    tellModel(`User is viewing the video "${d.title}" (video_id ${d.id}).`);
    const img = d.cover_image || d.thumbnail;
    const ep = d.episode_info || {};
    return `<div class="hero">${img ? `<img alt="" src="${esc(thumb(img,400,225))}" data-orig="${esc(img)}">` : "<div></div>"}
      <div><h1>${esc(d.title)}</h1>
      <div class="meta">${d.duration && d.duration !== "N/A" ? `<span>⏱ ${esc(d.duration)}</span>` : ""}
        ${d.quality ? `<span>${esc(d.quality)}</span>` : ""}${d.release_year ? `<span>${esc(d.release_year)}</span>` : ""}
        ${(ep.seriesInformation || {}).title ? `<span>${esc(ep.seriesInformation.title)}${ep.episodeNumber ? " · الحلقة " + esc(ep.episodeNumber) : ""}</span>` : ""}</div>
      <p class="desc">${esc(d.description)}</p>
      ${lockText(d.access_level) ? `<span class="lock">${esc(lockText(d.access_level))}</span>` : ""}
      ${(d.tags || []).length ? `<div class="tags">${d.tags.slice(0,10).map(t => `<span class="tag">${esc(t)}</span>`).join("")}</div>` : ""}
      <div class="actions"><button class="btn primary" data-act="play" data-id="${esc(d.id)}">▶ شاهد هنا</button>
      <button class="btn" data-act="open" data-url="${esc(d.watch_url)}">افتح على الجزيرة 360 ↗</button>
      ${(ep.seriesInformation || {}).id ? `<button class="btn" data-act="series" data-id="${esc(ep.seriesInformation.id)}">كل حلقات البرنامج</button>` : ""}
      <button class="btn" data-act="ask" data-text="${esc("حدثني أكثر عن حلقة «" + d.title + "»")}">اسأل عنها</button></div></div></div>`;
  },
  play_video(d){
    tellModel(`User is watching "${d.title}" (video_id ${d.id}) in the embedded Al Jazeera 360 player.`);
    const poster = d.thumbnail ? `<img class="poster" alt="" src="${esc(d.thumbnail)}">` : "";
    setTimeout(() => startPlayer(d), 0);
    return `<h2>${esc(d.title)}</h2>
      <div class="player" id="player">${poster}<div class="overlay"><div class="spinner"></div>جارٍ تجهيز المشغّل…</div></div>
      <div class="actions" style="margin-top:10px">
        <button class="btn" data-act="fullscreen">⛶ ملء الشاشة</button>
        <button class="btn" data-act="open" data-url="${esc(d.watch_url)}">افتح على الجزيرة 360 ↗</button>
        <button class="btn" data-act="video" data-id="${esc(d.id)}">التفاصيل</button></div>
      <p class="note">يعمل المشغّل الرسمي للجزيرة 360 داخل المحادثة. إذا لم يبدأ التشغيل، افتح الحلقة على الموقع.${
        d.requires_sign_in ? " هذه الحلقة تتطلب تسجيل الدخول على الجزيرة 360." : ""}</p>`;
  },
};

function episodesHTML(d){
  const eps = d.episodes || [];
  if (!eps.length) return `<div class="state">لا توجد حلقات.</div>`;
  return `<div class="eps">${eps.map(e => `<button class="ep" data-act="video" data-id="${esc(e.id)}">
    <div class="thumb">${e.thumbnail ? `<img loading="lazy" alt="" src="${esc(thumb(e.thumbnail,400,225))}" data-orig="${esc(e.thumbnail)}">` : ""}
    ${e.duration && e.duration !== "N/A" ? `<span class="dur">${esc(e.duration)}</span>` : ""}</div>
    <div><div class="t" style="font-weight:600">${e.episode_number ? esc(e.episode_number) + ". " : ""}${esc(e.title)}</div>
    <div class="s" style="color:var(--muted);font-size:12.5px">${esc((e.description || "").slice(0,140))}</div>
    ${lockText(e.access_level) ? `<span class="lock">${esc(lockText(e.access_level))}</span>` : ""}</div></button>`).join("")}</div>`;
}

async function hasProtectedPlayback(){
  if (!navigator.requestMediaKeySystemAccess) return false;
  const cfg = [{initDataTypes:["cenc"], videoCapabilities:[{contentType:'video/mp4; codecs="avc1.42E01E"'}]}];
  for (const ks of ["com.widevine.alpha","com.microsoft.playready","com.apple.fps.1_0","com.apple.fps"]) {
    try { await navigator.requestMediaKeySystemAccess(ks, cfg); return true; } catch(e){}
  }
  return false;
}
async function startPlayer(d){
  const box = document.getElementById("player"); if (!box) return;
  const drm = await hasProtectedPlayback();
  if (!drm) {
    box.querySelector(".overlay").innerHTML = `<div>هذا التطبيق لا يسمح بتشغيل الفيديو المحمي داخل المحادثة.</div>
      <button class="btn primary" data-act="open" data-url="${esc(d.watch_url)}">▶ شاهد على الجزيرة 360</button>`;
    return;
  }
  const f = document.createElement("iframe");
  f.src = d.embed_url || d.watch_url;
  f.allow = "autoplay; encrypted-media; fullscreen; picture-in-picture";
  f.allowFullscreen = true; f.referrerPolicy = "strict-origin-when-cross-origin";
  f.title = d.title || "Al Jazeera 360";
  f.addEventListener("load", () => { const o = box.querySelector(".overlay"); if (o) o.remove(); const p = box.querySelector(".poster"); if (p) p.remove(); });
  box.appendChild(f);
}

async function loadSeason(seasonId){
  const el = document.getElementById("eps"); if (!el) return;
  el.innerHTML = `<div class="state"><div class="spinner"></div>جارٍ تحميل الحلقات…</div>`;
  $app.querySelectorAll('[data-act="season"]').forEach(b => b.setAttribute("aria-pressed", String(b.dataset.id == seasonId)));
  try {
    const d = parseResult(await callTool("get_season_episodes", {season_id: Number(seasonId), max_episodes: 50}));
    if (document.getElementById("eps") === el) el.innerHTML = d && !d.error ? episodesHTML(d) : `<div class="state">تعذّر تحميل الحلقات.</div>`;
    wireImages(el); reportSize();
  } catch(e){ el.innerHTML = `<div class="state">تعذّر تحميل الحلقات.</div>`; }
}
function wireImages(root){
  root.querySelectorAll("img[data-orig]").forEach(img => img.addEventListener("error", () => {
    if (img.src !== img.dataset.orig) img.src = img.dataset.orig; else img.remove();
  }));
}

function show(tool, data, push){
  if (push && current) history.push(current);
  current = {tool, data};
  if (!data) return renderState("لا توجد بيانات.");
  if (data.error) return renderState("تعذّر جلب البيانات من الجزيرة 360: " + data.error);
  const v = views[tool] || guessView(data);
  mount(v ? v(data) : `<div class="state">لا يوجد عرض لهذه البيانات.</div>`);
  window.scrollTo(0, 0);
}
function guessView(d){
  if (d.results) return views.search_videos;
  if (d.programs) return views.browse_section;
  if (d.categories && d.featured) return views.get_trending_content;
  if (d.latest_episodes) return views.get_latest_episodes;
  if (d.seasons) return views.get_series_details;
  if (d.episodes) return views.get_season_episodes;
  if (d.embed_url) return views.play_video;
  if (d.watch_url && d.title) return views.get_video_details;
  return null;
}
async function go(tool, args){
  renderState("جارٍ التحميل…", true);
  try { show(tool, parseResult(await callTool(tool, args)), true); }
  catch(e){ renderState("تعذّر الاتصال بالخادم: " + e.message); }
}

function onToolResult(res){
  // The initial result of the tool the model called.
  const d = parseResult(res);
  const tool = initialTool;
  history.length = 0; current = null;
  show(tool && views[tool] ? tool : null, d, false);
}

/* ------------------------------------------------------------------ events */
$app.addEventListener("click", (ev) => {
  const b = ev.target.closest("[data-act]"); if (!b || b.tagName === "FORM") return;
  const {act, id, url, text} = b.dataset;
  if (act === "back") { const prev = history.pop(); if (prev) { current = null; show(prev.tool, prev.data, false); } }
  else if (act === "video") go("get_video_details", {video_id: Number(id)});
  else if (act === "series") go("get_series_details", {series_id: Number(id)});
  else if (act === "play") go("play_video", {video_id: Number(id)});
  else if (act === "season") loadSeason(id);
  else if (act === "open") openLink(url);
  else if (act === "ask") sendMessage(text);
  else if (act === "fullscreen") requestFullscreen();
  else if (act === "section") { activeChip = id; id === "__trending" ? go("get_trending_content", {}) : go("browse_section", {section_id: id}); }
});
$app.addEventListener("submit", (ev) => {
  ev.preventDefault();
  const q = new FormData(ev.target).get("q"); if (q && String(q).trim()) go("search_videos", {query: String(q).trim(), max_results: 24});
});

/* -------------------------------------------------------------------- boot */
(async function boot(){
  if (openai) {
    applyContext({theme: openai.theme});
    if (openai.toolOutput) show(null, openai.toolOutput, false);
    window.addEventListener("openai:set_globals", () => { if (openai.toolOutput) show(null, openai.toolOutput, false); });
    return;
  }
  try {
    const init = await request("ui/initialize", {
      protocolVersion: "2026-01-26",
      appInfo: {name: "aljazeera360-app", version: "1.0.0"},
      appCapabilities: {availableDisplayModes: ["inline", "fullscreen"]},
    });
    hostCaps = (init && init.hostCapabilities) || {};
    const ti = init && init.hostContext && init.hostContext.toolInfo;
    initialTool = (ti && ti.tool && ti.tool.name) || null;
    applyContext(init && init.hostContext);
    notify("ui/notifications/initialized", {});
  } catch(e) {
    renderState("لم يتم الاتصال بالمضيف.");
  }
})();
})();
</script>
</body>
</html>
"""


def register_ui(mcp) -> None:
    """Register the ``ui://`` view resource on a FastMCP server."""
    if not UI_ENABLED:
        return

    @mcp.resource(
        APP_URI,
        name="aljazeera360-app",
        title="Al Jazeera 360 — interactive view",
        description="Interactive catalog, series browser and player for Al Jazeera 360 (MCP Apps view).",
        mime_type=APP_MIME_TYPE,
        meta=RESOURCE_META,
    )
    def aljazeera360_app() -> str:
        return APP_HTML
