"""Try to get stream URL using the DICE CDN and intercept approach."""
import asyncio
import httpx
import os
import json

API_BASE = "https://dce-frontoffice.imggaming.com"
API_KEY = os.environ.get("AJ360_API_KEY", "")  # Set AJ360_API_KEY env var
REALM = "dce.aljazeera"
CDN_BASE = "https://dve-videos.imggaming.com"

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
        # Get full VOD details
        r = await c.get(f"{API_BASE}/api/v4/vod/{video_id}", headers=auth_headers)
        vod = r.json()
        ext_id = vod.get("externalAssetId", "")
        print(f"externalAssetId: {ext_id}")
        
        # The DICE platform uses a "playerUrlCallback" pattern
        # Try the standard DICE stream endpoint
        stream_endpoints = [
            f"{API_BASE}/api/v4/vod/{video_id}/stream",
            f"{API_BASE}/api/v4/vod/{video_id}/streamingUrl",
            f"{CDN_BASE}/vod/{video_id}/hls/index.m3u8",
            f"{CDN_BASE}/vod/{ext_id}/hls/index.m3u8",
        ]
        
        for url in stream_endpoints:
            try:
                r2 = await c.get(url, headers=auth_headers)
                print(f"  {url.split('/')[-2:]}: HTTP {r2.status_code}")
                if r2.status_code == 200:
                    print(f"  Content: {r2.text[:200]}")
            except Exception as e:
                print(f"  Error: {e}")
        
        # Try the DICE "playerUrl" endpoint which is the standard way
        # POST to get a signed playback URL
        print("\n--- Trying POST to get signed URL ---")
        for ep in [
            f"/api/v4/vod/{video_id}/playerUrl",
            f"/api/v4/vod/{video_id}/streamUrl",
        ]:
            r3 = await c.post(
                f"{API_BASE}{ep}",
                headers=auth_headers,
                json={"device": "BROWSER", "platform": "WEB"}
            )
            print(f"POST {ep}: HTTP {r3.status_code}")
            if r3.status_code == 200:
                print(f"  Response: {r3.text[:300]}")
            elif r3.status_code not in [404, 405]:
                print(f"  Response: {r3.text[:150]}")
        
        # Check if there's a "plugins" field with stream info
        plugins = vod.get("plugins", {})
        if plugins:
            print(f"\nPlugins: {json.dumps(plugins, ensure_ascii=False, indent=2)[:400]}")
        
        # Check subEvents
        sub_events = vod.get("subEvents", [])
        if sub_events:
            print(f"\nsubEvents: {json.dumps(sub_events[:2], ensure_ascii=False, indent=2)[:400]}")

asyncio.run(test())
