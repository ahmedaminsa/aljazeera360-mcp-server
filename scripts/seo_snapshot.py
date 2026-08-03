#!/usr/bin/env python3
"""SEO snapshot collector for aljazeera360.com.

Runs the SEO analysis tools from this repo's `server` module against the live
platform, appends one metrics row to reports/seo/history/metrics.jsonl, and
renders a markdown report (reports/seo/YYYY-MM-DD.md) with deltas vs the
previous snapshot. Reports are on-demand and local-only (reports/ is
gitignored — never committed).

Designed as a small list of *collectors* so new metric sources (e.g. Google
Search Console, SEMrush — see integrations/README.md) can be added without
restructuring: each collector returns a dict that is merged into the row.

Environment:
    AJ360_API_KEY          required — platform API key
    AJ360_REFRESH_TOKEN    optional — guest mode works for read-only analysis
    SNAPSHOT_SECTIONS      csv of section ids to score
                           (default: AJA,AJD,AJ360-Originals,Podcast,Documentaries)
    SNAPSHOT_AUDIT_ITEMS   items audited per section (default 30)
    SNAPSHOT_TAGS_ITEMS    videos scanned for the tag map (default 12; each is
                           an extra API call, keep small in CI)

Usage:
    python scripts/seo_snapshot.py
"""

import asyncio
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

# server.py lives at the repo root — no install step needed.
sys.path.insert(0, str(REPO_ROOT))
import server  # noqa: E402
REPORTS_DIR = REPO_ROOT / "reports" / "seo"
HISTORY_FILE = REPORTS_DIR / "history" / "metrics.jsonl"

SECTIONS = [
    s.strip()
    for s in os.environ.get(
        "SNAPSHOT_SECTIONS", "AJA,AJD,AJ360-Originals,Podcast,Documentaries"
    ).split(",")
    if s.strip()
]
AUDIT_ITEMS = int(os.environ.get("SNAPSHOT_AUDIT_ITEMS", "30"))
TAGS_ITEMS = int(os.environ.get("SNAPSHOT_TAGS_ITEMS", "12"))


def _pct(value: str) -> float:
    """'78.0%' -> 78.0"""
    try:
        return float(str(value).rstrip("%"))
    except (ValueError, TypeError):
        return 0.0


async def _call(tool, *args, **kwargs) -> dict:
    """Call an MCP tool function and parse its JSON string result."""
    raw = await tool(*args, **kwargs)
    data = json.loads(raw)
    if isinstance(data, dict) and "error" in data and len(data) == 1:
        raise RuntimeError(f"{tool.__name__}: {data['error']}")
    return data


# ---------------------------------------------------------------------------
# Collectors — each returns a dict merged into the snapshot row.
# To add a new source (GSC, SEMrush…), append (name, coroutine_fn) below.
# ---------------------------------------------------------------------------

async def collect_sections() -> dict:
    """Per-section AI discoverability + metadata health."""
    out = {}
    for section in SECTIONS:
        entry = {}
        try:
            disc = await _call(
                server.get_ai_discoverability_score, section_id=section, max_items=AUDIT_ITEMS
            )
            s = disc["summary"]
            entry.update(
                discoverability_avg=s["average_score"],
                discoverability_grade=s["average_grade"],
                grade_distribution=s["grade_distribution"],
                analyzed=s["total_analyzed"],
                needs_improvement=[
                    {"id": i["id"], "title": i["title"], "score": i["score"]}
                    for i in disc.get("needs_improvement", [])
                ],
            )
        except Exception as e:  # noqa: BLE001 — one failing section must not kill the run
            entry["discoverability_error"] = str(e)
        try:
            audit = await _call(
                server.audit_metadata_quality,
                section_id=section,
                max_items=AUDIT_ITEMS,
                page_size=AUDIT_ITEMS,
            )
            entry.update(
                health_score=_pct(audit["health_score"]),
                audited=audit["total_audited"],
                issues={k: v["count"] for k, v in audit["summary"].items()},
                recommendations=audit.get("recommendations", []),
            )
        except Exception as e:  # noqa: BLE001
            entry["audit_error"] = str(e)
        out[section] = entry
    return {"sections": out}


async def collect_catalog() -> dict:
    """Whole-catalog freshness overview."""
    data = await _call(server.compare_sections)
    s = data["summary"]
    return {
        "catalog": {
            "total_sections": s["total_sections"],
            "active_sections_7d": s["active_sections_last_7_days"],
            "stale_sections_30d": s["stale_sections_over_30_days"],
            "most_active": s["most_active"],
            "least_active": s["least_active"],
            "stale_list": [
                sec["section_id"]
                for sec in data.get("sections", [])
                if sec.get("days_since_update", 0) > 30
            ],
        }
    }


async def collect_tags() -> dict:
    """What the audience actually searches for (typed tags)."""
    data = await _call(server.get_searchable_tags_map, max_items=TAGS_ITEMS, top_n=25)
    return {
        "tags": {
            "videos_scanned": data["total_videos_scanned"],
            "top": data["top_searchable_tags"][:15],
            "top_countries": data["top_countries"][:10],
        }
    }


async def collect_trending() -> dict:
    """Trending keywords + publishing cadence from the homepage."""
    data = await _call(server.get_trending_topics, top_n=15)
    return {
        "trending": {
            "top_keywords": data["top_keywords"],
            "top_categories": data["top_categories"][:5],
            "quality_distribution": data["quality_distribution"],
            "published_last_7d": len(data.get("recent_content_last_7_days", [])),
        }
    }


