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


def test_default_profile_registers_14_tools():
    tools = server.mcp._tool_manager._tools
    assert len(tools) == 14 or os.environ.get("AJ360_ENABLE_SEO_TOOLS")


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


# ---------------------------------------------------------------------------
# Video understanding (video_intel.py) — offline
# ---------------------------------------------------------------------------

import io as _io  # noqa: E402
import struct as _struct  # noqa: E402
import wave as _wave  # noqa: E402

import video_intel  # noqa: E402


def _fake_bif(n=6, interval_ms=15000):
    from PIL import Image as PILImage
    jpegs = []
    for i in range(n):
        b = _io.BytesIO()
        PILImage.new("RGB", (320, 180), (i * 40, 0, 0)).save(b, format="JPEG")
        jpegs.append(b.getvalue())
    header = video_intel.BIF_MAGIC + _struct.pack("<III", 0, n, interval_ms) + b"\0" * 44
    offset = 64 + (n + 1) * 8
    index, offs = b"", offset
    for i, j in enumerate(jpegs):
        index += _struct.pack("<II", i, offs)
        offs += len(j)
    index += _struct.pack("<II", 0xFFFFFFFF, offs)
    return header + index + b"".join(jpegs)


def test_bif_parsing_and_contact_sheet():
    interval, frames = video_intel.parse_bif(_fake_bif())
    assert interval == 15 and [t for t, _ in frames] == [0, 15, 30, 45, 60, 75]
    picked = video_intel.pick_frames(frames, 30, 60, 10)
    assert [t for t, _ in picked] == [30, 45, 60]
    sheet = video_intel.contact_sheet(picked)
    assert sheet[:2] == b"\xff\xd8"  # JPEG


def test_arabic_normalisation_and_timestamps():
    assert video_intel.normalize("الذكاءُ الإصطناعيّ") == video_intel.normalize("الذكاء الاصطناعي")
    assert video_intel.parse_ts("14:30") == 870 and video_intel.parse_ts("1:02:03") == 3723
    assert video_intel.fmt_ts(870) == "14:30"


def test_whisper_hallucinations_are_filtered():
    assert video_intel.is_hallucination("اشتركوا في القناة")
    assert video_intel.is_hallucination("شكراً للمشاهدة!")
    assert not video_intel.is_hallucination("ايوه الأحرار")


def test_local_index_roundtrip(tmp_path, monkeypatch):
    monkeypatch.setattr(video_intel, "LOCAL_DB", str(tmp_path / "idx.db"))
    idx = video_intel.VideoIndex()
    idx.remote = False
    analysis = {"summary": "s", "chapters": [{"start": "04:30", "title": "تقرير"}],
                "people": [{"name": "نيت سواريس", "role": "باحث", "first_seen": "21:15"}],
                "topics": ["الذكاء الاصطناعي"]}
    moments = video_intel.moments_from_analysis(analysis)
    video = {"id": 7, "title": "t", "series": None, "duration": 100, "watch_url": "u"}
    asyncio.run(idx.save(video, analysis, ["chapter", "person", "topic"], moments))
    found = asyncio.run(idx.search("سواريس", "person", 10))["results"]
    assert found and found[0]["t_sec"] == 1275
    assert asyncio.run(idx.get(None))["videos"][0]["video_id"] == 7


def test_audio_is_decoded_into_timed_chunks(tmp_path):
    path = tmp_path / "a.wav"
    with _wave.open(str(path), "wb") as w:
        w.setnchannels(2)
        w.setsampwidth(2)
        w.setframerate(44100)
        w.writeframes(b"\0\0\0\0" * 44100 * 65)
    chunks = video_intel.decode_to_chunks(str(path), 0, None)
    assert [o for o, _ in chunks] == [0, 30, 60]
    assert video_intel.decode_to_chunks(str(path), 30, 60)[0][0] == 30


def test_read_only_video_tools_are_public_and_writers_are_team_only():
    public = set(server.mcp._tool_manager._tools)
    assert {"watch_video", "search_video_index", "get_video_analysis", "get_transcript"} <= public
    writers = {"save_video_analysis", "transcribe_audio", "listen_to_video"}
    assert not (writers & public) or os.environ.get("AJ360_ENABLE_SEO_TOOLS")


