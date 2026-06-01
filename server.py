"""
Al Jazeera 360 MCP Server
=========================
A Model Context Protocol (MCP) server for Al Jazeera 360 streaming platform.
Provides AI assistants with access to Al Jazeera 360's video content catalog,
including documentaries, talk shows, podcasts, investigative programs, and more.

Platform: https://www.aljazeera360.com
API Backend: Vesper/Dice (dce-frontoffice.imggaming.com)
Search: Vesper Search (search.dce-prod.dicelaboratory.com)

Discovered & Tested Endpoints:
- GET /api/v4/content/home — Homepage content (heroes + buckets)
- GET /api/v4/content/{section} — Section content
- GET /api/v4/vod/{id} — Video details
- GET /api/v4/series/{id} — Series details with seasons list
- GET /api/v4/season/{id} — Season episodes
- GET search.dce-prod.dicelaboratory.com/search — Full-text search
"""

import json
import logging
import os
import time
from typing import Optional
from datetime import datetime, timedelta
from functools import wraps

import httpx
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
from mcp.server.fastmcp import FastMCP

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("aljazeera360-mcp")

# ============================================================================
# Configuration
# ============================================================================

API_BASE = "https://dce-frontoffice.imggaming.com"
SEARCH_API = "https://search.dce-prod.dicelaboratory.com/search"
API_KEY = os.environ.get("AJ360_API_KEY", "REDACTED_API_KEY")
REALM = "dce.aljazeera"
APP_VERSION = "6.60.0.4ccbbae"
PLATFORM_URL = "https://www.aljazeera360.com"

# Available sections/channels
SECTIONS = {
    "AJ360-Originals": "أعمال الجزيرة 360 الأصلية",
    "AJA": "قناة الجزيرة العربية",
    "AJD": "الجزيرة الوثائقية",
    "Atheer": "أثير",
    "AJ-Plus": "AJ+ عربي",
    "Talk Show": "برامج حوارية",
    "Investigative Show": "برامج تحقيقية",
    "Podcast": "بودكاست",
    "Documentaries": "برامج وثائقية",
    "Field Show": "برامج ميدانية",
    "Policy Series": "سلاسل سياسية",
    "Social Series": "سلاسل اجتماعية",
    "Historical Series": "سلاسل تاريخية",
    "Biographical Series": "سلاسل سيرة ذاتية",
    "Culture and Arts Series": "سلاسل ثقافة وفنون",
}

# ============================================================================
# Utilities: TTL Cache & Retry
# ============================================================================

def ttl_cache(ttl_seconds: int = 300):
    """Simple TTL cache decorator for async functions."""
    def decorator(func):
        cache = {}
        
        @wraps(func)
        async def wrapper(*args, **kwargs):
            key = (args, tuple(sorted(kwargs.items())))
            now = time.time()
            if key in cache:
                result, timestamp = cache[key]
                if now - timestamp < ttl_seconds:
                    return result
            result = await func(*args, **kwargs)
            cache[key] = (result, now)
            return result
        
        wrapper.cache_clear = lambda: cache.clear()
        return wrapper
    return decorator


# Retry decorator for API calls (retries on 5xx and timeouts)
api_retry = retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=1, max=10),
    retry=retry_if_exception_type((httpx.HTTPStatusError, httpx.TimeoutException)),
    reraise=True,
)


# ============================================================================
# Token Management
# ============================================================================

