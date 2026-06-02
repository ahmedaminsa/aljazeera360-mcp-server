#!/usr/bin/env python3
"""Investigate the Vesper search API to find the best relevance parameters."""
import asyncio
import httpx
import json

API_BASE = "https://dce-frontoffice.imggaming.com"
SEARCH_API = "https://search.dce-prod.dicelaboratory.com/search"
API_KEY = "REDACTED_API_KEY"
REALM = "dce.aljazeera"

async def get_token():
    async with httpx.AsyncClient(timeout=15) as http:
        resp = await http.get(
            f"{API_BASE}/api/v1/init/",
            params={"lk": "language", "menuTargetPlatform": "WEB", "rpp": "12", "section": "home"},
            headers={"Accept": "application/json", "x-api-key": API_KEY, "Realm": REALM}
        )
        return resp.json()["authentication"]["authorisationToken"]

def get_headers(token):
    return {
        "Accept": "application/json",
        "x-api-key": API_KEY,
        "Realm": REALM,
        "Authorization": f"Bearer {token}",
    }

def extract_titles(data):
    """Extract titles from search response."""
    titles = []
    for element in data.get("elements", []):
        if element.get("$type") == "cardList":
            cards = element.get("attributes", {}).get("cards", [])
            for card in cards:
                attrs = card.get("attributes", {})
                # Try to get title from contentTokens
                tokens = attrs.get("contentTokens", [])
                title = ""
                for t in tokens:
                    if t.get("type") == "TITLE":
                        title = t.get("value", "")
                        break
                if not title:
                    title = attrs.get("title", attrs.get("label", "?"))
                titles.append(title)
    return titles

async def test_search_params(token, query="غزة"):
    """Test different search parameter combinations."""
    print(f"\n{'='*60}")
    print(f"Testing search for: '{query}'")
    print(f"{'='*60}")
    
    async with httpx.AsyncClient(timeout=30) as http:
        headers = get_headers(token)
        
        # Test 1: Basic search (current implementation)
        print("\n[1] Basic search (current):")
        resp = await http.get(SEARCH_API, params={"term": query, "pageSize": 5, "timezone": "UTC"}, headers=headers)
        if resp.status_code == 200:
            titles = extract_titles(resp.json())
            print(f"   Results: {titles[:5]}")
        else:
            print(f"   Error: {resp.status_code}")
        
        # Test 2: With sort=RELEVANCE
        print("\n[2] With sort=RELEVANCE:")
        resp = await http.get(SEARCH_API, params={"term": query, "pageSize": 5, "timezone": "UTC", "sort": "RELEVANCE"}, headers=headers)
        if resp.status_code == 200:
            titles = extract_titles(resp.json())
            print(f"   Results: {titles[:5]}")
        else:
            print(f"   Error {resp.status_code}: {resp.text[:100]}")
        
        # Test 3: With sort=SCORE
        print("\n[3] With sort=SCORE:")
        resp = await http.get(SEARCH_API, params={"term": query, "pageSize": 5, "timezone": "UTC", "sort": "SCORE"}, headers=headers)
        if resp.status_code == 200:
            titles = extract_titles(resp.json())
            print(f"   Results: {titles[:5]}")
        else:
            print(f"   Error {resp.status_code}: {resp.text[:100]}")
        
        # Test 4: With type=VOD filter
        print("\n[4] With type=VOD:")
        resp = await http.get(SEARCH_API, params={"term": query, "pageSize": 5, "timezone": "UTC", "type": "VOD"}, headers=headers)
        if resp.status_code == 200:
            titles = extract_titles(resp.json())
            print(f"   Results: {titles[:5]}")
        else:
            print(f"   Error {resp.status_code}: {resp.text[:100]}")
        
        # Test 5: Check what fields are available in the response
        print("\n[5] Full response structure (first result):")
        resp = await http.get(SEARCH_API, params={"term": query, "pageSize": 2, "timezone": "UTC"}, headers=headers)
        if resp.status_code == 200:
            data = resp.json()
            print(f"   Top-level keys: {list(data.keys())}")
            elements = data.get("elements", [])
            if elements:
                el = elements[0]
                print(f"   First element type: {el.get('$type')}")
                attrs = el.get("attributes", {})
                print(f"   Attributes keys: {list(attrs.keys())[:10]}")
                cards = attrs.get("cards", [])
                if cards:
                    card = cards[0]
                    card_attrs = card.get("attributes", {})
                    print(f"   Card attributes keys: {list(card_attrs.keys())[:15]}")
                    # Check for score/relevance fields
                    print(f"   Card score: {card_attrs.get('score', 'N/A')}")
                    print(f"   Card rank: {card_attrs.get('rank', 'N/A')}")
                    action = card_attrs.get("action", {})
                    action_data = action.get("data", {})
                    print(f"   Action data keys: {list(action_data.keys())[:10]}")
        
        # Test 6: Try the frontoffice search endpoint
        print("\n[6] Frontoffice search endpoint (/api/v4/vod/search):")
        resp = await http.get(
            f"{API_BASE}/api/v4/vod/search",
            params={"q": query, "rpp": 5},
            headers=headers
        )
        print(f"   Status: {resp.status_code}")
        if resp.status_code == 200:
            data = resp.json()
            print(f"   Keys: {list(data.keys())}")
            vods = data.get("vods", data.get("data", []))
            print(f"   Count: {len(vods)}")
            for v in vods[:3]:
                print(f"   - {v.get('title', '?')}")
        else:
            print(f"   Error: {resp.text[:200]}")
        
        # Test 7: Try the frontoffice search v2
        print("\n[7] Frontoffice search (/api/v2/search):")
        resp = await http.get(
            f"{API_BASE}/api/v2/search",
            params={"term": query, "rpp": 5},
            headers=headers
        )
        print(f"   Status: {resp.status_code}")
        if resp.status_code == 200:
            data = resp.json()
            print(f"   Keys: {list(data.keys())}")
        else:
            print(f"   Error: {resp.text[:100]}")
        
        # Test 8: Vesper search with different realm/customer params
        print("\n[8] Vesper search with realm param:")
        resp = await http.get(
            SEARCH_API,
            params={"term": query, "pageSize": 5, "timezone": "UTC", "realm": REALM},
            headers=headers
        )
        if resp.status_code == 200:
            titles = extract_titles(resp.json())
            print(f"   Results: {titles[:5]}")
        else:
            print(f"   Error {resp.status_code}: {resp.text[:100]}")

async def main():
    print("Getting auth token...")
    token = await get_token()
    print(f"Got token: {token[:40]}...")
    
    # Test with "غزة" (Gaza) - the problematic query
    await test_search_params(token, "غزة")
    
    # Test with "فلسطين" (Palestine) for comparison
    await test_search_params(token, "فلسطين")
    
    print("\n" + "="*60)
    print("Investigation complete!")

if __name__ == "__main__":
    asyncio.run(main())