MASTER = """#EXTM3U
#EXT-X-MEDIA:TYPE=AUDIO,GROUP-ID="audio-hi",URI="audio/hi/index.m3u8?t=1"
#EXT-X-MEDIA:TYPE=AUDIO,GROUP-ID="audio-lo",DEFAULT=YES,URI="audio/lo/index.m3u8?t=1"
#EXT-X-STREAM-INF:BANDWIDTH=9000000,AUDIO="audio-hi"
video/hi.m3u8
#EXT-X-STREAM-INF:BANDWIDTH=800000,AUDIO="audio-lo"
video/lo.m3u8
"""

AUDIO = """#EXTM3U
#EXT-X-MAP:URI="init.mp4?t=1",BYTERANGE="1285@0"
#EXTINF:6.0,
#EXT-X-BYTERANGE:1000@1285
init.mp4?t=1
#EXTINF:6.0,
#EXT-X-BYTERANGE:1100
init.mp4?t=1
#EXTINF:6.0,
#EXT-X-BYTERANGE:900
init.mp4?t=1
"""


def test_hls_audio_rendition_and_byte_ranges():
    url = video_intel.pick_audio_playlist(MASTER, "https://cdn/x/master.m3u8?t=1")
    assert url == "https://cdn/x/audio/lo/index.m3u8?t=1"
    pl = video_intel.parse_media_playlist(AUDIO)
    assert not pl["encrypted"] and pl["map"] == ("init.mp4?t=1", 1285, 0)
    assert [(s[0], s[3], s[4]) for s in pl["segments"]] == [(0.0, 1000, 1285), (6.0, 1100, 2285), (12.0, 900, 3385)]


def test_encrypted_audio_is_detected():
    pl = video_intel.parse_media_playlist('#EXTM3U\n#EXT-X-KEY:METHOD=SAMPLE-AES,URI="skd://k"\n#EXTINF:6,\na.ts\n')
    assert pl["encrypted"]


VTT = """WEBVTT

00:08.220 --> 00:11.521 align:center
أكثرية الإسرائيليين
<i>كانوا يدعمون</i> اجتياح غزة

1:02:03.000 --> 1:02:05.500
الجملة الأخيرة
"""

SRT = """1
00:00:01,000 --> 00:00:02,500
مرحبا

2
00:00:03,000 --> 00:00:04,000
{\\an8}بكم
"""


def test_subtitles_are_parsed_from_vtt_and_srt():
    cues = video_intel.parse_subtitles(VTT)
    assert cues[0] == {"start": 8.22, "end": 11.521, "text": "أكثرية الإسرائيليين كانوا يدعمون اجتياح غزة"}
    assert cues[1]["start"] == 3723.0
    assert [c["text"] for c in video_intel.parse_subtitles(SRT)] == ["مرحبا", "بكم"]


def test_subtitle_track_prefers_language_then_readable_format():
    tracks = [{"format": "scc", "language": "ar", "url": "a.scc"},
              {"format": "srt", "language": "ar", "url": "a.srt"},
              {"format": "vtt", "language": "en", "url": "e.vtt"},
              {"format": "vtt", "language": "ar", "url": "a.vtt"}]
    assert video_intel.pick_subtitle(tracks, "ar")["url"] == "a.vtt"
    assert video_intel.pick_subtitle(tracks, "fr")["url"] in ("e.vtt", "a.vtt")
    assert video_intel.pick_subtitle([{"format": "scc", "language": "ar", "url": "x"}], "ar") is None


def test_transcript_renders_srt():
    cues = [{"start": 1.0, "end": 2.5, "text": "مرحبا"}]
    assert server._render_cues(cues, "srt") == "1\n00:00:01,000 --> 00:00:02,500\nمرحبا"
    assert server._render_cues(cues, "text") == "[00:01] مرحبا"


# -- Studio: ad breaks, social pack, clips ------------------------------------
import studio  # noqa: E402


def _cues():
    words = lambda t, text: [[t + i * 0.4, t + i * 0.4 + 0.35, w] for i, w in enumerate(text.split())]  # noqa: E731
    lines = [(10, "مرحبا بكم في حلقة اليوم عن السفر والطيران."),
             (200, "تحدثنا عن السياحة في المنطقة وأسعار الفنادق."),
             (400, "ثم انتقلنا إلى الحرب والقصف وسقوط الضحايا."),
             (620, "وفي الختام نتحدث عن التكنولوجيا والذكاء الاصطناعي لأول مرة في تاريخ البرنامج.")]
    return [{"start": t, "end": t + 5, "text": x, "words": words(t, x)} for t, x in lines]


