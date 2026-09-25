"""
MCP Apps (interactive UI) for the Al Jazeera 360 MCP server.

Implements the MCP Apps extension (``io.modelcontextprotocol/ui``, spec
2026-01-26): tools declare a ``ui://`` resource in their ``_meta``, and hosts
that support the extension (Claude, ChatGPT, and others) render that resource
as a sandboxed HTML view next to the tool result. Hosts without support ignore
the metadata and keep using the plain JSON text, so nothing changes for them.

One self-contained single-page view serves every UI-bound tool. It uses
the aljazeera360.com design system (AlJazeera typeface, black background,
#00B7D4 primary, official logo, poster rows and 16:9 cards), always dark:

* Home     — hero carousel with calligraphy title art, then editorial rows.
* Catalog  — search results, section rows and latest episodes as cards,
             with the site-style section nav and a search box.
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
    "https://static.diceplatform.com",           # AlJazeera fonts, hero art
    "https://content-images.onvesper.com",       # Al Jazeera 360 logo
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
<meta name="color-scheme" content="dark">
<title>الجزيرة 360</title>
<style>
/* Design system of aljazeera360.com (Vesper/Dice theme), read from the live
   site: AlJazeera typeface, black background, white text, #00B7D4 primary. */
@font-face{font-family:"AJ";font-weight:400;font-display:swap;
  src:url("https://static.diceplatform.com/prod/original/dce.aljazeera/fonts/AlJazeera-Regular.ttf") format("truetype")}
@font-face{font-family:"AJ";font-weight:700;font-display:swap;
  src:url("https://static.diceplatform.com/prod/original/dce.aljazeera/fonts/AlJazeera-Bold.ttf") format("truetype")}
:root{
  --primary:#00B7D4; --bg:#000; --text:#fff; --text-2:rgba(255,255,255,.9); --muted:rgba(255,255,255,.62);
  --line:rgba(255,255,255,.32); --surface:#141414; --surface-2:#1f1f1f; --alert:#b60e0e;
  --r-card:5px; --r-btn:4px; --gutter:16px;
  color-scheme:dark;
}
*{box-sizing:border-box}
html,body{margin:0;background:var(--bg);color:var(--text);
  font:400 16px/1.5 "AJ",Tahoma,Arial,sans-serif;-webkit-font-smoothing:antialiased}
button{font:inherit;color:inherit;cursor:pointer;background:none;border:0;padding:0}
img{display:block}
.app{padding:0 0 22px}

/* ---- header (logo · nav · search), like the site's top bar ---- */
.hdr{display:flex;align-items:center;gap:18px;padding:12px var(--gutter);position:relative;z-index:3;
  background:linear-gradient(to bottom,rgba(0,0,0,.85),rgba(0,0,0,0))}
.logo{flex:none;display:flex;align-items:center}
.logo img{height:34px;width:auto}
.logo .txt{font-weight:700;font-size:18px;display:none}
.nav{flex:1;display:flex;gap:18px;overflow-x:auto;scrollbar-width:none;white-space:nowrap}
.nav::-webkit-scrollbar{display:none}
.nav button{font-size:16px;color:var(--text);padding:4px 0}
.nav button:hover,.nav button[aria-current="true"]{color:var(--primary)}
.icon-btn{flex:none;width:36px;height:36px;display:grid;place-items:center;border-radius:50%}
.icon-btn:hover{color:var(--primary)}
.icon-btn svg{width:20px;height:20px}
.search{display:none;padding:0 var(--gutter) 10px}
.search.open{display:flex;gap:8px}
.search input{flex:1;min-width:0;background:var(--surface);border:1px solid var(--line);color:var(--text);
  border-radius:var(--r-btn);padding:10px 14px;font:inherit}
.search input:focus{outline:none;border-color:var(--primary)}
.hdr .back{margin-inline-end:-10px;color:var(--text)}
.hdr .back svg{width:22px;height:22px}

/* ---- buttons ---- */
.btn{display:inline-flex;align-items:center;justify-content:center;gap:10px;min-height:46px;padding:10px 20px;
  border-radius:var(--r-btn);font-weight:700;font-size:16px;line-height:1}
.btn svg{width:16px;height:16px;flex:none}
.btn-primary{background:var(--primary);color:#fff}
.btn-primary:hover{background:#fff;color:#000}
.btn-light{background:#fff;color:#000;border-radius:3px}
.btn-light:hover{background:var(--primary);color:#fff}
.btn-ghost{color:var(--text);font-weight:400;padding:10px 12px}
.btn-ghost:hover{color:var(--primary)}
.actions{display:flex;flex-wrap:wrap;align-items:center;gap:10px}

/* ---- hero (home carousel, series, video) ---- */
.hero{position:relative;min-height:360px;display:flex;align-items:flex-end;overflow:hidden}
.hero .bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:left center}
.hero::after{content:"";position:absolute;inset:0;pointer-events:none;
  background:linear-gradient(to left,rgba(0,0,0,.92) 0%,rgba(0,0,0,.6) 38%,rgba(0,0,0,0) 72%),
             linear-gradient(to top,#000 0%,rgba(0,0,0,0) 45%)}
.hero .inner{position:relative;z-index:1;padding:80px var(--gutter) 22px;max-width:560px}
.hero .logoart{max-width:230px;max-height:96px;width:auto;margin-bottom:14px}
.hero h1{font-weight:700;font-size:30px;line-height:1.25;margin:0 0 10px}
.hero .sub{font-weight:700;font-size:16px;margin:0 0 10px}
.hero .desc{font-size:16px;line-height:1.75;color:var(--text-2);margin:0 0 18px;
  display:-webkit-box;-webkit-line-clamp:4;-webkit-box-orient:vertical;overflow:hidden}
.meta{display:flex;flex-wrap:wrap;align-items:center;gap:6px 0;color:var(--muted);font-size:15px;margin:0 0 12px}
.meta span+span::before{content:"";display:inline-block;width:5px;height:5px;border-radius:50%;
  background:var(--muted);margin:0 10px;vertical-align:middle}
.lock{display:inline-block;font-size:12px;border:1px solid var(--primary);color:var(--primary);
  border-radius:2px;padding:2px 8px;margin-bottom:14px}
.dots{position:absolute;bottom:10px;left:0;right:0;display:flex;justify-content:center;gap:10px;z-index:2}
.dots button{width:10px;height:10px;border-radius:50%;background:rgba(255,255,255,.4)}
.dots button[aria-current="true"]{background:#fff}
.arrow{position:absolute;top:50%;transform:translateY(-50%);z-index:2;width:36px;height:56px;display:grid;place-items:center;color:#fff;opacity:.8}
.arrow:hover{opacity:1;color:var(--primary)}
.arrow svg{width:22px;height:22px}
.arrow.prev{right:2px}.arrow.next{left:2px}

/* the header floats over a hero that directly follows it, as on the site */
.search:not(.open) + .hero, .search:not(.open) + #hero > .hero{margin-top:-60px}
.search:not(.open) + .hero .inner, .search:not(.open) + #hero > .hero .inner{padding-top:110px}

/* ---- rows of cards ---- */
.row-title{font-weight:700;font-size:17.6px;color:var(--text-2);margin:26px var(--gutter) 12px}
.row{display:grid;grid-auto-flow:column;gap:12px;overflow-x:auto;padding:0 var(--gutter) 6px;
  scroll-snap-type:x proximity;scrollbar-width:none}
.row::-webkit-scrollbar{display:none}
.row.video{grid-auto-columns:240px}
.row.series{grid-auto-columns:150px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(210px,1fr));gap:18px 12px;padding:0 var(--gutter)}
.card{scroll-snap-align:start;text-align:start;display:flex;flex-direction:column;gap:8px}
.card .img{position:relative;border-radius:var(--r-card);overflow:hidden;background:var(--surface-2);aspect-ratio:16/9}
.card.poster .img{aspect-ratio:5/7}
.card .img img{width:100%;height:100%;object-fit:cover}
.card:hover .img,.card:focus-visible .img{outline:2px solid var(--primary);outline-offset:2px}
.card:focus-visible{outline:none}
.card .t{font-weight:700;font-size:15px;line-height:1.4;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.card .s{font-size:13px;color:var(--muted);margin-top:-4px;display:-webkit-box;-webkit-line-clamp:1;-webkit-box-orient:vertical;overflow:hidden}
.chip{display:inline-block;border:1px solid var(--line);border-radius:2px;padding:3px 8px;font-size:12px;line-height:1.3;direction:ltr;color:var(--text-2)}
.card .img .chip{position:absolute;bottom:6px;left:6px;background:rgba(0,0,0,.7);border-color:transparent}
.card .img .live{position:absolute;top:6px;right:6px;background:var(--alert);color:#fff;font-size:12px;font-weight:700;padding:2px 8px;border-radius:2px}

/* ---- tabs + episodes (series page) ---- */
.tabs{display:flex;gap:30px;overflow-x:auto;padding:0 var(--gutter);margin:6px 0 18px;scrollbar-width:none}
.tabs button{font-weight:700;font-size:17px;color:var(--muted);padding:6px 0 8px;border-bottom:3px solid transparent;white-space:nowrap}
.tabs button[aria-selected="true"]{color:#fff;border-bottom-color:var(--primary)}
.eps{display:flex;flex-direction:column;gap:22px;padding:0 var(--gutter)}
.ep{display:grid;grid-template-columns:260px 1fr;gap:20px;align-items:start;text-align:start}
.ep .img{position:relative;border-radius:var(--r-card);overflow:hidden;background:var(--surface-2);aspect-ratio:16/9}
.ep .img img{width:100%;height:100%;object-fit:cover}
.ep .img .play{position:absolute;inset:0;display:grid;place-items:center;opacity:0;transition:opacity .15s;background:rgba(0,0,0,.35)}
.ep .img .play svg{width:40px;height:40px;color:#fff}
.ep:hover .img .play,.ep:focus-visible .img .play{opacity:1}
.ep:hover .img,.ep:focus-visible .img{outline:2px solid var(--primary);outline-offset:2px}
.ep:focus-visible{outline:none}
.ep h3{font-weight:700;font-size:16px;margin:2px 0 8px}
.ep p{font-size:15px;line-height:1.7;color:var(--text-2);margin:0 0 10px;
  display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical;overflow:hidden}
.ep .chips{display:flex;gap:8px;flex-wrap:wrap}

/* ---- player ---- */
.stage{position:relative;aspect-ratio:16/9;background:#000;margin:0 var(--gutter);border-radius:var(--r-card);overflow:hidden}
.stage iframe{position:absolute;inset:0;width:100%;height:100%;border:0}
.stage .poster{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:.4}
.stage .overlay{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;
  gap:16px;text-align:center;padding:20px;font-size:16px}
.below{padding:16px var(--gutter) 0}
.below h1{font-weight:700;font-size:22px;margin:0 0 8px}
.note{color:var(--muted);font-size:13px;margin:12px 0 0}

/* ---- diagnostics ---- */
table.diag{width:100%;border-collapse:collapse;font-size:15px}
table.diag td{padding:10px 8px;border-bottom:1px solid var(--line);vertical-align:top}
table.diag td:first-child{font-weight:700}
table.diag td:last-child{color:var(--muted);font-size:13px;direction:ltr;text-align:end}
table.diag .ok{color:var(--primary);white-space:nowrap}
table.diag .bad{color:#ff6b6b;white-space:nowrap}

/* ---- states ---- */
.state{padding:64px var(--gutter);text-align:center;color:var(--muted)}
.spinner{width:44px;height:44px;margin:0 auto 14px;border-radius:50%;
  background:conic-gradient(from 90deg,rgba(0,183,212,0),#00B7D4 55%,#fff);animation:spin .9s linear infinite;
  -webkit-mask:radial-gradient(farthest-side,transparent calc(100% - 3px),#000 calc(100% - 3px));
          mask:radial-gradient(farthest-side,transparent calc(100% - 3px),#000 calc(100% - 3px))}
@keyframes spin{to{transform:rotate(360deg)}}

@media (max-width:560px){
  .hero{min-height:300px}.hero h1{font-size:24px}.hero .logoart{max-width:170px}
  .ep{grid-template-columns:1fr;gap:10px}.row.video{grid-auto-columns:200px}.row.series{grid-auto-columns:128px}
  .grid{grid-template-columns:repeat(auto-fill,minmax(160px,1fr))}
}
</style>
</head>
<body>
<div class="app" id="app"><div class="state"><div class="spinner"></div>جارٍ التحميل…</div></div>
<script>
(() => {
"use strict";
const SITE = "https://www.aljazeera360.com";
const LOGO = "https://content-images.onvesper.com/prod/AUTOx600-webp/dce.aljazeera/settings/AJ_360_White_Logo.ZIUa6.moCtF.fxIHZ.png?ts=1740478474";
const NAV = [
  ["__trending","الرئيسية"], ["AJ360-Originals","أعمال أصلية"], ["AJA","الجزيرة"], ["AJD","الوثائقية"],
  ["Atheer","أثير"], ["AJ-Plus","AJ+ عربي"], ["Podcast","بودكاست"], ["Documentaries","وثائقيات"],
  ["Talk Show","برامج حوارية"], ["Investigative Show","برامج تحقيقية"]
];
const ICON = {
  play:'<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M7 4.5v15l12.5-7.5z"/></svg>',
  search:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" aria-hidden="true"><circle cx="10.5" cy="10.5" r="6.5"/><path d="M15.5 15.5 21 21"/></svg>',
  share:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round" aria-hidden="true"><path d="M21 3 3 10.5l7.5 3L21 3zM21 3l-7.5 18-3-7.5"/></svg>',
  prev:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="m9 5 7 7-7 7"/></svg>',
  next:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="m15 5-7 7 7 7"/></svg>',
  back:'<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="m9 5 7 7-7 7"/></svg>',
  full:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M4 9V4h5M20 9V4h-5M4 15v5h5M20 15v5h-5"/></svg>',
  ask:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M4 5h16v11H9l-5 4z"/></svg>',
};
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
    case "ui/notifications/host-context-changed": break;   // the site look is always dark
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
  // dve-images resizes on the fly via a /WxH/ path, like the site does.
  return url.replace("https://dve-images.imggaming.com/original/", `https://dve-images.imggaming.com/${w}x${h}/`);
}
const isSeries = (t) => /SERIES/i.test(t || "");
const isLive = (t) => /LIVE/i.test(t || "");
const lockText = (a) => a === "GRANTED_ON_SIGN_IN" ? "يتطلب تسجيل الدخول" : (a && a !== "GRANTED" && a !== "UNKNOWN" ? "محتوى مقيّد" : "");
const dur = (d) => d && d !== "N/A" ? String(d).replace(/^00:/, "") : "";
function dateAr(iso){
  if (!iso) return "";
  const d = new Date(iso); if (isNaN(d)) return "";
  return `${d.getUTCDate()}/${d.getUTCMonth() + 1}/${d.getUTCFullYear()}`;   // site format: 21/9/2026
}
function card(it){
  return {
    kind: isSeries(it.type) ? "series" : isLive(it.type) ? "live" : "video",
    url: it.watch_url || it.url || "",
    id: String(it.id || ""),
    title: it.title || "",
    sub: it.series || "",
    image: it.thumbnail || it.poster || it.image || "",
    duration: dur(it.duration),
  };
}
const cards = (arr) => (arr || []).filter(x => x && x.id).map(card);

/* ------------------------------------------------------------------ render */
function esc(s){ return String(s == null ? "" : s).replace(/[&<>"']/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c])); }
const history = [];
let current = null, lastInput = {}, activeNav = "", initialTool = null, searchOpen = false, heroTimer = null, hostInfo = null;

function header(){
  return `<header class="hdr">
      ${history.length ? `<button class="icon-btn back" data-act="back" aria-label="رجوع" title="رجوع">${ICON.back}</button>` : ""}
      <button class="logo" data-act="nav" data-id="__trending" aria-label="الجزيرة 360 — الرئيسية">
        <img class="logo-img" src="${LOGO}" alt="الجزيرة 360"><span class="txt">الجزيرة 360</span></button>
      <nav class="nav">${NAV.map(([id,l]) =>
        `<button data-act="nav" data-id="${esc(id)}" aria-current="${activeNav===id}">${esc(l)}</button>`).join("")}</nav>
      <button class="icon-btn" data-act="toggle-search" aria-label="بحث">${ICON.search}</button>
    </header>
    <form class="search${searchOpen ? " open" : ""}"><input name="q" placeholder="ابحث عن برامج، حلقات، مواضيع…" aria-label="بحث">
      <button class="btn btn-primary" type="submit">بحث</button></form>`;
}
function img(url, w, h, cls){
  if (!url) return "";
  return `<img ${cls ? `class="${cls}"` : ""} loading="lazy" alt="" src="${esc(thumb(url, w, h))}" data-orig="${esc(url)}">`;
}
function cardHTML(c){
  const poster = c.kind === "series";
  const act = c.kind === "live" ? `data-act="open" data-url="${esc(c.url)}"` : `data-act="${c.kind}" data-id="${esc(c.id)}"`;
  return `<button class="card${poster ? " poster" : ""}" ${act} aria-label="${esc(c.title)}">
    <div class="img">${img(c.image, poster ? 300 : 400, poster ? 420 : 225)}
      ${c.duration ? `<span class="chip">${esc(c.duration)}</span>` : ""}${c.kind === "live" ? `<span class="live">مباشر</span>` : ""}</div>
    ${poster ? "" : `<div class="t">${esc(c.title)}</div>${c.sub ? `<div class="s">${esc(c.sub)}</div>` : ""}`}</button>`;
}
function rowHTML(title, items, asGrid){
  if (!items.length) return "";
  const allPosters = items.every(c => c.kind === "series");
  const body = asGrid
    ? `<div class="grid">${items.map(cardHTML).join("")}</div>`
    : `<div class="row ${allPosters ? "series" : "video"}">${items.map(cardHTML).join("")}</div>`;
  return `${title ? `<h2 class="row-title">${esc(title)}</h2>` : ""}${body}`;
}
function rowsHTML(rows){
  const html = rows.map(r => rowHTML(r.title, r.items, false)).join("");
  return html || `<div class="state">لا توجد نتائج.</div>`;
}
function wireImages(root){
  root.querySelectorAll("img[data-orig]").forEach(im => im.addEventListener("error", () => {
    if (im.src !== im.dataset.orig) im.src = im.dataset.orig; else im.remove();
  }));
}
function mount(html){
  clearInterval(heroTimer);
  $app.innerHTML = header() + html;
  const logo = $app.querySelector(".logo-img");
  if (logo) logo.addEventListener("error", () => {
    const box = logo.parentNode; logo.remove();
    if (box) box.querySelector(".txt").style.display = "block";   // text fallback
  });
  wireImages($app);
  reportSize();
}
function renderState(text, spin){ mount(`<div class="state">${spin ? '<div class="spinner"></div>' : ""}${esc(text)}</div>`); }

/* ---- hero ---- */
function heroHTML(o){
  // o: {bg, logoart, title, sub, meta[], desc, lock, buttons}
  return `<section class="hero">${o.bg ? `<img class="bg" alt="" src="${esc(o.bg)}"${o.bgOrig ? ` data-orig="${esc(o.bgOrig)}"` : ""}>` : ""}
    <div class="inner">
      ${o.logoart ? `<img class="logoart" alt="${esc(o.title)}" src="${esc(o.logoart)}">` : `<h1>${esc(o.title)}</h1>`}
      ${o.sub ? `<p class="sub">${esc(o.sub)}</p>` : ""}
      ${(o.meta || []).filter(Boolean).length ? `<div class="meta">${o.meta.filter(Boolean).map(m => `<span>${esc(m)}</span>`).join("")}</div>` : ""}
      ${o.desc ? `<p class="desc">${esc(o.desc)}</p>` : ""}
      ${o.lock ? `<span class="lock">${esc(o.lock)}</span>` : ""}
      <div class="actions">${o.buttons || ""}</div>
    </div>${o.extra || ""}</section>`;
}
function carousel(featured){
  const slides = (featured || []).filter(f => f.image);
  if (!slides.length) return "";
  let i = 0;
  const slide = (f) => heroHTML({
    bg: f.image, logoart: f.title_image, title: f.title, desc: f.description,
    buttons: f.video_id ? `<button class="btn btn-primary" data-act="play" data-id="${esc(f.video_id)}">${esc(f.cta_text || "شاهد الآن")}</button>`
      + (f.series_id ? `<button class="btn btn-ghost" data-act="series" data-id="${esc(f.series_id)}">كل الحلقات</button>` : "") : "",
    extra: slides.length > 1 ? `<button class="arrow prev" data-act="hero-step" data-id="-1" aria-label="السابق">${ICON.prev}</button>
      <button class="arrow next" data-act="hero-step" data-id="1" aria-label="التالي">${ICON.next}</button>
      <div class="dots">${slides.map((_, k) => `<button data-act="hero-go" data-id="${k}" aria-label="${k + 1}" aria-current="${k === 0}"></button>`).join("")}</div>` : "",
  });
  setTimeout(() => {
    const host = document.getElementById("hero"); if (!host) return;
    const go = (k) => {
      i = (k + slides.length) % slides.length;
      host.innerHTML = slide(slides[i]); wireImages(host);
      host.querySelectorAll(".dots button").forEach((b, n) => b.setAttribute("aria-current", String(n === i)));
    };
    host._go = go; host._step = (d) => go(i + d);
    clearInterval(heroTimer);
    if (slides.length > 1) heroTimer = setInterval(() => { if (document.getElementById("hero") === host) host._step(1); else clearInterval(heroTimer); }, 7000);
  }, 0);
  return `<div id="hero">${slide(slides[0])}</div>`;
}

const views = {
  get_trending_content(d){
    activeNav = "__trending";
    tellModel("User is browsing the Al Jazeera 360 home page (trending content).");
    return carousel(d.featured) + rowsHTML((d.categories || []).map(c => ({title:c.name, items:cards(c.items)})));
  },
  browse_section(d){
    activeNav = d.section_id || activeNav;
    tellModel(`User is browsing the Al Jazeera 360 section "${d.section || d.section_id}".`);
    const f = (d.featured || [])[0];
    return `<h2 class="row-title" style="font-size:24px;margin-top:8px">${esc(d.section || "")}</h2>`
      + (f && f.description ? `<p style="margin:0 var(--gutter);color:var(--muted)">${esc(f.description)}</p>` : "")
      + rowsHTML((d.programs || []).map(p => ({title:p.category, items:cards(p.items)})));
  },
  search_videos(d){
    activeNav = "";
    tellModel(`User is viewing Al Jazeera 360 search results for "${d.query}".`);
    const items = cards(d.results);
    return `<h2 class="row-title" style="font-size:22px;margin-top:8px">نتائج البحث عن «${esc(d.query || "")}»</h2>`
      + (items.length ? rowHTML("", items, true) : `<div class="state">لا توجد نتائج.</div>`);
  },
  get_latest_episodes(d){
    activeNav = d.section_id || "";
    return `<h2 class="row-title" style="font-size:22px;margin-top:8px">أحدث الحلقات — ${esc(d.section || "")}</h2>`
      + rowHTML("", cards(d.latest_episodes), true);
  },
  get_series_details(d){
    tellModel(`User is viewing the series "${d.title}" (series_id ${d.id}).`);
    const seasons = d.seasons || [];
    const total = seasons.reduce((n, s) => n + (s.episode_count || 0), 0);
    setTimeout(() => { if (seasons[0]) loadSeason(seasons[0].season_id); }, 0);
    return heroHTML({
      bg: thumb(d.cover || d.poster, 1280, 720), bgOrig: d.cover || d.poster, title: d.title,
      sub: total ? `${d.title} - الحلقات (${total})` : "",
      meta: ["الجزيرة 360", seasons.length > 1 ? `${seasons.length} مواسم` : "", ...(d.tags || []).slice(0, 4)],
      desc: d.description,
      buttons: `<button class="btn btn-primary" data-act="play-first" id="play-first" disabled style="opacity:.6">${ICON.play} بدء المشاهدة</button>
        <button class="btn btn-ghost" data-act="open" data-url="${esc(d.url)}">${ICON.share} شارك</button>
        <button class="btn btn-ghost" data-act="ask" data-text="${esc("لخّص لي برنامج «" + d.title + "» وأهم حلقاته")}">${ICON.ask} اسأل عنه</button>`,
    }) + `<div class="tabs" role="tablist">${seasons.length > 1
        ? seasons.map((s, k) => `<button role="tab" data-act="season" data-id="${s.season_id}" aria-selected="${k === 0}">${esc(s.title || ("الموسم " + s.season_number))}</button>`).join("")
        : `<button role="tab" aria-selected="true">حلقات</button>`}</div>
      <div id="eps"><div class="state"><div class="spinner"></div>جارٍ تحميل الحلقات…</div></div>`;
  },
  get_season_episodes(d){
    return `<h2 class="row-title" style="font-size:22px;margin-top:8px">${esc(d.series_title || d.season_title || "")}</h2>
      <div class="tabs"><button aria-selected="true">${esc(d.season_title || "حلقات")}</button></div>` + episodesHTML(d);
  },
  get_video_details(d){
    tellModel(`User is viewing the video "${d.title}" (video_id ${d.id}).`);
    const ep = d.episode_info || {}, si = ep.seriesInformation || {};
    return heroHTML({
      bg: thumb(d.cover_image || d.thumbnail, 1280, 720), bgOrig: d.cover_image || d.thumbnail, title: d.title,
      sub: si.title ? `${si.title}${ep.episodeNumber ? " - الحلقة " + ep.episodeNumber : ""}` : "",
      meta: [dur(d.duration), d.release_year, d.quality, ...(d.tags || []).slice(0, 3)],
      desc: d.description, lock: lockText(d.access_level),
      buttons: `<button class="btn btn-primary" data-act="play" data-id="${esc(d.id)}">${ICON.play} شاهد الآن</button>
        ${si.id ? `<button class="btn btn-light" data-act="series" data-id="${esc(si.id)}">كل الحلقات</button>` : ""}
        <button class="btn btn-ghost" data-act="open" data-url="${esc(d.watch_url)}">${ICON.share} شارك</button>
        <button class="btn btn-ghost" data-act="ask" data-text="${esc("حدثني أكثر عن حلقة «" + d.title + "»")}">${ICON.ask} اسأل عنها</button>`,
    });
  },
  run_diagnostics(d){
    tellModel("User opened the Al Jazeera 360 playback diagnostics.");
    setTimeout(runDiagnostics, 0);
    return `<div class="below"><h1>فحص التشغيل داخل المحادثة</h1>
      <div id="diag"><div class="state"><div class="spinner"></div>جارٍ فحص ما يسمح به هذا التطبيق…</div></div></div>`;
  },
  play_video(d){
    tellModel(`User is watching "${d.title}" (video_id ${d.id}) in the embedded Al Jazeera 360 player.`);
    setTimeout(() => startPlayer(d), 0);
    return `<div class="stage" id="player">${d.thumbnail ? `<img class="poster" alt="" src="${esc(thumb(d.thumbnail, 1280, 720))}" data-orig="${esc(d.thumbnail)}">` : ""}
        <div class="overlay"><div class="spinner"></div></div></div>
      <div class="below"><h1>${esc(d.title)}</h1>
        <div class="meta">${[d.series_title, d.episode_number ? "الحلقة " + d.episode_number : "", dur(d.duration)].filter(Boolean).map(m => `<span>${esc(m)}</span>`).join("")}</div>
        <div class="actions">
          <button class="btn btn-ghost" data-act="fullscreen">${ICON.full} ملء الشاشة</button>
          <button class="btn btn-ghost" data-act="open" data-url="${esc(d.watch_url)}">${ICON.share} افتح على الجزيرة 360</button>
          ${d.series_id ? `<button class="btn btn-ghost" data-act="series" data-id="${esc(d.series_id)}">كل الحلقات</button>` : ""}
          <button class="btn btn-ghost" data-act="video" data-id="${esc(d.id)}">التفاصيل</button></div>
        <p class="note">المشغّل الرسمي للجزيرة 360.${d.requires_sign_in ? " هذه الحلقة تتطلب تسجيل الدخول." : ""}</p></div>`;
  },
};

function episodesHTML(d){
  const eps = d.episodes || [];
  if (!eps.length) return `<div class="state">لا توجد حلقات.</div>`;
  return `<div class="eps">${eps.map(e => `<button class="ep" data-act="video" data-id="${esc(e.id)}">
    <div class="img">${img(e.thumbnail, 320, 180)}<span class="play">${ICON.play}</span></div>
    <div><h3>${e.episode_number ? esc(e.episode_number) + ". " : ""}${esc(e.title)}</h3>
      <p>${esc(e.description || "")}</p>
      <div class="chips">${dur(e.duration) ? `<span class="chip">${esc(dur(e.duration))}</span>` : ""}
        ${dateAr(e.published_date) ? `<span class="chip">${esc(dateAr(e.published_date))}</span>` : ""}
        ${lockText(e.access_level) ? `<span class="chip" style="direction:rtl">${esc(lockText(e.access_level))}</span>` : ""}</div></div></button>`).join("")}</div>`;
}

/* ------------------------------------------------------ playback diagnostics */
// What the host sandbox allows decides whether the official (DRM) player can
// run inside the chat. These probes collect capability flags only: no IP
// address, no personal data.
async function probe(){
  const cfg = [{initDataTypes:["cenc"], videoCapabilities:[{contentType:'video/mp4; codecs="avc1.42E01E"'}]}];
  const eme = {};
  for (const [k, ks] of [["widevine","com.widevine.alpha"],["playready","com.microsoft.playready"],["fairplay","com.apple.fps.1_0"],["clearkey","org.w3.clearkey"]]) {
    try {
      if (!navigator.requestMediaKeySystemAccess) throw {name:"NoEME"};
      await navigator.requestMediaKeySystemAccess(ks, cfg); eme[k] = "yes";
    } catch(e){ eme[k] = ({SecurityError:"blocked", NotSupportedError:"unsupported", NotAllowedError:"denied"})[e && e.name] || (e && e.name) || "no"; }
  }
  const pp = document.permissionsPolicy || document.featurePolicy;
  const allows = (f) => pp && pp.allowsFeature ? (pp.allowsFeature(f) ? "yes" : "no") : "?";
  return {  // most important first: the Worker logs a bounded string
    host: hostInfo ? `${hostInfo.name || "?"} ${hostInfo.version || ""}`.trim() : (openai ? "openai-apps-sdk" : "?"),
    origin: location.hostname.replace(/^[^.]+\.(?=[^.]+\.[^.]+$)/, "*."),
    drm: ["widevine","playready","fairplay"].some(k => eme[k] === "yes") ? "yes" : "no",
    widevine: eme.widevine, playready: eme.playready, fairplay: eme.fairplay, clearkey: eme.clearkey,
    pp_eme: allows("encrypted-media"), pp_fullscreen: allows("fullscreen"), pp_autoplay: allows("autoplay"),
    mse: window.MediaSource && MediaSource.isTypeSupported('video/mp4; codecs="avc1.42E01E"') ? "yes" : "no",
    fullscreen_api: document.fullscreenEnabled ? "yes" : "no",
  };
}
function compact(o){ return Object.entries(o).map(([k, v]) => `${k}=${v}`).join(";"); }
function report(kind, o){ callTool("run_diagnostics", {report: `${kind} ${compact(o)}`}).catch(() => {}); }

// Watches an iframe: "loaded", "blocked" (host CSP refused the frame) or "timeout".
function watchFrame(f, ms){
  return new Promise((resolve) => {
    let done = false;
    const finish = (r) => { if (!done) { done = true; document.removeEventListener("securitypolicyviolation", onCsp); resolve(r); } };
    const onCsp = (e) => { if (/frame/.test(e.violatedDirective || e.effectiveDirective || "") && String(e.blockedURI || "").includes("aljazeera360")) finish("blocked"); };
    document.addEventListener("securitypolicyviolation", onCsp);
    f.addEventListener("load", () => setTimeout(() => finish("loaded"), 150));
    setTimeout(() => finish("timeout"), ms);
  });
}
function fallback(box, d, text){
  const o = box.querySelector(".overlay") || box.appendChild(Object.assign(document.createElement("div"), {className: "overlay"}));
  o.innerHTML = `<div>${esc(text)}</div>
    <button class="btn btn-primary" data-act="open" data-url="${esc(d.watch_url)}">${ICON.play} شاهد على الجزيرة 360</button>`;
}
async function startPlayer(d){
  const box = document.getElementById("player"); if (!box) return;
  const p = await probe();
  if (p.drm !== "yes") {
    fallback(box, d, "هذا التطبيق لا يسمح بتشغيل الفيديو المحمي داخل المحادثة.");
    report("player", {vid: d.id, frame: "skipped", ...p});
    return;
  }
  const f = document.createElement("iframe");
  f.src = d.embed_url || d.watch_url;
  f.allow = "autoplay; encrypted-media; fullscreen; picture-in-picture";
  f.allowFullscreen = true; f.referrerPolicy = "strict-origin-when-cross-origin";
  f.title = d.title || "Al Jazeera 360";
  const watched = watchFrame(f, 20000);
  box.appendChild(f);
  const frame = await watched;
  if (frame === "blocked") { f.remove(); fallback(box, d, "هذا التطبيق لا يسمح بعرض مشغّل الجزيرة 360 داخل المحادثة."); }
  else box.querySelectorAll(".overlay,.poster").forEach(n => n.remove());
  report("player", {vid: d.id, frame, ...p});
}

async function runDiagnostics(){
  const el = document.getElementById("diag"); if (!el) return;
  const p = await probe();
  let frame = "skipped";
  const f = document.createElement("iframe");
  f.src = SITE + "/"; f.allow = "autoplay; encrypted-media; fullscreen";
  f.style.cssText = "position:absolute;width:1px;height:1px;opacity:0;pointer-events:none;border:0";
  const watched = watchFrame(f, 20000); document.body.appendChild(f); frame = await watched; f.remove();
  const ok = (v) => v === "yes" || v === "loaded";
  const row = (label, v, hint) => `<tr><td>${esc(label)}</td><td class="${ok(v) ? "ok" : "bad"}">${ok(v) ? "✓ متاح" : "✗ غير متاح"}</td><td>${esc(hint || v)}</td></tr>`;
  const verdict = p.drm === "yes" && frame === "loaded"
    ? "المشغّل الرسمي يقدر يشتغل داخل هذه المحادثة."
    : frame === "blocked" ? "هذا التطبيق يمنع عرض موقع الجزيرة 360 داخل المحادثة، فالتشغيل يتم على الموقع."
    : p.drm !== "yes" ? "هذا التطبيق لا يسمح بتشغيل الفيديو المحمي (DRM) داخل المحادثة، فالتشغيل يتم على الموقع."
    : "تعذّر التأكد من تحميل مشغّل الجزيرة 360 داخل المحادثة.";
  el.innerHTML = `<p class="desc" style="margin:0 0 16px">${esc(verdict)}</p>
    <table class="diag"><tbody>
      ${row("الفيديو المحمي — Widevine", p.widevine)}${row("الفيديو المحمي — PlayReady", p.playready)}${row("الفيديو المحمي — FairPlay", p.fairplay)}
      ${row("إذن الفيديو المحمي من التطبيق", p.pp_eme)}${row("عرض موقع الجزيرة 360 داخل المحادثة", frame)}
      ${row("ملء الشاشة", p.pp_fullscreen === "?" ? p.fullscreen_api : p.pp_fullscreen)}${row("التشغيل التلقائي", p.pp_autoplay)}
      ${row("تشغيل البث (MSE)", p.mse)}</tbody></table>
    <p class="note">التطبيق المضيف: ${esc(p.host)} · ${esc(p.origin)}</p>`;
  reportSize();
  report("diagnostics", {frame, ...p});
}

let firstEpisode = null;
async function loadSeason(seasonId){
  const el = document.getElementById("eps"); if (!el) return;
  el.innerHTML = `<div class="state"><div class="spinner"></div>جارٍ تحميل الحلقات…</div>`;
  $app.querySelectorAll('[data-act="season"]').forEach(b => b.setAttribute("aria-selected", String(b.dataset.id == seasonId)));
  try {
    const d = parseResult(await callTool("get_season_episodes", {season_id: Number(seasonId), max_episodes: 50}));
    if (document.getElementById("eps") !== el) return;
    el.innerHTML = d && !d.error ? episodesHTML(d) : `<div class="state">تعذّر تحميل الحلقات.</div>`;
    const eps = (d && d.episodes) || [];
    // "Start watching" plays the first episode, as on the site.
    const first = eps.slice().sort((a, b) => (a.episode_number || 1e9) - (b.episode_number || 1e9))[0];
    const btn = document.getElementById("play-first");
    if (first && btn) { firstEpisode = first.id; btn.disabled = false; btn.style.opacity = ""; }
    wireImages(el); reportSize();
  } catch(e){ el.innerHTML = `<div class="state">تعذّر تحميل الحلقات.</div>`; }
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
  if (d.diagnostics) return views.run_diagnostics;
  if (d.watch_url && d.title) return views.get_video_details;
  return null;
}
async function go(tool, args){
  renderState("جارٍ التحميل…", true);
  try { show(tool, parseResult(await callTool(tool, args)), true); }
  catch(e){ renderState("تعذّر الاتصال بالخادم: " + e.message); }
}
function onToolResult(res){
  history.length = 0; current = null;
  show(initialTool && views[initialTool] ? initialTool : null, parseResult(res), false);
}

/* ------------------------------------------------------------------ events */
$app.addEventListener("click", (ev) => {
  const b = ev.target.closest("[data-act]"); if (!b || b.disabled) return;
  const {act, id, url, text} = b.dataset;
  if (act === "back") { const prev = history.pop(); if (prev) { current = null; show(prev.tool, prev.data, false); } }
  else if (act === "video") go("get_video_details", {video_id: Number(id)});
  else if (act === "series") go("get_series_details", {series_id: Number(id)});
  else if (act === "play") go("play_video", {video_id: Number(id)});
  else if (act === "play-first") { if (firstEpisode) go("play_video", {video_id: Number(firstEpisode)}); }
  else if (act === "season") loadSeason(id);
  else if (act === "open") openLink(url);
  else if (act === "ask") sendMessage(text);
  else if (act === "fullscreen") requestFullscreen();
  else if (act === "hero-step") { const h = document.getElementById("hero"); if (h && h._step) { clearInterval(heroTimer); h._step(Number(id)); } }
  else if (act === "hero-go") { const h = document.getElementById("hero"); if (h && h._go) { clearInterval(heroTimer); h._go(Number(id)); } }
  else if (act === "toggle-search") {
    searchOpen = !searchOpen;
    const f = $app.querySelector("form.search"); f.classList.toggle("open", searchOpen);
    if (searchOpen) f.querySelector("input").focus();
    reportSize();
  }
  else if (act === "nav") { activeNav = id; id === "__trending" ? go("get_trending_content", {}) : go("browse_section", {section_id: id}); }
});
$app.addEventListener("submit", (ev) => {
  ev.preventDefault();
  const q = new FormData(ev.target).get("q");
  if (q && String(q).trim()) go("search_videos", {query: String(q).trim(), max_results: 24});
});

/* -------------------------------------------------------------------- boot */
(async function boot(){
  if (openai) {
    if (openai.toolOutput) show(null, openai.toolOutput, false);
    window.addEventListener("openai:set_globals", () => { if (openai.toolOutput) show(null, openai.toolOutput, false); });
    return;
  }
  try {
    const init = await request("ui/initialize", {
      protocolVersion: "2026-01-26",
      appInfo: {name: "aljazeera360-app", version: "1.1.0"},
      appCapabilities: {availableDisplayModes: ["inline", "fullscreen"]},
    });
    hostCaps = (init && init.hostCapabilities) || {};
    hostInfo = (init && init.hostInfo) || null;
    const ti = init && init.hostContext && init.hostContext.toolInfo;
    initialTool = (ti && ti.tool && ti.tool.name) || null;
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
