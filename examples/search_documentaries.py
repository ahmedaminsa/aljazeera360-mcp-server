"""
Example: Search for documentaries on Al Jazeera 360.

This script demonstrates how to use the MCP server programmatically
(without an AI client) to search for documentaries about a topic.

Usage:
    export AJ360_REFRESH_TOKEN="your-token"
    python examples/search_documentaries.py "فلسطين"
"""

import asyncio
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from server import AlJazeera360Client, token_manager


async def main():
    topic = sys.argv[1] if len(sys.argv) > 1 else "غزة"
    
    client = AlJazeera360Client()
    
    print(f"🔍 Searching Al Jazeera 360 for: {topic}")
    print("-" * 50)
    
    results = await client.search(topic, content_type="VOD")
    
    if "error" in results:
        print(f"❌ Error: {results['error']}")
        return
    
    cards = results.get("cardList", [])
    print(f"📺 Found {len(cards)} results:\n")
    
    for i, card in enumerate(cards, 1):
        title = card.get("title", "Unknown")
        content_id = card.get("id", "")
        duration = card.get("duration", "")
        
        # Format duration
        if duration:
            mins = int(duration) // 60
            secs = int(duration) % 60
            duration_str = f" ({mins}:{secs:02d})"
        else:
            duration_str = ""
        
        watch_url = f"https://www.aljazeera360.com/video/{content_id}"
        
        print(f"  {i}. {title}{duration_str}")
        print(f"     🔗 {watch_url}")
        print()


if __name__ == "__main__":
    asyncio.run(main())