def test_word_timings_give_the_exact_second_of_a_phrase():
    w = [[12.0, 12.3, "ثم"], [12.3, 12.9, "والسفر"], [12.9, 13.4, "بالطائرة"]]
    assert video_intel.exact_time(w, "السفر") == 12.3
    assert video_intel.exact_time(w, "السفر بالطائرة") == 12.3
    assert video_intel.exact_time(w, "القطار") is None


def test_transcript_saves_only_replace_their_own_range(tmp_path, monkeypatch):
    monkeypatch.setattr(video_intel, "LOCAL_DB", str(tmp_path / "i.db"))
    idx = video_intel.VideoIndex()
    idx.remote = False
    m = lambda t, x: {"t_sec": t, "kind": "transcript", "text": x, "norm": x, "words": [[t, t + 1, x]]}  # noqa: E731
    asyncio.run(idx.save({"id": 5}, {}, ["transcript"], [m(10, "a"), m(3000, "b")], span=[0, 3600]))
    asyncio.run(idx.save({"id": 5}, {}, ["transcript"], [m(3700, "c")], span=[3600, 7200]))
    got = asyncio.run(idx.get(5, words=True))["moments"]
    assert [x["text"] for x in got] == ["a", "b", "c"] and got[0]["words"] == [[10, 11, "a"]]


def test_classify_flags_sensitive_content_and_categories():
    assert studio.classify("رحلة سفر وحجز فندق")["categories"][0] == "travel"
    c = studio.classify("القصف وسقوط الضحايا")
    assert c["brand_safety"] == "sensitive" and c["sensitive_terms"]


def test_ad_breaks_sit_in_pauses_spaced_apart_with_safety():
    tl = studio.speech_timeline(_cues())
    br = studio.ad_breaks(900, tl, [(205, 0.9), (410, 0.8)], [400], min_gap_minutes=3)
    times = [b["at_sec"] for b in br]
    assert times and all(180 <= t <= 840 for t in times)
    assert all(b - a >= 180 for a, b in zip(times, times[1:]))
    assert any(b["brand_safety"] == "sensitive" for b in br)
    placements = studio.keyword_placements(["السياحة"], _cues(), br)
    assert placements[0]["said_at_sec"] == 200.8
    assert studio.cue_sheet(br).startswith("break,time,seconds")


def test_ad_breaks_without_transcript_use_scene_changes():
    br = studio.ad_breaks(1200, [], [(300, 0.9), (320, 0.1), (800, 0.7)], [], min_gap_minutes=5)
    assert [b["at_sec"] for b in br] == [300.0, 800.0]


def test_social_pack_quotes_clips_and_hashtags():
    q = studio.quote_candidates(_cues(), 3)
    assert q and all(x["out_sec"] > x["in_sec"] for x in q)
    assert "لأول مرة" in q[-1]["text"]
    assert studio.clip_moments(q, _cues())[0]["seconds"] <= 60
    tags = studio.hashtags("السلاح المسعور", "ثمن الحرب", _cues())
    assert tags[0] == "#ثمن_الحرب" and "#الجزيرة_360" in tags


def test_video_variant_is_chosen_by_height():
    master = ("#EXTM3U\n#EXT-X-STREAM-INF:BANDWIDTH=5000000,RESOLUTION=1920x1080\nv1080.m3u8\n"
              "#EXT-X-STREAM-INF:BANDWIDTH=2500000,RESOLUTION=1280x720\nv720.m3u8\n"
              "#EXT-X-STREAM-INF:BANDWIDTH=800000,RESOLUTION=640x360\nv360.m3u8\n")
    assert studio.pick_video_playlist(master, "https://x/m.m3u8", 720) == "https://x/v720.m3u8"
    assert studio.pick_video_playlist(master, "https://x/m.m3u8", 100) == "https://x/v360.m3u8"


def test_studio_tools_are_team_only():
    public = set(server.mcp._tool_manager._tools)
    assert not ({"suggest_ad_breaks", "get_social_pack", "make_clip"} & public) or os.environ.get("AJ360_ENABLE_SEO_TOOLS")


def test_download_links_only_on_the_team_endpoint(monkeypatch):
    monkeypatch.setattr(server, "STUDIO_URL", "")
    assert server._downloads(7) is None
    monkeypatch.setattr(server, "STUDIO_URL", "https://h/team/t/studio")
    d = server._downloads(7, ads=True)
    assert d["srt"] == "https://h/team/t/studio/7.srt" and d["ad_breaks_csv"].endswith("7-ads.csv")


