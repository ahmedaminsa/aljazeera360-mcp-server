"""
Example: Explore a series on Al Jazeera 360.

This script searches for a series by name, retrieves its details
(all seasons), and lists episodes from the latest season.

Usage:
    export AJ360_REFRESH_TOKEN="your-token"
    python examples/explore_series.py "الدحيح"
"""

import asyncio
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from server import AlJazeera360Client, format_search_results, format_duration, PLATFORM_URL


async def main():
    series_name = sys.argv[1] if len(sys.argv) > 1 else "الدحيح"
    
    client = AlJazeera360Client()
    
    print(f"🔍 Searching for series: {series_name}")
    print("=" * 60)
    
    # Step 1: Search for the series
    data = await client.search_content(series_name)
    
    if not data:
        print("❌ Error: No response from API")
        return
    
    results = format_search_results(data)
    
    # Find a SERIES type result
    series_item = None
    for item in results:
        if item.get("type") == "SERIES":
            series_item = item
            break
    
    # If no SERIES found, show first result
    if not series_item and results:
        series_item = results[0]
    
    if not series_item:
        print(f"❌ Series '{series_name}' not found")
        return
    
    series_id = series_item.get("id")
    print(f"\n✅ Found: {series_item.get('title')}")
    print(f"   Type: {series_item.get('type')}")
    print(f"   ID: {series_id}")
    
    # Step 2: Get series details (only works for SERIES type)
    if series_item.get("type") != "SERIES":
        print(f"\n⚠️  Result is a {series_item.get('type')}, not a SERIES. Cannot fetch seasons.")
        print(f"   🔗 {series_item.get('watch_url')}")
        return
    
    print(f"\n📺 Fetching series details...")
    details = await client.get_series_details(int(series_id))
    
    if not details:
        print("❌ Error: Could not fetch series details")
        return
    
    title = details.get("title", "Unknown")
    description = details.get("description", "No description")
    seasons = details.get("seasons", [])
    
    print(f"\n{'─' * 60}")
    print(f"📺 {title}")
    print(f"{'─' * 60}")
    print(f"📝 {description[:200]}")
    print(f"🗓️  Seasons: {len(seasons)}")
    print()
    
    for season in seasons:
        s_title = season.get("title", f"Season {season.get('seasonNumber', '?')}")
        s_id = season.get("id", "")
        ep_count = season.get("episodeCount", "?")
        print(f"   • {s_title} — {ep_count} episodes (ID: {s_id})")
    
    # Step 3: Get episodes from latest season
    if seasons:
        latest_season = seasons[-1]
        season_id = latest_season.get("id")
        print(f"\n📋 Episodes from: {latest_season.get('title', 'Latest Season')}")
        print("-" * 40)
        
        episodes_data = await client.get_season_episodes(int(season_id))
        
        if episodes_data:
            ep_list = episodes_data.get("episodes", [])
            for i, ep in enumerate(ep_list, 1):
                ep_title = ep.get("title", "Unknown")
                ep_id = ep.get("id", "")
                duration = ep.get("duration")
                duration_str = format_duration(duration) if duration else "N/A"
                
                print(f"   {i:2d}. {ep_title} ({duration_str})")
                print(f"       🔗 {PLATFORM_URL}/video/{ep_id}")


if __name__ == "__main__":
    asyncio.run(main())