class TokenManager:
    """Manages authentication tokens for the Dice/Vesper API.
    
    Authentication flow (in priority order):
    1. Use existing valid token (if not expired)
    2. Refresh using refresh token (POST /api/v4/session/token/refresh)
    3. Create new guest session (POST /api/v4/session)
    4. Fall back to AJ360_AUTH_TOKEN environment variable
    
    Token lifecycle:
    - Auth tokens expire every ~10 minutes
    - Refresh tokens are long-lived (~1 year)
    - Guest sessions are anonymous but fully functional
    """
    
    def __init__(self):
        self._auth_token: Optional[str] = os.environ.get("AJ360_AUTH_TOKEN", "") or None
        self._refresh_token: Optional[str] = os.environ.get("AJ360_REFRESH_TOKEN", "") or None
        self._token_expiry: Optional[datetime] = None
        
        # Try loading persisted refresh token from disk (from previous rotation)
        if not self._refresh_token:
            self._refresh_token = self._load_persisted_refresh_token()
        
        if self._auth_token:
            # Assume env token is fresh for 5 minutes
            self._token_expiry = datetime.now() + timedelta(minutes=5)
    
    async def get_token(self) -> str:
        """Get a valid auth token, refreshing if necessary."""
        if self._auth_token and self._token_expiry and datetime.now() < self._token_expiry:
            return self._auth_token
        
        # Try refresh token first (most reliable)
        if self._refresh_token:
            refreshed = await self._refresh_auth_token()
            if refreshed:
                return self._auth_token or ""
        
        # Fall back to new guest session
        await self._get_guest_token()
        return self._auth_token or ""
    
    async def _refresh_auth_token(self) -> bool:
        """Refresh the auth token using the refresh token."""
        async with httpx.AsyncClient(timeout=15) as http:
            try:
                resp = await http.post(
                    f"{API_BASE}/api/v4/session/token/refresh",
                    headers={
                        "Accept": "application/json",
                        "Content-Type": "application/json",
                        "x-api-key": API_KEY,
                        "Realm": REALM,
                        "app": "dice",
                    },
                    json={"refreshToken": self._refresh_token}
                )
                
                if resp.status_code == 200:
                    data = resp.json()
                    self._auth_token = data.get("authorisationToken", "")
                    new_refresh = data.get("refreshToken")
                    if new_refresh:
                        self._refresh_token = new_refresh
                        self._persist_refresh_token(new_refresh)
                    self._token_expiry = datetime.now() + timedelta(minutes=9)
                    logger.info("Successfully refreshed auth token")
                    return True
                else:
                    logger.warning(f"Token refresh returned {resp.status_code}")
                    return False
            except Exception as e:
                logger.error(f"Failed to refresh token: {e}")
                return False
    
    async def _get_guest_token(self):
        """Get a guest/anonymous token from the platform."""
        async with httpx.AsyncClient(timeout=15) as http:
            try:
                resp = await http.post(
                    f"{API_BASE}/api/v4/session",
                    headers={
                        "Accept": "application/json",
                        "Content-Type": "application/json",
                        "x-api-key": API_KEY,
                        "Realm": REALM,
                        "app": "dice",
                    },
                    json={"device": "BROWSER"}
                )
                
                if resp.status_code == 200:
                    data = resp.json()
                    self._auth_token = data.get("authorisationToken", "")
                    self._refresh_token = data.get("refreshToken", "")
                    self._token_expiry = datetime.now() + timedelta(minutes=9)
                    logger.info("Successfully obtained guest token")
                else:
                    logger.warning(f"Session endpoint returned {resp.status_code}")
            except Exception as e:
                logger.error(f"Failed to get guest token: {e}")
    
    def set_token(self, auth_token: str, refresh_token: str = ""):
        """Manually set tokens (useful for initialization with logged-in user token)."""
        self._auth_token = auth_token
        self._refresh_token = refresh_token
        self._token_expiry = datetime.now() + timedelta(minutes=9)
        if refresh_token:
            self._persist_refresh_token(refresh_token)
    
    @staticmethod
    def _load_persisted_refresh_token() -> Optional[str]:
        """Load a previously persisted refresh token from disk."""
        try:
            token_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".refresh_token")
            if os.path.exists(token_path):
                with open(token_path, "r") as f:
                    token = f.read().strip()
                if token:
                    logger.info("Loaded persisted refresh token from disk")
                    return token
        except OSError:
            pass
        return None
    
    def _persist_refresh_token(self, token: str):
        """Persist rotated refresh token to disk so it survives restarts.
        
        Writes to .refresh_token in the working directory. This file is
        gitignored. If writing fails (e.g., read-only filesystem), the
        server continues with the in-memory token.
        """
        try:
            token_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".refresh_token")
            with open(token_path, "w") as f:
                f.write(token)
            logger.debug("Persisted rotated refresh token to disk")
        except OSError:
            pass  # Read-only filesystem (e.g., Docker), skip silently


# ============================================================================
# API Client
# ============================================================================

