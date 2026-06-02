"""Extract stream URL from onlinePlayback and computedReleases fields."""
import asyncio
import httpx
import os
import json

API_BASE = "https://dce-frontoffice.imggaming.com"
API_KEY = os.environ.get("AJ360_API_KEY", "REDACTED_API_KEY")
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
        r = await c.get(f"{API_BASE}/api/v4/vod/{video_id}", headers=auth_headers)
        vod = r.json()
        
        print(f"Video: {vod.get('title')}")
        
        # Check onlinePlayback
        op = vod.get("onlinePlayback")
        print(f"\nonlinePlayback: {json.dumps(op, ensure_ascii=False, indent=2)[:600] if op else 'None'}")
        
        # Check onlinePlaybackMetadata
        opm = vod.get("onlinePlaybackMetadata")
        print(f"\nonlinePlaybackMetadata: {json.dumps(opm, ensure_ascii=False, indent=2)[:400] if opm else 'None'}")
        
        # Check computedReleases
        cr = vod.get("computedReleases")
        print(f"\ncomputedReleases: {json.dumps(cr, ensure_ascii=False, indent=2)[:600] if cr else 'None'}")
        
        # Check playbackType
        print(f"\nplaybackType: {vod.get('playbackType')}")
        
        # Try to get the playerUrlCallback
        if op and isinstance(op, dict):
            callback = op.get("playerUrlCallback") or op.get("url") or op.get("hls")
            if callback:
                print(f"\n✅ Found stream URL: {callback[:150]}")
                # Try to fetch it
                r2 = await c.get(callback, headers=auth_headers)
                print(f"Stream URL response: HTTP {r2.status_code}")
                if r2.status_code == 200:
                    print(f"Content: {r2.text[:300]}")

asyncio.run(test())
