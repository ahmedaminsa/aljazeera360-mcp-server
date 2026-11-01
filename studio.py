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
import json
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
    "هذه هذا الذي كيف لماذا ماذا متى اين هل اسمه اسمها ممكن واحد واحده وحده كمان هيك هاي هاد هادا شو كتير كثير "
    "عم بدو بده بدنا لازم يعني عشان علشان برضه بردو زي مثل حيث التي الذين كانوا يكون تكون صار صارت راح رح قال "
    "قالت قالوا يقول تقول عندما عندنا عندهم لدينا لديهم شيء اشياء مره كانت اكثر اقل جميع لقد".split())}


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
            if len(nw) >= 5 and nw not in STOPWORDS and not nw.isdigit():
                words[w] += 1
    # Repeated content words only: a name or topic comes up more than once.
    tags += [tag(w) for w, n in words.most_common(limit * 2) if n >= 2]
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


# ----------------------------------------------------------------------------
# Language model (Workers AI via the Worker): translation, chapters, guests, names
# ----------------------------------------------------------------------------
LLM_MODEL = "@cf/meta/llama-3.3-70b-instruct-fp8-fast"
WINDOW_SECONDS = 480          # transcript window per analysis call (~8 minutes)
TRANSLATE_BATCH = 30          # subtitle lines per translation call
LANGUAGES = {"en": "English", "fr": "French", "es": "Spanish", "tr": "Turkish"}
TITLES = [normalize(t) for t in ("الدكتور", "الدكتوره", "د.", "الاستاذ", "الاستاذه", "الشيخ", "المهندس",
                                 "السيد", "السيده", "البروفيسور", "الرئيس", "الجنرال", "اللواء", "العميد")]


def llm_available() -> bool:
    from video_intel import CF_ACCOUNT, CF_AI_TOKEN, INDEX_URL, INTERNAL_TOKEN
    return bool((INDEX_URL and INTERNAL_TOKEN) or (CF_ACCOUNT and CF_AI_TOKEN))


async def llm(client: httpx.AsyncClient, system: str, user: str, max_tokens: int = 3000) -> str:
    from video_intel import CF_ACCOUNT, CF_AI_TOKEN, INDEX_URL, INTERNAL_TOKEN
    body = {"messages": [{"role": "system", "content": system}, {"role": "user", "content": user}],
            "max_tokens": max_tokens, "temperature": 0.2}
    if INDEX_URL and INTERNAL_TOKEN:
        resp = await client.post(f"{INDEX_URL}/internal/llm", json={**body, "model": LLM_MODEL},
                                 headers={"x-internal-token": INTERNAL_TOKEN})
    elif CF_ACCOUNT and CF_AI_TOKEN:
        resp = await client.post(f"https://api.cloudflare.com/client/v4/accounts/{CF_ACCOUNT}/ai/run/{LLM_MODEL}",
                                 json=body, headers={"Authorization": f"Bearer {CF_AI_TOKEN}"})
    else:
        raise RuntimeError("no language model backend configured")
    resp.raise_for_status()
    res = resp.json().get("result", {})
    out = res.get("response") if isinstance(res, dict) else res
    return out if isinstance(out, str) else json.dumps(out, ensure_ascii=False)


def parse_json(text: str) -> dict:
    """First JSON object in a model reply (tolerates ``` fences and chatter)."""
    t = re.sub(r"```(?:json)?", "", text or "")
    start = t.find("{")
    if start < 0:
        return {}
    depth, in_str, esc = 0, False, False
    for i in range(start, len(t)):
        ch = t[i]
        if in_str:
            if esc:
                esc = False
            elif ch == "\\":
                esc = True
            elif ch == '"':
                in_str = False
            continue
        if ch == '"':
            in_str = True
        elif ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                try:
                    return json.loads(t[start:i + 1])
                except ValueError:
                    return {}
    return {}


def windows(cues: list[dict], size: int = WINDOW_SECONDS) -> list[list[dict]]:
    out, cur, start = [], [], None
    for c in cues:
        if start is None:
            start = c["start"]
        if c["start"] - start >= size and cur:
            out.append(cur)
            cur, start = [], c["start"]
        cur.append(c)
    if cur:
        out.append(cur)
    return out


def _stamped(cues: list[dict]) -> str:
    return "\n".join(f"[{fmt_ts(c['start'])}] {c['text']}" for c in cues)


ANALYSE_PROMPT = """You analyse part of an Arabic TV programme transcript produced by speech recognition, so
proper names may be misspelled. Programme: «{title}» from «{series}». {description}
Return ONLY JSON:
{{"people":[{{"name":"correct full name in Arabic","name_en":"English spelling","role":"who they are, short, in Arabic","type":"guest|presenter|mentioned","first_at":"mm:ss"}}],
 "chapters":[{{"start":"mm:ss","title":"short Arabic chapter title (2-6 words)"}}]}}
Rules: people = real named individuals only; type is guest/presenter only if they speak in the programme,
otherwise mentioned. chapters = where the subject changes, at most one per 2 minutes.
Times come from the [mm:ss] marks."""

