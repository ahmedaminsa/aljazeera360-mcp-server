# Al Jazeera 360 MCP Server

[![CI](https://github.com/ahmedaminsa/aljazeera360-mcp-server/actions/workflows/ci.yml/badge.svg)](https://github.com/ahmedaminsa/aljazeera360-mcp-server/actions/workflows/ci.yml)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![MCP Protocol](https://img.shields.io/badge/MCP-Compatible-purple.svg)](https://modelcontextprotocol.io)
[![Smithery](https://smithery.ai/badge/aljazeera360-mcp)](https://smithery.ai/server/aljazeera360-mcp)

> Connect any AI assistant to Al Jazeera 360's streaming catalog — search, browse, and retrieve Arabic video content with direct watch links.

An MCP (Model Context Protocol) server that gives AI tools like Claude, ChatGPT, Gemini, and Cursor real-time access to [Al Jazeera 360](https://www.aljazeera360.com)'s full content library: documentaries, investigative programs, talk shows, podcasts, and original productions.

> ⚠️ **Unofficial community project.** Not affiliated with, endorsed by, or sponsored by Al Jazeera Media Network. It uses the platform's publicly accessible API and links back to `aljazeera360.com` for all content.

---

## ⚡ Quick Connect — No Install Needed

A hosted instance is live on Cloudflare. Add this to your MCP client config and you're done:

```json
{
  "mcpServers": {
    "aljazeera360": {
      "type": "http",
      "url": "https://aljazeera360-mcp.ahmed-26d.workers.dev/mcp"
    }
  }
}
```

> First request after idle takes a few seconds (container cold start) — subsequent requests are fast.

Then ask your assistant: *"What's trending on Al Jazeera 360?"* — or in Arabic: *"ايه أحدث حلقات الدحيح؟"*

---

## What It Does

Ask your AI assistant questions like:

- *"What's trending on Al Jazeera 360?"*
- *"Find documentaries about Palestine"*
- *"Show me the latest episodes of Al Daheeh"*
- *"Search for videos about Gaza"*

The AI connects to this server, fetches real data from Al Jazeera 360, and returns actual video titles, descriptions, durations, and **direct watch links** to `aljazeera360.com`.

---

## Tools Available

The server ships with two tool profiles:

| Profile | Tools | For whom | How |
| :--- | :--- | :--- | :--- |
| **Core** (default) | 8 discovery tools | End users asking AI assistants about content | Works out of the box |
| **Full** | All 24 tools (+ SEO & analytics) | Content teams, SEO analysts | Set `AJ360_ENABLE_SEO_TOOLS=1` |

A small default toolset keeps AI tool selection fast and accurate. Enable the full profile only if you need the SEO/analytics tools.

### Core Discovery Tools (always on)

| Tool | What It Does |
| :--- | :--- |
| `list_sections` | Lists all 15 sections/channels available on the platform |
| `get_trending_content` | Returns featured and most-watched content from the homepage |
| `browse_section` | Browses all content within a specific section (e.g., Documentaries, Podcasts) |
| `get_video_details` | Returns full metadata for a video: title, description, duration, quality (up to 4K), watch URL |
| `get_series_details` | Returns series info with all available seasons |
| `get_season_episodes` | Lists all episodes within a specific season |
| `search_videos` | Full-text search across all content (Arabic & English), with optional content type filter |
| `get_latest_episodes` | Returns the most recently published episodes from any section |

### SEO & Metadata Tools (requires `AJ360_ENABLE_SEO_TOOLS=1`)

| Tool | What It Does |
| :--- | :--- |
| `generate_seo_content` | Generates optimized Arabic titles, descriptions, and keywords for a video |
| `generate_sitemap` | Generates a Google Search Console-ready Video XML Sitemap (paginated) |
| `audit_metadata_quality` | Audits catalog health — missing descriptions, thumbnails, and categories (paginated) |
| `get_trending_topics` | Extracts the top trending keywords and topics across the catalog |
| `compare_sections` | Compares content freshness and activity across all sections |
| `get_series_seo_map` | Generates a complete SEO map for a series with all episodes |

### Advanced AI & Analytics Tools (requires `AJ360_ENABLE_SEO_TOOLS=1`)

| Tool | What It Does |
| :--- | :--- |
| `build_knowledge_graph` | Builds an entity knowledge graph from catalog metadata |
| `generate_faq_schema` | Generates FAQ Schema JSON-LD for a video |
| `get_ai_discoverability_score` | Scores how discoverable content is by AI assistants |
| `build_topic_clusters` | Groups content into SEO topic clusters with pillar and supporting pages |
| `find_evergreen_content` | Identifies content that stays relevant over time |
| `get_host_profile` | Generates a Person Schema and profile for a show host |
| `get_genre_report` | Reports on genre distribution and SEO opportunities |
| `get_searchable_tags_map` | Maps the most searched keywords across the catalog (paginated) |
| `get_country_content_map` | Maps content by country for geo-targeted SEO (paginated) |
| `generate_series_schema` | Generates TVSeries + TVEpisode JSON-LD Schema for a series |

---

## Sections

| ID | Channel |
| :--- | :--- |
| `AJ360-Originals` | Al Jazeera 360 Originals |
| `AJA` | Al Jazeera Arabic |
| `AJD` | Al Jazeera Documentary |
| `Atheer` | Atheer |
| `AJ-Plus` | AJ+ Arabic |
| `Talk Show` | Talk Shows |
| `Investigative Show` | Investigative Programs |
| `Podcast` | Podcasts |
| `Documentaries` | Documentaries |
| `Field Show` | Field Reporting |
| `Policy Series` | Political Series |
| `Social Series` | Social Series |
| `Historical Series` | Historical Series |
| `Biographical Series` | Biographical Series |
| `Culture and Arts Series` | Culture & Arts |

---

## Quick Start

### Install

```bash
git clone https://github.com/ahmedaminsa/aljazeera360-mcp-server.git
cd aljazeera360-mcp-server
pip install -r requirements.txt
```

### Configure Authentication

The server supports multiple authentication methods (in priority order):

1. **Refresh Token (Recommended)** — Auto-refreshes every 10 minutes, valid for ~1 year:
   ```bash
   export AJ360_REFRESH_TOKEN="eyJ..."
   ```
   
2. **Auth Token** — Direct token, expires in ~10 minutes:
   ```bash
   export AJ360_AUTH_TOKEN="eyJ..."
   ```

3. **Guest Mode** — No configuration needed. The server auto-creates a guest session.

**How to get your refresh token:**
1. Open https://www.aljazeera360.com in your browser
2. Log in with your account
3. Open DevTools → Console → Run: `localStorage.getItem('dice:refreshToken')`
4. Copy the token value

### Test

```bash
python test_server.py
```

Core tools are tested against the live API.

### Run

```bash
python server.py
```

---

## Use with Claude Desktop

Add to your config file:

**macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`  
**Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "aljazeera360": {
      "command": "python",
      "args": ["/full/path/to/aljazeera360-mcp-server/server.py"],
      "env": {
        "AJ360_REFRESH_TOKEN": "your-refresh-token-here"
      }
    }
  }
}
```

Restart Claude Desktop. The Al Jazeera 360 tools will appear automatically.

---

## Use with Any MCP Client

This server speaks the standard MCP protocol over `stdio` (local) and Streamable HTTP (hosted). It works with any MCP-compatible client:

- [Claude Desktop](https://claude.ai/download)
- [Cursor](https://cursor.sh)
- [Continue](https://continue.dev)
- [Windsurf](https://windsurf.ai)
- [MCP Inspector](https://github.com/modelcontextprotocol/inspector) (for testing)
- Any custom MCP client

---

## Configuration

| Variable | Required | Default | Description |
| :--- | :--- | :--- | :--- |
| `AJ360_REFRESH_TOKEN` | No | — | Long-lived refresh token (~1 year). Best for production. |
| `AJ360_AUTH_TOKEN` | No | Guest mode | Short-lived auth token (~10 min). Good for quick testing. |
| `AJ360_API_KEY` | Yes | — | Platform API key (public, from browser network requests). No default is bundled — you must provide it. |
| `MCP_TRANSPORT` | No | `streamable-http` | Transport mode: `stdio` (local), `streamable-http` (cloud, recommended), or `sse` (legacy cloud). |
| `MCP_PORT` | No | `8080` | Port for the HTTP transport (cloud deployment). |
| `AJ360_ALLOWED_HOST` | Cloud only | — | Public hostname of your deployment (no scheme). Required when self-hosting on a custom domain — the DNS-rebinding protection rejects unknown hosts with 421. |
| `AJ360_ENABLE_SEO_TOOLS` | No | off | Set to `1` to register the 16 SEO/analytics tools (full profile). |
| `AJ360_ENABLE_DASHBOARD` | No | `true` | Enable/disable the analytics dashboard. |
| `AJ360_DASHBOARD_PORT` | No | `9090` | Port for the analytics dashboard. |
| `AJ360_DASHBOARD_TOKEN` | No | — | Shared secret for the analytics data endpoints (`/api/stats`, `/api/recent`). When set, callers must send `Authorization: Bearer <token>` or `?token=<token>`. **Strongly recommended for any public/cloud deployment.** |
| `AJ360_ANALYTICS_DB` | No | `analytics.db` | Path to SQLite analytics database. |

The server needs only `AJ360_API_KEY` to run — authentication falls back to an automatic guest session. For full content access, also provide a refresh token.

---

## Deploy

The production instance runs on **Cloudflare Containers** — full walkthrough in
[`deploy/cloudflare/README.md`](deploy/cloudflare/README.md) (wraps the Dockerfile in a
Cloudflare Container behind a tiny Worker; requires the Workers Paid plan and local
Docker for deploys). Any container platform works — alternatives below.

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/ahmedaminsa/aljazeera360-mcp-server)

### Docker

```bash
docker build -t aljazeera360-mcp .
docker run -p 8080:8080 -e MCP_TRANSPORT=streamable-http -e AJ360_REFRESH_TOKEN=your-token aljazeera360-mcp
```

### Google Cloud Run

```bash
gcloud builds submit --tag gcr.io/YOUR_PROJECT/aljazeera360-mcp
gcloud run deploy aljazeera360-mcp \
  --image gcr.io/YOUR_PROJECT/aljazeera360-mcp \
  --platform managed \
  --allow-unauthenticated \
  --set-env-vars="MCP_TRANSPORT=streamable-http,AJ360_REFRESH_TOKEN=your-token"
```

### Render / Railway / Fly.io

Connect this repo — auto-deploys from the included Dockerfile. Set environment variables in the dashboard (including `AJ360_ALLOWED_HOST=<your-domain>` so the DNS-rebinding protection accepts your host).

---

## How It Works

```
Your AI Assistant
       │
       │  MCP Protocol (stdio / Streamable HTTP)
       ▼
┌──────────────────────────┐
│  This MCP Server         │
│  ┌────────────────────┐  │
│  │ Token Manager      │  │
│  │ (auto-refresh)     │  │
│  ├────────────────────┤  │
│  │ 24 Tools + Prompts │  │
│  │ + Retry + Cache    │  │
│  └────────────────────┘  │
└──────────┬───────────────┘
           │
           │  HTTPS (authenticated)
           ▼
┌──────────────────────────┐
│  Al Jazeera 360 API      │
│  (Vesper/Dice Platform)  │
└──────────┬───────────────┘
           │
           ▼
┌──────────────────────────┐
│  aljazeera360.com        │
│  (Direct watch links)    │
└──────────────────────────┘
```

---

## Built-in Prompts

The server includes pre-built prompts for common AI scenarios:

| Prompt | Description |
| :--- | :--- |
| `recommend_documentary` | Find and recommend documentaries about a specific topic |
| `summarize_latest` | Summarize the latest episodes from a section |
| `explore_series` | Explore a series — find all seasons and episodes |

---

## Example Output

Calling `search_videos("غزة")` returns:

```json
{
  "query": "غزة",
  "total_results": 20,
  "results": [
    {
      "title": "المسعفون أهداف إسرائيل المتنقلة!",
      "type": "VOD",
      "duration": "24:53",
      "id": "965741",
      "watch_url": "https://www.aljazeera360.com/video/965741"
    },
    {
      "title": "قيادة السنوار لجهاز حماس الأمني",
      "type": "VOD",
      "duration": "54:57",
      "id": "953659",
      "watch_url": "https://www.aljazeera360.com/video/953659"
    }
  ]
}
```

---

## Analytics Dashboard

The server includes a **built-in analytics dashboard** that tracks every request made by AI tools.

### What It Tracks

- Which AI tool made the request (Claude, ChatGPT, Cursor, etc.)
- Which MCP tool was called (`search_videos`, `get_trending_content`, etc.)
- When each request happened (timestamp)
- How long each request took (response time in ms)
- Whether it succeeded or failed
- Top search terms (what users are asking about)
- Daily/hourly activity patterns

### Access the Dashboard

The dashboard starts automatically on port `9090` when you run the server:

```
http://localhost:9090
```

For cloud deployments, expose port 9090 alongside the MCP port (8080).

### API Endpoints

| Endpoint | Returns |
| :--- | :--- |
| `GET /` | Interactive HTML dashboard (auto-refreshes every 10s) |
| `GET /api/stats` | JSON summary: total requests, tools usage, top searches, daily breakdown |
| `GET /api/recent` | JSON list of the 50 most recent requests with full details |
| `GET /api/health` | Health check with version, transport, and links to `/privacy` and `/docs` |
| `GET /privacy` | Privacy Policy page |
| `GET /docs` | Server documentation page |

### Configuration

| Variable | Default | Description |
| :--- | :--- | :--- |
| `AJ360_ENABLE_DASHBOARD` | `true` | Set to `false` to disable the dashboard |
| `AJ360_DASHBOARD_PORT` | `9090` | Port for the analytics HTTP server |
| `AJ360_DASHBOARD_TOKEN` | — | Shared secret required to read `/api/stats` and `/api/recent`. Set this on any public deployment. |
| `AJ360_ANALYTICS_DB` | `analytics.db` | SQLite database file path |

### Example Stats Output

```json
{
  "total_requests": 1247,
  "success_rate": "99.2%",
  "tools_usage": [
    {"tool": "search_videos", "calls": 523, "avg_response_ms": 340},
    {"tool": "get_trending_content", "calls": 312, "avg_response_ms": 180}
  ],
  "clients": [
    {"client": "claude-desktop", "requests": 890},
    {"client": "cursor", "requests": 357}
  ],
  "top_searches": [
    {"term": "\u063a\u0632\u0629", "count": 89},
    {"term": "\u0641\u0644\u0633\u0637\u064a\u0646", "count": 67}
  ]
}
```

---

## Tech Stack

| Component | Technology |
| :--- | :--- |
| Language | Python 3.10+ |
| MCP SDK | `mcp` (Anthropic official) |
| HTTP | `httpx` (async) |
| Retry | `tenacity` (exponential backoff) |
| Auth | Firebase JWT (auto-managed with refresh) |
| Analytics | SQLite + built-in HTTP dashboard |
| Video Quality | Up to 4K (2160p) |
| Transport | stdio (local) / Streamable HTTP (cloud, recommended) / SSE (legacy) |

---

## License

MIT

---

## SEO Ops & Vesper Knowledge Base (AI-assisted)

This repo doubles as an AI-assisted SEO operations workspace for the platform.
Open it in [Claude Code](https://claude.com/claude-code) and you get:

| Piece | What it does |
| :--- | :--- |
| `.claude/agents/onvesper-expert.md` | Expert agent on the Vesper/Deltatre platform that powers aljazeera360.com — ask it anything about Back Office, DVE, licences, advertising, etc. |
| `onvesper-kb/` | Full offline mirror of the official Vesper docs (317 pages, rebuild anytime with `bash onvesper-kb/refresh.sh`) |
| `/seo-report` skill | On-demand deep SEO analysis: runs the SEO tools, reads trends, and turns findings into exact Back Office fix steps |
| `scripts/seo_snapshot.py` | Metrics collector behind the skill (discoverability scores, metadata audits, tag maps). Reports are generated locally on demand — never committed. |

```bash
export AJ360_API_KEY=…
python scripts/seo_snapshot.py   # → reports/seo/<date>.md (local only)
```

## Contributing

PRs welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

Run tests before submitting:

```bash
python test_server.py
```