COLLECTORS = [
    ("sections", collect_sections),
    ("catalog", collect_catalog),
    ("tags", collect_tags),
    ("trending", collect_trending),
    # ("gsc", collect_gsc),        ← future: integrations/README.md
    # ("semrush", collect_semrush) ← future
]


# ---------------------------------------------------------------------------
# Report rendering
# ---------------------------------------------------------------------------

def _delta(cur, prev) -> str:
    if prev is None or cur is None:
        return "—"
    d = round(cur - prev, 1)
    if d > 0:
        return f"🟢 +{d}"
    if d < 0:
        return f"🔴 {d}"
    return "⚪ 0"


def render_report(row: dict, prev: dict | None) -> str:
    date = row["date"]
    lines = [
        f"# SEO Snapshot — {date}",
        "",
        f"> Generated by `scripts/seo_snapshot.py` at {row['ts']} · "
        f"sections: {', '.join(SECTIONS)} · {AUDIT_ITEMS} items/section",
        "",
        "## Scorecard per section",
        "",
        "| Section | AI Discoverability | Δ | Grade | Metadata Health | Δ | Audited |",
        "|---|---|---|---|---|---|---|",
    ]
    prev_sections = (prev or {}).get("sections", {})
    for sec, m in row.get("sections", {}).items():
        p = prev_sections.get(sec, {})
        disc = m.get("discoverability_avg")
        health = m.get("health_score")
        lines.append(
            f"| {sec} "
            f"| {disc if disc is not None else '⚠️ err'} "
            f"| {_delta(disc, p.get('discoverability_avg'))} "
            f"| {m.get('discoverability_grade', '—')} "
            f"| {health if health is not None else '⚠️ err'}% "
            f"| {_delta(health, p.get('health_score'))} "
            f"| {m.get('audited', m.get('analyzed', '—'))} |"
        )

    cat = row.get("catalog", {})
    if cat:
        lines += [
            "",
            "## Catalog freshness",
            "",
            f"- **Active sections (last 7d):** {cat.get('active_sections_7d')} / {cat.get('total_sections')}",
            f"- **Stale sections (>30d):** {cat.get('stale_sections_30d')}"
            + (f" — {', '.join(cat['stale_list'])}" if cat.get("stale_list") else ""),
            f"- **Most active:** {cat.get('most_active')} · **Least active:** {cat.get('least_active')}",
        ]

    trend = row.get("trending", {})
    if trend:
        kw = ", ".join(f"{k['keyword']} ({k['count']})" for k in trend.get("top_keywords", [])[:8])
        lines += [
            "",
            "## Trending now",
            "",
            f"- **Top keywords:** {kw}",
            f"- **Published in last 7 days:** {trend.get('published_last_7d')}",
        ]

    tags = row.get("tags", {})
    if tags:
        tg = ", ".join(f"{t['keyword']} ({t['frequency']})" for t in tags.get("top", [])[:10])
        lines += [
            "",
            "## Audience search tags (typed tags)",
            "",
            f"- **Top searchable tags:** {tg}",
            f"- _Scanned {tags.get('videos_scanned')} videos — raise `SNAPSHOT_TAGS_ITEMS` for wider coverage._",
        ]

    # Action list: worst offenders across sections
    fixes = []
    for sec, m in row.get("sections", {}).items():
        for item in m.get("needs_improvement", [])[:3]:
            fixes.append(
                f"- [ ] **{sec}** · [{item['title']}](https://www.aljazeera360.com/video/{item['id']})"
                f" — discoverability {item['score']}/100 → fix metadata in Back Office (DVE → Video → Metadata)"
            )
        for rec in m.get("recommendations", [])[:2]:
            fixes.append(f"- [ ] **{sec}** · {rec}")
    if fixes:
        lines += ["", "## Action items", ""] + fixes

    errors = [
        f"- `{sec}`: {m.get('discoverability_error') or m.get('audit_error')}"
        for sec, m in row.get("sections", {}).items()
        if m.get("discoverability_error") or m.get("audit_error")
    ] + [f"- `{name}`: {err}" for name, err in row.get("collector_errors", {}).items()]
    if errors:
        lines += ["", "## Collector errors", ""] + errors

    lines += [
        "",
        "---",
        "_For a deep-dive with Vesper Back Office fix instructions, run the `/seo-report` skill._",
        "",
    ]
    return "\n".join(lines)


# ---------------------------------------------------------------------------

async def main() -> int:
    if not os.environ.get("AJ360_API_KEY"):
        print("ERROR: AJ360_API_KEY is required", file=sys.stderr)
        return 1

    now = datetime.now(timezone.utc)
    row: dict = {"date": now.strftime("%Y-%m-%d"), "ts": now.isoformat(timespec="seconds")}
    errors: dict = {}

    for name, collector in COLLECTORS:
        print(f"→ collecting {name} ...", flush=True)
        try:
            row.update(await collector())
        except Exception as e:  # noqa: BLE001 — record and continue
            errors[name] = str(e)
            print(f"  ⚠️  {name} failed: {e}", file=sys.stderr)
    if errors:
        row["collector_errors"] = errors

    # Previous snapshot for deltas
    prev = None
    if HISTORY_FILE.exists():
        history_lines = HISTORY_FILE.read_text().strip().splitlines()
        if history_lines:
            prev = json.loads(history_lines[-1])

    HISTORY_FILE.parent.mkdir(parents=True, exist_ok=True)
    with HISTORY_FILE.open("a") as f:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")

    report_path = REPORTS_DIR / f"{row['date']}.md"
    report_path.write_text(render_report(row, prev), encoding="utf-8")

    print(f"✅ snapshot appended to {HISTORY_FILE.relative_to(REPO_ROOT)}")
    print(f"✅ report written to {report_path.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