class AlJazeera360Client:
    """Client for Al Jazeera 360 Vesper/Dice API.
    
    All endpoints tested and verified against the production API.
    """
    
    def __init__(self):
        self.token_manager = TokenManager()
        # Initialize with env token if available
        env_token = os.environ.get("AJ360_AUTH_TOKEN", "")
        if env_token:
            self.token_manager.set_token(env_token)
    
    def _get_headers(self, token: str) -> dict:
        """Build request headers."""
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json",
            "x-api-key": API_KEY,
            "app": "dice",
            "Accept-Language": "ar-AE",
            "Realm": REALM,
            "x-app-var": APP_VERSION,
        }
        if token:
            headers["Authorization"] = f"Bearer {token}"
        return headers
    
    @api_retry
    @ttl_cache(ttl_seconds=120)
    async def get_home_content(self, items_per_bucket: int = 12) -> dict:
        """Get the home page content with all buckets.
        
        Tested: Returns heroes[], buckets[] with contentList[] containing
        VOD and VOD_SERIES items.
        """
        token = await self.token_manager.get_token()
        async with httpx.AsyncClient(timeout=30) as client:
            resp = await client.get(
                f"{API_BASE}/api/v4/content/home",
                params={
                    "bpp": 10,
                    "rpp": items_per_bucket,
                    "displaySectionLinkBuckets": "SHOW",
                    "displayEpgBuckets": "HIDE",
                    "displayEmptyBucketShortcuts": "SHOW",
                    "displayContentAvailableOnSignIn": "SHOW",
                    "displayGeoblocked": "SHOW",
                    "bspp": 20,
                    "premiereEventContentDisplay": "SHOW",
                },
                headers=self._get_headers(token),
            )
            resp.raise_for_status()
            return resp.json()
    
    @api_retry
    @ttl_cache(ttl_seconds=300)
    async def get_section_content(self, section_id: str, items_per_bucket: int = 12) -> dict:
        """Get content for a specific section/channel.
        
        Tested: Works with all section IDs listed in SECTIONS dict.
        """
        token = await self.token_manager.get_token()
        async with httpx.AsyncClient(timeout=30) as client:
            resp = await client.get(
                f"{API_BASE}/api/v4/content/{section_id}",
                params={
                    "bpp": 10,
                    "rpp": items_per_bucket,
                    "displaySectionLinkBuckets": "SHOW",
                    "displayEpgBuckets": "HIDE",
                    "displayEmptyBucketShortcuts": "SHOW",
                    "displayContentAvailableOnSignIn": "SHOW",
                    "displayGeoblocked": "SHOW",
                    "bspp": 20,
                    "premiereEventContentDisplay": "SHOW",
                },
                headers=self._get_headers(token),
            )
            resp.raise_for_status()
            return resp.json()
    
    @api_retry
    @ttl_cache(ttl_seconds=600)
    async def get_vod_details(self, vod_id: int) -> dict:
        """Get detailed information about a specific video.
        
        Tested: Returns full metadata including title, description, duration,
        thumbnailUrl, coverUrl, maxHeight (quality), categories, publishedDate.
        Example: vod_id=953659 returns "عدنان مندريس" with 4340s duration, 2160p quality.
        """
        token = await self.token_manager.get_token()
        async with httpx.AsyncClient(timeout=30) as client:
            resp = await client.get(
                f"{API_BASE}/api/v4/vod/{vod_id}",
                headers=self._get_headers(token),
            )
            resp.raise_for_status()
            return resp.json()
    
    @api_retry
    @ttl_cache(ttl_seconds=600)
    async def get_series_details(self, series_id: int) -> dict:
        """Get series details including seasons list.
        
        Tested: GET /api/v4/series/{id}
        Returns title, description, seasons[] with (id, seasonNumber, episodeCount).
        Example: series_id=2355 returns "الدحيح" with 4 seasons.
        """
        token = await self.token_manager.get_token()
        async with httpx.AsyncClient(timeout=30) as client:
            resp = await client.get(
                f"{API_BASE}/api/v4/series/{series_id}",
                headers=self._get_headers(token),
            )
            resp.raise_for_status()
            return resp.json()
    
    @api_retry
    @ttl_cache(ttl_seconds=300)
    async def get_season_episodes(self, season_id: int, page_size: int = 20) -> dict:
        """Get episodes for a specific season.
        
        Tested: GET /api/v4/season/{season_id}
        Returns title, episodes[], paging, series info.
        Example: season_id=35416 returns الدحيح Season 5 (2026) episodes.
        """
        token = await self.token_manager.get_token()
        async with httpx.AsyncClient(timeout=30) as client:
            resp = await client.get(
                f"{API_BASE}/api/v4/season/{season_id}",
                params={"pageSize": page_size},
                headers=self._get_headers(token),
            )
            resp.raise_for_status()
            return resp.json()
    
    @api_retry
    async def search_content(self, query: str, page_size: int = 20) -> dict:
        """Search for content across the platform.
        
        Tested: Returns elements[] with cardList containing cards.
        Each card has action.data with (type, title, id, accessLevel).
        """
        token = await self.token_manager.get_token()
        async with httpx.AsyncClient(timeout=30) as client:
            resp = await client.get(
                SEARCH_API,
                params={
                    "term": query,
                    "pageSize": page_size,
                    "timezone": "UTC",
                },
                headers=self._get_headers(token),
            )
            resp.raise_for_status()
            return resp.json()


