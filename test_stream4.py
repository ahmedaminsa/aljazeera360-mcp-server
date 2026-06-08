"""Try yt-dlp to extract stream URL, and also try the DICE player API."""
import asyncio
import httpx
import os
import json
import subprocess

API_BASE = "https://dce-frontoffice.imggaming.com"
API_KEY = os.environ.get("AJ360_API_KEY", "")  # Set AJ360_API_KEY env var
REALM = "dce.aljazeera"

async def get_token():
    headers = {
        "x-api-key": API_KEY,
        "Realm": REALM,
        "app": "dice",
        "Content-Type": "application/json",
    }
    async with httpx.AsyncClient(timeout=15) as c:
        r = await c.get(f"{API_BASE}/api/v1/init", headers=headers)
        data = r.json()
        auth = data.get("authentication", {})
        return auth.get("authorisationToken", ""), headers

async def test():
    token, base_headers = await get_token()
    auth_headers = {**base_headers, "Authorization": f"Bearer {token}"}
    
    video_id = 953659
    video_url = f"https://www.aljazeera360.com/video/{video_id}"
    
    async with httpx.AsyncClient(timeout=20, follow_redirects=True) as c:
        # Try the DICE player token endpoint (used by the web player)
        endpoints = [
            f"/api/v4/vod/{video_id}/playerToken",
            f"/api/v4/vod/{video_id}/streamToken",
            f"/api/v4/vod/{video_id}/accessToken",
            f"/api/v4/vod/{video_id}/play",
        ]
        for ep in endpoints:
            r = await c.post(f"{API_BASE}{ep}", headers=auth_headers, json={})
            if r.status_code == 200:
                print(f"✅ POST {ep}: {r.text[:300]}")
            elif r.status_code not in [404, 405]:
                print(f"⚠️  POST {ep}: HTTP {r.status_code} — {r.text[:100]}")
        
        # Try GET with different content types
        for ep in [f"/api/v4/vod/{video_id}/playerToken"]:
            r = await c.get(f"{API_BASE}{ep}", headers=auth_headers)
            if r.status_code == 200:
                print(f"✅ GET {ep}: {r.text[:300]}")
        
        # Try the DICE CDN directly - look for the externalAssetId
        r2 = await c.get(f"{API_BASE}/api/v4/vod/{video_id}", headers=auth_headers)
        vod = r2.json()
        ext_id = vod.get("externalAssetId", "")
        print(f"\nexternalAssetId: {ext_id}")
        
        # Try brightcove-style URL if externalAssetId looks like a Brightcove ID
        if ext_id:
            print(f"Trying Brightcove: https://edge.api.brightcove.com/playback/v1/accounts/...")
    
    # Try yt-dlp
    print("\n--- Trying yt-dlp ---")
    result = subprocess.run(
        ["yt-dlp", "--list-formats", "--no-download", video_url],
        capture_output=True, text=True, timeout=30
    )
    if result.returncode == 0:
        print("✅ yt-dlp works!")
        print(result.stdout[:500])
    else:
        print(f"yt-dlp failed: {result.stderr[:300]}")

asyncio.run(test())