# -- Translation, chapters, guests, name review --------------------------------
def test_model_json_is_parsed_from_fenced_or_chatty_replies():
    assert studio.parse_json('```json\n{"a": "x \\" }", "b": [1]}\n```') == {"a": 'x " }', "b": [1]}
    assert studio.parse_json("Sure! {\"lines\": [\"hi\"]} hope it helps") == {"lines": ["hi"]}
    assert studio.parse_json("no json") == {}


def test_windows_merge_people_fixes_and_spaced_chapters():
    parts = [
        {"people": [{"name": "الدكتور جيرالد بول", "role": "عالم", "type": "mentioned", "first_at": "14:40"}],
         "name_fixes": [{"heard": "مردخايف عنونه", "correct": "مردخاي فعنونو", "at": "19:36"}],
         "chapters": [{"start": "00:30", "title": "البداية"}, {"start": "01:10", "title": "قريب جدًا"},
                      {"start": "07:00", "title": "مشبك الورق"}]},
        {"people": [{"name": "جيرالد بول", "name_en": "Gerald Bull", "type": "guest", "first_at": "12:00"}],
         "name_fixes": [{"heard": "مردخايف عنونه", "correct": "x"}, {"heard": "بول", "correct": "بول"}],
         "chapters": [{"start": "24:50", "title": "آخر ثواني"}]},
    ]
    m = studio.merge_analysis(parts, 1500)
    assert len(m["people"]) == 1
    p = m["people"][0]
    assert p["type"] == "guest" and p["first_at"] == "12:00" and p["name_en"] == "Gerald Bull" and p["role"] == "عالم"
    assert [f["correct"] for f in m["name_fixes"]] == ["مردخاي فعنونو"]
    assert [(c["start"], c["title"]) for c in m["chapters"]] == [("00:00", "البداية"), ("07:00", "مشبك الورق")]


def test_name_fixes_rewrite_text_and_word_timings():
    cues = [{"start": 1, "end": 3, "text": "قصة مردخايف عنونه بدأت",
             "words": [[1, 1.4, "قصة"], [1.4, 2.0, "مردخايف"], [2.0, 2.5, "عنونه"], [2.5, 3, "بدأت"]]}]
    out, n = studio.apply_fixes(cues, [{"heard": "مردخايف عنونه", "correct": "مردخاي فعنونو"}])
    assert n == 1 and out[0]["text"] == "قصة مردخاي فعنونو بدأت"
    assert out[0]["words"] == [[1, 1.4, "قصة"], [1.4, 2.5, "مردخاي فعنونو"], [2.5, 3, "بدأت"]]


def test_translation_keeps_timing_and_falls_back_per_batch(monkeypatch):
    async def fake_llm(client, system, user, max_tokens=3000):
        n = len(user.splitlines())
        return json.dumps({"lines": [f"line {i}" for i in range(n)]}) if "bad" not in user else "{}"
    monkeypatch.setattr(studio, "llm", fake_llm)
    monkeypatch.setattr(studio, "TRANSLATE_BATCH", 2)
    cues = [{"start": i, "end": i + 1, "text": t} for i, t in enumerate(["أ", "ب", "bad", "د"])]
    out = asyncio.run(studio.translate_cues(cues, "en"))
    assert [c["start"] for c in out] == [0, 1, 2, 3]
    assert out[0]["text"] == "line 0" and out[0]["translated"]
    assert out[2]["text"] == "bad" and not out[2]["translated"]


def test_people_search_lists_everyone_with_empty_query(tmp_path, monkeypatch):
    monkeypatch.setattr(video_intel, "LOCAL_DB", str(tmp_path / "p.db"))
    idx = video_intel.VideoIndex()
    idx.remote = False
    rows = [{"t_sec": 5, "kind": "guest", "text": "جيرالد بول — عالم", "norm": "جيرالد بول — عالم"},
            {"t_sec": 9, "kind": "transcript", "text": "كلام", "norm": "كلام"}]
    asyncio.run(idx.save({"id": 3, "title": "t"}, {}, ["guest", "transcript"], rows))
    got = asyncio.run(idx.search("", "people", 50))["results"]
    assert [r["kind"] for r in got] == ["guest"]
