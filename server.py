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
from mcp.server.transport_security import TransportSecuritySettings
from mcp.types import ToolAnnotations

# Analytics & Request Tracking
from analytics import tracker, track_request, start_dashboard, ENABLE_DASHBOARD, DASHBOARD_PORT, DASHBOARD_HTML

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("aljazeera360-mcp")

# ============================================================================
# Configuration
# ============================================================================

API_BASE = "https://dce-frontoffice.imggaming.com"
SEARCH_API = "https://search.dce-prod.dicelaboratory.com/search"
# API key is required — set AJ360_API_KEY environment variable.
# This is the platform API key visible in browser network requests to dce-frontoffice.imggaming.com.
# No default is provided here for security reasons.
API_KEY = os.environ.get("AJ360_API_KEY", "")
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
    2. Refresh using refresh token (POST /api/v2/token/refresh)
    3. Create new guest session via GET /api/v1/init (returns auth + refresh tokens)
    4. Fall back to AJ360_AUTH_TOKEN environment variable
    
    Token lifecycle:
    - Auth tokens expire every ~10 minutes
    - Refresh tokens are long-lived (~1 year)
    - Guest sessions are anonymous but fully functional
    
    Note: The old /api/v4/session and /api/v4/session/token/refresh endpoints
    are no longer available (404). The new endpoints are /api/v1/init and
    /api/v2/token/refresh.
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
        """Refresh the auth token using the refresh token.
        
        Uses /api/v2/token/refresh (new endpoint, replaces deprecated /api/v4/session/token/refresh).
        Requires the refresh token in both Authorization header and request body.
        """
        async with httpx.AsyncClient(timeout=15) as http:
            try:
                resp = await http.post(
                    f"{API_BASE}/api/v2/token/refresh",
                    headers={
                        "Accept": "application/json",
                        "Content-Type": "application/json",
                        "x-api-key": API_KEY,
                        "Realm": REALM,
                        "Authorization": f"Bearer {self._refresh_token}",
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
                    logger.info("Successfully refreshed auth token via /api/v2/token/refresh")
                    return True
                else:
                    logger.warning(f"Token refresh returned {resp.status_code}: {resp.text[:100]}")
                    return False
            except Exception as e:
                logger.error(f"Failed to refresh token: {e}")
                return False
    
    async def _get_guest_token(self):
        """Get a guest/anonymous token from the platform.
        
        Uses GET /api/v1/init (new endpoint, replaces deprecated POST /api/v4/session).
        Returns authentication.authorisationToken and authentication.refreshToken.
        """
        async with httpx.AsyncClient(timeout=15) as http:
            try:
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
                
                if resp.status_code == 200:
                    data = resp.json()
                    auth = data.get("authentication", {})
                    self._auth_token = auth.get("authorisationToken", "")
                    new_refresh = auth.get("refreshToken", "")
                    if new_refresh:
                        self._refresh_token = new_refresh
                        self._persist_refresh_token(new_refresh)
                    self._token_expiry = datetime.now() + timedelta(minutes=9)
                    logger.info("Successfully obtained guest token via /api/v1/init")
                else:
                    logger.warning(f"Init endpoint returned {resp.status_code}: {resp.text[:100]}")
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
        
        Note: The Vesper search API supports sort values: title, relevance, publicationDate.
        We use sort=relevance and fetch more results (3x) then apply client-side
        relevance filtering to ensure query terms appear in titles/descriptions.
        """
        token = await self.token_manager.get_token()
        # Fetch 3x results to allow client-side relevance filtering
        fetch_size = min(page_size * 3, 60)
        async with httpx.AsyncClient(timeout=30) as client:
            resp = await client.get(
                SEARCH_API,
                params={
                    "term": query,
                    "pageSize": fetch_size,
                    "timezone": "UTC",
                    "sort": "relevance",
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


def _score_result_relevance(result: dict, query: str) -> int:
    """Score a search result by relevance to the query.
    
    Higher score = more relevant. Used to re-rank results after fetching.
    Scoring:
    - Title contains exact query: +10
    - Title contains any query word: +5 per word
    - Series title contains query: +3
    - Content type is VOD or SERIES (not channel): +1
    """
    score = 0
    query_lower = query.strip().lower()
    query_words = [w for w in query_lower.split() if len(w) > 1]
    
    title = result.get("title", "").lower()
    series = result.get("series", "").lower()
    content_type = result.get("type", "")
    
    # Exact query match in title (highest priority)
    if query_lower in title:
        score += 10
    
    # Individual word matches in title
    for word in query_words:
        if word in title:
            score += 5
    
    # Series title match
    if query_lower in series:
        score += 3
    for word in query_words:
        if word in series:
            score += 2
    
    # Prefer actual content over channels/categories
    if content_type in ("VOD", "SERIES"):
        score += 1
    
    return score


def format_search_results(data: dict, query: str = "", max_results: int = 20) -> list:
    """Parse search API response and extract content items.
    
    Applies client-side relevance re-ranking:
    1. Extracts all results from the API response
    2. Scores each result by how well it matches the query
    3. Returns results sorted by relevance score (highest first)
    4. Falls back to original API order if no query provided
    """
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
    
    # Apply client-side relevance re-ranking if query provided
    if query and results:
        # Score all results
        scored = [(r, _score_result_relevance(r, query)) for r in results]
        # Sort by score descending, preserving API order for ties
        scored.sort(key=lambda x: x[1], reverse=True)
        # Return top max_results, prioritizing those with score > 0
        ranked = [r for r, s in scored]
        return ranked[:max_results]
    
    return results[:max_results]


# ============================================================================
# MCP Server
# ============================================================================

# Determine transport mode early to configure security settings
_transport_mode = os.environ.get("MCP_TRANSPORT", "streamable-http")

# Configure Transport Security for Cloud Deployment
if _transport_mode in ("streamable-http", "sse"):
    # Configure DNS Rebinding Protection, Allowed Hosts, and Allowed Origins
    # Re-enabling protection and defining strict allowed hosts/origins for security compliance
    _allowed_hosts = [
        "localhost",
        "127.0.0.1",
        "aljazeera360-mcp-server-production.up.railway.app", # Railway production domain
        "aljazeera360-mcp.up.railway.app",
    ]
    # Add any custom host from environment if deployed elsewhere
    _custom_host = os.environ.get("AJ360_ALLOWED_HOST")
    if _custom_host:
        _allowed_hosts.append(_custom_host)
        
    _security = TransportSecuritySettings(
        enable_dns_rebinding_protection=True,
        allowed_hosts=_allowed_hosts,
        allowed_origins=[
            "http://localhost",
            "http://127.0.0.1",
            "https://aljazeera360.com",
            "https://www.aljazeera360.com",
        ]
    )
    mcp = FastMCP(
        "aljazeera360",
        host="0.0.0.0",
        port=int(os.environ.get("MCP_PORT", "8080")),
        transport_security=_security,
    )
else:
    mcp = FastMCP("aljazeera360")
client = AlJazeera360Client()

# ----------------------------------------------------------------------------
# Tool Profiles
# ----------------------------------------------------------------------------
# The 8 core discovery tools are always registered. The 16 SEO/analytics tools
# target content teams rather than end users, and a small default toolset keeps
# AI tool selection accurate — so they are opt-in via AJ360_ENABLE_SEO_TOOLS.
SEO_TOOLS_ENABLED = os.environ.get("AJ360_ENABLE_SEO_TOOLS", "").strip().lower() in ("1", "true", "yes")


def seo_tool(*args, **kwargs):
    """Like @mcp.tool(), but only registers the tool when AJ360_ENABLE_SEO_TOOLS is set.

    The decorated function is always returned unchanged, so direct imports
    (e.g. from tests or examples) work in both profiles.
    """
    if SEO_TOOLS_ENABLED:
        return mcp.tool(*args, **kwargs)

    def _unregistered(fn):
        return fn

    return _unregistered


@mcp.tool(annotations=ToolAnnotations(title="Get Trending Content (المحتوى الرائج)", readOnlyHint=True))
@track_request("get_trending_content")
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


@mcp.tool(annotations=ToolAnnotations(title="Browse Section (تصفح الأقسام)", readOnlyHint=True))
@track_request("browse_section")
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


@mcp.tool(annotations=ToolAnnotations(title="Get Video Details (تفاصيل الفيديو)", readOnlyHint=True))
@track_request("get_video_details")
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


@mcp.tool(annotations=ToolAnnotations(title="Get Series Details (تفاصيل البرامج والسلاسل)", readOnlyHint=True))
@track_request("get_series_details")
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


@mcp.tool(annotations=ToolAnnotations(title="Get Season Episodes (حلقات الموسم)", readOnlyHint=True))
@track_request("get_season_episodes")
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


@mcp.tool(annotations=ToolAnnotations(title="Search Videos (البحث عن الفيديوهات)", readOnlyHint=True))
@track_request("search_videos")
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
        # Pass query for client-side relevance re-ranking
        results = format_search_results(data, query=query, max_results=max_results)
        
        # Apply content_type filter if specified
        if content_type:
            content_type_upper = content_type.upper()
            results = [r for r in results if r.get("type", "").upper() == content_type_upper]
        
        # Count how many results are actually relevant (score > 0)
        query_lower = query.strip().lower()
        query_words = [w for w in query_lower.split() if len(w) > 1]
        relevant_count = sum(
            1 for r in results
            if any(kw in r.get("title", "").lower() for kw in [query_lower] + query_words)
        )
        
        # If Vesper search returned few relevant results, supplement with browse-based search
        # The Vesper API returns trending content regardless of query, so we browse sections
        # and filter by keyword to find actual matching content
        browse_results = []
        if relevant_count < 3 and len(query_words) > 0:
            logger.info(f"Low relevance from Vesper search ({relevant_count} relevant). Trying browse fallback.")
            # Browse key sections and filter by query
            browse_sections = ["AJA", "AJD", "AJ360-Originals", "Documentaries"]
            seen_ids = {r.get("id") for r in results}
            
            for section_id in browse_sections:
                try:
                    section_data = await client.get_section_content(section_id, items_per_bucket=20)
                    for bucket in section_data.get("buckets", []):
                        for item in bucket.get("contentList", []):
                            item_title = item.get("title", "").lower()
                            item_id = str(item.get("id", ""))
                            # Check if any query word appears in the title
                            if item_id not in seen_ids and any(kw in item_title for kw in query_words):
                                seen_ids.add(item_id)
                                item_type = item.get("type", "VOD")
                                url = (
                                    f"{PLATFORM_URL}/video/{item_id}"
                                    if item_type == "VOD"
                                    else f"{PLATFORM_URL}/series/{item_id}"
                                )
                                browse_results.append({
                                    "title": item.get("title", ""),
                                    "series": "",
                                    "type": item_type,
                                    "id": item_id,
                                    "image": item.get("thumbnailUrl", item.get("coverUrl", "")),
                                    "watch_url": url,
                                    "access_level": item.get("accessLevel", "UNKNOWN"),
                                    "source": "browse",
                                })
                except Exception as browse_err:
                    logger.warning(f"Browse fallback failed for {section_id}: {browse_err}")
                    continue
            
            if browse_results:
                logger.info(f"Browse fallback found {len(browse_results)} relevant results")
                # If we have enough keyword-matched results (≥5), use them exclusively
                # to avoid mixing unrelated trending content into the results
                if len(browse_results) >= 5:
                    results = browse_results[:max_results]
                else:
                    # Not enough browse results — supplement with Vesper trending
                    merged = browse_results[:max_results]
                    remaining_slots = max_results - len(merged)
                    browse_ids = {r.get("id") for r in merged}
                    for r in results:
                        if r.get("id") not in browse_ids and remaining_slots > 0:
                            merged.append(r)
                            remaining_slots -= 1
                    results = merged
        
        output = {
            "query": query,
            "content_type_filter": content_type,
            "total_results": len(results),
            "platform": "Al Jazeera 360",
            "search_note": "Results include both keyword-matched and trending content" if browse_results else "Results from platform search",
            "results": results,
        }
        
        return json.dumps(output, ensure_ascii=False, indent=2)
    
    except Exception as e:
        logger.error(f"Error searching for '{query}': {e}")
        return json.dumps({"error": str(e)}, ensure_ascii=False)


@mcp.tool(annotations=ToolAnnotations(title="List Sections (قائمة الأقسام المتاحة)", readOnlyHint=True))
@track_request("list_sections")
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


@mcp.tool(annotations=ToolAnnotations(title="Get Latest Episodes (أحدث الحلقات)", readOnlyHint=True))
@track_request("get_latest_episodes")
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


@seo_tool(annotations=ToolAnnotations(title="Generate SEO Content (توليد محتوى SEO)", readOnlyHint=True))
@track_request("generate_seo_content")
async def generate_seo_content(video_id: int) -> str:
    """
    Generate complete SEO content for a video on Al Jazeera 360 — 100% free, no AI API needed.
    
    توليد محتوى SEO كامل ومجاني لأي فيديو على منصة الجزيرة 360.
    يعمل بالكامل من بيانات الـ API العامة بدون أي تكلفة.
    
    Generates:
    - Optimized meta title (trimmed to 60 chars)
    - Meta description (trimmed to 160 chars with CTA)
    - Focus keyword extracted from title
    - 7-10 keywords from title + categories + series
    - VideoObject JSON-LD schema markup (ready to embed in HTML)
    - Extended page description
    - Suggested tags
    - SEO audit notes (what's good, what needs improvement)
    
    Args:
        video_id: The video ID (e.g., 953659)
    """
    try:
        # Get video details from the API
        vod = await client.get_vod_details(video_id)
        
        title = vod.get("title", "")
        description = vod.get("description", "")
        long_description = vod.get("longDescription", description)
        duration_sec = vod.get("duration", 0)
        published_date = vod.get("publishedDate", "")
        thumbnail_url = vod.get("thumbnailUrl", vod.get("coverUrl", ""))
        categories = vod.get("categories", [])
        max_height = vod.get("maxHeight", 0)
        episode_info = vod.get("episodeInformation", {}) or {}
        display_tags = vod.get("displayableTags", []) or []
        release_year = vod.get("releaseYear", "")
        
        # ----------------------------------------------------------------
        # 1. ISO 8601 duration for schema
        # ----------------------------------------------------------------
        hours = duration_sec // 3600
        mins = (duration_sec % 3600) // 60
        secs = duration_sec % 60
        iso_duration = f"PT{hours}H{mins}M{secs}S" if hours > 0 else f"PT{mins}M{secs}S"
        duration_label = f"{hours}ساعة {mins}دقيقة" if hours > 0 else f"{mins} دقيقة"
        
        # ----------------------------------------------------------------
        # 2. Category names (handle both string and dict formats)
        # ----------------------------------------------------------------
        cat_names = []
        for c in categories:
            if isinstance(c, dict):
                name = c.get("name", c.get("title", ""))
                if name:
                    cat_names.append(name)
            elif isinstance(c, str) and c:
                cat_names.append(c)
        
        # ----------------------------------------------------------------
        # 3. Episode / series context
        # ----------------------------------------------------------------
        series_title = episode_info.get("seriesTitle", "")
        season_num = episode_info.get("seasonNumber", "")
        ep_num = episode_info.get("episodeNumber", "")
        
        episode_label = ""
        if series_title:
            episode_label = series_title
            if season_num:
                episode_label += f" – الموسم {season_num}"
            if ep_num:
                episode_label += f" – الحلقة {ep_num}"
        
        # ----------------------------------------------------------------
        # 4. Quality label
        # ----------------------------------------------------------------
        quality = "4K Ultra HD" if max_height >= 2160 else "Full HD" if max_height >= 1080 else "HD"
        
        # ----------------------------------------------------------------
        # 5. Build META TITLE (max 60 chars)
        # Rule: "{title} | الجزيرة 360"
        # If too long, trim title to fit
        # ----------------------------------------------------------------
        suffix = " | الجزيرة 360"
        max_title_len = 60
        if len(title) + len(suffix) <= max_title_len:
            meta_title = title + suffix
        else:
            trimmed = title[:max_title_len - len(suffix) - 1].rstrip()
            # Try to cut at last space
            last_space = trimmed.rfind(" ")
            if last_space > 20:
                trimmed = trimmed[:last_space]
            meta_title = trimmed + "…" + suffix
        
        # ----------------------------------------------------------------
        # 6. Build META DESCRIPTION (max 160 chars)
        # Rule: first sentence of description + quality + CTA
        # ----------------------------------------------------------------
        cta = " – شاهد الآن بجودة " + quality + " على الجزيرة 360."
        desc_clean = description.strip().replace("\n", " ")
        # Take first sentence
        for sep in [". ", ".،", "\u060c"]:
            if sep in desc_clean:
                first_sentence = desc_clean.split(sep)[0] + "."
                break
        else:
            first_sentence = desc_clean
        
        max_desc = 160
        if len(first_sentence) + len(cta) <= max_desc:
            meta_description = first_sentence + cta
        else:
            available = max_desc - len(cta) - 1
            meta_description = first_sentence[:available].rstrip() + "…" + cta
        
        # ----------------------------------------------------------------
        # 7. Keywords extraction (rule-based, no AI)
        # Sources: title words + categories + series title + year
        # ----------------------------------------------------------------
        keywords = []
        
        # Primary: full title as main keyword
        if title:
            keywords.append(title)
        
        # Series title if exists
        if series_title and series_title not in keywords:
            keywords.append(series_title)
        
        # Categories
        for cat in cat_names:
            if cat not in keywords:
                keywords.append(cat)
        
        # Displayable tags
        for tag in display_tags[:5]:
            tag_title = tag.get("title", "") if isinstance(tag, dict) else str(tag)
            if tag_title and tag_title not in keywords:
                keywords.append(tag_title)
        
        # Platform keyword
        keywords.append("الجزيرة 360")
        
        # Year if available
        if release_year:
            keywords.append(str(release_year))
        
        # Deduplicate and limit to 10
        seen = set()
        unique_keywords = []
        for kw in keywords:
            if kw not in seen:
                seen.add(kw)
                unique_keywords.append(kw)
        keywords = unique_keywords[:10]
        
        # Focus keyword = title (most specific)
        focus_keyword = title
        
        # ----------------------------------------------------------------
        # 8. Extended description for the page
        # ----------------------------------------------------------------
        parts = []
        if long_description and long_description != description:
            parts.append(long_description.strip())
        elif description:
            parts.append(description.strip())
        
        if episode_label:
            parts.append(f"هذا المحتوى جزء من {episode_label}.")
        
        if cat_names:
            parts.append(f"التصنيف: {' – '.join(cat_names)}.")
        
        parts.append(f"المدة: {duration_label}. الجودة: {quality}.")
        parts.append(f"شاهد هذا المحتوى وغيره الكثير على منصة الجزيرة 360 – مشاهدة بلا قيود.")
        extended_description = " ".join(parts)
        
        # ----------------------------------------------------------------
        # 9. Suggested tags
        # ----------------------------------------------------------------
        suggested_tags = list(dict.fromkeys(
            [title] + cat_names + ([series_title] if series_title else []) + ["الجزيرة 360", "وثائقي", "برامج عربية"]
        ))[:8]
        
        # ----------------------------------------------------------------
        # 10. SEO audit notes
        # ----------------------------------------------------------------
        audit_notes = []
        if len(description) < 100:
            audit_notes.append("⚠️ الوصف قصير (أقل من 100 حرف) — ينصح بتوسيعه")
        else:
            audit_notes.append("✅ الوصف كافي")
        
        if not cat_names:
            audit_notes.append("⚠️ لا تصنيفات — أضف تصنيفات لتحسين الكلمات المفتاحية")
        else:
            audit_notes.append(f"✅ يحتوي على {len(cat_names)} تصنيفات")
        
        if thumbnail_url:
            audit_notes.append("✅ صورة مصغرة متاحة للـ schema")
        else:
            audit_notes.append("⚠️ لا صورة مصغرة — مطلوبة لـ VideoObject schema")
        
        if published_date:
            audit_notes.append("✅ تاريخ نشر متاح للـ schema")
        
        if max_height >= 2160:
            audit_notes.append("✅ جودة 4K — ميزة تنافسية قوية")
        
        audit_notes.append("⚠️ الصفحة SPA (JavaScript) — الـ schema يجب حقنه في الـ HTML المرسل من السيرفر")
        
        # ----------------------------------------------------------------
        # 11. VideoObject JSON-LD schema (ready to embed)
        # ----------------------------------------------------------------
        schema_markup = {
            "@context": "https://schema.org",
            "@type": "VideoObject",
            "name": meta_title.replace(suffix, "").strip(" …"),
            "description": meta_description,
            "thumbnailUrl": thumbnail_url,
            "uploadDate": published_date[:10] if published_date else "",
            "duration": iso_duration,
            "contentUrl": f"{PLATFORM_URL}/video/{video_id}",
            "embedUrl": f"{PLATFORM_URL}/video/{video_id}",
            "keywords": ", ".join(keywords),
            "inLanguage": "ar",
            "publisher": {
                "@type": "Organization",
                "name": "الجزيرة 360",
                "url": PLATFORM_URL,
                "logo": {
                    "@type": "ImageObject",
                    "url": "https://www.aljazeera360.com/favicon.ico"
                }
            },
        }
        if cat_names:
            schema_markup["genre"] = cat_names[0]
        if series_title:
            schema_markup["partOfSeries"] = {
                "@type": "TVSeries",
                "name": series_title
            }
        
        schema_html = f'<script type="application/ld+json">\n{json.dumps(schema_markup, ensure_ascii=False, indent=2)}\n</script>'
        
        # ----------------------------------------------------------------
        # 12. Final result
        # ----------------------------------------------------------------
        result = {
            "video_id": video_id,
            "original_title": title,
            "watch_url": f"{PLATFORM_URL}/video/{video_id}",
            "thumbnail": thumbnail_url,
            "duration_iso": iso_duration,
            "quality": quality,
            "generation_method": "rule-based (free, no AI API)",
            "seo": {
                "meta_title": meta_title,
                "meta_title_length": len(meta_title),
                "meta_description": meta_description,
                "meta_description_length": len(meta_description),
                "focus_keyword": focus_keyword,
                "keywords": keywords,
                "extended_description": extended_description,
                "suggested_tags": suggested_tags,
                "audit_notes": audit_notes,
            },
            "schema_markup": schema_markup,
            "schema_markup_html": schema_html,
        }
        
        logger.info(f"Generated SEO content (rule-based) for video {video_id}: {title}")
        return json.dumps(result, ensure_ascii=False, indent=2)
    
    except Exception as e:
        logger.error(f"Error generating SEO content for video {video_id}: {e}")
        return json.dumps({"error": str(e), "video_id": video_id}, ensure_ascii=False)


# ============================================================================
# SEO & Analytics Tools
# ============================================================================

@seo_tool(annotations=ToolAnnotations(title="Generate Video Sitemap (توليد خريطة الفيديو)", readOnlyHint=True))
@track_request("generate_sitemap")
async def generate_sitemap(sections: str = "all", max_per_section: int = 100, page: int = 1, page_size: int = 100) -> str:
    """
    Generate a complete Video Sitemap XML for Al Jazeera 360 — ready to submit to Google Search Console.

    توليد Video Sitemap XML كامل لمنصة الجزيرة 360 جاهز للرفع على Google Search Console.
    يحتوي على عناوين وأوصاف وصور مصغرة وتواريخ نشر لكل فيديو.

    Args:
        sections: Comma-separated section IDs to include, or "all" for all sections (default: "all")
        max_per_section: Maximum videos per section to include (default: 100)
        page: Page number for pagination (default: 1)
        page_size: Number of items per page (default: 100)
    """
    try:
        from xml.etree.ElementTree import Element, SubElement, tostring
        from xml.dom import minidom
        import datetime

        # Determine which sections to process
        if sections == "all":
            section_ids = list(SECTIONS.keys())
        else:
            section_ids = [s.strip() for s in sections.split(",") if s.strip() in SECTIONS]

        if not section_ids:
            return json.dumps({"error": "No valid section IDs provided"}, ensure_ascii=False)

        # Build XML structure
        urlset = Element("urlset")
        urlset.set("xmlns", "http://www.sitemaps.org/schemas/sitemap/0.9")
        urlset.set("xmlns:video", "http://www.google.com/schemas/sitemap-video/1.1")

        total_urls = 0
        section_counts = {}
        errors = []

        for section_id in section_ids:
            try:
                data = await client.get_section_content(section_id, items_per_bucket=max_per_section)
                items = []
                if isinstance(data, dict):
                    for bucket in data.get("buckets", []):
                        if isinstance(bucket, dict):
                            items.extend(bucket.get("contentList", []))

                # Apply pagination to items list
                start_idx = (page - 1) * page_size
                end_idx = start_idx + page_size
                paginated_items = items[start_idx:end_idx]

                count = 0
                for item in paginated_items:
                    if not isinstance(item, dict):
                        continue
                    video_id = item.get("id") or item.get("vodId")
                    title = item.get("title", "")
                    description = item.get("description", "") or ""
                    thumbnail = item.get("thumbnailUrl") or item.get("coverUrl", "")
                    published = item.get("publishedDate", "") or ""
                    duration_sec = item.get("duration", 0) or 0

                    if not video_id or not title:
                        continue

                    page_url = f"{PLATFORM_URL}/video/{video_id}"

                    url_el = SubElement(urlset, "url")
                    loc = SubElement(url_el, "loc")
                    loc.text = page_url

                    if published:
                        lastmod = SubElement(url_el, "lastmod")
                        lastmod.text = published[:10]

                    video_el = SubElement(url_el, "video:video")

                    thumb_el = SubElement(video_el, "video:thumbnail_loc")
                    thumb_el.text = thumbnail or f"https://cdn.aljazeera360.com/thumbnails/{video_id}.jpg"

                    title_el = SubElement(video_el, "video:title")
                    title_el.text = title[:100]

                    if description:
                        desc_el = SubElement(video_el, "video:description")
                        desc_el.text = description[:2048]

                    content_url_el = SubElement(video_el, "video:content_loc")
                    content_url_el.text = page_url

                    player_el = SubElement(video_el, "video:player_loc")
                    player_el.text = page_url

                    if duration_sec > 0:
                        dur_el = SubElement(video_el, "video:duration")
                        dur_el.text = str(duration_sec)

                    if published:
                        pub_el = SubElement(video_el, "video:publication_date")
                        pub_el.text = published[:19] + "+00:00" if len(published) >= 19 else published[:10] + "T00:00:00+00:00"

                    lang_el = SubElement(video_el, "video:tag")
                    lang_el.text = "الجزيرة 360"

                    total_urls += 1
                    count += 1

                section_counts[section_id] = count

            except Exception as e:
                errors.append(f"{section_id}: {str(e)}")
                section_counts[section_id] = 0

        # Pretty-print XML
        xml_str = minidom.parseString(tostring(urlset, encoding="unicode")).toprettyxml(indent="  ")
        # Remove the extra XML declaration added by toprettyxml
        xml_lines = xml_str.split("\n")
        if xml_lines[0].startswith("<?xml"):
            xml_lines[0] = '<?xml version="1.0" encoding="UTF-8"?>'
        xml_output = "\n".join(xml_lines)

        result = {
            "total_urls": total_urls,
            "sections_processed": len(section_ids),
            "section_counts": section_counts,
            "errors": errors,
            "generated_at": datetime.datetime.utcnow().isoformat() + "Z",
            "instructions": [
                "1. احفظ الـ XML في ملف video-sitemap.xml",
                "2. ارفعه على الموقع: https://www.aljazeera360.com/video-sitemap.xml",
                "3. أضفه في robots.txt: Sitemap: https://www.aljazeera360.com/video-sitemap.xml",
                "4. ارفعه في Google Search Console تحت Sitemaps",
            ],
            "sitemap_xml": xml_output,
        }

        logger.info(f"Generated video sitemap with {total_urls} URLs across {len(section_ids)} sections")
        return json.dumps(result, ensure_ascii=False, indent=2)

    except Exception as e:
        logger.error(f"Error generating sitemap: {e}")
        return json.dumps({"error": str(e)}, ensure_ascii=False)


@seo_tool(annotations=ToolAnnotations(title="Audit Metadata Quality (تدقيق جودة البيانات)", readOnlyHint=True))
@track_request("audit_metadata_quality")
async def audit_metadata_quality(section_id: str = "AJA", max_items: int = 50, page: int = 1, page_size: int = 20) -> str:
    """
    Audit the metadata quality of videos in a section and return a detailed report.

    تدقيق جودة الـ metadata للفيديوهات في قسم معين وإرجاع تقرير تفصيلي.
    يكشف الفيديوهات ذات الوصف القصير أو المفقود أو بدون تصنيفات أو بدون صورة مصغرة.

    Args:
        section_id: Section to audit (e.g., "AJA", "AJD", "AJ360-Originals"). Default: "AJA"
        max_items: Maximum number of videos to audit (default: 50)
        page: Page number for pagination (default: 1)
        page_size: Number of audited items to return in this page (default: 20)
    """
    try:
        data = await client.get_section_content(section_id, items_per_bucket=max_items)

        items = []
        if isinstance(data, dict):
            for bucket in data.get("buckets", []):
                if isinstance(bucket, dict):
                    items.extend(bucket.get("contentList", []))

        issues = {
            "missing_description": [],
            "short_description": [],
            "missing_thumbnail": [],
            "missing_categories": [],
            "short_title": [],
            "missing_published_date": [],
            "low_quality": [],
        }
        good_items = []
        total = 0

        # Apply pagination to audited items
        start_idx = (page - 1) * page_size
        end_idx = start_idx + page_size
        paginated_items = items[start_idx:end_idx]
        
        for item in paginated_items:
            if not isinstance(item, dict):
                continue
            video_id = item.get("id") or item.get("vodId")
            title = item.get("title", "") or ""
            description = item.get("description", "") or ""
            thumbnail = item.get("thumbnailUrl") or item.get("coverUrl", "")
            categories = item.get("categories", []) or []
            published = item.get("publishedDate", "") or ""
            max_height = item.get("maxHeight", 0) or 0

            if not video_id or not title:
                continue

            total += 1
            item_issues = []
            entry = {"id": video_id, "title": title[:60], "url": f"{PLATFORM_URL}/video/{video_id}"}

            if not description:
                issues["missing_description"].append(entry)
                item_issues.append("وصف مفقود")
            elif len(description) < 80:
                issues["short_description"].append({**entry, "desc_length": len(description)})
                item_issues.append(f"وصف قصير ({len(description)} حرف)")

            if not thumbnail:
                issues["missing_thumbnail"].append(entry)
                item_issues.append("صورة مصغرة مفقودة")

            if not categories:
                issues["missing_categories"].append(entry)
                item_issues.append("بدون تصنيفات")

            if len(title) < 10:
                issues["short_title"].append({**entry, "title_length": len(title)})
                item_issues.append(f"عنوان قصير ({len(title)} حرف)")

            if not published:
                issues["missing_published_date"].append(entry)
                item_issues.append("تاريخ نشر مفقود")

            if max_height < 720:
                issues["low_quality"].append({**entry, "max_height": max_height})
                item_issues.append(f"جودة منخفضة ({max_height}p)")

            if not item_issues:
                good_items.append(entry)

        # Calculate scores
        def pct(n): return round(n / total * 100, 1) if total > 0 else 0

        total_issues = sum(len(v) for v in issues.values())
        health_score = round((good_items.__len__() / total * 100), 1) if total > 0 else 0

        result = {
            "section": section_id,
            "section_name": SECTIONS.get(section_id, {}).get("name", section_id) if isinstance(SECTIONS.get(section_id), dict) else str(SECTIONS.get(section_id, section_id)),
            "page": page,
            "page_size": page_size,
            "total_audited": total,
            "health_score": f"{health_score}%",
            "items_with_no_issues": len(good_items),
            "summary": {
                "missing_description": {"count": len(issues["missing_description"]), "pct": f"{pct(len(issues['missing_description']))}%"},
                "short_description": {"count": len(issues["short_description"]), "pct": f"{pct(len(issues['short_description']))}%"},
                "missing_thumbnail": {"count": len(issues["missing_thumbnail"]), "pct": f"{pct(len(issues['missing_thumbnail']))}%"},
                "missing_categories": {"count": len(issues["missing_categories"]), "pct": f"{pct(len(issues['missing_categories']))}%"},
                "short_title": {"count": len(issues["short_title"]), "pct": f"{pct(len(issues['short_title']))}%"},
                "missing_published_date": {"count": len(issues["missing_published_date"]), "pct": f"{pct(len(issues['missing_published_date']))}%"},
                "low_quality_video": {"count": len(issues["low_quality"]), "pct": f"{pct(len(issues['low_quality']))}%"},
            },
            "top_issues": issues,
            "recommendations": [
                f"أضف وصفاً لـ {len(issues['missing_description'])} فيديو بدون وصف" if issues["missing_description"] else None,
                f"طوّل وصف {len(issues['short_description'])} فيديو (أقل من 80 حرف)" if issues["short_description"] else None,
                f"أضف تصنيفات لـ {len(issues['missing_categories'])} فيديو بدون تصنيف" if issues["missing_categories"] else None,
                f"أضف صور مصغرة لـ {len(issues['missing_thumbnail'])} فيديو" if issues["missing_thumbnail"] else None,
            ],
        }
        result["recommendations"] = [r for r in result["recommendations"] if r]

        logger.info(f"Audited {total} items in section {section_id}: health score {health_score}%")
        return json.dumps(result, ensure_ascii=False, indent=2)

    except Exception as e:
        logger.error(f"Error auditing metadata quality: {e}")
        return json.dumps({"error": str(e)}, ensure_ascii=False)


@seo_tool(annotations=ToolAnnotations(title="Get Trending Topics (المواضيع الرائجة للـ SEO)", readOnlyHint=True))
@track_request("get_trending_topics")
async def get_trending_topics(top_n: int = 20) -> str:
    """
    Analyze trending content and extract the most common topics, keywords, and themes.

    تحليل المحتوى الرائج واستخراج أكثر المواضيع والكلمات المفتاحية انتشاراً.
    مفيد لاستراتيجية المحتوى وتحديد الكلمات المفتاحية المستهدفة.

    Args:
        top_n: Number of top topics to return (default: 20)
    """
    try:
        import re
        from collections import Counter

        # Get trending from multiple sections
        all_items = []
        for section_id in ["AJA", "AJD", "AJ360-Originals", "Most-Watched"]:
            try:
                data = await client.get_section_content(section_id, items_per_bucket=30)
                if isinstance(data, dict):
                    for bucket in data.get("buckets", []):
                        if isinstance(bucket, dict):
                            all_items.extend(bucket.get("contentList", []))
            except Exception:
                continue

        # Extract words from titles
        stop_words = {"في", "من", "إلى", "على", "هل", "ما", "كيف", "لم", "لا", "وال", "وفي",
                        "عن", "بين", "أن", "ال", "وا", "به", "له", "مع", "أو", "ثم", "قد",
                        "the", "of", "in", "a", "an", "and", "to", "for", "is", "are"}

        word_counter = Counter()
        category_counter = Counter()
        quality_counter = Counter()
        recent_titles = []
        total_items = 0

        for item in all_items:
            if not isinstance(item, dict):
                continue
            title = item.get("title", "") or ""
            categories = item.get("categories", []) or []
            max_height = item.get("maxHeight", 0) or 0
            published = item.get("publishedDate", "") or ""

            if not title:
                continue

            total_items += 1

            # Count words in title
            words = re.findall(r'[\u0600-\u06ff]{3,}|[a-zA-Z]{4,}', title)
            for word in words:
                if word not in stop_words and len(word) > 2:
                    word_counter[word] += 1

            # Count categories
            for cat in categories:
                cat_name = cat.get("name", "") if isinstance(cat, dict) else str(cat)
                if cat_name:
                    category_counter[cat_name] += 1

            # Quality distribution
            if max_height >= 2160:
                quality_counter["4K"] += 1
            elif max_height >= 1080:
                quality_counter["Full HD"] += 1
            elif max_height >= 720:
                quality_counter["HD"] += 1
            else:
                quality_counter["SD"] += 1

            # Recent content (last 7 days)
            if published:
                try:
                    import datetime
                    pub_date = datetime.datetime.fromisoformat(published.replace("Z", "+00:00"))
                    days_ago = (datetime.datetime.now(datetime.timezone.utc) - pub_date).days
                    if days_ago <= 7:
                        recent_titles.append({"title": title, "published": published[:10], "days_ago": days_ago})
                except Exception:
                    pass

        result = {
            "total_items_analyzed": total_items,
            "top_keywords": [{"keyword": w, "count": c} for w, c in word_counter.most_common(top_n)],
            "top_categories": [{"category": cat, "count": c} for cat, c in category_counter.most_common(10)],
            "quality_distribution": dict(quality_counter),
            "recent_content_last_7_days": sorted(recent_titles, key=lambda x: x["days_ago"])[:10],
            "content_strategy_insights": [
                f"الكلمة الأكثر ظهوراً: '{word_counter.most_common(1)[0][0]}' ({word_counter.most_common(1)[0][1]} مرة)" if word_counter else "لا توجد بيانات كافية",
                f"أكثر تصنيف ظهوراً: '{category_counter.most_common(1)[0][0]}' ({category_counter.most_common(1)[0][1]} فيديو)" if category_counter else None,
                f"نسبة المحتوى بجودة 4K: {round(quality_counter.get('4K', 0) / total_items * 100, 1)}%" if total_items > 0 else None,
                f"عدد المحتوىات المنشورة خلال آخر 7 أيام: {len(recent_titles)}",
            ],
        }
        result["content_strategy_insights"] = [i for i in result["content_strategy_insights"] if i]

        logger.info(f"Analyzed {total_items} items for trending topics")
        return json.dumps(result, ensure_ascii=False, indent=2)

    except Exception as e:
        logger.error(f"Error getting trending topics: {e}")
        return json.dumps({"error": str(e)}, ensure_ascii=False)


@seo_tool(annotations=ToolAnnotations(title="Compare Sections Activity (مقارنة نشاط الأقسام)", readOnlyHint=True))
@track_request("compare_sections")
async def compare_sections() -> str:
    """
    Compare all sections by content count, quality distribution, and freshness.

    مقارنة جميع الأقسام من حيث عدد المحتوى وجودة الفيديوهات وحداثة المحتوى.
    يساعد في تحديد الأقسام المهملة والأقسام ذات الأداء القوي.
    """
    try:
        import datetime
        results = []

        for section_id, section_info in SECTIONS.items():
            section_name = section_info.get("name", section_id) if isinstance(section_info, dict) else str(section_info)
            try:
                data = await client.get_section_content(section_id, items_per_bucket=20)
                items = []
                if isinstance(data, dict):
                    for bucket in data.get("buckets", []):
                        if isinstance(bucket, dict):
                            items.extend(bucket.get("contentList", []))

                total = len([i for i in items if isinstance(i, dict) and (i.get("id") or i.get("vodId"))])
                heights = [i.get("maxHeight", 0) or 0 for i in items if isinstance(i, dict)]
                has_4k = sum(1 for h in heights if h >= 2160)
                has_fhd = sum(1 for h in heights if 1080 <= h < 2160)
                has_hd = sum(1 for h in heights if 720 <= h < 1080)

                # Find most recent item
                dates = []
                for i in items:
                    if isinstance(i, dict) and i.get("publishedDate"):
                        try:
                            d = datetime.datetime.fromisoformat(i["publishedDate"].replace("Z", "+00:00"))
                            dates.append(d)
                        except Exception:
                            pass

                latest_date = max(dates).strftime("%Y-%m-%d") if dates else "unknown"
                days_since_update = (datetime.datetime.now(datetime.timezone.utc) - max(dates)).days if dates else 999

                results.append({
                    "section_id": section_id,
                    "section_name": section_name,
                    "items_loaded": total,
                    "quality": {
                        "4K": has_4k,
                        "Full_HD": has_fhd,
                        "HD": has_hd,
                        "pct_4K": f"{round(has_4k/total*100, 1)}%" if total > 0 else "0%"
                    },
                    "latest_content": latest_date,
                    "days_since_update": days_since_update,
                    "freshness": "🟢 حديث" if days_since_update <= 7 else "🟡 متوسط" if days_since_update <= 30 else "🔴 قديم",
                })

            except Exception as e:
                results.append({
                    "section_id": section_id,
                    "section_name": section_name,
                    "error": str(e),
                    "items_loaded": 0,
                })

        # Sort by freshness
        results.sort(key=lambda x: x.get("days_since_update", 999))

        # Summary
        active = [r for r in results if r.get("days_since_update", 999) <= 7]
        stale = [r for r in results if r.get("days_since_update", 999) > 30]

        summary = {
            "total_sections": len(results),
            "active_sections_last_7_days": len(active),
            "stale_sections_over_30_days": len(stale),
            "most_active": results[0]["section_name"] if results else "N/A",
            "least_active": results[-1]["section_name"] if results else "N/A",
        }

        logger.info(f"Compared {len(results)} sections")
        return json.dumps({"summary": summary, "sections": results}, ensure_ascii=False, indent=2)

    except Exception as e:
        logger.error(f"Error comparing sections: {e}")
        return json.dumps({"error": str(e)}, ensure_ascii=False)


@seo_tool(annotations=ToolAnnotations(title="Get Series SEO Map (خريطة SEO للبرامج والسلاسل)", readOnlyHint=True))
@track_request("get_series_seo_map")
async def get_series_seo_map(series_id: int) -> str:
    """
    Build a complete SEO map for a series: all seasons, episodes, internal links, and schema.

    بناء خريطة SEO كاملة لسلسلة: جميع المواسم والحلقات مع روابط داخلية مقترحة.
    مفيد لتحسين الـ internal linking واكتشاف السلسلة في نتائج البحث.

    Args:
        series_id: The series ID (get from get_series_details or search_videos)
    """
    try:
        # Get series details
        series_data = await client.get_vod_details(series_id)

        series_title = series_data.get("title", f"Series {series_id}")
        series_description = series_data.get("description", "")
        series_thumbnail = series_data.get("thumbnailUrl") or series_data.get("coverUrl", "")
        seasons = series_data.get("seasons", []) or []

        episodes_map = []
        total_episodes = 0

        for season in seasons[:5]:  # Limit to 5 seasons
            if not isinstance(season, dict):
                continue
            season_id = season.get("id")
            season_num = season.get("seasonNumber", season.get("number", ""))
            season_title = season.get("title", f"الموسم {season_num}")

            if not season_id:
                continue

            try:
                season_episodes = await client.get_season_episodes_data(season_id, max_episodes=20)
                for ep in season_episodes:
                    if not isinstance(ep, dict):
                        continue
                    ep_id = ep.get("id") or ep.get("vodId")
                    ep_title = ep.get("title", "")
                    ep_num = ep.get("episodeNumber", "")
                    ep_desc = ep.get("description", "")
                    ep_published = ep.get("publishedDate", "")
                    ep_duration = ep.get("duration", 0) or 0
                    ep_thumb = ep.get("thumbnailUrl") or ep.get("coverUrl", "")

                    if not ep_id or not ep_title:
                        continue

                    total_episodes += 1
                    episodes_map.append({
                        "season": season_num,
                        "season_title": season_title,
                        "episode": ep_num,
                        "id": ep_id,
                        "title": ep_title,
                        "url": f"{PLATFORM_URL}/video/{ep_id}",
                        "description_length": len(ep_desc),
                        "published": ep_published[:10] if ep_published else "",
                        "duration_min": ep_duration // 60,
                        "has_thumbnail": bool(ep_thumb),
                        "suggested_meta_title": f"{ep_title} | {series_title} | الجزيرة 360"[:60],
                        "internal_link_text": f"شاهد الحلقة {ep_num} من {series_title}",
                    })
            except Exception:
                continue

        # Build TVSeries schema
        tv_series_schema = {
            "@context": "https://schema.org",
            "@type": "TVSeries",
            "name": series_title,
            "description": series_description,
            "url": f"{PLATFORM_URL}/series/{series_id}",
            "thumbnailUrl": series_thumbnail,
            "inLanguage": "ar",
            "numberOfEpisodes": total_episodes,
            "numberOfSeasons": len(seasons),
            "publisher": {
                "@type": "Organization",
                "name": "الجزيرة 360",
                "url": PLATFORM_URL
            }
        }

        result = {
            "series_id": series_id,
            "series_title": series_title,
            "total_seasons": len(seasons),
            "total_episodes_mapped": total_episodes,
            "series_url": f"{PLATFORM_URL}/series/{series_id}",
            "episodes": episodes_map,
            "tv_series_schema": tv_series_schema,
            "tv_series_schema_html": f'<script type="application/ld+json">\n{json.dumps(tv_series_schema, ensure_ascii=False, indent=2)}\n</script>',
            "seo_recommendations": [
                f"بناء صفحة رئيسية لـ '{series_title}' تجمع كل الحلقات",
                "إضافة TVSeries schema في صفحة السلسلة",
                "ربط كل حلقة بالحلقة التالية والسابقة (internal linking)",
                f"استخدام الكلمة المفتاحية '{series_title}' في عناوين كل حلقة",
            ],
        }

        logger.info(f"Built SEO map for series {series_id}: {series_title} ({total_episodes} episodes)")
        return json.dumps(result, ensure_ascii=False, indent=2)

    except Exception as e:
        logger.error(f"Error building series SEO map: {e}")
        return json.dumps({"error": str(e)}, ensure_ascii=False)


# ============================================================================
# Advanced Scientific & Practical Tools
# ============================================================================

@seo_tool(annotations=ToolAnnotations(title="Build Knowledge Graph (بناء خريطة المعرفة)", readOnlyHint=True))
async def build_knowledge_graph(sections: str = "AJA,AJD") -> str:
    """Build a knowledge graph of entities (topics, countries, people) from content titles.
    
    Extracts named entities from video titles across sections and builds
    a network showing how topics, countries, and themes interconnect.
    
    Args:
        sections: Comma-separated section IDs (default: AJA,AJD)
    
    Returns:
        JSON with entity network, top entities, co-occurrence matrix, and insights
    """
    import re
    from collections import defaultdict, Counter
    
    # Arabic stopwords to filter out
    STOPWORDS = {
        'في', 'من', 'إلى', 'على', 'عن', 'مع', 'هل', 'ما', 'لا', 'أن', 'كان',
        'هذا', 'هذه', 'التي', 'الذي', 'كيف', 'لماذا', 'متى', 'أين', 'بين',
        'بعد', 'قبل', 'حتى', 'أو', 'و', 'ف', 'ب', 'ل', 'ك', 'أكثر', 'أقل',
        'كل', 'بعض', 'جميع', 'هو', 'هي', 'هم', 'نحن', 'أنا', 'أنت', 'عام',
        'العام', 'الـ', 'يوم', 'أيام', 'سنة', 'سنوات', 'مليون', 'مليار',
        'الجزيرة', '360', 'الجزيرة360'
    }
    
    # High-value entity keywords (topics, countries, themes)
    ENTITY_PATTERNS = [
        # Countries & regions
        r'(فلسطين|غزة|إسرائيل|لبنان|سوريا|العراق|إيران|اليمن|السودان|ليبيا|مصر|تونس|المغرب|الجزائر|تركيا|روسيا|أمريكا|الصين|أوروبا|أفريقيا|الخليج|السعودية)',
        # Political entities
        r'(حماس|حزب الله|الناتو|الأمم المتحدة|مجلس الأمن|الاتحاد الأوروبي|البنك الدولي)',
        # Themes
        r'(الحرب|السلام|الانتخابات|الاقتصاد|المناخ|التكنولوجيا|الذكاء الاصطناعي|الهجرة|اللاجئين|الطاقة|النفط|الغاز)',
    ]
    
    try:
        section_list = [s.strip() for s in sections.split(',') if s.strip()]
        all_titles = []
        all_items = []
        
        for section_id in section_list:
            try:
                data = await client.get_section_content(section_id, items_per_bucket=20)
                if isinstance(data, dict):
                    for bucket in data.get('buckets', []):
                        if isinstance(bucket, dict):
                            for item in bucket.get('contentList', []):
                                if isinstance(item, dict) and item.get('title'):
                                    all_titles.append(item['title'])
                                    all_items.append({
                                        'id': item.get('id'),
                                        'title': item['title'],
                                        'section': section_id
                                    })
            except Exception:
                continue
        
        if not all_titles:
            return json.dumps({'error': 'No content found'}, ensure_ascii=False)
        
        # Extract entities from titles
        entity_counter = Counter()
        entity_items = defaultdict(list)  # entity -> list of video titles
        co_occurrence = defaultdict(Counter)  # entity -> {other_entity: count}
        
        for item in all_items:
            title = item['title']
            found_entities = set()
            
            # Pattern-based entity extraction
            for pattern in ENTITY_PATTERNS:
                matches = re.findall(pattern, title)
                found_entities.update(matches)
            
            # Word-level extraction (words > 3 chars, not stopwords)
            words = re.findall(r'[\u0600-\u06FF]{4,}', title)
            for word in words:
                if word not in STOPWORDS and not any(word in e for e in found_entities):
                    found_entities.add(word)
            
            for entity in found_entities:
                entity_counter[entity] += 1
                entity_items[entity].append(item['title'][:50])
            
            # Co-occurrence
            entity_list = list(found_entities)
            for i, e1 in enumerate(entity_list):
                for e2 in entity_list[i+1:]:
                    co_occurrence[e1][e2] += 1
                    co_occurrence[e2][e1] += 1
        
        # Top entities
        top_entities = [
            {
                'entity': entity,
                'count': count,
                'percentage': round(count / len(all_titles) * 100, 1),
                'sample_titles': entity_items[entity][:3],
                'related_entities': [
                    {'entity': k, 'co_occurrences': v}
                    for k, v in sorted(co_occurrence[entity].items(), key=lambda x: -x[1])[:5]
                ]
            }
            for entity, count in entity_counter.most_common(20)
        ]
        
        # Topic clusters (entities that frequently co-occur)
        clusters = []
        processed = set()
        for entity, count in entity_counter.most_common(10):
            if entity in processed:
                continue
            related = [k for k, v in co_occurrence[entity].items() if v >= 2]
            if related:
                clusters.append({
                    'core_topic': entity,
                    'related_topics': related[:5],
                    'total_videos': count
                })
                processed.add(entity)
                processed.update(related[:3])
        
        result = {
            'summary': {
                'total_videos_analyzed': len(all_titles),
                'unique_entities_found': len(entity_counter),
                'sections_analyzed': section_list,
            },
            'top_entities': top_entities,
            'topic_clusters': clusters,
            'insights': [
                f"أكثر موضوع تكراراً: {entity_counter.most_common(1)[0][0]} ({entity_counter.most_common(1)[0][1]} فيديو)" if entity_counter else "لا توجد بيانات كافية",
                f"إجمالي الكيانات المكتشفة: {len(entity_counter)} موضوع/كيان فريد",
                f"إجمالي الفيديوهات المحللة: {len(all_titles)} فيديو",
            ]
        }
        
        logger.info(f"Built knowledge graph: {len(entity_counter)} entities from {len(all_titles)} videos")
        return json.dumps(result, ensure_ascii=False, indent=2)
        
    except Exception as e:
        logger.error(f"Error building knowledge graph: {e}")
        return json.dumps({'error': str(e)}, ensure_ascii=False)


@seo_tool(annotations=ToolAnnotations(title="Generate FAQ Schema (توليد مخطط الأسئلة الشائعة)", readOnlyHint=True))
async def generate_faq_schema(video_id: int) -> str:
    """Generate FAQ Schema (JSON-LD) for a video to improve AI discoverability.
    
    Creates structured FAQ data based on video title and description.
    FAQ Schema helps content appear in AI answers (ChatGPT, Gemini, Perplexity)
    and Google's People Also Ask section.
    
    Args:
        video_id: The video ID to generate FAQ schema for
    
    Returns:
        JSON with FAQ questions/answers and ready-to-use JSON-LD schema
    """
    try:
        vod_data = await client.get_vod_details(video_id)
        if not isinstance(vod_data, dict):
            return json.dumps({'error': 'Video not found'}, ensure_ascii=False)
        
        title = vod_data.get('title', '')
        description = vod_data.get('description', '')
        duration_secs = vod_data.get('duration', 0)
        duration_mins = round(duration_secs / 60) if duration_secs else 0
        max_height = vod_data.get('maxHeight', 0)
        quality = '4K Ultra HD' if max_height >= 2160 else ('Full HD' if max_height >= 1080 else 'HD')
        
        categories = []
        raw_cats = vod_data.get('categories', [])
        for c in raw_cats:
            if isinstance(c, dict):
                categories.append(c.get('name', ''))
            elif isinstance(c, str):
                categories.append(c)
        
        # Generate contextual FAQ questions based on content
        faqs = []
        
        # Q1: What is this about?
        faqs.append({
            'question': f'ما موضوع {title}؟',
            'answer': description if description else f'{title} — محتوى حصري على الجزيرة 360 بجودة {quality}.'
        })
        
        # Q2: Duration
        if duration_mins > 0:
            faqs.append({
                'question': f'كم مدة {title}؟',
                'answer': f'مدة {title} هي {duration_mins} دقيقة، متاح للمشاهدة بجودة {quality} على منصة الجزيرة 360.'
            })
        
        # Q3: Where to watch
        faqs.append({
            'question': f'أين يمكن مشاهدة {title}؟',
            'answer': f'يمكن مشاهدة {title} على منصة الجزيرة 360 (aljazeera360.com) بجودة {quality} مجاناً.'
        })
        
        # Q4: Category-based question
        if categories:
            cat_str = ' و'.join(categories[:2])
            faqs.append({
                'question': f'هل {title} متعلق بـ{cat_str}؟',
                'answer': f'نعم، {title} يندرج ضمن تصنيف {cat_str} على منصة الجزيرة 360.'
            })
        
        # Q5: Quality
        faqs.append({
            'question': f'ما جودة {title} على الجزيرة 360؟',
            'answer': f'يتوفر {title} بجودة {quality} على منصة الجزيرة 360، مما يوفر تجربة مشاهدة استثنائية.'
        })
        
        # Build JSON-LD
        faq_schema = {
            '@context': 'https://schema.org',
            '@type': 'FAQPage',
            'mainEntity': [
                {
                    '@type': 'Question',
                    'name': faq['question'],
                    'acceptedAnswer': {
                        '@type': 'Answer',
                        'text': faq['answer']
                    }
                }
                for faq in faqs
            ]
        }
        
        result = {
            'video_id': video_id,
            'title': title,
            'faqs': faqs,
            'faq_count': len(faqs),
            'schema_jsonld': faq_schema,
            'schema_html': f'<script type="application/ld+json">\n{json.dumps(faq_schema, ensure_ascii=False, indent=2)}\n</script>',
            'usage_tips': [
                'أضف هذا الـ Schema في <head> صفحة الفيديو',
                'يساعد على الظهور في People Also Ask في Google',
                'يزيد احتمال ذكر المحتوى في إجابات ChatGPT و Gemini',
                'لا يحتاج أي تعديل — جاهز للنشر مباشرة'
            ]
        }
        
        logger.info(f"Generated FAQ schema for video {video_id}: {len(faqs)} questions")
        return json.dumps(result, ensure_ascii=False, indent=2)
        
    except Exception as e:
        logger.error(f"Error generating FAQ schema: {e}")
        return json.dumps({'error': str(e)}, ensure_ascii=False)


@seo_tool(annotations=ToolAnnotations(title="Get AI Discoverability Score (مؤشر الاكتشاف بالذكاء الاصطناعي)", readOnlyHint=True))
async def get_ai_discoverability_score(section_id: str = "AJA", max_items: int = 50) -> str:
    """Calculate AI Discoverability Score for content (0-100).
    
    Measures how well each video can be discovered and cited by AI systems
    (ChatGPT, Gemini, Perplexity, Claude) based on metadata completeness,
    content quality signals, and SEO readiness.
    
    Scoring criteria:
    - Title quality (length, keywords): 20 pts
    - Description completeness: 25 pts  
    - Video quality (4K/HD): 15 pts
    - Access level (free vs premium): 20 pts
    - Thumbnail availability: 10 pts
    - Duration (optimal 5-30 min): 10 pts
    
    Args:
        section_id: Section to analyze (default: AJA)
        max_items: Maximum items to score (default: 50)
    
    Returns:
        JSON with scores, distribution, top/bottom performers, and recommendations
    """
    from collections import Counter
    try:
        data = await client.get_section_content(section_id, items_per_bucket=10)
        
        items = []
        if isinstance(data, dict):
            for bucket in data.get('buckets', []):
                if isinstance(bucket, dict):
                    items.extend(bucket.get('contentList', []))
        
        if not items:
            return json.dumps({'error': f'No content found in section {section_id}'}, ensure_ascii=False)
        
        scored_items = []
        
        # Apply pagination to audited items
        start_idx = (page - 1) * page_size
        end_idx = start_idx + page_size
        paginated_items = items[start_idx:end_idx]
        
        for item in paginated_items:
            if not isinstance(item, dict):
                continue
            
            score = 0
            breakdown = {}
            recommendations = []
            
            title = item.get('title', '')
            description = item.get('description', '')
            thumbnail = item.get('thumbnailUrl', '')
            max_height = item.get('maxHeight', 0)
            access_level = item.get('accessLevel', '')
            duration = item.get('duration', 0)
            duration_mins = duration / 60 if duration else 0
            
            # 1. Title quality (20 pts)
            title_len = len(title)
            if title_len >= 30:
                title_score = 20
            elif title_len >= 20:
                title_score = 15
            elif title_len >= 10:
                title_score = 10
            else:
                title_score = 5
                recommendations.append('عنوان قصير جداً — أضف كلمات وصفية')
            
            # Bonus for question-style titles (great for AI)
            if any(q in title for q in ['؟', 'كيف', 'لماذا', 'ما', 'هل', 'من', 'أين', 'متى']):
                title_score = min(20, title_score + 3)
            
            score += title_score
            breakdown['title'] = title_score
            
            # 2. Description completeness (25 pts)
            desc_len = len(description)
            if desc_len >= 150:
                desc_score = 25
            elif desc_len >= 80:
                desc_score = 18
            elif desc_len >= 30:
                desc_score = 10
            elif desc_len > 0:
                desc_score = 5
                recommendations.append('وصف قصير — أضف تفاصيل أكثر (150+ حرف)')
            else:
                desc_score = 0
                recommendations.append('لا يوجد وصف — أضف وصفاً وصفياً كاملاً')
            
            score += desc_score
            breakdown['description'] = desc_score
            
            # 3. Video quality (15 pts)
            if max_height >= 2160:
                quality_score = 15
                quality_label = '4K'
            elif max_height >= 1080:
                quality_score = 12
                quality_label = 'FHD'
            elif max_height >= 720:
                quality_score = 8
                quality_label = 'HD'
            else:
                quality_score = 4
                quality_label = 'SD'
                recommendations.append('جودة منخفضة — الفيديوهات 4K/FHD أفضل للـ SEO')
            
            score += quality_score
            breakdown['quality'] = quality_score
            
            # 4. Access level (20 pts)
            if access_level == 'GRANTED':
                access_score = 20
            elif access_level == 'PREVIEW':
                access_score = 10
                recommendations.append('محتوى مقيّد — المحتوى المجاني أكثر قابلية للاكتشاف')
            else:
                access_score = 5
                recommendations.append('محتوى مقيّد — المحتوى المجاني أكثر قابلية للاكتشاف')
            
            score += access_score
            breakdown['access_level'] = access_score
            
            # 5. Thumbnail (10 pts)
            if thumbnail and thumbnail.startswith('http'):
                thumb_score = 10
            else:
                thumb_score = 0
                recommendations.append('لا توجد صورة مصغرة — أضف thumbnail')
            
            score += thumb_score
            breakdown['thumbnail'] = thumb_score
            
            # 6. Duration (10 pts) — optimal 5-30 mins for AI citation
            if 5 <= duration_mins <= 30:
                dur_score = 10
            elif 2 <= duration_mins < 5 or 30 < duration_mins <= 60:
                dur_score = 7
            elif duration_mins > 0:
                dur_score = 4
            else:
                dur_score = 0
            
            score += dur_score
            breakdown['duration'] = dur_score
            
            # Grade
            if score >= 85:
                grade = 'A'
            elif score >= 70:
                grade = 'B'
            elif score >= 55:
                grade = 'C'
            elif score >= 40:
                grade = 'D'
            else:
                grade = 'F'
            
            scored_items.append({
                'id': item.get('id'),
                'title': title,
                'score': score,
                'grade': grade,
                'breakdown': breakdown,
                'recommendations': recommendations,
                'quality': quality_label if 'quality_label' in dir() else 'Unknown',
                'access': access_level,
                'duration_mins': round(duration_mins, 1)
            })
        
        if not scored_items:
            return json.dumps({'error': 'No items scored'}, ensure_ascii=False)
        
        # Statistics
        scores = [i['score'] for i in scored_items]
        avg_score = round(sum(scores) / len(scores), 1)
        
        grade_dist = Counter(i['grade'] for i in scored_items)
        
        # Sort by score
        scored_items.sort(key=lambda x: -x['score'])
        
        result = {
            'summary': {
                'section': section_id,
                'total_analyzed': len(scored_items),
                'average_score': avg_score,
                'average_grade': 'A' if avg_score >= 85 else ('B' if avg_score >= 70 else ('C' if avg_score >= 55 else ('D' if avg_score >= 40 else 'F'))),
                'grade_distribution': dict(grade_dist),
                'score_range': {'min': min(scores), 'max': max(scores)}
            },
            'top_performers': scored_items[:5],
            'needs_improvement': [i for i in scored_items if i['grade'] in ['D', 'F']][:10],
            'all_scores': scored_items,
            'section_insights': [
                f"متوسط نقاط قابلية الاكتشاف: {avg_score}/100",
                f"نسبة المحتوى ممتاز (A/B): {round((grade_dist.get('A',0)+grade_dist.get('B',0))/len(scored_items)*100, 1)}%",
                f"نسبة المحتوى يحتاج تحسين (D/F): {round((grade_dist.get('D',0)+grade_dist.get('F',0))/len(scored_items)*100, 1)}%",
                f"أعلى نقاط: {max(scores)} | أقل نقاط: {min(scores)}"
            ]
        }
        
        logger.info(f"AI Discoverability Score for {section_id}: avg={avg_score}, n={len(scored_items)}")
        return json.dumps(result, ensure_ascii=False, indent=2)
        
    except Exception as e:
        logger.error(f"Error calculating discoverability score: {e}")
        return json.dumps({'error': str(e)}, ensure_ascii=False)


@seo_tool(annotations=ToolAnnotations(title="Build Topic Clusters (بناء المجموعات الموضوعية)", readOnlyHint=True))
async def build_topic_clusters(sections: str = "AJA,AJD") -> str:
    """Build SEO Topic Clusters (Pillar + Supporting content strategy).
    
    Analyzes content and groups it into topic clusters where each cluster has:
    - A Pillar topic (most content, highest authority)
    - Supporting content pieces around the pillar
    - Internal linking recommendations
    
    This is the most powerful modern SEO strategy (2024-2026).
    
    Args:
        sections: Comma-separated section IDs to analyze (default: AJA,AJD)
    
    Returns:
        JSON with topic clusters, pillar pages, supporting content, and linking strategy
    """
    import re
    from collections import defaultdict, Counter
    
    # Core topic seeds for clustering
    TOPIC_SEEDS = {
        'فلسطين وغزة': ['فلسطين', 'غزة', 'حماس', 'الضفة', 'القدس', 'أونروا', 'إسرائيل'],
        'الحروب والنزاعات': ['حرب', 'معركة', 'نزاع', 'صراع', 'هجوم', 'قصف', 'اليمن', 'السودان', 'سوريا', 'ليبيا'],
        'السياسة والانتخابات': ['انتخابات', 'رئيس', 'حكومة', 'برلمان', 'سياسة', 'ديمقراطية', 'دبلوماسية'],
        'الاقتصاد والمال': ['اقتصاد', 'نفط', 'غاز', 'طاقة', 'تضخم', 'بنك', 'استثمار', 'تجارة'],
        'التكنولوجيا والذكاء الاصطناعي': ['تكنولوجيا', 'ذكاء اصطناعي', 'رقمي', 'إنترنت', 'تقنية', 'ابتكار'],
        'المناخ والبيئة': ['مناخ', 'بيئة', 'احترار', 'تلوث', 'طاقة متجددة', 'كوارث'],
        'الرياضة': ['كرة', 'رياضة', 'بطولة', 'كأس', 'أولمبياد', 'لاعب', 'فريق'],
        'التاريخ والحضارة': ['تاريخ', 'حضارة', 'تراث', 'قديم', 'أثري', 'عصر', 'إمبراطورية'],
        'المجتمع والثقافة': ['مجتمع', 'ثقافة', 'فن', 'موسيقى', 'سينما', 'أدب', 'شباب', 'مرأة'],
        'الصحة والعلوم': ['صحة', 'طب', 'علوم', 'بحث', 'دراسة', 'مرض', 'علاج', 'وباء'],
    }
    
    try:
        section_list = [s.strip() for s in sections.split(',') if s.strip()]
        all_items = []
        
        for section_id in section_list:
            try:
                data = await client.get_section_content(section_id, items_per_bucket=20)
                if isinstance(data, dict):
                    for bucket in data.get('buckets', []):
                        if isinstance(bucket, dict):
                            for item in bucket.get('contentList', []):
                                if isinstance(item, dict) and item.get('title'):
                                    all_items.append({
                                        'id': item.get('id'),
                                        'title': item['title'],
                                        'description': item.get('description', ''),
                                        'section': section_id,
                                        'access': item.get('accessLevel', ''),
                                        'quality': item.get('maxHeight', 0)
                                    })
            except Exception:
                continue
        
        if not all_items:
            return json.dumps({'error': 'No content found'}, ensure_ascii=False)
        
        # Assign items to clusters
        clusters = defaultdict(list)
        unassigned = []
        
        for item in all_items:
            text = item['title'] + ' ' + item['description']
            assigned = False
            
            for cluster_name, keywords in TOPIC_SEEDS.items():
                if any(kw in text for kw in keywords):
                    clusters[cluster_name].append(item)
                    assigned = True
                    break
            
            if not assigned:
                unassigned.append(item)
        
        # Build cluster report
        cluster_report = []
        for cluster_name, cluster_items in sorted(clusters.items(), key=lambda x: -len(x[1])):
            if not cluster_items:
                continue
            
            # Find pillar (best item = longest description + free access)
            def pillar_score(item):
                s = len(item.get('description', ''))
                if item.get('access') == 'GRANTED':
                    s += 100
                if item.get('quality', 0) >= 2160:
                    s += 50
                return s
            
            pillar = max(cluster_items, key=pillar_score)
            supporting = [i for i in cluster_items if i['id'] != pillar['id']]
            
            cluster_report.append({
                'cluster': cluster_name,
                'total_pieces': len(cluster_items),
                'pillar_content': {
                    'id': pillar['id'],
                    'title': pillar['title'],
                    'suggested_url': f"/topic/{cluster_name.replace(' ', '-')}",
                    'suggested_meta_title': f"{cluster_name} — الجزيرة 360",
                    'role': 'Pillar Page — المحتوى الرئيسي للموضوع'
                },
                'supporting_content': [
                    {
                        'id': i['id'],
                        'title': i['title'],
                        'link_anchor': i['title'][:30],
                        'role': 'Supporting Content'
                    }
                    for i in supporting[:8]
                ],
                'internal_links': [
                    f"اربط '{s['title'][:30]}' بـ Pillar Page '{pillar['title'][:30]}'"
                    for s in supporting[:5]
                ],
                'seo_strength': 'قوي' if len(cluster_items) >= 5 else ('متوسط' if len(cluster_items) >= 3 else 'ضعيف')
            })
        
        result = {
            'summary': {
                'total_items_analyzed': len(all_items),
                'items_in_clusters': sum(len(v) for v in clusters.values()),
                'items_unassigned': len(unassigned),
                'total_clusters': len(cluster_report),
                'strong_clusters': len([c for c in cluster_report if c['seo_strength'] == 'قوي']),
            },
            'clusters': cluster_report,
            'unassigned_content': [{'id': i['id'], 'title': i['title']} for i in unassigned[:10]],
            'strategy_recommendations': [
                'ابنِ Pillar Page لكل cluster قوي (5+ فيديوهات)',
                'أضف روابط داخلية من كل Supporting Content للـ Pillar Page',
                'المحتوى غير المصنّف يحتاج تصنيف أو تحسين العنوان',
                f"أقوى cluster: {cluster_report[0]['cluster']} ({cluster_report[0]['total_pieces']} فيديو)" if cluster_report else ''
            ]
        }
        
        logger.info(f"Built topic clusters: {len(cluster_report)} clusters from {len(all_items)} items")
        return json.dumps(result, ensure_ascii=False, indent=2)
        
    except Exception as e:
        logger.error(f"Error building topic clusters: {e}")
        return json.dumps({'error': str(e)}, ensure_ascii=False)


@seo_tool(annotations=ToolAnnotations(title="Find Evergreen Content (المحتوى دائم الخضرة)", readOnlyHint=True))
async def find_evergreen_content(sections: str = "AJA,AJD") -> str:
    """Identify evergreen content (timeless value) vs time-sensitive news content.
    
    Evergreen content has lasting SEO value and should be prioritized for:
    - Schema markup investment
    - Internal linking
    - Meta description optimization
    - Featured snippet targeting
    
    Args:
        sections: Comma-separated section IDs (default: AJA,AJD)
    
    Returns:
        JSON with evergreen/news classification, SEO priority scores, and recommendations
    """
    import re
    
    # News/time-sensitive indicators
    NEWS_KEYWORDS = [
        'اليوم', 'أمس', 'الآن', 'عاجل', 'خبر', 'أخبار', 'تقرير', 'بيان',
        '2024', '2025', '2026', 'يناير', 'فبراير', 'مارس', 'أبريل', 'مايو',
        'يونيو', 'يوليو', 'أغسطس', 'سبتمبر', 'أكتوبر', 'نوفمبر', 'ديسمبر',
        'الأسبوع', 'الشهر', 'انتخابات', 'قمة', 'مؤتمر', 'اجتماع'
    ]
    
    # Evergreen indicators
    EVERGREEN_KEYWORDS = [
        'تاريخ', 'حضارة', 'تراث', 'كيف', 'لماذا', 'ما هو', 'ما هي',
        'دليل', 'شرح', 'تعلم', 'أساسيات', 'مقدمة', 'وثائقي', 'قصة',
        'رحلة', 'اكتشاف', 'علوم', 'طبيعة', 'حياة', 'إنسان', 'فلسفة',
        'فن', 'موسيقى', 'أدب', 'ثقافة', 'تقاليد', 'عادات'
    ]
    
    try:
        section_list = [s.strip() for s in sections.split(',') if s.strip()]
        all_items = []
        
        for section_id in section_list:
            try:
                data = await client.get_section_content(section_id, items_per_bucket=20)
                if isinstance(data, dict):
                    for bucket in data.get('buckets', []):
                        if isinstance(bucket, dict):
                            for item in bucket.get('contentList', []):
                                if isinstance(item, dict) and item.get('title'):
                                    all_items.append({
                                        'id': item.get('id'),
                                        'title': item['title'],
                                        'description': item.get('description', ''),
                                        'section': section_id,
                                        'access': item.get('accessLevel', ''),
                                        'quality': item.get('maxHeight', 0),
                                        'duration': item.get('duration', 0)
                                    })
            except Exception:
                continue
        
        if not all_items:
            return json.dumps({'error': 'No content found'}, ensure_ascii=False)
        
        evergreen = []
        news_content = []
        mixed = []
        
        for item in all_items:
            text = item['title'] + ' ' + item['description']
            
            news_score = sum(1 for kw in NEWS_KEYWORDS if kw in text)
            evergreen_score = sum(1 for kw in EVERGREEN_KEYWORDS if kw in text)
            
            # Calculate SEO priority score
            seo_priority = 0
            
            # Evergreen gets higher base priority
            if evergreen_score > news_score:
                content_type = 'evergreen'
                seo_priority += 40
            elif news_score > evergreen_score:
                content_type = 'news'
                seo_priority += 10
            else:
                content_type = 'mixed'
                seo_priority += 25
            
            # Quality bonus
            if item['quality'] >= 2160:
                seo_priority += 20
            elif item['quality'] >= 1080:
                seo_priority += 15
            
            # Free access bonus
            if item['access'] == 'GRANTED':
                seo_priority += 20
            
            # Description bonus
            if len(item['description']) >= 100:
                seo_priority += 10
            
            # Duration bonus (5-30 mins is optimal)
            dur_mins = item['duration'] / 60 if item['duration'] else 0
            if 5 <= dur_mins <= 30:
                seo_priority += 10
            
            item_result = {
                'id': item['id'],
                'title': item['title'],
                'content_type': content_type,
                'seo_priority_score': seo_priority,
                'evergreen_signals': evergreen_score,
                'news_signals': news_score,
                'quality': f"{item['quality']}p" if item['quality'] else 'unknown',
                'access': item['access'],
                'action': (
                    '🟢 أولوية عالية — استثمر في Schema + Internal Links + Meta'
                    if content_type == 'evergreen' and seo_priority >= 60
                    else '🟡 أولوية متوسطة — حسّن الـ metadata'
                    if seo_priority >= 40
                    else '🔴 أولوية منخفضة — محتوى إخباري عابر'
                )
            }
            
            if content_type == 'evergreen':
                evergreen.append(item_result)
            elif content_type == 'news':
                news_content.append(item_result)
            else:
                mixed.append(item_result)
        
        # Sort by SEO priority
        evergreen.sort(key=lambda x: -x['seo_priority_score'])
        mixed.sort(key=lambda x: -x['seo_priority_score'])
        
        result = {
            'summary': {
                'total_analyzed': len(all_items),
                'evergreen_count': len(evergreen),
                'news_count': len(news_content),
                'mixed_count': len(mixed),
                'evergreen_percentage': round(len(evergreen) / len(all_items) * 100, 1),
                'sections_analyzed': section_list
            },
            'top_evergreen_priorities': evergreen[:10],
            'mixed_content': mixed[:5],
            'news_content_sample': news_content[:5],
            'seo_investment_guide': [
                f"🟢 {len(evergreen)} محتوى دائم الخضرة — استثمر فيه أولاً",
                f"🟡 {len(mixed)} محتوى مختلط — يستحق تحسين الـ metadata",
                f"🔴 {len(news_content)} محتوى إخباري — أولوية منخفضة للـ SEO طويل المدى",
                "ركّز الـ Schema markup والـ Internal Links على المحتوى الدائم أولاً",
                "المحتوى الدائم يستمر في جلب الزيارات لسنوات بعد النشر"
            ]
        }
        
        logger.info(f"Evergreen analysis: {len(evergreen)} evergreen, {len(news_content)} news, {len(mixed)} mixed")
        return json.dumps(result, ensure_ascii=False, indent=2)
        
    except Exception as e:
        logger.error(f"Error finding evergreen content: {e}")
        return json.dumps({'error': str(e)}, ensure_ascii=False)


# ============================================================================
# Advanced Tools — typedTags & episodeInformation
# ============================================================================

@seo_tool(annotations=ToolAnnotations(title="Get Host Profile (ملف مقدم البرنامج والـ Person Schema)", readOnlyHint=True))
async def get_host_profile(host_name: str, max_items: int = 20) -> str:
    """
    Get a complete profile for a show host/presenter including all their content,
    genres covered, shows hosted, and an SEO-ready host page schema.
    
    Args:
        host_name: Name of the host/presenter (Arabic or English)
        max_items: Maximum number of items to scan per section (default: 20)
    """
    try:
        host_name_lower = host_name.strip()
        host_videos = []
        genres_set = set()
        shows_set = set()
        countries_set = set()
        tags_list = []

        # Scan all sections for content by this host
        for section_id in list(SECTIONS.keys())[:8]:  # scan first 8 sections
            try:
                data = await client.get_section_content(section_id, items_per_bucket=max_items)
                buckets = data.get("buckets", []) if isinstance(data, dict) else []
                for bucket in buckets:
                    for item in bucket.get("contentList", []):
                        vid_id = item.get("id")
                        if not vid_id:
                            continue
                        try:
                            vod = await client.get_vod_details(vid_id)
                            if not isinstance(vod, dict):
                                continue
                            typed_tags = vod.get("typedTags", [])
                            # Check if this host is in the typedTags
                            host_match = False
                            for tag in typed_tags:
                                if tag.get("name") in ("Host", "Host Name", "Featured Host"):
                                    if host_name_lower.lower() in tag.get("value", "").lower():
                                        host_match = True
                                if tag.get("name") in ("Genre", "Featured Genre"):
                                    genres_set.add(tag.get("value", ""))
                                if tag.get("name") == "Show Name":
                                    shows_set.add(tag.get("value", ""))
                                if tag.get("name") == "Related Country":
                                    countries_set.add(tag.get("value", ""))
                                if tag.get("name") == "Searchable Tags":
                                    tags_list.append(tag.get("value", ""))
                            if host_match:
                                ep_info = vod.get("episodeInformation", {})
                                host_videos.append({
                                    "id": vid_id,
                                    "title": vod.get("title", ""),
                                    "description": vod.get("description", "")[:120],
                                    "duration": vod.get("duration", 0),
                                    "publishedDate": vod.get("publishedDate", "")[:10],
                                    "show": ep_info.get("seriesInformation", {}).get("title", ""),
                                    "season": ep_info.get("seasonNumber", ""),
                                    "episode": ep_info.get("episodeNumber", ""),
                                    "thumbnail": vod.get("thumbnailUrl", ""),
                                    "accessLevel": vod.get("accessLevel", "")
                                })
                        except Exception:
                            continue
            except Exception:
                continue

        if not host_videos:
            return json.dumps({"error": f"No content found for host: {host_name}"}, ensure_ascii=False)

        # Build Person + ItemList Schema
        from collections import Counter
        top_tags = [t for t, _ in Counter(tags_list).most_common(10)]
        schema = {
            "@context": "https://schema.org",
            "@type": "Person",
            "name": host_name,
            "worksFor": {"@type": "Organization", "name": "الجزيرة 360"},
            "knowsAbout": list(genres_set),
            "sameAs": f"https://www.aljazeera360.com/search?q={host_name}"
        }

        result = {
            "host": host_name,
            "total_videos": len(host_videos),
            "shows_hosted": sorted(shows_set),
            "genres_covered": sorted(genres_set),
            "countries_covered": sorted(countries_set),
            "top_keywords": top_tags,
            "seo_meta_title": f"{host_name} | مقدّم برامج الجزيرة 360",
            "seo_meta_description": f"شاهد جميع حلقات ومقاطع {host_name} على الجزيرة 360 — {len(host_videos)} فيديو في {', '.join(list(shows_set)[:3])}.",
            "person_schema": schema,
            "videos": host_videos[:20]
        }
        return json.dumps(result, ensure_ascii=False, indent=2)
    except Exception as e:
        return json.dumps({"error": str(e)}, ensure_ascii=False)


@seo_tool(annotations=ToolAnnotations(title="Get Genre Report (تقرير تصنيف المحتوى والـ Genres)", readOnlyHint=True))
async def get_genre_report(genre: str = "", max_items: int = 15) -> str:
    """
    Get a full report of content by genre or sub-genre using typedTags data.
    Lists all content in that genre with SEO metadata for building category pages.
    
    Args:
        genre: Genre name in Arabic (e.g. صحة, رياضة, سياسة, وثائقي) — leave empty for all genres
        max_items: Items per section to scan (default: 15)
    """
    try:
        genre_map = {}  # genre -> list of videos
        subgenre_map = {}  # subgenre -> list of videos

        for section_id in list(SECTIONS.keys())[:8]:
            try:
                data = await client.get_section_content(section_id, items_per_bucket=max_items)
                buckets = data.get("buckets", []) if isinstance(data, dict) else []
                for bucket in buckets:
                    for item in bucket.get("contentList", []):
                        vid_id = item.get("id")
                        if not vid_id:
                            continue
                        try:
                            vod = await client.get_vod_details(vid_id)
                            if not isinstance(vod, dict):
                                continue
                            typed_tags = vod.get("typedTags", [])
                            vid_genre = ""
                            vid_subgenre = ""
                            vid_tags = []
                            for tag in typed_tags:
                                if tag.get("name") in ("Genre", "Featured Genre"):
                                    vid_genre = tag.get("value", "")
                                if tag.get("name") == "Sub-Genre":
                                    vid_subgenre = tag.get("value", "")
                                if tag.get("name") == "Searchable Tags":
                                    vid_tags.append(tag.get("value", ""))

                            # Filter by genre if specified
                            if genre and genre.lower() not in (vid_genre + vid_subgenre).lower():
                                continue

                            video_entry = {
                                "id": vid_id,
                                "title": vod.get("title", ""),
                                "genre": vid_genre,
                                "subgenre": vid_subgenre,
                                "tags": vid_tags,
                                "duration": vod.get("duration", 0),
                                "publishedDate": vod.get("publishedDate", "")[:10],
                                "accessLevel": vod.get("accessLevel", "")
                            }

                            if vid_genre:
                                genre_map.setdefault(vid_genre, []).append(video_entry)
                            if vid_subgenre:
                                subgenre_map.setdefault(vid_subgenre, []).append(video_entry)
                        except Exception:
                            continue
            except Exception:
                continue

        if not genre_map and not subgenre_map:
            return json.dumps({"error": "No genre data found"}, ensure_ascii=False)

        # Build summary
        genre_summary = [
            {"genre": g, "count": len(vids),
             "seo_page_title": f"محتوى {g} | الجزيرة 360",
             "seo_description": f"شاهد {len(vids)} فيديو في تصنيف {g} على الجزيرة 360 بجودة 4K.",
             "sample_videos": [v["title"] for v in vids[:5]]}
            for g, vids in sorted(genre_map.items(), key=lambda x: -len(x[1]))
        ]
        subgenre_summary = [
            {"subgenre": sg, "count": len(vids),
             "sample_videos": [v["title"] for v in vids[:3]]}
            for sg, vids in sorted(subgenre_map.items(), key=lambda x: -len(x[1]))
        ]

        result = {
            "filter": genre or "all",
            "total_genres": len(genre_map),
            "total_subgenres": len(subgenre_map),
            "genres": genre_summary,
            "subgenres": subgenre_summary
        }
        return json.dumps(result, ensure_ascii=False, indent=2)
    except Exception as e:
        return json.dumps({"error": str(e)}, ensure_ascii=False)


@seo_tool(annotations=ToolAnnotations(title="Get Searchable Tags Map (خريطة الكلمات المفتاحية الأكثر بحثاً)", readOnlyHint=True))
async def get_searchable_tags_map(max_items: int = 20, top_n: int = 50, page: int = 1, page_size: int = 20) -> str:
    """
    Extract and rank all Searchable Tags from the entire catalog.
    These are the exact keywords the audience searches for — ideal for SEO keyword strategy.
    Also returns Related Countries and Genres distribution.
    
    Args:
        max_items: Items per section to scan (default: 20)
        top_n: Number of top tags to return (default: 50)
        page: Page number for returned tags (default: 1)
        page_size: Number of tags per page (default: 20)
    """
    try:
        from collections import Counter
        all_tags = Counter()
        all_countries = Counter()
        all_genres = Counter()
        all_subgenres = Counter()
        all_formats = Counter()
        all_hosts = Counter()
        total_videos = 0

        for section_id in list(SECTIONS.keys())[:10]:
            try:
                data = await client.get_section_content(section_id, items_per_bucket=max_items)
                buckets = data.get("buckets", []) if isinstance(data, dict) else []
                for bucket in buckets:
                    for item in bucket.get("contentList", []):
                        vid_id = item.get("id")
                        if not vid_id:
                            continue
                        try:
                            vod = await client.get_vod_details(vid_id)
                            if not isinstance(vod, dict):
                                continue
                            total_videos += 1
                            for tag in vod.get("typedTags", []):
                                name = tag.get("name", "")
                                value = tag.get("value", "").strip()
                                if not value:
                                    continue
                                if name == "Searchable Tags":
                                    all_tags[value] += 1
                                elif name == "Related Country":
                                    all_countries[value] += 1
                                elif name in ("Genre", "Featured Genre"):
                                    all_genres[value] += 1
                                elif name == "Sub-Genre":
                                    all_subgenres[value] += 1
                                elif name == "Format":
                                    all_formats[value] += 1
                                elif name in ("Host", "Featured Host"):
                                    all_hosts[value] += 1
                        except Exception:
                            continue
            except Exception:
                continue

        result = {
            "total_videos_scanned": total_videos,
            "page": page,
            "page_size": page_size,
            "top_searchable_tags": [
                {"keyword": tag, "frequency": count, "seo_priority": "high" if count >= 5 else "medium" if count >= 2 else "low"}
                for tag, count in all_tags.most_common(top_n)[(page - 1) * page_size : page * page_size]
            ],
            "top_countries": [{"country": c, "count": n} for c, n in all_countries.most_common(20)],
            "genres_distribution": [{"genre": g, "count": n} for g, n in all_genres.most_common()],
            "subgenres_distribution": [{"subgenre": sg, "count": n} for sg, n in all_subgenres.most_common(20)],
            "content_formats": [{"format": f, "count": n} for f, n in all_formats.most_common()],
            "top_hosts": [{"host": h, "count": n} for h, n in all_hosts.most_common(10)],
            "seo_insight": f"أعلى 3 كلمات مفتاحية: {', '.join([t for t, _ in all_tags.most_common(3)])}. أكثر الدول تغطيةً: {', '.join([c for c, _ in all_countries.most_common(3)])}"
        }
        return json.dumps(result, ensure_ascii=False, indent=2)
    except Exception as e:
        return json.dumps({"error": str(e)}, ensure_ascii=False)


@seo_tool(annotations=ToolAnnotations(title="Get Country Content Map (خريطة توزيع المحتوى جغرافياً)", readOnlyHint=True))
async def get_country_content_map(country: str = "", max_items: int = 20, page: int = 1, page_size: int = 10) -> str:
    """
    Map all content by Related Country from typedTags.
    Useful for geo-targeted SEO, international content strategy, and country-specific landing pages.
    
    Args:
        country: Filter by specific country name in Arabic (e.g. فلسطين, تركيا, فرنسا) — leave empty for all countries
        max_items: Items per section to scan (default: 20)
        page: Page number for returned countries (default: 1)
        page_size: Number of countries per page (default: 10)
    """
    try:
        country_map = {}  # country -> list of videos

        for section_id in list(SECTIONS.keys())[:8]:
            try:
                data = await client.get_section_content(section_id, items_per_bucket=max_items)
                buckets = data.get("buckets", []) if isinstance(data, dict) else []
                for bucket in buckets:
                    for item in bucket.get("contentList", []):
                        vid_id = item.get("id")
                        if not vid_id:
                            continue
                        try:
                            vod = await client.get_vod_details(vid_id)
                            if not isinstance(vod, dict):
                                continue
                            vid_countries = []
                            vid_genre = ""
                            vid_tags = []
                            for tag in vod.get("typedTags", []):
                                if tag.get("name") == "Related Country":
                                    vid_countries.append(tag.get("value", ""))
                                if tag.get("name") in ("Genre", "Featured Genre"):
                                    vid_genre = tag.get("value", "")
                                if tag.get("name") == "Searchable Tags":
                                    vid_tags.append(tag.get("value", ""))

                            if not vid_countries:
                                continue

                            video_entry = {
                                "id": vid_id,
                                "title": vod.get("title", ""),
                                "genre": vid_genre,
                                "tags": vid_tags[:5],
                                "duration": vod.get("duration", 0),
                                "publishedDate": vod.get("publishedDate", "")[:10],
                                "accessLevel": vod.get("accessLevel", "")
                            }

                            for c in vid_countries:
                                if not country or country.lower() in c.lower():
                                    country_map.setdefault(c, []).append(video_entry)
                        except Exception:
                            continue
            except Exception:
                continue

        if not country_map:
            return json.dumps({"error": f"No content found for country: {country or 'any'}"}, ensure_ascii=False)

        # Build summary with SEO page suggestions
        country_summary = []
        for c, vids in sorted(country_map.items(), key=lambda x: -len(x[1])):
            from collections import Counter
            all_tags = [t for v in vids for t in v.get("tags", [])]
            top_tags = [t for t, _ in Counter(all_tags).most_common(5)]
            country_summary.append({
                "country": c,
                "video_count": len(vids),
                "top_keywords": top_tags,
                "seo_page_title": f"محتوى عن {c} | الجزيرة 360",
                "seo_description": f"شاهد {len(vids)} فيديو ووثائقي عن {c} على الجزيرة 360 بجودة 4K Ultra HD.",
                "sample_videos": [v["title"] for v in vids[:5]]
            })

        # Paginate countries summary
        start_idx = (page - 1) * page_size
        end_idx = start_idx + page_size
        paginated_summary = country_summary[start_idx:end_idx]

        result = {
            "filter": country or "all countries",
            "page": page,
            "page_size": page_size,
            "total_countries": len(country_map),
            "total_videos_with_country": sum(len(v) for v in country_map.values()),
            "countries": paginated_summary
        }
        return json.dumps(result, ensure_ascii=False, indent=2)
    except Exception as e:
        return json.dumps({"error": str(e)}, ensure_ascii=False)


@seo_tool(annotations=ToolAnnotations(title="Generate Series Schema (توليد مخطط السلاسل والحلقات)", readOnlyHint=True))
async def generate_series_schema(series_id: int) -> str:
    """
    Generate complete TVSeries + TVEpisode JSON-LD Schema for a series.
    Uses episodeInformation from typedTags for rich structured data.
    This is the most powerful Schema type for video series in Google Search.
    
    Args:
        series_id: The series/show ID (get from get_video_details episodeInformation.seriesInformation.id)
    """
    try:
        # Get series info by browsing sections and finding episodes of this series
        episodes = []
        series_title = ""
        series_genres = set()
        series_hosts = set()
        series_countries = set()
        series_tags = []

        for section_id in list(SECTIONS.keys())[:10]:
            try:
                data = await client.get_section_content(section_id, items_per_bucket=20)
                buckets = data.get("buckets", []) if isinstance(data, dict) else []
                for bucket in buckets:
                    for item in bucket.get("contentList", []):
                        vid_id = item.get("id")
                        if not vid_id:
                            continue
                        try:
                            vod = await client.get_vod_details(vid_id)
                            if not isinstance(vod, dict):
                                continue
                            ep_info = vod.get("episodeInformation", {})
                            series_info = ep_info.get("seriesInformation", {})
                            if series_info.get("id") != series_id:
                                continue

                            series_title = series_info.get("title", series_title)

                            for tag in vod.get("typedTags", []):
                                if tag.get("name") in ("Genre", "Featured Genre"):
                                    series_genres.add(tag.get("value", ""))
                                if tag.get("name") in ("Host", "Featured Host"):
                                    series_hosts.add(tag.get("value", ""))
                                if tag.get("name") == "Related Country":
                                    series_countries.add(tag.get("value", ""))
                                if tag.get("name") == "Searchable Tags":
                                    series_tags.append(tag.get("value", ""))

                            episodes.append({
                                "id": vid_id,
                                "title": vod.get("title", ""),
                                "description": vod.get("description", ""),
                                "duration": vod.get("duration", 0),
                                "episodeNumber": ep_info.get("episodeNumber", ""),
                                "seasonNumber": ep_info.get("seasonNumber", ""),
                                "publishedDate": vod.get("publishedDate", "")[:10],
                                "thumbnail": vod.get("thumbnailUrl", ""),
                                "url": f"https://www.aljazeera360.com/video/{vid_id}"
                            })
                        except Exception:
                            continue
            except Exception:
                continue
            if len(episodes) >= 20:
                break

        if not episodes:
            return json.dumps({"error": f"No episodes found for series_id: {series_id}"}, ensure_ascii=False)

        # Sort episodes by episode number
        episodes.sort(key=lambda x: (x.get("seasonNumber", 0), x.get("episodeNumber", 0)))

        # Build TVSeries Schema
        def iso_duration(seconds):
            if not seconds:
                return "PT0S"
            m, s = divmod(int(seconds), 60)
            h, m = divmod(m, 60)
            return f"PT{h}H{m}M{s}S" if h else f"PT{m}M{s}S"

        tv_series_schema = {
            "@context": "https://schema.org",
            "@type": "TVSeries",
            "name": series_title,
            "url": f"https://www.aljazeera360.com/series/{series_id}",
            "description": f"مسلسل وثائقي {series_title} على الجزيرة 360",
            "genre": list(series_genres),
            "inLanguage": "ar",
            "producer": {"@type": "Organization", "name": "الجزيرة 360"},
            "actor": [{"@type": "Person", "name": h} for h in series_hosts],
            "numberOfEpisodes": len(episodes),
            "episode": [
                {
                    "@type": "TVEpisode",
                    "name": ep["title"],
                    "description": ep["description"][:200],
                    "episodeNumber": ep["episodeNumber"],
                    "partOfSeason": {"@type": "TVSeason", "seasonNumber": ep["seasonNumber"]},
                    "duration": iso_duration(ep["duration"]),
                    "datePublished": ep["publishedDate"],
                    "thumbnailUrl": ep["thumbnail"],
                    "url": ep["url"]
                }
                for ep in episodes[:10]  # first 10 episodes in schema
            ]
        }

        from collections import Counter
        top_tags = [t for t, _ in Counter(series_tags).most_common(8)]

        result = {
            "series_id": series_id,
            "series_title": series_title,
            "total_episodes_found": len(episodes),
            "genres": list(series_genres),
            "hosts": list(series_hosts),
            "countries_covered": list(series_countries),
            "top_keywords": top_tags,
            "seo_meta_title": f"{series_title} | الجزيرة 360",
            "seo_meta_description": f"شاهد جميع حلقات {series_title} على الجزيرة 360 — {len(episodes)} حلقة بجودة 4K.",
            "tv_series_schema": tv_series_schema,
            "schema_html": f'<script type="application/ld+json">\n{json.dumps(tv_series_schema, ensure_ascii=False, indent=2)}\n</script>',
            "episodes": episodes
        }
        return json.dumps(result, ensure_ascii=False, indent=2)
    except Exception as e:
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
# Custom Routes (Dashboard & Health — served on same port as MCP)
# ============================================================================

from starlette.requests import Request
from starlette.responses import HTMLResponse, JSONResponse



# ============================================================================
# Privacy Policy & Documentation Routes (For MCP Directory compliance)
# ============================================================================

PRIVACY_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Privacy Policy - Al Jazeera 360 MCP Server</title>
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; line-height: 1.6; color: #333; max-width: 800px; margin: 0 auto; padding: 40px 20px; }
        h1 { color: #005a9c; border-bottom: 2px solid #eee; padding-bottom: 10px; }
        h2 { color: #333; margin-top: 30px; }
        footer { margin-top: 50px; font-size: 0.85em; color: #777; border-top: 1px solid #eee; padding-top: 20px; }
    </style>
</head>
<body>
    <h1>Privacy Policy</h1>
    <p>Last updated: June 8, 2026</p>
    
    <p>This Privacy Policy describes how the <strong>Al Jazeera 360 MCP Server</strong> handles data. Our server is an open-source tool designed to connect AI assistants to the public catalog of Al Jazeera 360.</p>
    
    <h2>1. Data Collection and Processing</h2>
    <p>The Al Jazeera 360 MCP Server does not collect, store, or share any personal data or personally identifiable information (PII). All operations are performed programmatically to fetch public streaming metadata directly from Al Jazeera 360's public API endpoints.</p>
    
    <h2>2. Authentication and Security</h2>
    <p>Any API keys or tokens (such as <code>AJ360_REFRESH_TOKEN</code>) provided to this server are used strictly to authenticate requests with the official Al Jazeera 360 backend on behalf of the user. These tokens are stored securely in your environment variables and are never transmitted to any third party other than Al Jazeera 360.</p>
    
    <h2>3. Client-Side Analytics & Data Retention</h2>
    <p>The server includes a local, self-hosted analytics dashboard to monitor request rates and latency. This analytical data is stored entirely in memory within the running container and is completely cleared/deleted when the container restarts. No data is persisted long-term, and no analytics data is ever transmitted to external tracking services or third parties.</p>
    
    <h2>4. Contact Information</h2>
    <p>If you have any questions or concerns about this Privacy Policy or how data is handled by this server, please contact us via email at: <a href="mailto:support@aljazeera360.com">support@aljazeera360.com</a> or open an issue in our public GitHub repository.</p>

    <h2>5. Changes to This Policy</h2>
    <p>Since this is an open-source project, any future changes to this policy will be documented in our public GitHub repository. You are encouraged to review this policy periodically.</p>
    
    <footer>
        <p>&copy; 2026 Al Jazeera 360 MCP Server Contributors. This tool is independent and not officially affiliated with Al Jazeera Network.</p>
    </footer>
</body>
</html>
"""

DOCS_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Documentation - Al Jazeera 360 MCP Server</title>
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; line-height: 1.6; color: #333; max-width: 900px; margin: 0 auto; padding: 40px 20px; }
        h1 { color: #005a9c; border-bottom: 2px solid #eee; padding-bottom: 10px; }
        h2 { color: #005a9c; margin-top: 30px; border-bottom: 1px solid #eee; padding-bottom: 5px; }
        code { background: #f4f4f4; padding: 2px 6px; border-radius: 4px; font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace; font-size: 0.9em; }
        pre { background: #f4f4f4; padding: 15px; border-radius: 6px; overflow-x: auto; font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace; }
        ul { padding-left: 20px; }
        .badge { background: #e1f5fe; color: #0288d1; padding: 3px 8px; border-radius: 12px; font-size: 0.85em; font-weight: bold; }
    </style>
</head>
<body>
    <h1>Al Jazeera 360 MCP Server Documentation</h1>
    <p>Welcome to the documentation for the <strong>Al Jazeera 360 Model Context Protocol (MCP) Server</strong>. This server allows LLMs (such as Claude and ChatGPT) to explore, search, and analyze Al Jazeera 360's extensive catalog of Arabic streaming content, programs, and metadata.</p>
    
    <h2>Getting Started</h2>
    <p>To connect your AI assistant to this server, use the following configuration based on your transport mode:</p>
    
    <h3>1. Streamable HTTP Transport (Recommended)</h3>
    <p>Expose the server as a web service. This is ideal for cloud deployments (Railway, Render, etc.):</p>
    <pre>URL: https://your-deployed-mcp-server.com/mcp</pre>
    
    <h3>2. STDIO Transport (Local)</h3>
    <p>For local use with Claude Desktop or Cursor, add the following to your configuration file:</p>
    <pre>{
  "mcpServers": {
    "aljazeera360": {
      "command": "python3",
      "args": ["/path/to/server.py"],
      "env": {
        "AJ360_REFRESH_TOKEN": "your_optional_token"
      }
    }
  }
}</pre>

    <h2>Available Tools (24 Tools)</h2>
    <p>The server exposes 24 specialized tools for metadata discovery, SEO generation, and deep catalog analysis. Key tools include:</p>
    <ul>
        <li><code>get_trending_content</code>: Fetch the current trending carousel items.</li>
        <li><code>browse_section</code>: Browse a specific content section (e.g., AJA, AJD).</li>
        <li><code>get_video_details</code>: Retrieve full metadata for a specific video.</li>
        <li><code>generate_seo_content</code>: Generate optimized Arabic titles, descriptions, and keywords.</li>
        <li><code>generate_sitemap</code>: Generate Google Search Console-ready video XML sitemaps.</li>
        <li><code>audit_metadata_quality</code>: Audit catalog health, short descriptions, and missing thumbnails.</li>
    </ul>

    <h2>Compliance & Security</h2>
    <p>This server implements secure practices including:</p>
    <ul>
        <li><strong>Origin Validation:</strong> Rejects requests from unauthorized web origins to prevent cross-origin exploits.</li>
        <li><strong>Pagination:</strong> Protects the server from memory exhaustion by paginating large catalog responses.</li>
    </ul>
</body>
</html>
"""

@mcp.custom_route("/privacy", methods=["GET"])
async def privacy_page(request: Request):
    """Serve the Privacy Policy HTML."""
    return HTMLResponse(PRIVACY_HTML)

@mcp.custom_route("/docs", methods=["GET"])
async def docs_page(request: Request):
    """Serve the documentation HTML."""
    return HTMLResponse(DOCS_HTML)

# Origin Validation Middleware / Helper
def validate_origin(request: Request) -> bool:
    """Validate that the Origin header is authorized."""
    origin = request.headers.get("origin")
    if not origin:
        return True # Allow non-browser clients (like direct MCP clients)

    # Allowed origins: local development and official platforms
    allowed_origins = [
        "http://localhost",
        "http://127.0.0.1",
        "https://aljazeera360.com",
        "https://www.aljazeera360.com",
    ]
    # Check if origin matches or is a subdomain of allowed origins
    for allowed in allowed_origins:
        if origin.startswith(allowed):
            return True
    return False


# Optional shared secret for the analytics data endpoints. When set, callers
# must present it as `Authorization: Bearer <token>` or `?token=<token>`.
# Strongly recommended for any public (SSE/cloud) deployment, since the
# analytics endpoints expose request history and search terms.
DASHBOARD_TOKEN = os.environ.get("AJ360_DASHBOARD_TOKEN", "").strip()


def authorize_analytics(request: Request) -> Optional[JSONResponse]:
    """Guard the analytics data endpoints.

    Returns a JSONResponse to short-circuit with (403) when the request is not
    authorized, or None when it may proceed. Enforces origin validation and,
    when AJ360_DASHBOARD_TOKEN is set, a bearer/query token.
    """
    if not validate_origin(request):
        return JSONResponse({"error": "Unauthorized Origin"}, status_code=403)

    if DASHBOARD_TOKEN:
        provided = ""
        auth_header = request.headers.get("authorization", "")
        if auth_header.lower().startswith("bearer "):
            provided = auth_header[7:].strip()
        if not provided:
            provided = request.query_params.get("token", "").strip()
        if provided != DASHBOARD_TOKEN:
            return JSONResponse({"error": "Unauthorized"}, status_code=403)

    return None

@mcp.custom_route("/", methods=["GET"])
async def dashboard_root(request: Request):
    """Serve the Analytics Dashboard HTML at the root URL."""
    return HTMLResponse(DASHBOARD_HTML)


@mcp.custom_route("/dashboard", methods=["GET"])
async def dashboard_page(request: Request):
    """Serve the Analytics Dashboard HTML."""
    return HTMLResponse(DASHBOARD_HTML)


@mcp.custom_route("/api/stats", methods=["GET"])
async def api_stats(request: Request):
    """Return analytics stats as JSON."""
    denied = authorize_analytics(request)
    if denied is not None:
        return denied
    days = int(request.query_params.get("days", "7"))
    stats = tracker.get_stats(days=days)
    return JSONResponse(stats)


@mcp.custom_route("/api/recent", methods=["GET"])
async def api_recent(request: Request):
    """Return recent requests as JSON."""
    denied = authorize_analytics(request)
    if denied is not None:
        return denied
    limit = int(request.query_params.get("limit", "50"))
    recent = tracker.get_recent_requests(limit=limit)
    return JSONResponse(recent)


@mcp.custom_route("/api/health", methods=["GET"])
async def api_health(request: Request):
    """Health check endpoint for monitoring."""
    # Origin validation check
    if not validate_origin(request):
        return JSONResponse({"error": "Unauthorized Origin"}, status_code=403)

    return JSONResponse({
        "status": "ok",
        "server": "aljazeera360-mcp",
        "version": "2.0.0",
        "transport": _transport_mode,
        "privacy_policy": "/privacy",
        "documentation": "/docs",
        "dns_protection": mcp.settings.transport_security.enable_dns_rebinding_protection if mcp.settings.transport_security else False,
        "allowed_hosts": mcp.settings.transport_security.allowed_hosts if mcp.settings.transport_security else [],
    })


# ============================================================================
# Entry Point
# ============================================================================

def main():
    """Run the MCP server.
    
    Transport is determined by MCP_TRANSPORT env var:
    - "stdio" (default): For local MCP clients (Claude Desktop, Cursor, etc.)
    - "sse": For cloud deployment (Cloud Run, Render, Railway, etc.)
    
    Analytics dashboard is served on the same port as the MCP server via custom routes:
    - / and /dashboard → Analytics Dashboard HTML
    - /api/stats → Stats JSON
    - /api/recent → Recent requests JSON
    - /api/health → Health check
    - /sse → MCP SSE endpoint
    
    Optionally, a standalone dashboard can also run on a separate port (default: 9090).
    Disable with AJ360_ENABLE_DASHBOARD=false.
    """
    transport = os.environ.get("MCP_TRANSPORT", "streamable-http")
    
    # Optionally start standalone analytics dashboard on separate port
    if ENABLE_DASHBOARD and transport == "stdio":
        start_dashboard(DASHBOARD_PORT)
        logger.info(f"Analytics dashboard also running at http://localhost:{DASHBOARD_PORT}")
    
    if transport == "streamable-http":
        port = mcp.settings.port
        logger.info(f"Starting Al Jazeera 360 MCP Server (Streamable HTTP transport on port {port})")
        logger.info(f"Dashboard: http://0.0.0.0:{port}/")
        logger.info(f"MCP HTTP:  http://0.0.0.0:{port}/mcp")
        logger.info("DNS rebinding protection: ENABLED (allowed_hosts + allowed_origins configured)")
        mcp.run(transport="streamable-http")
    elif transport == "sse":
        port = mcp.settings.port
        logger.info(f"Starting Al Jazeera 360 MCP Server (SSE transport on port {port})")
        logger.info(f"Dashboard: http://0.0.0.0:{port}/")
        logger.info(f"MCP SSE:   http://0.0.0.0:{port}/sse")
        logger.info("DNS rebinding protection: ENABLED (allowed_hosts + allowed_origins configured)")
        mcp.run(transport="sse")
    else:
        logger.info("Starting Al Jazeera 360 MCP Server (stdio transport)")
        mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
