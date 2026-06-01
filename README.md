# Al Jazeera 360 — MCP Server 🎬

> A production-ready [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) server that connects AI assistants directly to [Al Jazeera 360](https://www.aljazeera360.com) — the streaming platform of Al Jazeera Media Network.

This server allows AI tools like **Claude**, **ChatGPT**, **Gemini**, **Cursor**, and any MCP-compatible agent to search, browse, and retrieve video content from Al Jazeera 360's catalog of documentaries, talk shows, investigative programs, podcasts, and original productions — with direct watch links back to the platform.

---

## Table of Contents

- [What is MCP?](#what-is-mcp)
- [Why This Matters](#why-this-matters)
- [Features & Tools](#features--tools)
- [Architecture](#architecture)
- [Quick Start](#quick-start)
- [Configuration](#configuration)
- [Deployment](#deployment)
- [Testing](#testing)
- [API Reference](#api-reference)
- [Publishing & Promotion](#publishing--promotion)
- [Verifying AI Tools Are Using It](#verifying-ai-tools-are-using-it)
- [Roadmap](#roadmap)
- [License](#license)

---

## What is MCP?

**Model Context Protocol (MCP)** is an open standard created by Anthropic that allows AI assistants to connect to external data sources and tools. Think of it as a **USB port for AI** — any AI application that supports MCP can plug into this server and instantly access Al Jazeera 360's content.

```
User asks Claude: "Show me documentaries about Palestine"
         ↓
Claude connects to Al Jazeera 360 MCP Server
         ↓
Server queries Al Jazeera 360's internal API
         ↓
Returns: 20 videos with titles, descriptions, thumbnails, and watch URLs
         ↓
User clicks link → watches on aljazeera360.com 🎬
```

---

## Why This Matters

| Problem | Solution |
| :--- | :--- |
| AI tools hallucinate news and fabricate sources | MCP delivers **real, verified content** from Al Jazeera 360 |
| Al Jazeera 360 content is invisible to AI agents | MCP makes it **discoverable and accessible** to every AI tool |
| No revenue from AI-driven traffic | MCP creates a **new distribution channel** that drives viewers to the platform |
| Competitors (Washington Post, AP, Reuters) are already doing this | Al Jazeera 360 stays ahead with **first-mover advantage in Arabic content** |

---

## Features & Tools

This server provides **8 production-tested tools** that AI assistants can call:

| # | Tool | Description | Example Query |
| :--- | :--- | :--- | :--- |
| 1 | `list_sections` | List all 15 available sections/channels | "What sections does Al Jazeera 360 have?" |
| 2 | `get_trending_content` | Get featured, most-watched, and latest content from homepage | "What's trending on Al Jazeera 360?" |
| 3 | `browse_section` | Browse all content in a specific section | "Show me all documentaries" |
| 4 | `get_video_details` | Get full metadata for a specific video (title, duration, 4K quality, etc.) | "Tell me about video #953659" |
| 5 | `get_series_details` | Get series info with all seasons | "How many seasons does Al Daheeh have?" |
| 6 | `get_season_episodes` | List all episodes in a season | "Show me Al Daheeh 2026 episodes" |
| 7 | `search_videos` | Full-text search in Arabic & English across all content | "Search for videos about Gaza" |
| 8 | `get_latest_episodes` | Get the most recently published episodes | "What's new today?" |

### Available Sections (15 total)

| Section ID | Name (Arabic) | Content Type |
| :--- | :--- | :--- |
| `AJ360-Originals` | أعمال الجزيرة 360 الأصلية | Original productions |
| `AJA` | قناة الجزيرة العربية | Al Jazeera Arabic channel |
| `AJD` | الجزيرة الوثائقية | Al Jazeera Documentary |
| `Atheer` | أثير | Atheer channel |
| `AJ-Plus` | AJ+ عربي | AJ+ Arabic |
| `Talk Show` | برامج حوارية | Talk shows |
| `Investigative Show` | برامج تحقيقية | Investigative journalism |
| `Podcast` | بودكاست | Podcasts |
| `Documentaries` | برامج وثائقية | Documentaries |
| `Field Show` | برامج ميدانية | Field reporting |
| `Policy Series` | سلاسل سياسية | Political series |
| `Social Series` | سلاسل اجتماعية | Social series |
| `Historical Series` | سلاسل تاريخية | Historical series |
| `Biographical Series` | سلاسل سيرة ذاتية | Biographical series |
| `Culture and Arts Series` | سلاسل ثقافة وفنون | Culture & arts |

---

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    AI Applications                            │
│  (Claude, ChatGPT, Gemini, Cursor, Custom AI Agents)        │
└─────────────────────┬───────────────────────────────────────┘
                      │ MCP Protocol (stdio or HTTP/SSE)
                      ▼
┌─────────────────────────────────────────────────────────────┐
│              Al Jazeera 360 MCP Server                        │
│  ┌─────────────┐  ┌──────────────┐  ┌───────────────────┐  │
│  │ Token Mgmt  │  │  8 MCP Tools │  │  2 MCP Resources  │  │
│  │ (Firebase)  │  │  (see above) │  │  (about/sections) │  │
│  └──────┬──────┘  └──────┬───────┘  └───────────────────┘  │
└─────────┼────────────────┼──────────────────────────────────┘
          │                │
          ▼                ▼
┌─────────────────────────────────────────────────────────────┐
│            Vesper/Dice Backend (IMG Arena)                    │
│  ┌────────────────────────┐  ┌────────────────────────────┐ │
│  │ Content API            │  │ Search API                  │ │
│  │ dce-frontoffice.       │  │ search.dce-prod.            │ │
│  │ imggaming.com          │  │ dicelaboratory.com          │ │
│  └────────────────────────┘  └────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
          │
          ▼
┌─────────────────────────────────────────────────────────────┐
│              Al Jazeera 360 Platform                          │
│              https://www.aljazeera360.com                     │
│  (User watches content here — driving views & engagement)    │
└─────────────────────────────────────────────────────────────┘
```

---

## Quick Start

### Prerequisites
- Python 3.10+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/ahmedaminsa/aljazeera360-mcp-server.git
cd aljazeera360-mcp-server

# Install dependencies
pip install -r requirements.txt

# Run tests to verify everything works
python test_server.py

# Start the MCP server
python server.py
```

### Connect to Claude Desktop

Add to your Claude Desktop config file:

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

Restart Claude Desktop. You'll see "Al Jazeera 360" in the tools list. Try asking:
> "What's trending on Al Jazeera 360 today?"

---

## Configuration

| Environment Variable | Required | Description |
| :--- | :--- | :--- |
| `AJ360_AUTH_TOKEN` | No | Firebase auth token for full access (server works without it in guest mode) |
| `AJ360_API_KEY` | No | Override default API key (default is built-in) |

The server works **out of the box** without any configuration. It automatically obtains a guest session token from the platform.

---

## Deployment

### Option 1: Docker (Recommended for Production)

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8080
CMD ["python", "server.py"]
```

```bash
docker build -t aljazeera360-mcp .
docker run -p 8080:8080 aljazeera360-mcp
```

### Option 2: Google Cloud Run

```bash
# Build and deploy
gcloud builds submit --tag gcr.io/YOUR_PROJECT/aljazeera360-mcp
gcloud run deploy aljazeera360-mcp \
  --image gcr.io/YOUR_PROJECT/aljazeera360-mcp \
  --platform managed \
  --allow-unauthenticated \
  --region us-central1
```

### Option 3: Render / Railway / Fly.io

Simply connect this GitHub repo to any of these platforms — they'll auto-detect the Dockerfile and deploy.

---

## Testing

Run the comprehensive test suite that tests all 8 tools against the **live production API**:

```bash
python test_server.py
```

Expected output:
```
TEST 1: list_sections()          ✅ PASS (15 sections)
TEST 2: get_trending_content()   ✅ PASS (5 featured + 6 categories)
TEST 3: browse_section()         ✅ PASS (Documentaries: 4 categories)
TEST 4: get_video_details()      ✅ PASS (عدنان مندريس — 4K, 01:12:20)
TEST 5: get_series_details()     ✅ PASS (الدحيح — 4 seasons)
TEST 6: get_season_episodes()    ✅ PASS (Season 5: 13 episodes)
TEST 7: search_videos()          ✅ PASS ("غزة" → 20 results)
TEST 8: get_latest_episodes()    ✅ PASS (5 new episodes)

Results: 8/8 tests passed
```

---

## API Reference

### Discovered Backend Endpoints

| Endpoint | Method | Description |
| :--- | :--- | :--- |
| `/api/v4/content/home` | GET | Homepage content (heroes + content buckets) |
| `/api/v4/content/{section_id}` | GET | Section-specific content |
| `/api/v4/vod/{id}` | GET | Single video full metadata |
| `/api/v4/series/{id}` | GET | Series details with seasons list |
| `/api/v4/season/{id}` | GET | Season episodes list |
| `search.dce-prod.dicelaboratory.com/search` | GET | Full-text search |

### Authentication Flow
1. Server sends `POST /api/v4/session` with `{"device": "BROWSER"}`
2. Receives JWT auth token (valid ~10 minutes) + refresh token (valid ~1 year)
3. All subsequent requests include `Authorization: Bearer {token}`
4. Token auto-refreshes before expiry

---

## Publishing & Promotion

### Step 1: Register on MCP Directories

Once deployed, register your server on these directories so AI tools can discover it:

| Directory | URL | How to Register |
| :--- | :--- | :--- |
| **MCP Servers Directory** | [mcpservers.org](https://mcpservers.org) | Submit via web form |
| **Awesome MCP Servers** | [github.com/punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | Open a Pull Request |
| **MCP Hub** | [mcphub.io](https://mcphub.io) | Submit via web form |
| **Smithery** | [smithery.ai](https://smithery.ai) | Publish via CLI |
| **Glama** | [glama.ai/mcp/servers](https://glama.ai/mcp/servers) | Submit via web form |

### Step 2: Publish on Package Managers

```bash
# Publish to PyPI (so users can `pip install aljazeera360-mcp`)
pip install build twine
python -m build
twine upload dist/*

# Publish to npm (for Node.js wrapper)
npm publish
```

### Step 3: Submit to AI Platform Marketplaces

| Platform | How | Benefit |
| :--- | :--- | :--- |
| **Anthropic MCP Registry** | Apply at [anthropic.com](https://docs.anthropic.com/en/docs/agents-and-tools/mcp) | Claude users see it natively |
| **OpenAI Plugin Store** | Wrap as OpenAI plugin + submit | ChatGPT users can install it |
| **Google Gemini Extensions** | Apply via Google AI Studio | Gemini users get access |
| **Apify Marketplace** | Publish as Apify Actor | Enterprise customers find it |

### Step 4: Promote on Developer Communities

| Channel | Action |
| :--- | :--- |
| **Hacker News** | Post "Show HN: MCP Server for Al Jazeera 360 — Arabic AI content" |
| **Reddit r/artificial** | Share with demo video |
| **Reddit r/ChatGPT** | Post tutorial on using it with ChatGPT |
| **Twitter/X** | Thread showing live demo with Claude |
| **Dev.to / Medium** | Write "How I Built an MCP Server for Al Jazeera 360" |
| **Product Hunt** | Launch as a developer tool |
| **Arabic Tech Communities** | Share on Arabic developer forums and Telegram groups |

### Step 5: Partner with AI Companies

| Company | Proposal |
| :--- | :--- |
| **Anthropic** | Official Arabic news source for Claude |
| **OpenAI** | Licensed content provider for ChatGPT |
| **Google** | Gemini Arabic content partnership |
| **Perplexity** | Real-time Arabic video source |

---

## Verifying AI Tools Are Using It

### Method 1: Server-Side Logging

Add request logging to track every call:

```python
# Already built into the server via Python logging
# Check logs for:
INFO:httpx:HTTP Request: GET .../api/v4/content/home "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: GET .../search?term=غزة "HTTP/1.1 200 OK"
```

### Method 2: Analytics Dashboard

Deploy with a monitoring service to track:

```python
# Add to server.py for production monitoring
import time

request_log = []

@mcp.tool()
async def search_videos(query: str, max_results: int = 20) -> str:
    # Log the request
    request_log.append({
        "tool": "search_videos",
        "query": query,
        "timestamp": time.time(),
        "source": "mcp_client"
    })
    # ... rest of function
```

### Method 3: Cloud Monitoring (Recommended for Production)

| Service | What It Tracks |
| :--- | :--- |
| **Google Cloud Monitoring** | Request count, latency, errors per tool |
| **Datadog** | Real-time dashboard of API calls |
| **Grafana + Prometheus** | Custom metrics (queries/min, popular searches) |
| **PostHog** | User analytics (which AI tools are calling) |

### Method 4: Test It Yourself

1. **Open Claude Desktop** → Ask: "Search Al Jazeera 360 for documentaries about Palestine"
2. **Check Claude's response** → It should show real video titles and watch URLs
3. **Click a watch URL** → It should open `aljazeera360.com/video/{id}` with the actual video

### Method 5: MCP Inspector Tool

```bash
# Use the official MCP Inspector to verify your server
npx @modelcontextprotocol/inspector python server.py
```

This opens a web UI where you can:
- See all registered tools
- Call each tool manually
- Verify responses are correct

### Method 6: Track GitHub Stars & Forks

Monitor adoption through:
- GitHub Stars (developers interested)
- GitHub Forks (developers building on it)
- GitHub Issues (users reporting bugs = users using it)
- npm/PyPI download counts

---

## Roadmap

| Phase | Timeline | Features |
| :--- | :--- | :--- |
| **v1.0 (Current)** | ✅ Done | 8 tools, search, browse, video details, series/seasons |
| **v1.1** | Next | Rate limiting, caching, error retry logic |
| **v1.2** | Next | Live streaming schedule, EPG (Electronic Program Guide) |
| **v2.0** | Future | User authentication, watchlist management, personalized recommendations |
| **v3.0** | Future | Revenue API (pay-per-query), enterprise licensing, SLA guarantees |

---

## Technical Details

| Component | Technology |
| :--- | :--- |
| **Language** | Python 3.11 |
| **MCP SDK** | `mcp` (official Python SDK by Anthropic) |
| **HTTP Client** | `httpx` (async) |
| **Backend Platform** | Vesper/Dice by IMG Arena |
| **Authentication** | Firebase Auth (JWT tokens) |
| **Search Engine** | Dice Laboratory Search |
| **Video Quality** | Up to 4K Ultra HD (2160p) |
| **Content Language** | Arabic (primary), English (search supported) |

---

## License

MIT License — Free to use, modify, and distribute.

---

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## Acknowledgments

- **Al Jazeera Media Network** — For creating world-class Arabic content
- **Anthropic** — For creating the MCP standard
- **IMG Arena / Dice** — For the robust streaming infrastructure

---

*Built with ❤️ for the Arabic-speaking world and the future of AI-powered media.*
