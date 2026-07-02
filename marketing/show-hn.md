# Show HN

Best time to post: **Tuesday–Thursday, ~9:00 AM US Eastern.** Post, then add the first comment immediately.

---

## Title

```
Show HN: Al Jazeera 360 MCP – Connect AI assistants to Arabic streaming content
```

(Keep under 80 chars. Alternatives if you want to test:)
- `Show HN: An MCP server for Al Jazeera 360's Arabic video catalog`
- `Show HN: First MCP server for Arabic streaming content`

## URL

```
https://github.com/ahmedaminsa/aljazeera360-mcp-server
```

---

## First comment (post right after submitting)

I built this because there was no good way for AI assistants to reach Arabic
video content. Every MCP server I found was English-first, and when you asked
Claude or ChatGPT about Arabic shows it would either refuse or hallucinate URLs.

This connects any MCP client to Al Jazeera 360's live catalog. You ask
something like "find documentaries about Gaza" or "what's the latest episode of
Al Daheeh" and it returns real titles, durations, quality, and direct
aljazeera360.com watch links — no made-up links.

Some technical notes:
- Python / FastMCP. The upstream API is a Vesper/Dice (IMG Arena) backend I
  reverse-engineered from the web player. It's guest-auth with a short-lived
  token, so the server auto-refreshes tokens and persists the refresh token.
- Three transports: stdio for local clients, streamable-HTTP and SSE for cloud.
  There's a hosted instance so you can try it with zero install — just point
  your client at the /mcp URL (in the README).
- Two tool profiles: 8 core discovery tools by default (a small toolset makes
  the model pick the right tool far more reliably), and an optional 16 SEO /
  analytics tools behind an env var for content teams.
- It's an unofficial community project — not affiliated with Al Jazeera. It
  uses their public API and links back to their site for playback.

Happy to answer questions about the MCP protocol side, the token handling, or
why I split the tools into profiles. Feedback very welcome — especially on what
other Arabic content sources would be worth adding.

---

## Notes for engaging in comments

- If asked "why not just scrape?": the point is structured, real-time access
  the model can call as a tool — with stable IDs and watch links, not scraped HTML.
- If asked about legality: it's the same public API the website's own player uses;
  it links back to the official site rather than rehosting anything.
- If asked about other platforms: honest answer — you're focused on Al Jazeera 360
  for now; the architecture could generalize but that's not the current goal.
