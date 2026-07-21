# Integrations — future metric sources (GSC, SEMrush, …)

This folder is the prepared slot for external SEO data sources. Nothing here is
implemented yet — by design. The snapshot script (`scripts/seo_snapshot.py`) is
built around a small **collectors list**; each integration becomes one more
collector that merges extra keys into the same `metrics.jsonl` row and adds a
section to the weekly report. No restructuring needed.

## Pattern (matches the MCP server's `AJ360_ENABLE_SEO_TOOLS` convention)

Each integration is **env-gated**: if its credentials env var is absent, the
collector is skipped silently. Add the collector module here, register it in
`COLLECTORS` in `scripts/seo_snapshot.py`, and add the secret to the GitHub
Action.

## Google Search Console (first candidate)

What it adds: real Google data per URL — clicks, impressions, CTR, average
position, indexing coverage. Combined with the internal metadata scores this
answers "did fixing metadata actually move rankings?"

To implement (short session once you have access):

1. In Google Cloud: create a project → enable **Search Console API** → create a
   **Service Account** → download its JSON key.
2. In Search Console: add the service account email as a (restricted) user on
   the `aljazeera360.com` property.
3. Secrets: `GSC_SERVICE_ACCOUNT_JSON` (the key file content),
   `GSC_PROPERTY=sc-domain:aljazeera360.com`.
4. Collector: `integrations/gsc.py` using `searchanalytics.query`
   (dimensions: page, query; last 7 days) → merge as `row["gsc"] = {...}`.

## SEMrush (second candidate)

What it adds: keyword rankings vs competitors, backlinks, site audit issues.

- Secret: `SEMRUSH_API_KEY`
- Collector: `integrations/semrush.py` → `row["semrush"] = {...}`
- Note: SEMrush API units are metered — keep the weekly pull narrow
  (tracked keywords + domain overview only).

## Row schema contract

Whatever the source, a collector returns `{"<name>": {…}}` and must:
- never raise for missing credentials (return `{}` / be skipped),
- keep values JSON-serializable and small (this file lives in git),
- add its own section to `render_report()` guarded by `row.get("<name>")`.
