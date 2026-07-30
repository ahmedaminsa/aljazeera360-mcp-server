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


def test_default_profile_registers_8_tools():
    tools = server.mcp._tool_manager._tools
    assert len(tools) == 8 or os.environ.get("AJ360_ENABLE_SEO_TOOLS")


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
