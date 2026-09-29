"""
Studio: turning an understood episode into work for the ad and social teams.

- Ad breaks: natural pause points (word timings), scene changes (preview frames)
  and chapter boundaries, each with a rough ad category and a brand-safety flag.
- Social pack: quotable lines, clip-ready moments and hashtag candidates.
- Clips: cut a time range of an unencrypted episode into an MP4 (stream copy).

Everything here is deterministic and cheap. The categories and quotes are a
first pass from keyword lists; the assistant reading the result refines them.
"""
from __future__ import annotations

import io
import os
import re
import tempfile
from collections import Counter
from typing import Optional

import httpx

from video_intel import (ProtectedAudio, _attrs, fmt_ts, normalize, parse_media_playlist,
                         pick_audio_playlist)

# ----------------------------------------------------------------------------
# Keyword lists (Arabic + English, matched on normalised text, as word stems)
# ----------------------------------------------------------------------------
AD_CATEGORIES = {
    "travel": ["سفر", "رحله", "طيران", "مطار", "فندق", "سياحه", "سياح", "عطله", "travel", "flight", "hotel"],
    "food": ["طعام", "اكل", "مطعم", "طبخ", "وجبه", "مطبخ", "قهوه", "شاي", "food", "restaurant", "coffee"],
    "technology": ["تكنولوجيا", "تقنيه", "هاتف", "ذكاء اصطناعي", "انترنت", "تطبيق", "رقمي", "حاسوب", "كمبيوتر",
                   "برمجه", "technology", "phone", "app", "ai"],
    "automotive": ["سياره", "سيارات", "محرك", "قياده", "car", "cars"],
    "finance": ["اقتصاد", "بنك", "بنوك", "استثمار", "اسهم", "بورصه", "عمله", "دولار", "ذهب", "تمويل", "ضرائب",
                "economy", "bank", "invest"],
    "health": ["صحه", "طبيب", "اطباء", "مستشفي", "علاج", "دواء", "رياضه بدنيه", "تغذيه", "health", "doctor"],
    "sports": ["كره القدم", "مباراه", "رياضه", "منتخب", "دوري", "بطوله", "لاعب", "football", "match"],
    "education": ["تعليم", "جامعه", "مدرسه", "طلاب", "طالب", "دراسه", "education", "university"],
    "real_estate": ["عقار", "عقارات", "سكن", "شقه", "بناء", "real estate"],
    "energy": ["نفط", "طاقه", "غاز", "كهرباء", "شمسيه", "energy", "oil"],
    "family_lifestyle": ["اسره", "اطفال", "زواج", "امهات", "منزل", "family", "kids"],
    "culture": ["ثقافه", "فن", "فنون", "كتاب", "روايه", "شعر", "موسيقي", "سينما", "تاريخ", "culture", "art"],
    "religion_ramadan": ["رمضان", "عيد", "حج", "عمره", "صلاه", "مسجد", "ramadan", "eid"],
}

# Terms that make the surrounding minute unsafe for most brands.
SENSITIVE = ["حرب", "قتل", "قتلي", "قصف", "شهيد", "شهداء", "دماء", "دم ", "جثث", "جثه", "انفجار", "اغتيال",
             "تعذيب", "اغتصاب", "ارهاب", "مجزره", "مجازر", "اباده", "اسري", "غاره", "غارات", "صاروخ", "صواريخ",
             "جرحي", "ضحايا", "اعدام", "مخدرات", "انتحار", "war", "killed", "bomb", "massacre", "genocide"]

_CAT_NORM = {c: [normalize(w) for w in ws] for c, ws in AD_CATEGORIES.items()}
_SENS_NORM = [normalize(w) for w in SENSITIVE]

STOPWORDS = {normalize(w) for w in (
    "في من علي الي إلى عن مع هذا هذه ذلك تلك التي الذي الذين هو هي هم نحن انا أنت انت كان كانت يكون لا لم لن ما "
    "و او أو ثم قد كل بعض لكن لكن بين حتى عند بعد قبل هناك هنا اذا إذا أن ان إن كما ايضا أيضا يعني يا اللي ده دي "
    "كده مش عشان جدا شيء فيه فيها منه منها عليه عليها لها له لهم به بها the a an of to in and is are was that this "
    "for it on with as be مرحبا بكم حلقه حلقتنا اليوم برنامج مشاهدينا الكرام سيداتي سادتي نعم طيب الان الآن "
    "هذه هذا الذي كيف لماذا ماذا متى اين هل".split())}


