# Al Jazeera 360 MCP Server

[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![MCP Protocol](https://img.shields.io/badge/MCP-Compatible-purple.svg)](https://modelcontextprotocol.io)
[![Smithery](https://smithery.ai/badge/aljazeera360-mcp)](https://smithery.ai/server/aljazeera360-mcp)

> Connect any AI assistant to Al Jazeera 360's streaming catalog — search, browse, and retrieve Arabic video content with direct watch links.

An MCP (Model Context Protocol) server that gives AI tools like Claude, ChatGPT, Gemini, and Cursor real-time access to [Al Jazeera 360](https://www.aljazeera360.com)'s full content library: documentaries, investigative programs, talk shows, podcasts, and original productions.

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

All 8 tools are tested against the live API. Expected result: `8/8 tests passed`.

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

This server uses the standard MCP protocol over `stdio`. It works with any MCP-compatible client:

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
| `AJ360_API_KEY` | No | Built-in | Platform API key (public, from browser network requests). |
| `MCP_TRANSPORT` | No | `stdio` | Transport mode: `stdio` (local) or `sse` (cloud). |
| `MCP_PORT` | No | `8080` | Port for SSE transport (cloud deployment). |

The server works **without any configuration** in guest mode. For full content access, provide a refresh token.

---

## Deploy

### Docker

```bash
docker build -t aljazeera360-mcp .
docker run -p 8080:8080 -e MCP_TRANSPORT=sse -e AJ360_REFRESH_TOKEN=your-token aljazeera360-mcp
```

### Google Cloud Run

```bash
gcloud builds submit --tag gcr.io/YOUR_PROJECT/aljazeera360-mcp
gcloud run deploy aljazeera360-mcp \
  --image gcr.io/YOUR_PROJECT/aljazeera360-mcp \
  --platform managed \
  --allow-unauthenticated \
  --set-env-vars="MCP_TRANSPORT=sse,AJ360_REFRESH_TOKEN=your-token"
```

### Render / Railway / Fly.io

Connect this repo — auto-deploys from the included Dockerfile. Set environment variables in the dashboard.

---

## How It Works

```
Your AI Assistant
       │
       │  MCP Protocol (stdio or SSE)
       ▼
┌──────────────────────────┐
│  This MCP Server         │
│  ┌────────────────────┐  │
│  │ Token Manager      │  │
│  │ (auto-refresh)     │  │
│  ├────────────────────┤  │
│  │ 8 Tools + Prompts  │  │
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

## Tech Stack

| Component | Technology |
| :--- | :--- |
| Language | Python 3.11+ |
| MCP SDK | `mcp` (Anthropic official) |
| HTTP | `httpx` (async) |
| Retry | `tenacity` (exponential backoff) |
| Auth | Firebase JWT (auto-managed with refresh) |
| Video Quality | Up to 4K (2160p) |
| Transport | stdio (local) / SSE (cloud) |

---

## License

MIT

---

## Contributing

PRs welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

Run tests before submitting:

```bash
python test_server.py
```
