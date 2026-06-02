"""Test the 5 new typedTags-based tools"""
import asyncio, json, os, sys
os.environ['MCP_TRANSPORT'] = 'stdio'
sys.path.insert(0, '/home/ubuntu/aljazeera360-mcp-server')

from server import (
    get_searchable_tags_map,
    get_genre_report,
    get_country_content_map,
    get_host_profile,
    generate_series_schema
)

async def main():
    print("=" * 60)
    print("TEST 1: get_searchable_tags_map (top 20 tags)")
    print("=" * 60)
    result = await get_searchable_tags_map(max_items=10, top_n=20)
    data = json.loads(result)
    if "error" not in data:
        print(f"✅ Scanned {data['total_videos_scanned']} videos")
        print(f"Top 10 Searchable Tags:")
        for t in data['top_searchable_tags'][:10]:
            print(f"  [{t['seo_priority'].upper()}] {t['keyword']} ({t['frequency']}x)")
        print(f"Top Countries: {[c['country'] for c in data['top_countries'][:5]]}")
        print(f"Genres: {[g['genre'] for g in data['genres_distribution'][:5]]}")
        print(f"Top Hosts: {[h['host'] for h in data['top_hosts'][:3]]}")
        print(f"SEO Insight: {data['seo_insight']}")
    else:
        print(f"❌ Error: {data['error']}")

    print()
    print("=" * 60)
    print("TEST 2: get_genre_report (صحة)")
    print("=" * 60)
    result = await get_genre_report(genre="صحة", max_items=10)
    data = json.loads(result)
    if "error" not in data:
        print(f"✅ Genres: {data['total_genres']}, Subgenres: {data['total_subgenres']}")
        for g in data['genres'][:3]:
            print(f"  Genre: {g['genre']} ({g['count']} videos)")
            print(f"  SEO Title: {g['seo_page_title']}")
        for sg in data['subgenres'][:5]:
            print(f"  Sub-genre: {sg['subgenre']} ({sg['count']} videos)")
    else:
        print(f"❌ Error: {data['error']}")

    print()
    print("=" * 60)
    print("TEST 3: get_country_content_map (all countries)")
    print("=" * 60)
    result = await get_country_content_map(country="", max_items=10)
    data = json.loads(result)
    if "error" not in data:
        print(f"✅ Total countries: {data['total_countries']}, Total videos: {data['total_videos_with_country']}")
        for c in data['countries'][:5]:
            print(f"  {c['country']}: {c['video_count']} videos | Keywords: {c['top_keywords'][:3]}")
    else:
        print(f"❌ Error: {data['error']}")

    print()
    print("=" * 60)
    print("TEST 4: get_host_profile (أحمد فاخوري)")
    print("=" * 60)
    result = await get_host_profile(host_name="أحمد فاخوري", max_items=10)
    data = json.loads(result)
    if "error" not in data:
        print(f"✅ Host: {data['host']}, Videos: {data['total_videos']}")
        print(f"  Shows: {data['shows_hosted']}")
        print(f"  Genres: {data['genres_covered']}")
        print(f"  SEO Title: {data['seo_meta_title']}")
        print(f"  Top Keywords: {data['top_keywords'][:5]}")
    else:
        print(f"❌ {data['error']} (host may not be in scanned sections)")

    print()
    print("=" * 60)
    print("TEST 5: generate_series_schema (series 2715 - شبكات)")
    print("=" * 60)
    result = await generate_series_schema(series_id=2715)
    data = json.loads(result)
    if "error" not in data:
        print(f"✅ Series: {data['series_title']}")
        print(f"  Episodes found: {data['total_episodes_found']}")
        print(f"  Genres: {data['genres']}")
        print(f"  Hosts: {data['hosts']}")
        print(f"  SEO Title: {data['seo_meta_title']}")
        print(f"  Top Keywords: {data['top_keywords'][:5]}")
        schema = data['tv_series_schema']
        print(f"  Schema type: {schema['@type']}")
        print(f"  Episodes in schema: {len(schema.get('episode', []))}")
    else:
        print(f"❌ {data['error']}")

asyncio.run(main())