def _hits(text_norm: str, stems: list[str]) -> list[str]:
    return [s for s in stems if s and s in text_norm]


def classify(text: str) -> dict:
    """{'categories': [...], 'brand_safety': 'safe'|'sensitive', 'sensitive_terms': [...]}."""
    t = f" {normalize(text)} "
    scored = sorted(((len(_hits(t, stems)), c) for c, stems in _CAT_NORM.items()), reverse=True)
    cats = [c for n, c in scored if n][:3]
    sens = sorted({s.strip() for s in _hits(t, _SENS_NORM)})
    return {"categories": cats, "brand_safety": "sensitive" if sens else "safe", "sensitive_terms": sens[:6]}


# ----------------------------------------------------------------------------
# Signals
# ----------------------------------------------------------------------------
def scene_changes(frames: list[tuple[int, bytes]]) -> list[tuple[int, float]]:
    """[(timestamp, 0..1)] visual change between each preview frame and the one before."""
    from PIL import Image

    out, prev = [], None
    for ts, jpeg in frames:
        try:
            img = Image.open(io.BytesIO(jpeg)).convert("L").resize((32, 18))
        except Exception:
            prev = None
            continue
        px = list(img.getdata())
        if prev is not None:
            out.append((ts, min(1.0, sum(abs(a - b) for a, b in zip(px, prev)) / len(px) / 64)))
        prev = px
    return out


def speech_timeline(cues: list[dict]) -> list[tuple[float, float, str]]:
    """Flatten transcript cues into [(start, end, word_or_text)], using word timings when present."""
    items = []
    for c in cues:
        if c.get("words"):
            items += [(float(w[0]), float(w[1]), w[2]) for w in c["words"]]
        else:
            items.append((float(c["start"]), float(c["end"]), c["text"]))
    return sorted(items)


def pauses(timeline: list[tuple[float, float, str]], min_gap: float = 0.6) -> list[tuple[float, float]]:
    """[(time, gap_seconds)] silences between consecutive words/lines.

    The break time is just after the last word (at most half a second into the
    silence), so the ad follows the sentence it closes.
    """
    out = []
    for (s1, e1, _), (s2, _, _) in zip(timeline, timeline[1:]):
        gap = s2 - e1
        if gap >= min_gap:
            out.append((round(e1 + min(gap / 2, 0.5), 2), round(gap, 2)))
    return out


def text_between(timeline, start: float, end: float) -> str:
    return " ".join(t for s, e, t in timeline if e > start and s < end).strip()