NAMES_PROMPT = """You proofread proper names in an Arabic speech-recognition transcript of «{title}» ({series}).
Speech recognition often fuses or splits names and swaps letters (e.g. «مردخايف عنونه» for «مردخاي فعنونو»).
List EVERY proper name of a person, place or organisation in the text, copied character for character as
written, with its standard Arabic spelling.
Return ONLY JSON: {{"names":[{{"written":"...","standard":"...","misheard":true,"at":"mm:ss"}}]}}
misheard = true when the written form is a recognition error, false when it is only a variant spelling."""
NAMES_WINDOW = 240


def _strip_titles(name: str) -> str:
    n = normalize(name)
    for t in TITLES:
        if n.startswith(t + " "):
            n = n[len(t) + 1:]
    return n.strip()


def person_key(name: str, name_en: Optional[str] = None) -> str:
    """Dedup key: the English spelling when known (Arabic spellings of foreign names vary)."""
    en = re.sub(r"[^a-z ]", "", (name_en or "").lower()).strip()
    return f"en:{en}" if en else _strip_titles(name)


def name_suggestions(items: list[dict]) -> list[dict]:
    """Keep real recognition errors (high) and near spelling variants of one word (low). Drop the rest:
    same spelling after normalisation, longer forms («براون» → «فيرنر فون براون»), synonyms
    («أمريكا» → «الولايات المتحدة»)."""
    from difflib import SequenceMatcher
    from video_intel import parse_ts
    out: dict[str, dict] = {}
    for f in items:
        heard = (f.get("written") or "").strip()
        correct = (f.get("standard") or "").strip()
        nh, nc = normalize(heard), normalize(correct)
        if not heard or not correct or nh == nc or heard in out:
            continue
        if set(nh.split()) <= set(nc.split()) or nh in nc:
            continue
        ratio = SequenceMatcher(None, nh, nc).ratio()
        if f.get("misheard") is True and ratio >= 0.5:
            conf = "high"
        elif len(nh.split()) == 1 and ratio >= 0.8:
            conf = "low"
        else:
            continue
        out[heard] = {"heard": heard, "correct": correct, "at_sec": parse_ts(f.get("at", 0)), "confidence": conf}
    return sorted(out.values(), key=lambda f: (f["confidence"] != "high", f["at_sec"]))


def same_person(a: dict, b: dict) -> bool:
    """«Gerald Bull» / «Gerard Bull»: same surname and nearly the same English name."""
    from difflib import SequenceMatcher
    ea, eb = (a.get("name_en") or "").lower().split(), (b.get("name_en") or "").lower().split()
    if not ea or not eb or ea[-1] != eb[-1]:
        return False
    return SequenceMatcher(None, " ".join(ea), " ".join(eb)).ratio() >= 0.8


def merge_similar(people: list[dict]) -> list[dict]:
    out: list[dict] = []
    for p in people:
        twin = next((q for q in out if same_person(p, q)), None)
        if twin is None:
            out.append(p)
        elif p.get("type") in ("guest", "presenter"):
            twin["type"] = p["type"]
    return out


def merge_analysis(parts: list[dict], duration: float) -> dict:
    """Combine per-window results: one entry per person, unique fixes, spaced chapters."""
    from video_intel import parse_ts
    people: dict[str, dict] = {}
    rank = {"presenter": 2, "guest": 2, "mentioned": 1}
    for p in (x for part in parts for x in part.get("people") or [] if isinstance(x, dict) and x.get("name")):
        key = person_key(p["name"], p.get("name_en"))
        if not key:
            continue
        at = parse_ts(p.get("first_at", 0))
        cur = people.get(key)
        entry = {"name": p["name"].strip(), "name_en": (p.get("name_en") or "").strip(),
                 "role": (p.get("role") or "").strip(),
                 "type": p.get("type") if p.get("type") in rank else "mentioned", "first_at_sec": at}
        if cur is None:
            people[key] = entry
            continue
        if rank[entry["type"]] > rank[cur["type"]]:
            cur["type"] = entry["type"]
        cur["first_at_sec"] = min(cur["first_at_sec"], at)
        for k in ("name_en", "role"):
            if not cur[k] and entry[k]:
                cur[k] = entry[k]
    fixes = name_suggestions([x for part in parts for x in (part.get("names") or []) if isinstance(x, dict)])
    chapters = []
    for c in sorted((x for part in parts for x in part.get("chapters") or [] if isinstance(x, dict) and x.get("title")),
                    key=lambda c: parse_ts(c.get("start", 0))):
        t = parse_ts(c.get("start", 0))
        if duration and t >= duration - 30:
            continue
        if not chapters or t - chapters[-1]["start_sec"] >= 120:
            chapters.append({"start_sec": t, "title": c["title"].strip()})
    if chapters and chapters[0]["start_sec"] > 0:
        if chapters[0]["start_sec"] < 60:
            chapters[0]["start_sec"] = 0
        else:
            chapters.insert(0, {"start_sec": 0, "title": "مقدمة"})
    for c in chapters:
        c["start"] = fmt_ts(c["start_sec"])
    ppl = merge_similar(sorted(people.values(), key=lambda p: p["first_at_sec"]))
    for p in ppl:
        p["first_at"] = fmt_ts(p["first_at_sec"])
    return {"people": ppl, "name_fixes": fixes, "chapters": chapters}


