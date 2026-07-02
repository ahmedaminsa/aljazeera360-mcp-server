# Reddit posts

Post to one subreddit at a time (spacing them a day or two apart reads less
spammy). Read each sub's self-promotion rules first. r/ClaudeAI is the warmest
audience; lead there.

---

## r/ClaudeAI

**Title:**
```
I built an MCP server that connects Claude to Al Jazeera 360's Arabic video catalog
```

**Body:**

I kept hitting a wall: Claude couldn't answer questions about Arabic shows
without hallucinating links. So I built an MCP server for it.

It connects Claude (or any MCP client) to Al Jazeera 360 — documentaries,
podcasts, investigative shows. You ask "find documentaries about Gaza" or
"what's the latest episode of Al Daheeh" and it returns real titles, durations,
and direct watch links from the live API.

Zero-install if you want to try it — there's a hosted instance, you just add a
URL to your config:

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

Open source (MIT), Python/FastMCP, 8 core tools by default with an optional pro
profile for SEO/analytics. Unofficial community project.

Repo: https://github.com/ahmedaminsa/aljazeera360-mcp-server

Would love feedback — especially what other content sources are worth adding.

---

## r/LocalLLaMA

**Title:**
```
Open-source MCP server for Arabic streaming content (Al Jazeera 360) — works with any MCP client
```

**Body:**

Sharing an MCP server I built for Al Jazeera 360's catalog. Works with any
MCP-compatible client (Claude Desktop, Cursor, Continue, local setups via
stdio, or the hosted HTTP endpoint).

Technical bits that might interest this crowd:
- Python / FastMCP, three transports (stdio / streamable-HTTP / SSE)
- Reverse-engineered Vesper/Dice backend with auto token refresh + persistence
- Two tool profiles (8 core / 24 full) — found that a smaller default toolset
  measurably improves tool-selection accuracy
- Built-in SQLite analytics dashboard
- A daily GitHub Action smoke-tests the live upstream API so breakage surfaces fast

MIT licensed: https://github.com/ahmedaminsa/aljazeera360-mcp-server

Curious whether others have hit the "too many tools hurts selection" problem and
how you handled it.

---

## Other communities worth a post

- **r/SideProject** — frame it as a launch, lead with the zero-install demo
- Arabic dev Discord / Telegram groups — the AR thread from `x-thread-ar.md` works well
- **LinkedIn** — the Arabic tech audience is active there; repurpose the AR thread as a single post
