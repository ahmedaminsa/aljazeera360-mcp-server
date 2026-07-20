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
- **Sessions**: a single named instance (`getByName("mcp")`) keeps MCP
  streamable-http sessions on one backend. Don't raise `max_instances`
  without adding session-aware routing.
- **Custom domain**: add a route/custom domain in the Cloudflare dashboard,
  then set `AJ360_ALLOWED_HOST` to that domain and redeploy.
- The `@cloudflare/containers` API is still evolving; if a deploy fails after
  an SDK update, check https://developers.cloudflare.com/containers/
