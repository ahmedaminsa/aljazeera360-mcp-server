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
from server import AlJazeera360Client, token_manager


async def main():
    series_name = sys.argv[1] if len(sys.argv) > 1 else "الدحيح"
    
    client = AlJazeera360Client()
    
    print(f"🔍 Searching for series: {series_name}")
    print("=" * 60)
    
    # Step 1: Search for the series
    results = await client.search(series_name, content_type="SERIES")
    
    if "error" in results:
        print(f"❌ Error: {results['error']}")
        return
    
    cards = results.get("cardList", [])
    series_card = None
    
    for card in cards:
        if card.get("type") == "SERIES":
            series_card = card
            break
    
    if not series_card:
        # Try without content_type filter
        results = await client.search(series_name)
        cards = results.get("cardList", [])
        for card in cards:
            if card.get("type") == "SERIES":
                series_card = card
                break
    
    if not series_card:
        print(f"❌ Series '{series_name}' not found")
        return
    
    series_id = series_card.get("id")
    print(f"\n✅ Found: {series_card.get('title')}")
    print(f"   ID: {series_id}")
    
    # Step 2: Get series details
    print(f"\n📺 Fetching series details...")
    details = await client.get_series(series_id)
    
    if "error" in details:
        print(f"❌ Error: {details['error']}")
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
        s_title = season.get("title", "Unknown")
        s_id = season.get("id", "")
        print(f"   • {s_title} (ID: {s_id})")
    
    # Step 3: Get episodes from latest season
    if seasons:
        latest_season = seasons[-1]
        season_id = latest_season.get("id")
        print(f"\n📋 Episodes from: {latest_season.get('title')}")
        print("-" * 40)
        
        episodes = await client.get_season_episodes(season_id)
        
        if "error" not in episodes:
            ep_list = episodes.get("episodes", [])
            for i, ep in enumerate(ep_list, 1):
                ep_title = ep.get("title", "Unknown")
                ep_id = ep.get("id", "")
                duration = ep.get("duration", 0)
                mins = int(duration) // 60 if duration else 0
                
                print(f"   {i:2d}. {ep_title} ({mins} min)")
                print(f"       🔗 https://www.aljazeera360.com/video/{ep_id}")


if __name__ == "__main__":
    asyncio.run(main())