# ============================================================================
# Helper Functions
# ============================================================================

def format_duration(seconds: Optional[int]) -> str:
    """Convert seconds to HH:MM:SS format."""
    if not seconds:
        return "N/A"
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    if hours > 0:
        return f"{hours:02d}:{minutes:02d}:{secs:02d}"
    return f"{minutes:02d}:{secs:02d}"


def format_vod_item(item: dict) -> dict:
    """Format a VOD item for display."""
    vod_id = item.get("id")
    return {
        "id": vod_id,
        "title": item.get("title", ""),
        "description": item.get("description", ""),
        "duration": format_duration(item.get("duration")),
        "duration_seconds": item.get("duration"),
        "type": "VOD",
        "thumbnail": item.get("thumbnailUrl", item.get("coverUrl", "")),
        "quality": "4K" if item.get("maxHeight", 0) >= 2160 else "HD" if item.get("maxHeight", 0) >= 1080 else "SD",
        "watch_url": f"{PLATFORM_URL}/video/{vod_id}",
        "access_level": item.get("accessLevel", "UNKNOWN"),
    }


def format_series_item(item: dict) -> dict:
    """Format a series item for display."""
    series_id = item.get("id")
    return {
        "id": series_id,
        "title": item.get("title", ""),
        "description": item.get("description", item.get("longDescription", "")),
        "season_count": item.get("seasonCount", 0),
        "type": "SERIES",
        "poster": item.get("posterUrl", item.get("coverUrl", "")),
        "url": f"{PLATFORM_URL}/series/{series_id}",
    }


def format_search_results(data: dict) -> list:
    """Parse search API response and extract content items."""
    results = []
    for element in data.get("elements", []):
        if element.get("$type") == "cardList":
            cards = element.get("attributes", {}).get("cards", [])
            for card in cards:
                attrs = card.get("attributes", {})
                # Extract title from content tokens
                title = ""
                series_title = ""
                content_blocks = attrs.get("content", [])
                for block in content_blocks:
                    if block.get("$type") == "textBlock":
                        tokens = block.get("attributes", {}).get("tokens", [])
                        for token in tokens:
                            if token.get("key") == "title":
                                title = token.get("value", "")
                            elif token.get("key") == "seriesTitle":
                                series_title = token.get("value", "")
                
                # Extract image
                image = ""
                for header_item in attrs.get("header", []):
                    if header_item.get("$type") == "image":
                        image = header_item.get("attributes", {}).get("source", "")
                
                # Extract action/link info
                action = attrs.get("action", {})
                action_data = action.get("data", {})
                raw_id = action_data.get("id", "")
                vod_id = raw_id.replace("VOD#", "").replace("SERIES#", "")
                content_type = action_data.get("type", "VOD")
                
                final_title = title or action_data.get("title", "")
                if final_title:
                    url = f"{PLATFORM_URL}/video/{vod_id}" if content_type == "VOD" else f"{PLATFORM_URL}/series/{vod_id}"
                    results.append({
                        "title": final_title,
                        "series": series_title,
                        "type": content_type,
                        "id": vod_id,
                        "image": image,
                        "watch_url": url,
                        "access_level": action_data.get("accessLevel", "UNKNOWN"),
                    })
    return results


