"""
Test script for Al Jazeera 360 MCP Server
==========================================
Tests all tools against the live API to verify functionality.
Uses guest token auto-refresh — no hardcoded credentials needed.

Usage:
    python test_server.py
"""

import asyncio
import json
import sys

from server import (
    get_trending_content,
    browse_section,
    get_video_details,
    get_series_details,
    get_season_episodes,
    search_videos,
    list_sections,
    get_latest_episodes,
)


async def test_all():
    """Run all tests against the live API."""
    results = {}

    # Test 1: List Sections
    print("=" * 60)
    print("TEST 1: list_sections()")
    print("=" * 60)
    try:
        result = await list_sections()
        data = json.loads(result)
        assert data.get("total_sections") >= 10, "Expected at least 10 sections"
        print(f"  ✅ Total sections: {data.get('total_sections')}")
        for s in data.get("sections", [])[:3]:
            print(f"     - {s['id']}: {s['name_ar']}")
        results["list_sections"] = "PASS"
    except Exception as e:
        print(f"  ❌ Error: {e}")
        results["list_sections"] = f"FAIL: {e}"

    # Test 2: Get Trending Content
    print("\n" + "=" * 60)
    print("TEST 2: get_trending_content()")
    print("=" * 60)
    try:
        result = await get_trending_content()
        data = json.loads(result)
        assert "categories" in data, "Missing categories"
        print(f"  ✅ Featured: {len(data.get('featured', []))} items")
        print(f"  ✅ Categories: {len(data.get('categories', []))} buckets")
        for cat in data.get("categories", [])[:3]:
            print(f"     - {cat['name']}: {len(cat['items'])} items")
        results["get_trending"] = "PASS"
    except Exception as e:
        print(f"  ❌ Error: {e}")
        results["get_trending"] = f"FAIL: {e}"

    # Test 3: Browse Section
    print("\n" + "=" * 60)
    print("TEST 3: browse_section('Documentaries')")
    print("=" * 60)
    try:
        result = await browse_section("Documentaries")
        data = json.loads(result)
        assert data.get("section") == "برامج وثائقية", f"Unexpected section name: {data.get('section')}"
        print(f"  ✅ Section: {data.get('section')}")
        print(f"  ✅ Programs: {len(data.get('programs', []))} categories")
        for prog in data.get("programs", [])[:2]:
            print(f"     - {prog['category']}: {len(prog['items'])} items")
        results["browse_section"] = "PASS"
    except Exception as e:
        print(f"  ❌ Error: {e}")
        results["browse_section"] = f"FAIL: {e}"

    # Test 4: Get Video Details
    print("\n" + "=" * 60)
    print("TEST 4: get_video_details(953659)")
    print("=" * 60)
    try:
        result = await get_video_details(953659)
        data = json.loads(result)
        assert data.get("title"), "Missing title"
        assert data.get("watch_url"), "Missing watch_url"
        print(f"  ✅ Title: {data.get('title')}")
        print(f"  ✅ Duration: {data.get('duration')}")
        print(f"  ✅ Quality: {data.get('quality')}")
        print(f"  ✅ Watch URL: {data.get('watch_url')}")
        results["get_video_details"] = "PASS"
    except Exception as e:
        print(f"  ❌ Error: {e}")
        results["get_video_details"] = f"FAIL: {e}"

    # Test 5: Get Series Details
    print("\n" + "=" * 60)
    print("TEST 5: get_series_details(2355) — الدحيح")
    print("=" * 60)
    try:
        result = await get_series_details(2355)
        data = json.loads(result)
        assert data.get("title"), "Missing title"
        assert data.get("total_seasons") >= 1, "Expected at least 1 season"
        print(f"  ✅ Title: {data.get('title')}")
        print(f"  ✅ Total Seasons: {data.get('total_seasons')}")
        for season in data.get("seasons", [])[:3]:
            print(f"     - Season {season['season_number']}: {season['episode_count']} episodes (id={season['season_id']})")
        results["get_series_details"] = "PASS"

        # Test 6: Get Season Episodes (using first season from above)
        if data.get("seasons"):
            first_season_id = data["seasons"][0]["season_id"]
            print(f"\n{'=' * 60}")
            print(f"TEST 6: get_season_episodes({first_season_id})")
            print("=" * 60)
            result = await get_season_episodes(first_season_id)
            ep_data = json.loads(result)
            assert ep_data.get("episodes"), "No episodes returned"
            print(f"  ✅ Season: {ep_data.get('season_title')}")
            print(f"  ✅ Series: {ep_data.get('series_title')}")
            print(f"  ✅ Episodes: {ep_data.get('total_episodes')}")
            for ep in ep_data.get("episodes", [])[:3]:
                print(f"     - [{ep['id']}] {ep['title']} ({ep['duration']})")
            results["get_season_episodes"] = "PASS"
    except Exception as e:
        print(f"  ❌ Error: {e}")
        results["get_series_details"] = f"FAIL: {e}"

    # Test 7: Search Videos
    print("\n" + "=" * 60)
    print("TEST 7: search_videos('غزة')")
    print("=" * 60)
    try:
        result = await search_videos("غزة", max_results=5)
        data = json.loads(result)
        assert data.get("total_results") > 0, "No search results"
        print(f"  ✅ Query: {data.get('query')}")
        print(f"  ✅ Results: {data.get('total_results')}")
        for r in data.get("results", [])[:5]:
            print(f"     - [{r['id']}] {r['title']} ({r['type']})")
        results["search_videos"] = "PASS"
    except Exception as e:
        print(f"  ❌ Error: {e}")
        results["search_videos"] = f"FAIL: {e}"

    # Test 8: Get Latest Episodes
    print("\n" + "=" * 60)
    print("TEST 8: get_latest_episodes('AJA', count=5)")
    print("=" * 60)
    try:
        result = await get_latest_episodes("AJA", count=5)
        data = json.loads(result)
        assert data.get("latest_episodes"), "No episodes returned"
        print(f"  ✅ Section: {data.get('section')}")
        print(f"  ✅ Found: {data.get('total_found')} episodes")
        for ep in data.get("latest_episodes", [])[:3]:
            print(f"     - [{ep['id']}] {ep['title']} ({ep['duration']})")
        results["get_latest_episodes"] = "PASS"
    except Exception as e:
        print(f"  ❌ Error: {e}")
        results["get_latest_episodes"] = f"FAIL: {e}"

    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    passed = sum(1 for v in results.values() if v == "PASS")
    total = len(results)
    print(f"\n  Results: {passed}/{total} tests passed\n")
    for test, status in results.items():
        icon = "✅" if status == "PASS" else "❌"
        print(f"  {icon} {test}: {status}")

    return passed == total


if __name__ == "__main__":
    success = asyncio.run(test_all())
    sys.exit(0 if success else 1)
