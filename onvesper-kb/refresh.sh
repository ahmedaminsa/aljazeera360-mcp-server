#!/usr/bin/env bash
# Rebuild the local Onvesper docs mirror from docs.onvesper.com.
# Usage: bash onvesper-kb/refresh.sh   (run from the repo root or from onvesper-kb/)
#
# 1. Downloads the official flat index (llms.txt) and the page sitemap.
# 2. Rebuilds _sources/_urls.txt from the sitemap (so new pages are picked up).
# 3. Downloads every page as clean Markdown into pages/, mirroring the site URLs.
set -euo pipefail

cd "$(dirname "$0")"
BASE="https://docs.onvesper.com/platform-knowledge-base"

mkdir -p _sources pages

echo "Fetching index + sitemap..."
curl -sL --retry 2 "$BASE/llms.txt" -o _sources/llms.txt
curl -sL --retry 2 "$BASE/sitemap-pages.xml" -o _sources/sitemap-pages.xml

# Build _urls.txt: strip the base prefix from every <loc>; drop the root page.
grep -oE "<loc>[^<]+</loc>" _sources/sitemap-pages.xml \
  | sed -e 's|<loc>||' -e 's|</loc>||' -e "s|^$BASE/*||" \
  | grep -v '^$' > _sources/_urls.txt

TOTAL=$(wc -l < _sources/_urls.txt)
echo "Downloading $TOTAL pages (8 in parallel)..."

export BASE
xargs -P 8 -I{} sh -c '
  out="pages/{}.md"
  mkdir -p "$(dirname "$out")"
  curl -sL --retry 2 --max-time 30 "$BASE/{}.md" -o "$out" || echo "FAILED: {}"
' < _sources/_urls.txt

# Root/master index page
curl -sL --retry 2 "$BASE.md" -o pages/_master.md || true

PAGES=$(find pages -name '*.md' | wc -l)
echo "Done: $PAGES markdown pages in pages/"