# ============================================================================
# MCP Server
# ============================================================================

mcp = FastMCP("aljazeera360")
client = AlJazeera360Client()


@mcp.tool()
async def get_trending_content() -> str:
    """
    Get the trending and most-watched content on Al Jazeera 360 platform.
    Returns featured shows, most-watched videos, latest episodes, and editorial picks.
    
    الحصول على المحتوى الرائج والأكثر مشاهدة على منصة الجزيرة 360.
    يشمل: البرامج المميزة، الأكثر مشاهدة، أحدث الحلقات، واقتراحات المحررين.
    """
    try:
        data = await client.get_home_content()
        
        result = {
            "platform": "Al Jazeera 360",
            "url": PLATFORM_URL,
            "featured": [],
            "categories": [],
        }
        
        # Process heroes (featured content)
        for hero in data.get("heroes", []):
            result["featured"].append({
                "title": hero.get("title", ""),
                "description": hero.get("description", ""),
                "image": hero.get("imageUrl", ""),
            })
        
        # Process content buckets
        for bucket in data.get("buckets", []):
            bucket_name = bucket.get("name", "")
            bucket_type = bucket.get("type", "")
            
            # Skip resume/recommendations (user-specific)
            if bucket_type in ("VOD_RESUME", "VOD_RECOMMENDATIONS"):
                continue
            
            category = {
                "name": bucket_name,
                "type": bucket_type,
                "items": [],
            }
            
            for item in bucket.get("contentList", []):
                if item.get("type") == "VOD":
                    category["items"].append(format_vod_item(item))
                elif item.get("type") == "VOD_SERIES":
                    category["items"].append(format_series_item(item))
            
            if category["name"] and category["items"]:
                result["categories"].append(category)
        
        return json.dumps(result, ensure_ascii=False, indent=2)
    
    except Exception as e:
        logger.error(f"Error getting trending content: {e}")
        return json.dumps({"error": str(e)}, ensure_ascii=False)


@mcp.tool()
async def browse_section(section_id: str) -> str:
    """
    Browse content in a specific section/channel on Al Jazeera 360.
    
    تصفح محتوى قسم أو قناة محددة على منصة الجزيرة 360.
    
    Available sections (الأقسام المتاحة):
    - AJ360-Originals: أعمال الجزيرة 360 الأصلية
    - AJA: قناة الجزيرة العربية
    - AJD: الجزيرة الوثائقية
    - Atheer: أثير
    - AJ-Plus: AJ+ عربي
    - Talk Show: برامج حوارية
    - Investigative Show: برامج تحقيقية
    - Podcast: بودكاست
    - Documentaries: برامج وثائقية
    - Field Show: برامج ميدانية
    - Policy Series: سلاسل سياسية
    - Social Series: سلاسل اجتماعية
    - Historical Series: سلاسل تاريخية
    - Biographical Series: سلاسل سيرة ذاتية
    - Culture and Arts Series: سلاسل ثقافة وفنون
    
    Args:
        section_id: The section identifier (e.g., "AJA", "Documentaries", "Podcast")
    """
    try:
        data = await client.get_section_content(section_id)
        
        section_name = SECTIONS.get(section_id, section_id)
        result = {
            "section": section_name,
            "section_id": section_id,
            "platform_url": f"{PLATFORM_URL}/section/{section_id}",
            "featured": [],
            "programs": [],
        }
        
        # Process heroes
        for hero in data.get("heroes", []):
            result["featured"].append({
                "title": hero.get("title", ""),
                "description": hero.get("description", ""),
            })
        
        # Process buckets
        for bucket in data.get("buckets", []):
            bucket_info = {
                "category": bucket.get("name", ""),
                "items": [],
            }
            for item in bucket.get("contentList", []):
                if item.get("type") == "VOD":
                    bucket_info["items"].append(format_vod_item(item))
                elif item.get("type") == "VOD_SERIES":
                    bucket_info["items"].append(format_series_item(item))
            
            if bucket_info["items"]:
                result["programs"].append(bucket_info)
        
        return json.dumps(result, ensure_ascii=False, indent=2)
    
    except Exception as e:
        logger.error(f"Error browsing section {section_id}: {e}")
        return json.dumps({"error": str(e)}, ensure_ascii=False)


