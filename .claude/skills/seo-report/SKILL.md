---
name: seo-report
description: >-
  Deep SEO analysis for aljazeera360.com: reads the snapshot history, runs the
  MCP SEO tools for fresh data, and — via the onvesper-expert agent — turns every
  finding into concrete Vesper Back Office fix instructions. Produces a
  prioritized markdown report in reports/seo/. Use when the user asks for an SEO
  report, SEO analysis, "شوف الـ SEO", or wants to know what to fix this week.
---

# /seo-report — Deep SEO analysis with actionable Vesper fixes

You produce a prioritized, *actionable* SEO report for aljazeera360.com. The
difference between this and the raw snapshot script: you analyze trends,
prioritize, and translate every finding into exact Back Office steps.

## Inputs you have

1. **Snapshot history** — `reports/seo/history/metrics.jsonl` (gitignored,
   local-only; one JSON row per run) and rendered reports in `reports/seo/*.md`.
   If empty, this is a first run — generate a fresh baseline and say so instead
   of inventing trends.
2. **Live data** — run `python scripts/seo_snapshot.py` from the repo root for
   a fresh row (requires `AJ360_API_KEY` in env; `server.py` is imported
   directly from the repo, no install step), or import tools straight from the
   `server` module for targeted queries (e.g. `get_ai_discoverability_score`
   on one section, `get_series_seo_map` for one series,
   `audit_metadata_quality`).
3. **Platform expertise** — the `onvesper-expert` agent (`.claude/agents/`)
   knows the Vesper/Deltatre platform that powers the site, with the full docs
   mirror in `onvesper-kb/`. **Always consult it** to convert findings into
   exact Back Office/DVE steps.

## Procedure

1. Read the last snapshots from history; compute per-section trends
   (discoverability avg, health score) across the available weeks.
2. Run or refresh live data if the latest snapshot is older than 3 days.
3. Identify the top issues, e.g.:
   - Sections with declining or low (<55) discoverability
   - Videos in `needs_improvement` lists (recurring ones are top priority)
   - Metadata gaps: missing descriptions, categories, thumbnails
   - Stale sections (>30 days without new content)
   - Rising audience search tags with little matching content (content gaps)
4. For each issue class, ask the **onvesper-expert** agent HOW to fix it in the
   platform. Examples of the mapping you're after:
   - Missing/short video metadata → DVE → Video → Metadata (fields, limits)
   - Section SEO title/description → Back Office → Content → Sections (SEO metadata)
   - Typed tags coverage → DVE typed tags best practices + batch enum upload
   - Series schema/interstitials → collections & series curation pages
5. Write the report to `reports/seo/deep-dive-YYYY-MM-DD.md` (this directory
   is gitignored — reports are on-demand deliverables for the requester, never
   committed to the public repo):
   - **Executive summary** (5 lines max, Arabic)
   - **Trends** table (per section, across weeks)
   - **Priority actions** — each with: what, why (metric evidence), and *exact*
     Back Office steps (cite the onvesper-kb page used)
   - **Content gaps** — search tags/topics the audience wants but the catalog
     under-serves
6. Reply to the user with the executive summary and the report path.

## Rules

- Match the user's language (Egyptian Arabic → Arabic report body is fine;
  keep metric names in English).
- Never invent Back Office UI labels — if onvesper-expert can't confirm a
  step from the docs, say so and link the closest doc page.
- Keep the report scannable: tables + checkboxes, no walls of text.
