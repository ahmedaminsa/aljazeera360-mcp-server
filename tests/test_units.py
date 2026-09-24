"""Offline unit tests — no network, no credentials.

These run in CI on every push (unlike the test_*.py scripts in the repo root,
which are live-API integration scripts). They pin the input-validation and
safety behaviour of the server module.
"""

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("AJ360_API_KEY", "test-key")

import server  # noqa: E402


def test_bound_clamps_high():
    assert server._bound(5000, 1, 50, 20) == 50


def test_bound_clamps_low_and_zero():
    assert server._bound(-5, 1, 50, 20) == 1
    assert server._bound(0, 1, 1000, 1) == 1


def test_bound_non_numeric_falls_back_to_default():
    assert server._bound("lots", 1, 50, 20) == 20
    assert server._bound(None, 1, 50, 20) == 20


def test_bound_accepts_numeric_strings():
    assert server._bound("25", 1, 50, 20) == 25


def test_validate_section_known():
    assert server._validate_section("AJA") is None


def test_validate_section_unknown_returns_actionable_error():
    payload = json.loads(server._validate_section("NotASection"))
    assert "error" in payload
    assert payload["valid_section_ids"] == list(server.SECTIONS.keys())


def test_sections_catalog_has_15_entries():
    assert len(server.SECTIONS) == 15


def test_client_clamps_items_per_bucket():
    # The Dice API rejects rpp > 25 with 400 — the clamp must exist.
    assert server.AlJazeera360Client.MAX_ITEMS_PER_BUCKET == 25


def test_seo_tool_returns_function_unchanged_when_disabled():
    # Direct imports (snapshot script, tests) must work in both profiles.
    assert callable(server.audit_metadata_quality)


def test_default_profile_registers_10_tools():
    tools = server.mcp._tool_manager._tools
    assert len(tools) == 10 or os.environ.get("AJ360_ENABLE_SEO_TOOLS")


def test_dashboard_auth_denies_wrong_token():
    class QP(dict):
        def get(self, k, d=""):
            return dict.get(self, k, d)

    class Req:
        headers = {"authorization": "Bearer wrong"}
        query_params = QP()

    old = server.DASHBOARD_TOKEN
    try:
        server.DASHBOARD_TOKEN = "secret"
        resp = server.authorize_analytics(Req())
        assert resp is not None and resp.status_code == 403
    finally:
        server.DASHBOARD_TOKEN = old


# ---------------------------------------------------------------------------
# MCP Apps (interactive view)
# ---------------------------------------------------------------------------

import asyncio  # noqa: E402

import mcp_apps  # noqa: E402

UI_TOOLS = {
    "search_videos", "browse_section", "get_trending_content", "get_latest_episodes",
    "get_series_details", "get_season_episodes", "get_video_details", "play_video",
    "run_diagnostics",
}


def test_ui_tools_declare_the_view():
    tools = server.mcp._tool_manager._tools
    for name in UI_TOOLS:
        meta = tools[name].meta or {}
        assert meta.get("ui", {}).get("resourceUri") == mcp_apps.APP_URI, name
        assert meta.get("ui/resourceUri") == mcp_apps.APP_URI, name


def test_view_resource_is_registered_with_mcp_app_mime_and_csp():
    resources = asyncio.run(server.mcp.list_resources())
    view = [r for r in resources if str(r.uri) == mcp_apps.APP_URI]
    assert view, "ui:// resource missing"
    assert view[0].mimeType == "text/html;profile=mcp-app"
    csp = view[0].meta["ui"]["csp"]
    assert csp["frameDomains"] == ["https://www.aljazeera360.com"]
    assert "https://dve-images.imggaming.com" in csp["resourceDomains"]
    assert csp["connectDomains"] == []  # all data flows through tools/call