@mcp.tool()
async def get_video_details(video_id: int) -> str:
    """
    Get detailed information about a specific video on Al Jazeera 360.
    Returns title, description, duration, quality, categories, episode info, and watch URL.
    
    الحصول على معلومات تفصيلية عن فيديو محدد على منصة الجزيرة 360.
    يشمل: العنوان، الوصف، المدة، الجودة، التصنيفات، ورابط المشاهدة.
    
    Args:
        video_id: The numeric ID of the video (e.g., 953659)
    """
    try:
        data = await client.get_vod_details(video_id)
        
        # Determine quality
        max_height = data.get("maxHeight", 0)
        if max_height >= 2160:
            quality = "4K Ultra HD"
        elif max_height >= 1080:
            quality = "Full HD (1080p)"
        elif max_height >= 720:
            quality = "HD (720p)"
        else:
            quality = "SD"
        
        result = {
            "id": data.get("id"),
            "title": data.get("title", ""),
            "description": data.get("description", ""),
            "duration": format_duration(data.get("duration")),
            "duration_seconds": data.get("duration"),
            "quality": quality,
            "max_resolution": f"{max_height}p" if max_height else "N/A",
            "thumbnail": data.get("thumbnailUrl", ""),
            "cover_image": data.get("coverUrl", ""),
            "release_year": data.get("releaseYear"),
            "published_date": data.get("publishedDate", ""),
            "categories": [c for c in data.get("categories", []) if c],
            "tags": [tag.get("title", "") for tag in data.get("displayableTags", []) if tag.get("title")],
            "access_level": data.get("accessLevel", "UNKNOWN"),
            "watch_url": f"{PLATFORM_URL}/video/{data.get('id')}",
            "episode_info": data.get("episodeInformation"),
        }
        
        return json.dumps(result, ensure_ascii=False, indent=2)
    
    except Exception as e:
        logger.error(f"Error getting video details for {video_id}: {e}")
        return json.dumps({"error": str(e)}, ensure_ascii=False)


@mcp.tool()
async def get_series_details(series_id: int) -> str:
    """
    Get detailed information about a series on Al Jazeera 360, including all seasons.
    
    الحصول على معلومات تفصيلية عن مسلسل/برنامج على منصة الجزيرة 360 مع قائمة المواسم.
    
    Args:
        series_id: The numeric ID of the series (e.g., 2355 for الدحيح)
    """
    try:
        data = await client.get_series_details(series_id)
        
        seasons = []
        for season in data.get("seasons", []):
            seasons.append({
                "season_id": season.get("id"),
                "season_number": season.get("seasonNumber"),
                "title": season.get("title", ""),
                "episode_count": season.get("episodeCount", 0),
                "description": season.get("description", ""),
            })
        
        result = {
            "id": data.get("id"),
            "title": data.get("title", ""),
            "description": data.get("description", ""),
            "long_description": data.get("longDescription", ""),
            "poster": data.get("posterUrl", ""),
            "cover": data.get("coverUrl", ""),
            "total_seasons": len(seasons),
            "seasons": seasons,
            "tags": [tag.get("title", "") for tag in data.get("displayableTags", []) if tag.get("title")],
            "url": f"{PLATFORM_URL}/series/{series_id}",
        }
        
        return json.dumps(result, ensure_ascii=False, indent=2)
    
    except Exception as e:
        logger.error(f"Error getting series details for {series_id}: {e}")
        return json.dumps({"error": str(e)}, ensure_ascii=False)


