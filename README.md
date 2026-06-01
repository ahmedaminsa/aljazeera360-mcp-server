# Al Jazeera 360 MCP Server

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
| `search_videos` | Full-text search across all content (Arabic & English) |
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
      "args": ["/full/path/to/aljazeera360-mcp-server/server.py"]
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
- [MCP Inspector](https://github.com/modelcontextprotocol/inspector) (for testing)
- Any custom MCP client

---

## Configuration

| Variable | Required | Default | Description |
| :--- | :--- | :--- | :--- |
| `AJ360_AUTH_TOKEN` | No | Guest mode | Firebase auth token for full content access |
| `AJ360_API_KEY` | No | Built-in | Platform API key |

The server works **without any configuration**. It automatically authenticates as a guest.

---

## Deploy

### Docker

```bash
docker build -t aljazeera360-mcp .
docker run -p 8080:8080 aljazeera360-mcp
```

### Google Cloud Run

```bash
gcloud builds submit --tag gcr.io/YOUR_PROJECT/aljazeera360-mcp
gcloud run deploy aljazeera360-mcp \
  --image gcr.io/YOUR_PROJECT/aljazeera360-mcp \
  --platform managed \
  --allow-unauthenticated
```

### Render / Railway / Fly.io

Connect this repo — auto-deploys from the included Dockerfile.

---

## How It Works

```
Your AI Assistant
       │
       │  MCP Protocol
       ▼
┌──────────────────────┐
│  This MCP Server     │
│  (Token Management   │
│   + 8 Tools)         │
└──────────┬───────────┘
           │
           │  HTTPS
           ▼
┌──────────────────────┐
│  Al Jazeera 360 API  │
│  (Vesper/Dice)       │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│  aljazeera360.com    │
│  (Watch links)       │
└──────────────────────┘
```

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
      "id": "965741",
      "watch_url": "https://www.aljazeera360.com/video/965741"
    },
    {
      "title": "حقنة تذيب الأورام السرطانية",
      "type": "VOD",
      "id": "965738",
      "watch_url": "https://www.aljazeera360.com/video/965738"
    }
  ]
}
```

---

## Tech Stack

| Component | Technology |
| :--- | :--- |
| Language | Python 3.11 |
| MCP SDK | `mcp` (Anthropic official) |
| HTTP | `httpx` (async) |
| Auth | Firebase JWT (auto-managed) |
| Video Quality | Up to 4K (2160p) |

---

## License

MIT

---

## Contributing

PRs welcome. Please run `python test_server.py` before submitting.
