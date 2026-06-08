"""Test video stream access for transcription feasibility."""
import asyncio
import httpx
import os
import json

API_BASE = "https://dce-frontoffice.imggaming.com"
API_KEY = os.environ.get("AJ360_API_KEY", "")  # Set AJ360_API_KEY env var
REALM = "dce.aljazeera"

async def test():
    headers = {
        "x-api-key": API_KEY,
        "Realm": REALM,
        "app": "dice",
        "Content-Type": "application/json",
    }
    async with httpx.AsyncClient(timeout=20) as c:
        # Get guest token
        r = await c.get(f"{API_BASE}/api/v1/init", headers=headers)
        data = r.json()
        # The init endpoint returns token in different fields
        token = (data.get("authorisationToken") or 
                 data.get("token") or 
                 data.get("accessToken") or "")
        # Also check nested
        if not token and "authentication" in data:
            auth = data["authentication"]
            token = auth.get("authorisationToken") or auth.get("token", "")
        print(f"Token obtained: {bool(token)} ({len(token)} chars)")
        print(f"Init keys: {list(data.keys())}")
        if 'authentication' in data:
            print(f"Auth keys: {list(data['authentication'].keys())}")
            print(f"Auth sample: {json.dumps(data['authentication'], ensure_ascii=False)[:300]}")
        
        if not token:
            print("ERROR: No token!")
            print(json.dumps(data, ensure_ascii=False, indent=2)[:500])
            return
        
        auth_headers = {**headers, "Authorization": f"Bearer {token}"}
        
        # Get video details
        r2 = await c.get(f"{API_BASE}/api/v4/vod/953659", headers=auth_headers)
        vod = r2.json()
        print(f"\nVideo: {vod.get('title', 'N/A')}")
        print(f"Access level: {vod.get('accessLevel', 'N/A')}")
        print(f"Duration: {vod.get('duration', 'N/A')} seconds")
        
        # Check streaming info
        streaming = vod.get("streamingInfo", {})
        if streaming:
            print(f"Streaming keys: {list(streaming.keys())}")
        
        # Try playback URL endpoint
        for endpoint in [
            f"/api/v4/vod/953659/playbackUrl",
            f"/api/v4/vod/953659/stream",
            f"/api/v4/vod/953659/media",
        ]:
            r3 = await c.get(f"{API_BASE}{endpoint}", headers=auth_headers)
            print(f"\n{endpoint}: HTTP {r3.status_code}")
            if r3.status_code == 200:
                pb = r3.json()
                print(f"  Keys: {list(pb.keys())}")
                # Look for HLS/MP4 URL
                for key in ["hls", "url", "playerUrlCallback", "streamUrl", "mp4"]:
                    if key in pb:
                        print(f"  {key}: {str(pb[key])[:100]}")
                break
            elif r3.status_code != 404:
                print(f"  Response: {r3.text[:200]}")

asyncio.run(test())