@mcp.tool()
async def get_season_episodes(season_id: int, max_episodes: int = 20) -> str:
    """
    Get all episodes in a specific season. Use get_series_details first to find season IDs.
    
    الحصول على جميع حلقات موسم محدد. استخدم get_series_details أولاً للحصول على أرقام المواسم.
    
    Args:
        season_id: The season ID (obtained from get_series_details)
        max_episodes: Maximum number of episodes to return (default: 20)
    """
    try:
        data = await client.get_season_episodes(season_id, page_size=max_episodes)
        
        episodes = []
        for ep in data.get("episodes", []):
            episodes.append({
                "id": ep.get("id"),
                "title": ep.get("title", ""),
                "description": ep.get("description", ""),
                "duration": format_duration(ep.get("duration")),
                "duration_seconds": ep.get("duration"),
                "episode_number": ep.get("episodeInformation", {}).get("episodeNumber") if ep.get("episodeInformation") else None,
                "thumbnail": ep.get("thumbnailUrl", ""),
                "watch_url": f"{PLATFORM_URL}/video/{ep.get('id')}",
                "access_level": ep.get("accessLevel", "UNKNOWN"),
            })
        
        # Series info
        series_info = data.get("series", {})
        
        result = {
            "season_title": data.get("title", ""),
            "season_number": data.get("seasonNumber"),
            "season_id": season_id,
            "series_title": series_info.get("title", ""),
            "series_id": series_info.get("id"),
            "total_episodes": data.get("episodeCount", len(episodes)),
            "episodes": episodes,
        }
        
        return json.dumps(result, ensure_ascii=False, indent=2)
    
    except Exception as e:
        logger.error(f"Error getting season episodes for {season_id}: {e}")
        return json.dumps({"error": str(e)}, ensure_ascii=False)


@mcp.tool()
async def search_videos(query: str, content_type: Optional[str] = None, max_results: int = 20) -> str:
    """
    Search for videos, documentaries, and programs on Al Jazeera 360.
    Supports Arabic and English search queries.
    Optionally filter by content type.
    
    البحث عن فيديوهات ووثائقيات وبرامج على منصة الجزيرة 360.
    يدعم البحث بالعربية والإنجليزية. يمكن تصفية النتائج حسب نوع المحتوى.
    
    Examples:
    - "فلسطين" — videos about Palestine
    - "غزة" — videos about Gaza
    - "الدحيح" — Al Daheeh science show
    - "وثائقي تاريخي" — historical documentaries
    
    Args:
        query: Search term in Arabic or English
        content_type: Optional filter — "VOD" for single videos, "SERIES" for series only, None for all
        max_results: Maximum number of results to return (default: 20)
    """
    try:
        data = await client.search_content(query, page_size=max_results)
        results = format_search_results(data)
        
        # Apply content_type filter if specified
        if content_type:
            content_type_upper = content_type.upper()
            results = [r for r in results if r.get("type", "").upper() == content_type_upper]
        
        output = {
            "query": query,
            "content_type_filter": content_type,
            "total_results": len(results),
            "platform": "Al Jazeera 360",
            "results": results,
        }
        
        return json.dumps(output, ensure_ascii=False, indent=2)
    
    except Exception as e:
        logger.error(f"Error searching for '{query}': {e}")
        return json.dumps({"error": str(e)}, ensure_ascii=False)


@mcp.tool()
async def list_sections() -> str:
    """
    List all available sections and channels on Al Jazeera 360.
    Returns section IDs with their Arabic names for use with browse_section.
    
    عرض جميع الأقسام والقنوات المتاحة على منصة الجزيرة 360.
    يرجع معرفات الأقسام مع أسمائها العربية لاستخدامها مع browse_section.
    """
    result = {
        "platform": "Al Jazeera 360",
        "url": PLATFORM_URL,
        "sections": [
            {"id": k, "name_ar": v, "browse_url": f"{PLATFORM_URL}/section/{k}"}
            for k, v in SECTIONS.items()
        ],
        "total_sections": len(SECTIONS),
        "usage_note": "Use the 'id' field with browse_section() to explore content in each section.",
    }
    
    return json.dumps(result, ensure_ascii=False, indent=2)


@mcp.tool()
async def get_latest_episodes(section_id: str = "AJA", count: int = 10) -> str:
    """
    Get the latest episodes from a specific section on Al Jazeera 360.
    
    الحصول على أحدث الحلقات من قسم محدد على منصة الجزيرة 360.
    
    Args:
        section_id: Section to get latest from (default: "AJA" for Al Jazeera Arabic)
        count: Number of episodes to return (default: 10)
    """
    try:
        data = await client.get_section_content(section_id, items_per_bucket=count)
        
        latest = []
        for bucket in data.get("buckets", []):
            bucket_name = bucket.get("name", "")
            bucket_type = bucket.get("type", "")
            # Look for latest episodes or VOD playlists
            if "أحدث" in bucket_name or bucket_type == "VOD_PLAYLIST":
                for item in bucket.get("contentList", []):
                    if item.get("type") == "VOD":
                        latest.append(format_vod_item(item))
        
        # If no specific "latest" bucket found, get all VODs
        if not latest:
            for bucket in data.get("buckets", []):
                for item in bucket.get("contentList", []):
                    if item.get("type") == "VOD":
                        latest.append(format_vod_item(item))
        
        result = {
            "section": SECTIONS.get(section_id, section_id),
            "section_id": section_id,
            "latest_episodes": latest[:count],
            "total_found": min(len(latest), count),
        }
        
        return json.dumps(result, ensure_ascii=False, indent=2)
    
    except Exception as e:
        logger.error(f"Error getting latest episodes: {e}")
        return json.dumps({"error": str(e)}, ensure_ascii=False)


