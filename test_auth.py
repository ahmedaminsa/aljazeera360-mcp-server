#!/usr/bin/env python3
"""Test the new authentication endpoints."""
import asyncio
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

# Import the TokenManager from server
import importlib.util
spec = importlib.util.spec_from_file_location("server", "/home/ubuntu/aljazeera360-mcp-server/server.py")
# We can't import server directly due to FastMCP side effects, so test manually

import httpx

API_BASE = "https://dce-frontoffice.imggaming.com"
API_KEY = "REDACTED_API_KEY"
REALM = "dce.aljazeera"

async def test_guest_token():
    """Test the new /api/v1/init guest token endpoint."""
    print("=== Testing Guest Token (/api/v1/init) ===")
    async with httpx.AsyncClient(timeout=15) as http:
        resp = await http.get(
            f"{API_BASE}/api/v1/init/",
            params={
                "lk": "language",
                "menuTargetPlatform": "WEB",
                "rpp": "12",
                "section": "home",
            },
            headers={
                "Accept": "application/json",
                "x-api-key": API_KEY,
                "Realm": REALM,
            }
        )
        print(f"Status: {resp.status_code}")
        if resp.status_code == 200:
            data = resp.json()
            auth = data.get("authentication", {})
            auth_token = auth.get("authorisationToken", "")
            refresh_token = auth.get("refreshToken", "")
            print(f"✅ Got auth token: {auth_token[:50]}...")
            print(f"✅ Got refresh token: {refresh_token[:50]}...")
            return auth_token, refresh_token
        else:
            print(f"❌ Failed: {resp.text[:200]}")
            return None, None

async def test_content_with_token(auth_token):
    """Test content endpoints with the guest token."""
    print("\n=== Testing Content Endpoints ===")
    async with httpx.AsyncClient(timeout=15) as http:
        # Test search
        resp = await http.get(
            f"{API_BASE}/api/v4/vod/search",
            params={"q": "فلسطين", "rpp": "3"},
            headers={
                "Accept": "application/json",
                "x-api-key": API_KEY,
                "Realm": REALM,
                "Authorization": f"Bearer {auth_token}",
            }
        )
        print(f"Search status: {resp.status_code}")
        if resp.status_code == 200:
            data = resp.json()
            items = data.get("vods", data.get("data", []))
            print(f"✅ Search returned {len(items)} results")
        else:
            print(f"❌ Search failed: {resp.text[:200]}")
        
        # Test home content
        resp2 = await http.get(
            f"{API_BASE}/api/v4/content/home",
            params={"bpp": "5", "rpp": "5"},
            headers={
                "Accept": "application/json",
                "x-api-key": API_KEY,
                "Realm": REALM,
                "Authorization": f"Bearer {auth_token}",
            }
        )
        print(f"Home content status: {resp2.status_code}")
        if resp2.status_code == 200:
            data2 = resp2.json()
            buckets = data2.get("buckets", [])
            print(f"✅ Home content returned {len(buckets)} buckets")
        else:
            print(f"❌ Home content failed: {resp2.text[:200]}")

async def test_refresh_token(refresh_token):
    """Test the new /api/v2/token/refresh endpoint."""
    print("\n=== Testing Token Refresh (/api/v2/token/refresh) ===")
    async with httpx.AsyncClient(timeout=15) as http:
        resp = await http.post(
            f"{API_BASE}/api/v2/token/refresh",
            headers={
                "Accept": "application/json",
                "Content-Type": "application/json",
                "x-api-key": API_KEY,
                "Realm": REALM,
                "Authorization": f"Bearer {refresh_token}",
            },
            json={"refreshToken": refresh_token}
        )
        print(f"Refresh status: {resp.status_code}")
        if resp.status_code == 200:
            data = resp.json()
            new_auth = data.get("authorisationToken", "")
            print(f"✅ Got new auth token: {new_auth[:50]}...")
        else:
            print(f"⚠️  Refresh failed: {resp.text[:200]}")
            print("   (This is OK if guest refresh tokens don't support this endpoint)")

async def main():
    auth_token, refresh_token = await test_guest_token()
    if auth_token:
        await test_content_with_token(auth_token)
        await test_refresh_token(refresh_token)
    print("\n=== Done ===")

if __name__ == "__main__":
    asyncio.run(main())
