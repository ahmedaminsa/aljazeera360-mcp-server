"""
Example: Get trending content from Al Jazeera 360 homepage.

This script fetches the featured content and trending categories
from the Al Jazeera 360 homepage.

Usage:
    export AJ360_REFRESH_TOKEN="your-token"
    python examples/trending_content.py
"""

import asyncio
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from server import AlJazeera360Client, token_manager


async def main():
    client = AlJazeera360Client()
    
    print("🏠 Fetching Al Jazeera 360 Homepage...")
    print("=" * 60)
    
    data = await client.get_home_content()
    
    if "error" in data:
        print(f"❌ Error: {data['error']}")
        return
    
    # Featured content (heroes)
    heroes = data.get("heroes", [])
    if heroes:
        print(f"\n⭐ FEATURED ({len(heroes)} items):")
        print("-" * 40)
        for hero in heroes:
            title = hero.get("title", "Unknown")
            desc = hero.get("description", "")[:80]
            print(f"  • {title}")
            if desc:
                print(f"    {desc}...")
            print()
    
    # Content buckets (categories)
    buckets = data.get("buckets", [])
    if buckets:
        print(f"\n📂 CATEGORIES ({len(buckets)} sections):")
        print("-" * 40)
        for bucket in buckets:
            name = bucket.get("name", "Unknown")
            items = bucket.get("contents", [])
            print(f"\n  📁 {name} ({len(items)} items)")
            for item in items[:3]:  # Show first 3 per category
                title = item.get("title", "Unknown")
                content_id = item.get("id", "")
                print(f"     • {title}")
                print(f"       🔗 https://www.aljazeera360.com/video/{content_id}")


if __name__ == "__main__":
    asyncio.run(main())
