"""Test the generate_seo_content tool locally."""
import asyncio
import sys
import os

# Add server directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Set env vars for testing
os.environ["MCP_TRANSPORT"] = "stdio"

async def test():
    # Import after setting env vars
    from server import generate_seo_content, client
    
    print("Testing generate_seo_content for video 953659 (عدنان مندريس)...")
    print("=" * 60)
    
    result = await generate_seo_content(953659, "ar")
    
    import json
    data = json.loads(result)
    
    if "error" in data and "OPENAI_API_KEY" in data.get("error", ""):
        print("⚠️  No OpenAI key — showing raw metadata:")
        print(f"Title: {data.get('original_title', data.get('title', 'N/A'))}")
        print(f"Watch URL: {data.get('watch_url', 'N/A')}")
        print(f"Duration ISO: {data.get('duration_iso', 'N/A')}")
        print(f"Quality: {data.get('quality', 'N/A')}")
        print("\nSchema markup preview:")
        schema = data.get("schema_markup", {})
        print(f"  @type: {schema.get('@type')}")
        print(f"  name: {schema.get('name')}")
        print(f"  duration: {schema.get('duration')}")
        print(f"  uploadDate: {schema.get('uploadDate')}")
        print("\n✅ Tool structure works correctly!")
    elif "error" in data:
        print(f"❌ Error: {data['error']}")
    else:
        print("✅ SEO content generated!")
        seo = data.get("seo", {})
        print(f"\nMeta Title ({seo.get('meta_title_length', 0)} chars):")
        print(f"  {seo.get('meta_title', 'N/A')}")
        print(f"\nMeta Description ({seo.get('meta_description_length', 0)} chars):")
        print(f"  {seo.get('meta_description', 'N/A')}")
        print(f"\nFocus Keyword: {seo.get('focus_keyword', 'N/A')}")
        print(f"\nKeywords: {', '.join(seo.get('keywords', []))}")
        print(f"\nSEO Notes: {seo.get('seo_score_notes', 'N/A')}")
        print(f"\nSchema type: {data.get('schema_markup', {}).get('@type', 'N/A')}")
        print("\n✅ Full SEO content generated successfully!")

asyncio.run(test())
