"""Try to get subtitle/caption files for transcription."""
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
    }
    async with httpx.AsyncClient(timeout=15) as c:
        r = await c.get(f"{API_BASE}/api/v1/init/", headers=headers)
        data = r.json()
        auth = data.get("authentication", {})
        return auth.get("authorisationToken", ""), headers

async def test():
    token, base_headers = await get_token()
    auth_headers = {
        **base_headers,
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
        "Content-Type": "application/json",
        "x-app-var": "6.60.0.4ccbbae",
        "Accept-Language": "ar-AE",
    }
    
    video_id = 953659
    
    async with httpx.AsyncClient(timeout=20, follow_redirects=True) as c:
        # Get full VOD details
        r = await c.get(f"{API_BASE}/api/v4/vod/{video_id}", headers=auth_headers)
        vod = r.json()
        
        print(f"Video: {vod.get('title')}")
        
        # Check onlinePlaybackMetadata for subtitle info
        opm = vod.get("onlinePlaybackMetadata", {})
        subtitles = opm.get("subtitles", [])
        audio_tracks = opm.get("audioTracks", [])
        print(f"\nSubtitles: {json.dumps(subtitles, ensure_ascii=False)}")
        print(f"Audio tracks: {json.dumps(audio_tracks, ensure_ascii=False)}")
        
        # Try subtitle endpoints
        subtitle_endpoints = [
            f"/api/v4/vod/{video_id}/subtitles",
            f"/api/v4/vod/{video_id}/captions",
            f"/api/v4/vod/{video_id}/tracks",
            f"/api/v4/vod/{video_id}/textTracks",
        ]
        
        print("\n--- Testing subtitle endpoints ---")
        for ep in subtitle_endpoints:
            r2 = await c.get(f"{API_BASE}{ep}", headers=auth_headers)
            print(f"{ep}: HTTP {r2.status_code}")
            if r2.status_code == 200:
                print(f"  Response: {r2.text[:300]}")
            elif r2.status_code not in [404]:
                print(f"  Response: {r2.text[:100]}")
        
        # Check the externalAssetId - might be a Brightcove ID
        ext_id = vod.get("externalAssetId", "")
        print(f"\nexternalAssetId: {ext_id}")
        
        # Try the DICE CDN for subtitle files
        cdn_subtitle_urls = [
            f"https://dve-videos.imggaming.com/vod/{video_id}/subtitles/ar.vtt",
            f"https://dve-videos.imggaming.com/vod/{video_id}/captions/ar.srt",
            f"https://dve-videos.imggaming.com/subtitles/{video_id}/ar.vtt",
        ]
        
        print("\n--- Testing CDN subtitle URLs ---")
        for url in cdn_subtitle_urls:
            r3 = await c.get(url)
            print(f"{url.split('/')[-3:]}: HTTP {r3.status_code}")
            if r3.status_code == 200:
                print(f"  Content: {r3.text[:200]}")
        
        # Check plugins field for any subtitle/caption plugin
        plugins = vod.get("plugins", {})
        if plugins:
            print(f"\nPlugins: {json.dumps(plugins, ensure_ascii=False, indent=2)[:600]}")

asyncio.run(test())
