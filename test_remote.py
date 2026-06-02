"""
Test the remote MCP server deployed on Railway.
Connects via SSE and calls tools to generate analytics data.
"""
import asyncio
import json
from mcp import ClientSession
from mcp.client.sse import sse_client

SERVER_URL = "https://aljazeera360-mcp-server-production.up.railway.app/sse"


async def main():
    print(f"Connecting to: {SERVER_URL}")
    print("=" * 60)
    
    async with sse_client(SERVER_URL) as (read_stream, write_stream):
        async with ClientSession(read_stream, write_stream) as session:
            # Initialize
            await session.initialize()
            print("✅ Connected and initialized!")
            print()
            
            # List available tools
            tools = await session.list_tools()
            print(f"📦 Available tools ({len(tools.tools)}):")
            for tool in tools.tools:
                print(f"   - {tool.name}")
            print()
            
            # Call: list_sections
            print("🔧 Calling: list_sections")
            result = await session.call_tool("list_sections", {})
            data = json.loads(result.content[0].text)
            print(f"   → Got {len(data.get('sections', []))} sections")
            print()
            
            # Call: get_trending_content
            print("🔧 Calling: get_trending_content")
            result = await session.call_tool("get_trending_content", {})
            data = json.loads(result.content[0].text)
            categories = data.get("categories", [])
            print(f"   → Got {len(categories)} categories")
            if categories:
                print(f"   → First category: {categories[0].get('name', 'N/A')}")
            print()
            
            # Call: search_videos
            print("🔧 Calling: search_videos('وثائقي')")
            result = await session.call_tool("search_videos", {"query": "وثائقي"})
            data = json.loads(result.content[0].text)
            results_list = data.get("results", [])
            print(f"   → Got {len(results_list)} results")
            if results_list:
                print(f"   → First result: {results_list[0].get('title', 'N/A')}")
            print()
            
            # Call: browse_section
            print("🔧 Calling: browse_section('AJD')")
            result = await session.call_tool("browse_section", {"section_id": "AJD"})
            data = json.loads(result.content[0].text)
            section_categories = data.get("categories", [])
            print(f"   → Got {len(section_categories)} categories from AJD")
            print()
            
            # Call: search_videos again with different query
            print("🔧 Calling: search_videos('فلسطين')")
            result = await session.call_tool("search_videos", {"query": "فلسطين"})
            data = json.loads(result.content[0].text)
            results_list = data.get("results", [])
            print(f"   → Got {len(results_list)} results")
            print()
            
            print("=" * 60)
            print("✅ All tests passed! Check the dashboard for updated analytics.")
            print(f"   Dashboard: https://aljazeera360-mcp-server-production.up.railway.app/")


if __name__ == "__main__":
    asyncio.run(main())
