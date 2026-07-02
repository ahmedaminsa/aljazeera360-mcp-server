---
title: I Built the First MCP Server for Arabic Streaming Content
published: false
description: How I connected AI assistants to Al Jazeera 360's video catalog with the Model Context Protocol — and what I learned reverse-engineering a streaming API.
tags: mcp, ai, python, opensource
canonical_url: https://github.com/ahmedaminsa/aljazeera360-mcp-server
---

> **Note:** publish this on dev.to and/or Hashnode. Set `published: true` when ready.

If you ask Claude or ChatGPT "what's the latest episode of Al Daheeh?", you get
one of two things: a refusal, or a confidently wrong answer with a made-up link.
There was no bridge between AI assistants and Arabic video content. So I built one.

**[Al Jazeera 360 MCP Server](https://github.com/ahmedaminsa/aljazeera360-mcp-server)**
is an open-source [Model Context Protocol](https://modelcontextprotocol.io) server
that gives any MCP-compatible AI tool real-time access to
[Al Jazeera 360](https://www.aljazeera360.com)'s catalog — documentaries, podcasts,
talk shows, investigative programs — and returns real metadata with direct watch links.

## What it looks like in practice

Once connected, you can ask your assistant things like:

- *"What's trending on Al Jazeera 360?"*
- *"Find documentaries about Gaza"* / *"دوّرلي على وثائقيات عن غزة"*
- *"List the seasons of Al Daheeh and show me the latest episodes"*

The model calls a tool, the server hits the live API, and you get back actual
titles, durations, quality (up to 4K), and `aljazeera360.com` links you can click.

## Zero-install: connect to the hosted instance

The fastest way to try it — no clone, no pip. There's a hosted instance; point
your client at it:

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

## Three things I learned building it

### 1. Reverse-engineering a streaming API

Al Jazeera 360 runs on a Vesper/Dice (IMG Arena) backend. The web player
authenticates as a guest with a short-lived token (~10 min) and a long-lived
refresh token. I traced the calls in DevTools, mapped the endpoints
(`/api/v4/content/home`, `/vod/{id}`, `/series/{id}`, search), and wrapped them
in a `TokenManager` that auto-refreshes and persists the refresh token so it
survives restarts. When the upstream changed its auth path once, a daily
live-check GitHub Action caught it.

### 2. Fewer tools = better tool selection

I originally shipped everything — 24 tools including SEO and analytics helpers.
It made the assistant *worse*: with a long, overlapping tool list the model
picks the wrong tool more often, and every tool definition eats context. I split
them into profiles: **8 core discovery tools by default**, and the 16 SEO/analytics
tools behind an env var (`AJ360_ENABLE_SEO_TOOLS=1`) for content teams. The
default experience got noticeably sharper.

### 3. A remote MCP is a superpower for adoption

The single biggest lever for "will people actually try this" was the hosted
streamable-HTTP instance. Asking someone to `git clone && pip install` loses most
of them. Asking them to paste a URL loses almost none.

## Tech stack

- Python + [FastMCP](https://github.com/modelcontextprotocol/python-sdk)
- `httpx` (async) with `tenacity` retry + a small TTL cache
- Three transports: stdio (local), streamable-HTTP + SSE (cloud)
- A built-in analytics dashboard (SQLite) that tracks which tools assistants call

## Try it

The code is MIT-licensed and on GitHub:
**https://github.com/ahmedaminsa/aljazeera360-mcp-server**

It's an unofficial community project — not affiliated with Al Jazeera; it uses
their public API and links back to their site for playback.

If you build MCP servers, I'd love feedback on the token handling and the
profile split. And if you know Arabic content sources worth connecting next,
tell me.
