"""Test all new MCP tools locally."""
import asyncio
import sys
import os
import json

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ["MCP_TRANSPORT"] = "stdio"

async def test():
    from server import (
        generate_sitemap, audit_metadata_quality,
        get_trending_topics, compare_sections, get_series_seo_map
    )

    print("\n" + "="*60)
    print("TEST 1: audit_metadata_quality (AJA section)")
    print("="*60)
    result = await audit_metadata_quality("AJA", max_items=20)
    data = json.loads(result)
    if "error" in data:
        print(f"❌ Error: {data['error']}")
    else:
        print(f"✅ Audited {data['total_audited']} items")
        print(f"   Health Score: {data['health_score']}")
        print(f"   Items with no issues: {data['items_with_no_issues']}")
        s = data.get("summary", {})
        print(f"   Missing description: {s.get('missing_description', {}).get('count', 0)}")
        print(f"   Missing categories: {s.get('missing_categories', {}).get('count', 0)}")
        print(f"   Low quality video: {s.get('low_quality_video', {}).get('count', 0)}")

    print("\n" + "="*60)
    print("TEST 2: get_trending_topics")
    print("="*60)
    result = await get_trending_topics(top_n=10)
    data = json.loads(result)
    if "error" in data:
        print(f"❌ Error: {data['error']}")
    else:
        print(f"✅ Analyzed {data['total_items_analyzed']} items")
        print(f"   Top keywords: {[k['keyword'] for k in data.get('top_keywords', [])[:5]]}")
        print(f"   Quality: {data.get('quality_distribution', {})}")
        print(f"   Recent (7 days): {len(data.get('recent_content_last_7_days', []))} items")
        for insight in data.get("content_strategy_insights", []):
            print(f"   💡 {insight}")

    print("\n" + "="*60)
    print("TEST 3: compare_sections")
    print("="*60)
    result = await compare_sections()
    data = json.loads(result)
    if "error" in data:
        print(f"❌ Error: {data['error']}")
    else:
        summary = data.get("summary", {})
        print(f"✅ Compared {summary.get('total_sections', 0)} sections")
        print(f"   Active (last 7 days): {summary.get('active_sections_last_7_days', 0)}")
        print(f"   Stale (>30 days): {summary.get('stale_sections_over_30_days', 0)}")
        print(f"   Most active: {summary.get('most_active', 'N/A')}")
        sections = data.get("sections", [])[:3]
        for s in sections:
            print(f"   {s.get('freshness', '')} {s['section_name']}: {s.get('items_loaded', 0)} items, latest: {s.get('latest_content', 'N/A')}")

    print("\n" + "="*60)
    print("TEST 4: generate_sitemap (AJA section only for speed)")
    print("="*60)
    result = await generate_sitemap(sections="AJA", max_per_section=10)
    data = json.loads(result)
    if "error" in data:
        print(f"❌ Error: {data['error']}")
    else:
        print(f"✅ Generated sitemap with {data['total_urls']} URLs")
        print(f"   Sections: {data['section_counts']}")
        xml_preview = data.get("sitemap_xml", "")[:200]
        print(f"   XML preview: {xml_preview}...")

    print("\n✅ All tests completed!")

asyncio.run(test())