def test_view_html_speaks_the_mcp_apps_protocol():
    html = mcp_apps.APP_HTML
    for method in ("ui/initialize", "ui/notifications/initialized", "ui/notifications/tool-result",
                   "tools/call", "ui/open-link", "ui/notifications/size-changed"):
        assert method in html, method
    assert 'dir="rtl"' in html


def test_play_video_embeds_the_official_page():
    async def fake_details(vod_id):
        return {"id": vod_id, "title": "t", "accessLevel": "GRANTED_ON_SIGN_IN", "duration": 90,
                "episodeInformation": {"episodeNumber": 3, "seriesInformation": {"id": 2355, "title": "s"}}}

    old = server.client.get_vod_details
    try:
        server.client.get_vod_details = fake_details
        out = json.loads(asyncio.run(server.play_video(42)))
    finally:
        server.client.get_vod_details = old
    assert out["embed_url"] == "https://www.aljazeera360.com/video/42"
    assert out["requires_sign_in"] is True
    assert out["series_id"] == 2355 and out["series_title"] == "s"


def _search_payload(card_type, raw_id):
    return {"elements": [{"$type": "cardList", "attributes": {"cards": [{"attributes": {
        "content": [], "header": [],
        "action": {"data": {"id": raw_id, "type": card_type, "title": "x", "accessLevel": "GRANTED"}},
    }}]}}]}


def test_search_formats_live_channels_with_live_urls():
    out = server.format_search_results(_search_payload("LIVE_EVENT", "EVENT#284668"))
    assert out[0]["id"] == "284668"
    assert out[0]["watch_url"] == "https://www.aljazeera360.com/live/284668"


def test_search_retries_when_platform_returns_empty_layout():
    calls = []

    async def flaky(query, page_size=20):
        calls.append(query)
        return {"elements": []} if len(calls) == 1 else _search_payload("VOD", "VOD#7")

    old = server.client.search_content
    try:
        server.client.search_content = flaky
        # A one-letter query skips the section-browse fallback, so no network.
        out = json.loads(asyncio.run(server.search_videos("x", max_results=5)))
    finally:
        server.client.search_content = old
    assert len(calls) >= 2
    assert any(r["id"] == "7" for r in out["results"])


def test_view_uses_the_aljazeera360_design_system():
    html = mcp_apps.APP_HTML
    assert "AlJazeera-Regular.ttf" in html and "AlJazeera-Bold.ttf" in html
    assert "#00B7D4" in html            # platform primary colour
    assert "AJ_360_White_Logo" in html  # official logo
    domains = mcp_apps.RESOURCE_META["ui"]["csp"]["resourceDomains"]
    assert "https://static.diceplatform.com" in domains       # fonts
    assert "https://content-images.onvesper.com" in domains   # logo


def test_trending_heroes_carry_links_and_title_art():
    async def fake_home(items_per_bucket=12):
        return {"heroes": [{
            "title": "مع تميم", "description": "d", "imageUrl": "https://img/bg.jpg",
            "titleImage": "https://img/logo.png", "ctaText": "شاهد الآن",
            "link": {"event": {"type": "VOD", "id": 99, "title": "ep",
                               "episodeInformation": {"seriesInformation": {"id": 3920}}}},
        }], "buckets": []}

    old = server.client.get_home_content
    try:
        server.client.get_home_content = fake_home
        hero = json.loads(asyncio.run(server.get_trending_content()))["featured"][0]
    finally:
        server.client.get_home_content = old
    assert hero["video_id"] == 99 and hero["series_id"] == 3920
    assert hero["title_image"] == "https://img/logo.png"
    assert hero["cta_text"] == "شاهد الآن"


def test_diagnostics_tool_opens_the_view_and_accepts_reports():
    opened = json.loads(asyncio.run(server.run_diagnostics()))
    assert opened["diagnostics"] is True
    ack = json.loads(asyncio.run(server.run_diagnostics(report="player vid=1;drm=no;frame=skipped")))
    assert ack == {"received": True}
