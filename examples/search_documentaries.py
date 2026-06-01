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
from server import AlJazeera360Client, format_search_results


async def main():
    topic = sys.argv[1] if len(sys.argv) > 1 else "غزة"
    
    client = AlJazeera360Client()
    
    print(f"🔍 Searching Al Jazeera 360 for: {topic}")
    print("-" * 50)
    
    data = await client.search_content(topic)
    
    if not data:
        print("❌ Error: No response from API")
        return
    
    results = format_search_results(data)
    
    if not results:
        print("❌ No results found")
        return
    
    print(f"📺 Found {len(results)} results:\n")
    
    for i, item in enumerate(results, 1):
        title = item.get("title", "Unknown")
        content_type = item.get("type", "VOD")
        watch_url = item.get("watch_url", "")
        
        print(f"  {i}. [{content_type}] {title}")
        print(f"     🔗 {watch_url}")
        print()


if __name__ == "__main__":
    asyncio.run(main())