# ============================================================================
# MCP Resources
# ============================================================================

@mcp.resource("aljazeera360://sections")
async def sections_resource() -> str:
    """List of all available sections on Al Jazeera 360."""
    return json.dumps(SECTIONS, ensure_ascii=False, indent=2)


@mcp.resource("aljazeera360://about")
async def about_resource() -> str:
    """Information about Al Jazeera 360 platform."""
    return json.dumps({
        "name": "Al Jazeera 360",
        "name_ar": "الجزيرة 360",
        "tagline": "مشاهدة بلا قيود",
        "url": PLATFORM_URL,
        "description": "منصة البث المرئي الرقمية التابعة لشبكة الجزيرة الإعلامية. تقدم محتوى متنوعاً يشمل الوثائقيات والبرامج الحوارية والتحقيقية والبودكاست والبرامج الميدانية.",
        "content_types": [
            "وثائقيات", "برامج حوارية", "برامج تحقيقية",
            "بودكاست", "برامج ميدانية", "سلاسل تاريخية",
            "سلاسل سياسية", "سلاسل اجتماعية", "أعمال أصلية"
        ],
        "channels": ["الجزيرة العربية", "الجزيرة الوثائقية", "أثير", "AJ+ عربي"],
        "api_backend": "Vesper/Dice (IMG Arena)",
        "api_version": APP_VERSION,
    }, ensure_ascii=False, indent=2)


# ============================================================================
# MCP Prompts (Pre-built scenarios for AI assistants)
# ============================================================================

@mcp.prompt()
def recommend_documentary(topic: str) -> str:
    """Recommend a documentary about a specific topic from Al Jazeera 360."""
    return f"""Search Al Jazeera 360 for documentaries about \"{topic}\".
Use search_videos with the topic, then filter for documentary content.
For each result, get full details using get_video_details.
Present the top 3 recommendations with:
- Title and description
- Duration
- Direct watch link on aljazeera360.com
Prioritize content that is most relevant and recently published."""


@mcp.prompt()
def summarize_latest(section: str = "AJA") -> str:
    """Summarize the latest episodes from a section on Al Jazeera 360."""
    return f"""Get the latest episodes from the \"{section}\" section on Al Jazeera 360.
Use get_latest_episodes to fetch recent content.
For each episode, provide:
- Title
- Brief description
- Duration
- Watch link
Group them by topic if possible and highlight the most notable ones."""


@mcp.prompt()
def explore_series(series_name: str) -> str:
    """Explore a series on Al Jazeera 360 — find seasons and episodes."""
    return f"""Find the series \"{series_name}\" on Al Jazeera 360.
1. Use search_videos to find the series
2. Use get_series_details to get all seasons
3. Use get_season_episodes on the latest season
Present a complete overview: series description, number of seasons,
and list the latest season's episodes with watch links."""


# ============================================================================
# Entry Point
# ============================================================================

def main():
    """Run the MCP server.
    
    Transport is determined by MCP_TRANSPORT env var:
    - "stdio" (default): For local MCP clients (Claude Desktop, Cursor, etc.)
    - "sse": For cloud deployment (Cloud Run, Render, Railway, etc.)
    """
    transport = os.environ.get("MCP_TRANSPORT", "stdio")
    
    if transport == "sse":
        port = int(os.environ.get("MCP_PORT", "8080"))
        logger.info(f"Starting Al Jazeera 360 MCP Server (SSE transport on port {port})")
        mcp.run(transport="sse", host="0.0.0.0", port=port)
    else:
        logger.info("Starting Al Jazeera 360 MCP Server (stdio transport)")
        mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
