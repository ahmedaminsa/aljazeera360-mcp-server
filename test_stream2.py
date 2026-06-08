"""Find the correct playback URL endpoint for transcription."""
import asyncio
import httpx
import os
import json

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
    
    async with httpx.AsyncClient(timeout=20, follow_redirects=True) as c:
        # Get full VOD details to find stream info
        r = await c.get(f"{API_BASE}/api/v4/vod/{video_id}", headers=auth_headers)
        vod = r.json()
        
        print(f"Video: {vod.get('title')}")
        print(f"Access: {vod.get('accessLevel')}")
        print(f"Duration: {vod.get('duration')}s ({vod.get('duration', 0)//60} min)")
        print(f"\nAll VOD keys: {list(vod.keys())}")
        
        # Look for any URL-like fields
        for key, val in vod.items():
            if isinstance(val, str) and ('http' in val or 'url' in str(val).lower()):
                print(f"  URL field [{key}]: {str(val)[:100]}")
        
        # Check streamingInfo deeply
        si = vod.get("streamingInfo", {})
        if si:
            print(f"\nStreamingInfo: {json.dumps(si, ensure_ascii=False, indent=2)[:500]}")
        
        # Try different API versions and paths
        endpoints_to_try = [
            f"/api/v4/vod/{video_id}/url",
            f"/api/v4/vod/{video_id}/token",
            f"/api/v3/vod/{video_id}/playbackUrl",
            f"/api/v2/vod/{video_id}/playbackUrl",
            f"/api/v4/vod/{video_id}/playerUrl",
            f"/api/v4/vod/{video_id}/hls",
        ]
        
        print("\n--- Testing endpoints ---")
        for ep in endpoints_to_try:
            r2 = await c.get(f"{API_BASE}{ep}", headers=auth_headers)
            if r2.status_code == 200:
                print(f"✅ {ep}: {r2.text[:200]}")
            elif r2.status_code != 404:
                print(f"⚠️  {ep}: HTTP {r2.status_code} — {r2.text[:100]}")

asyncio.run(test())