# ----------------------------------------------------------------------------
# Ad breaks
# ----------------------------------------------------------------------------
def ad_breaks(duration: float, timeline, scenes, chapters: list[int], *, count: Optional[int] = None,
              min_gap_minutes: float = 7, first_after_minutes: float = 3, last_before_minutes: float = 1,
              context_seconds: int = 45) -> list[dict]:
    """Choose ad-break points: silences, near a scene change or chapter start, spaced apart."""
    lo, hi = first_after_minutes * 60, duration - last_before_minutes * 60
    cands = []
    if timeline:
        for t, gap in pauses(timeline):
            if lo <= t <= hi:
                cands.append({"t": t, "pause": gap})
    else:  # no transcript: scene changes are all we have
        cands = [{"t": float(ts), "pause": None} for ts, sc in scenes if lo <= ts <= hi and sc >= 0.25]
    for c in cands:
        scene = max((sc for ts, sc in scenes if abs(ts - c["t"]) <= 8), default=0.0)
        chapter = any(abs(ch - c["t"]) <= 15 for ch in chapters)
        c["scene_change"] = round(scene, 2)
        c["chapter_boundary"] = chapter
        c["score"] = round((min(c["pause"] / 2, 1) * 0.55 if c["pause"] else 0.3)
                           + scene * 0.3 + (0.15 if chapter else 0), 3)
    cands.sort(key=lambda c: -c["score"])
    gap = min_gap_minutes * 60
    limit = count or max(1, int((hi - lo) // gap) + 1) if hi > lo else 0
    chosen = []
    for c in cands:
        if len(chosen) >= limit:
            break
        if all(abs(c["t"] - o["t"]) >= gap for o in chosen):
            chosen.append(c)
    chosen.sort(key=lambda c: c["t"])
    out = []
    for i, c in enumerate(chosen, 1):
        before = text_between(timeline, c["t"] - context_seconds, c["t"]) if timeline else ""
        after = text_between(timeline, c["t"], c["t"] + context_seconds) if timeline else ""
        wide = text_between(timeline, c["t"] - 60, c["t"] + 60) if timeline else ""
        cls = classify(wide)
        out.append({"break": i, "at": fmt_ts(c["t"]), "at_sec": round(c["t"], 2),
                    "pause_sec": c["pause"], "scene_change": c["scene_change"],
                    "chapter_boundary": c["chapter_boundary"], "confidence": min(1.0, c["score"]),
                    "categories": cls["categories"], "brand_safety": cls["brand_safety"],
                    "sensitive_terms": cls["sensitive_terms"],
                    "before": before[-300:], "after": after[:300]})
    return out


def keyword_placements(keywords: list[str], cues: list[dict], breaks: list[dict], window: int = 300) -> list[dict]:
    """For advertiser keywords: where each is said, and the first ad break after it (within `window` s)."""
    out = []
    for kw in keywords:
        k = normalize(kw)
        if not k:
            continue
        for c in cues:
            if k not in normalize(c["text"]):
                continue
            t = float(c["start"])
            for w in c.get("words") or []:
                if k.split()[0] in normalize(w[2]):
                    t = float(w[0])
                    break
            nxt = next((b for b in breaks if 0 <= b["at_sec"] - t <= window), None)
            out.append({"keyword": kw, "said_at": fmt_ts(t), "said_at_sec": round(t, 2), "line": c["text"],
                        "next_break": nxt["at"] if nxt else None,
                        "next_break_brand_safety": nxt["brand_safety"] if nxt else None})
    return out


def cue_sheet(breaks: list[dict]) -> str:
    """CSV the ad-ops team can paste: time, seconds, categories, brand safety."""
    rows = ["break,time,seconds,categories,brand_safety"]
    for b in breaks:
        rows.append(f'{b["break"]},{b["at"]},{b["at_sec"]},"{" ".join(b["categories"])}",{b["brand_safety"]}')
    return "\n".join(rows)


# ----------------------------------------------------------------------------
# Social pack
# ----------------------------------------------------------------------------
_STRONG = [normalize(w) for w in (
    "اول مره", "لاول مره", "اكبر", "اخطر", "اهم", "الحقيقه", "السر", "لم يكن", "لن ", "ابدا", "مستحيل",
    "اعترف", "حذر", "كشف", "صدم", "مليون", "مليار", "بالمئه", "٪", "%")]


def sentences(cues: list[dict], max_words: int = 40) -> list[dict]:
    """Merge transcript lines into sentences (ending at . ؟ ! or a pause), with in/out times."""
    out, cur = [], None
    for c in cues:
        if cur and (float(c["start"]) - cur["end"] > 1.2 or len(cur["text"].split()) >= max_words):
            out.append(cur)
            cur = None
        if cur is None:
            cur = {"start": float(c["start"]), "end": float(c["end"]), "text": c["text"]}
        else:
            cur["end"] = float(c["end"])
            cur["text"] += " " + c["text"]
        if re.search(r"[.!؟?]$", c["text"].strip()):
            out.append(cur)
            cur = None
    if cur:
        out.append(cur)
    return out


def quote_candidates(cues: list[dict], limit: int = 8, skip_first: int = 45) -> list[dict]:
    scored = []
    for s in sentences(cues):
        n = len(s["text"].split())
        if s["start"] < skip_first or not 8 <= n <= 40:
            continue
        t = normalize(s["text"])
        score = sum(1 for w in _STRONG if w in t) * 2 + bool(re.search(r"\d", s["text"])) + (1 if 12 <= n <= 28 else 0)
        scored.append((score, s))
    scored.sort(key=lambda x: -x[0])
    picked = sorted((s for _, s in scored[:limit]), key=lambda s: s["start"])
    return [{"in": fmt_ts(max(0, s["start"] - 0.3)), "out": fmt_ts(s["end"] + 0.5),
             "in_sec": round(max(0, s["start"] - 0.3), 1), "out_sec": round(s["end"] + 0.5, 1),
             "text": s["text"]} for s in picked]


def clip_moments(quotes: list[dict], cues: list[dict], length: int = 45, limit: int = 5) -> list[dict]:
    """30–60 s windows around the strongest quotes, ending on a sentence boundary."""
    sents = sentences(cues)
    out = []
    for q in quotes[:limit]:
        start = q["in_sec"]
        end = next((s["end"] + 0.5 for s in sents if s["end"] >= start + length - 15), start + length)
        end = min(end, start + 60)
        out.append({"in": fmt_ts(start), "out": fmt_ts(end), "in_sec": start, "out_sec": round(end, 1),
                    "seconds": round(end - start), "hook": q["text"][:140]})
    return out


def hashtags(title: str, series: Optional[str], cues: list[dict], limit: int = 8) -> list[str]:
    def tag(s: str) -> str:
        return "#" + re.sub(r"[^\w]+", "_", s.strip()).strip("_")
    tags = [tag(x) for x in (series, title) if x and len(x) <= 30] + ["#الجزيرة_360"]
    words = Counter()
    for c in cues:
        for w in re.findall(r"[\w]+", c["text"]):
            nw = normalize(w)
            if len(nw) >= 4 and nw not in STOPWORDS and not nw.isdigit():
                words[w] += 1
    tags += [tag(w) for w, _ in words.most_common(limit * 2)]
    seen, out = set(), []
    for t in tags:
        if t not in seen and len(t) > 2:
            seen.add(t)
            out.append(t)
    return out[: limit + 2]


# ----------------------------------------------------------------------------
# Clips
# ----------------------------------------------------------------------------
MAX_CLIP_SECONDS = 180


def pick_video_playlist(master: str, master_url: str, max_height: int) -> str:
    from urllib.parse import urljoin
    lines = master.splitlines()
    variants = []
    for i, line in enumerate(lines):
        if line.startswith("#EXT-X-STREAM-INF") and i + 1 < len(lines):
            a = _attrs(line)
            h = int((a.get("RESOLUTION", "0x0").split("x") + ["0"])[1] or 0)
            variants.append((h, int(a.get("BANDWIDTH", "0") or 0), lines[i + 1]))
    if not variants:
        raise ValueError("no video variants in this stream")
    fit = [v for v in variants if v[0] <= max_height] or [min(variants)]
    return urljoin(master_url, max(fit)[2])


async def _download_range(client: httpx.AsyncClient, pl_url: str, start: float, end: float) -> tuple[str, float]:
    """Init + media segments covering [start, end] into one temp file. Returns (path, offset)."""
    from urllib.parse import urljoin
    pl = parse_media_playlist((await client.get(pl_url)).text)
    if pl["encrypted"]:
        raise ProtectedAudio()
    segs = [sg for sg in pl["segments"] if sg[0] + sg[1] > start and sg[0] < end]
    if not segs:
        raise ValueError("nothing in that range")

    async def get(uri, length, offset):
        headers = {"Range": f"bytes={offset}-{offset + length - 1}"} if length is not None else {}
        r = await client.get(urljoin(pl_url, uri), headers=headers)
        r.raise_for_status()
        return r.content

    fd, path = tempfile.mkstemp(prefix="aj360-clip-", suffix=".mp4")
    with os.fdopen(fd, "wb") as f:
        if pl["map"]:
            f.write(await get(*pl["map"]))
        if all(sg[3] is not None and sg[2].split("?")[0] == segs[0][2].split("?")[0] for sg in segs):
            first, last = segs[0], segs[-1]
            f.write(await get(first[2], last[4] + last[3] - first[4], first[4]))
        else:
            for sg in segs:
                f.write(await get(sg[2], sg[3], sg[4]))
    return path, float(segs[0][0])


def mux_clip(video_path: str, v_off: float, audio_path: Optional[str], a_off: float,
             start: float, end: float, out_path: str) -> float:
    """Stream-copy [start, end] of the video (from the keyframe at or before start) and its audio
    into one MP4. Returns the real start time of the clip (the keyframe)."""
    import av

    vin = av.open(video_path)
    ain = av.open(audio_path) if audio_path else None
    out = av.open(out_path, "w", format="mp4", options={"movflags": "+faststart"})
    try:
        vs = vin.streams.video[0]
        ov = out.add_stream_from_template(vs)
        a_src = None
        if ain is not None and ain.streams.audio:
            a_src = ain.streams.audio[0]
        elif vin.streams.audio:
            a_src = vin.streams.audio[0]
        oa = out.add_stream_from_template(a_src) if a_src is not None else None

        # Video: the last keyframe at or before `start`, then everything until `end`.
        # Segment timestamps may be absolute (fMP4 tfdt, TS PTS) or start at 0, so every
        # time is measured from the first packet, which sits at the playlist offset.
        packets = [p for p in vin.demux(vs) if p.pts is not None]
        v0 = min((p.pts for p in packets), default=0)
        rel = lambda p: v_off + float((p.pts - v0) * p.time_base)  # noqa: E731
        keys = [p for p in packets if p.is_keyframe and rel(p) <= start + 0.01]
        t0 = rel(keys[-1]) if keys else (rel(packets[0]) if packets else start)
        shift = None  # one shift for pts and dts keeps B-frame reordering intact
        for p in packets:
            t = rel(p)
            if t < t0 - 0.001 or t >= end:
                continue
            if shift is None:
                shift = p.dts if p.dts is not None else p.pts
            p.pts -= shift
            p.dts = (p.dts - shift) if p.dts is not None else p.pts
            p.stream = ov
            out.mux(p)
        if oa is not None:
            src = ain if (ain is not None and ain.streams.audio) else vin
            if src is vin:
                vin.seek(0)
            off = a_off if src is ain else v_off
            a_packets = [p for p in src.demux(a_src) if p.pts is not None]
            a0 = min((p.pts for p in a_packets), default=0)
            base_a = None
            for p in a_packets:
                t = off + float((p.pts - a0) * p.time_base)
                if t < t0 or t >= end:
                    continue
                if base_a is None:
                    base_a = p.pts
                p.pts -= base_a
                p.dts = p.pts
                p.stream = oa
                out.mux(p)
    finally:
        out.close()
        vin.close()
        if ain is not None:
            ain.close()
    return t0


async def cut_clip(hls_url: str, start: float, end: float, max_height: int = 720) -> tuple[str, float]:
    """Download and cut [start, end] of an unencrypted episode. Returns (mp4_path, real_start)."""
    import asyncio

    paths = []
    try:
        async with httpx.AsyncClient(timeout=httpx.Timeout(30, read=180), follow_redirects=True) as client:
            master = (await client.get(hls_url)).text
            v_url = pick_video_playlist(master, hls_url, max_height)
            try:
                a_url = pick_audio_playlist(master, hls_url)
            except ValueError:
                a_url = None
            if a_url == v_url:
                a_url = None
            v_path, v_off = await _download_range(client, v_url, start, end)
            paths.append(v_path)
            a_path, a_off = (None, 0.0)
            if a_url:
                a_path, a_off = await _download_range(client, a_url, start, end)
                paths.append(a_path)
        fd, out_path = tempfile.mkstemp(prefix="aj360-cut-", suffix=".mp4")
        os.close(fd)
        real = await asyncio.to_thread(mux_clip, v_path, v_off, a_path, a_off, start, end, out_path)
        return out_path, real
    finally:
        for p in paths:
            if os.path.exists(p):
                os.remove(p)
