# X / Twitter — English thread

> Post each tweet separately. Tweet 1 is the hook — keep it tight.

---

**1/ 🧵**

I built the first MCP server for Arabic streaming content.

You can now connect Claude, ChatGPT, or Cursor to **Al Jazeera 360**'s entire catalog — documentaries, podcasts, investigative shows — and get real titles + direct watch links back.

Open source, free, zero-install option 👇

---

**2/**

What it actually does:

Ask your AI: *"What's the latest episode of Al Daheeh?"* or *"Find documentaries about Gaza."*

It hits the live Al Jazeera 360 API, pulls real metadata (title, duration, quality up to 4K), and returns direct `aljazeera360.com` watch links. No hallucinated URLs.

---

**3/**

The easiest way — no install at all.

There's a hosted instance running. Drop this into your MCP client config and you're live:

```json
{
  "mcpServers": {
    "aljazeera360": {
      "type": "http",
      "url": "https://aljazeera360-mcp-server-production.up.railway.app/mcp"
    }
  }
}
```

---

**4/**

Tools included:

🔍 Full-text search (Arabic + English)
📺 Browse 15 sections/channels
🎬 Video / series / season / episode details
⭐ Trending + latest episodes

Plus an optional pro profile: 16 SEO & analytics tools (video sitemaps, JSON-LD schema, knowledge graph, discoverability scoring).

---

**5/**

Built in Python (FastMCP):
✅ auto token refresh
✅ retry + caching
✅ 3 transports (stdio / streamable-HTTP / SSE)
✅ built-in analytics dashboard

Code's all on GitHub 👇

github.com/ahmedaminsa/aljazeera360-mcp-server

Try it, break it, tell me what's missing. #MCP #AI #Claude
