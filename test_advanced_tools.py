"""Test script for the 5 new advanced scientific tools."""
import asyncio
import os
import json

os.environ['MCP_TRANSPORT'] = 'stdio'

from server import (
    build_knowledge_graph,
    generate_faq_schema,
    get_ai_discoverability_score,
    build_topic_clusters,
    find_evergreen_content
)

async def main():
    print("=" * 60)
    print("TEST 1: build_knowledge_graph (AJA)")
    print("=" * 60)
    result = await build_knowledge_graph(sections="AJA")
    data = json.loads(result)
    if 'error' not in data:
        s = data.get('summary', {})
        print(f"✅ Analyzed {s.get('total_videos_analyzed', 0)} videos")
        print(f"   Unique entities: {s.get('unique_entities_found', 0)}")
        top = data.get('top_entities', [])[:3]
        for e in top:
            print(f"   → {e['entity']}: {e['count']} videos ({e['percentage']}%)")
        clusters = data.get('topic_clusters', [])
        print(f"   Topic clusters: {len(clusters)}")
        for c in clusters[:3]:
            print(f"   → {c['core_topic']}: {c['total_videos']} videos, related: {c['related_topics'][:2]}")
    else:
        print(f"❌ Error: {data['error']}")

    print()
    print("=" * 60)
    print("TEST 2: generate_faq_schema (video 966083)")
    print("=" * 60)
    result = await generate_faq_schema(video_id=966083)
    data = json.loads(result)
    if 'error' not in data:
        print(f"✅ Generated {data.get('faq_count', 0)} FAQ questions")
        print(f"   Title: {data.get('title', '')[:50]}")
        for faq in data.get('faqs', [])[:2]:
            print(f"   Q: {faq['question'][:60]}")
            print(f"   A: {faq['answer'][:80]}...")
    else:
        print(f"❌ Error: {data['error']}")

    print()
    print("=" * 60)
    print("TEST 3: get_ai_discoverability_score (AJA)")
    print("=" * 60)
    result = await get_ai_discoverability_score(section_id="AJA", max_items=30)
    data = json.loads(result)
    if 'error' not in data:
        s = data.get('summary', {})
        print(f"✅ Scored {s.get('total_analyzed', 0)} videos")
        print(f"   Average score: {s.get('average_score', 0)}/100 (Grade: {s.get('average_grade', '?')})")
        print(f"   Grade distribution: {s.get('grade_distribution', {})}")
        top = data.get('top_performers', [])[:3]
        print(f"   Top performers:")
        for v in top:
            print(f"   → {v['title'][:40]}: {v['score']}/100 ({v['grade']})")
        needs = data.get('needs_improvement', [])
        print(f"   Needs improvement: {len(needs)} videos")
    else:
        print(f"❌ Error: {data['error']}")

    print()
    print("=" * 60)
    print("TEST 4: build_topic_clusters (AJA,AJD)")
    print("=" * 60)
    result = await build_topic_clusters(sections="AJA,AJD")
    data = json.loads(result)
    if 'error' not in data:
        s = data.get('summary', {})
        print(f"✅ Analyzed {s.get('total_items_analyzed', 0)} items")
        print(f"   Items in clusters: {s.get('items_in_clusters', 0)}")
        print(f"   Strong clusters: {s.get('strong_clusters', 0)}")
        clusters = data.get('clusters', [])[:4]
        for c in clusters:
            print(f"   → {c['cluster']}: {c['total_pieces']} videos ({c['seo_strength']})")
            print(f"     Pillar: {c['pillar_content']['title'][:40]}")
    else:
        print(f"❌ Error: {data['error']}")

    print()
    print("=" * 60)
    print("TEST 5: find_evergreen_content (AJA,AJD)")
    print("=" * 60)
    result = await find_evergreen_content(sections="AJA,AJD")
    data = json.loads(result)
    if 'error' not in data:
        s = data.get('summary', {})
        print(f"✅ Analyzed {s.get('total_analyzed', 0)} items")
        print(f"   Evergreen: {s.get('evergreen_count', 0)} ({s.get('evergreen_percentage', 0)}%)")
        print(f"   News: {s.get('news_count', 0)}")
        print(f"   Mixed: {s.get('mixed_count', 0)}")
        top = data.get('top_evergreen_priorities', [])[:3]
        print(f"   Top evergreen content:")
        for v in top:
            print(f"   → [{v['seo_priority_score']}pts] {v['title'][:50]}")
            print(f"     {v['action']}")
    else:
        print(f"❌ Error: {data['error']}")

    print()
    print("✅ All advanced tool tests completed!")

asyncio.run(main())
