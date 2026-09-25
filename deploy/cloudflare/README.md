# Deploy to Cloudflare (Containers)

Runs the Python MCP server on Cloudflare via **Cloudflare Containers** — the
existing `Dockerfile` wrapped by a tiny Worker that routes every request
(`/mcp`, `/api/health`, dashboard) into the container.

> **Requirements**
> - Cloudflare **Workers Paid** plan (~$5/mo — Containers are not on the free plan)
> - **Docker running locally** when you deploy (`docker info` must work)
> - Node 18+ and `npx`

## One-time deploy

```bash
cd deploy/cloudflare
npm install
npx wrangler login

# Secrets the Python server needs:
npx wrangler secret put AJ360_API_KEY          # required
npx wrangler secret put AJ360_REFRESH_TOKEN    # optional
npx wrangler secret put AJ360_DASHBOARD_TOKEN  # recommended (protects /api/stats)

# First deploy (builds the Docker image locally and pushes it):
npx wrangler deploy
```

The deploy output prints your URL, e.g.
`https://aljazeera360-mcp.<your-subdomain>.workers.dev`

**Then do the host fix (required):** edit `wrangler.jsonc` → set
`AJ360_ALLOWED_HOST` to that exact hostname (no `https://`) → `npx wrangler deploy`
again. Without this, the server's DNS-rebinding protection answers **421** to
every request.

## Verify

```bash
curl https://aljazeera360-mcp.<your-subdomain>.workers.dev/api/health
# → {"status":"ok", ...}
```

Then point your MCP client / claude.ai connector at:

```
https://aljazeera360-mcp.<your-subdomain>.workers.dev/mcp
```

and update the `remotes[0].url` in the repo's `server.json` to match.

## Notes & trade-offs

- **Cold starts**: the container sleeps after 15 min idle (`sleepAfter` in
  `src/index.js`) and takes a few seconds to wake. Raise `sleepAfter` if that
  annoys you.
- **Analytics reset**: the SQLite analytics DB lives on the container's
  ephemeral disk and resets when the instance sleeps. Fine for spot-checking,
  not for long-term stats.
- **Sessions**: the server runs stateless (`AJ360_STATELESS`, on by
  default), so a sleeping or redeployed container never strands a client on
  an expired session. The Worker still issues an `mcp-session-id` on
  `initialize`, used only to group a conversation's calls in the analytics;
  the server ignores it, so a stale id can never fail a request.
- **Custom domain**: add a route/custom domain in the Cloudflare dashboard,
  then set `AJ360_ALLOWED_HOST` to that domain and redeploy.
- The `@cloudflare/containers` API is still evolving; if a deploy fails after
  an SDK update, check https://developers.cloudflare.com/containers/

## Usage analytics (persistent)

The container's own `/api/stats` only covers the current container lifetime —
it resets whenever the instance sleeps. The Worker therefore logs every MCP
request to a **Cloudflare D1** database (`aj360-analytics`, schema in
`schema.sql`), which persists.

```bash
curl "https://<your-worker>/api/usage?days=30" \
  -H "Authorization: Bearer $AJ360_DASHBOARD_TOKEN"
```

Returns: totals, clients (AI client name + version), tools called, top content
queries, countries, daily breakdown, and recent sessions.

**Privacy:** no IP addresses and no personal identifiers are stored — only the
self-reported AI client type, the tool invoked, the content query, and the
coarse country code Cloudflare already attaches to every request. The endpoint
requires `AJ360_DASHBOARD_TOKEN` and fails closed when that secret is unset.

Re-apply the schema after recreating the database:

```bash
npx wrangler d1 execute aj360-analytics --remote --file=schema.sql
```


## Endpoints, rate limits and analytics (v2.1.1+)

| Path | Container | Tools | Rate limit |
|---|---|---|---|
| `/mcp` | `AJ360Container` | 10 core tools (public) | ~60 req/min per session (per /24 range without a session) |
| `/team/<AJ360_TEAM_TOKEN>/mcp` | `AJ360TeamContainer` | all 26 (SEO + analytics) | ~300 req/min |

- Set the team secret with `wrangler secret put AJ360_TEAM_TOKEN`. A wrong token returns 404.
- Cloudflare's rate limiter is eventually consistent: short bursts pass and sustained floods are blocked (measured: blocking began about 30 s into a continuous flood).
- Each D1 row has `kind` = `human` (Claude, ChatGPT, Cursor… — see `HUMAN_CLIENTS`), `team`, or `automated` (directory indexers, probes, scripts). `/api/usage` reports `kind=human` by default and always includes the `by_kind` totals; use `?kind=all|people|team|automated` for the rest.
- Existing databases need `ALTER TABLE events ADD COLUMN kind TEXT;` (see `schema.sql`).
- A Worker-only change doesn't restart a running container; to roll out new container settings, change the image (for example a `LABEL`) so the container is replaced.