async def analyse_transcript(cues: list[dict], meta: dict) -> dict:
    """People, likely misheard names and chapters for a whole episode (windowed LLM calls)."""
    import asyncio
    system = ANALYSE_PROMPT.format(title=meta.get("title", ""), series=meta.get("series") or "",
                                   description=(meta.get("description") or "")[:400])
    sem = asyncio.Semaphore(4)
    async with httpx.AsyncClient(timeout=180) as client:
        async def one(win):
            async with sem:
                for attempt in range(2):
                    try:
                        return parse_json(await llm(client, system, _stamped(win)))
                    except Exception:
                        if attempt:
                            return {}
                        await asyncio.sleep(2)
        names_system = NAMES_PROMPT.format(title=meta.get("title", ""), series=meta.get("series") or "")

        async def names(win):
            async with sem:
                try:
                    return parse_json(await llm(client, names_system, _stamped(win), 2500))
                except Exception:
                    return {}
        parts, name_parts = await asyncio.gather(
            asyncio.gather(*(one(w) for w in windows(cues))),
            asyncio.gather(*(names(w) for w in windows(cues, NAMES_WINDOW))))
    merged = merge_analysis(list(parts), float(meta.get("duration") or 0))
    merged["name_fixes"] = name_suggestions([x for p in name_parts for x in p.get("names") or [] if isinstance(x, dict)])
    return merged


TRANSLATE_PROMPT = """You translate Arabic TV documentary subtitles into natural {language} subtitles.
Programme: «{title}». Keep names correct (usual {language} spelling), keep each line short, keep the meaning
of dialect. Translate every numbered line on its own, even if it is a fragment: never merge or split lines.
Return ONLY JSON mapping each line number to its translation: {{"1": "...", "2": "...", ...}}"""


async def _translate_batch(client, batch: list[dict], language: str, title: str) -> dict[int, str]:
    system = TRANSLATE_PROMPT.format(language=language, title=title)
    user = "\n".join(f"{i + 1}. {c['text']}" for i, c in enumerate(batch))
    got = parse_json(await llm(client, system, user, 4000))
    if isinstance(got.get("lines"), list):  # tolerate the list form
        got = {str(i + 1): v for i, v in enumerate(got["lines"])}
    out = {}
    for k, v in got.items():
        if str(k).isdigit() and 1 <= int(k) <= len(batch) and isinstance(v, str) and v.strip():
            out[int(k) - 1] = v.strip()
    return out


async def translate_cues(cues: list[dict], language: str, title: str = "") -> list[dict]:
    """Same timing, text translated. Lines still missing after a retry keep the Arabic (marked)."""
    import asyncio
    lang = LANGUAGES.get(language, language)
    done: dict[int, str] = {}
    sem = asyncio.Semaphore(3)
    async with httpx.AsyncClient(timeout=180) as client:
        async def run(idxs: list[int]):
            async with sem:
                try:
                    part = await _translate_batch(client, [cues[i] for i in idxs], lang, title)
                except Exception:
                    return
                for j, text in part.items():
                    done[idxs[j]] = text
        for size in (TRANSLATE_BATCH, 10):  # second pass: smaller batches for whatever is missing
            todo = [i for i in range(len(cues)) if i not in done]
            if not todo:
                break
            await asyncio.gather(*(run(todo[k:k + size]) for k in range(0, len(todo), size)))
    return [{"start": c["start"], "end": c["end"], "text": done.get(i, c["text"]), "translated": i in done}
            for i, c in enumerate(cues)]


def apply_fixes(cues: list[dict], fixes: list[dict]) -> tuple[list[dict], int]:
    """Replace misheard names in the transcript text and its word timings. Returns (cues, replacements)."""
    count = 0
    out = []
    for c in cues:
        text, words = c["text"], [list(w) for w in c.get("words") or []]
        for f in fixes:
            heard, correct = f["heard"].strip(), f["correct"].strip()
            if not heard or heard not in text:
                continue
            count += text.count(heard)
            text = text.replace(heard, correct)
            hw = heard.split()
            i = 0
            while i <= len(words) - len(hw):
                span = " ".join(w[2] for w in words[i:i + len(hw)])
                if heard in span:
                    merged = [words[i][0], words[i + len(hw) - 1][1], span.replace(heard, correct)]
                    words[i:i + len(hw)] = [merged]
                i += 1
        out.append({**c, "text": text, "words": words})
    return out, count


def youtube_chapters(chapters: list[dict]) -> str:
    return "\n".join(f"{c['start']} {c['title']}" for c in chapters)
