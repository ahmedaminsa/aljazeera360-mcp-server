"""
Video understanding for the Al Jazeera 360 MCP server: see, read and hear
episodes, and keep what was learnt in a searchable index.

SEE / READ — every VOD on the platform ships a public BIF file (the
"trick-play" previews the player shows while scrubbing): one 320x180 JPEG
every ~15 s for the whole episode. It is not DRM-protected. ``watch_video``
turns a time range into timestamped contact sheets and returns them as
images, so the AI assistant calling the tool looks at the episode itself and
reads its on-screen text (guest names and titles, news tickers, quotes).
No vision API key is needed: the assistant's own model does the looking.

REMEMBER — ``save_video_analysis`` stores what the assistant found (summary,
chapters, people, topics, keywords, on-screen text) and ``search_video_index``
finds moments across every analysed episode ("who appeared", "when was X
discussed").

HEAR — ``listen_to_video`` transcribes an episode's own audio from the HLS
stream the official player receives, fetching only the requested byte range.
Most episodes' audio is unencrypted; if a stream is DRM-protected it is
refused, never decrypted. ``transcribe_audio`` transcribes an audio or video *file* the user is
entitled to (their archive, an export, a file they manage elsewhere): the
server decodes it with PyAV (FFmpeg), cuts 30-second 16 kHz mono chunks and
sends them to Whisper large-v3-turbo on Cloudflare Workers AI. The
transcript is stored in the index with timestamps.

Storage/transcription backends:
* Hosted (Cloudflare): the Worker exposes /internal/* endpoints backed by D1
  and Workers AI; the container reaches them with AJ360_INDEX_URL and the
  shared AJ360_INTERNAL_TOKEN.
* Self-hosted: a local SQLite file (AJ360_INDEX_DB), and Workers AI over its
  REST API if CLOUDFLARE_ACCOUNT_ID + CLOUDFLARE_AI_TOKEN are set.
"""

from __future__ import annotations

import asyncio
import base64
import io
import json
import os
import re
import sqlite3
import struct
import tempfile
import time
from typing import Any, Optional

import httpx

BIF_MAGIC = b"\x89BIF\r\n\x1a\n"
FRAME_W, FRAME_H = 320, 180
WHISPER_MODEL = "@cf/openai/whisper-large-v3-turbo"
CHUNK_SECONDS = 30
# Some hosts (e.g. Wikimedia) refuse requests without a descriptive agent.
USER_AGENT = "aljazeera360-mcp/2.2 (+https://github.com/ahmedaminsa/aljazeera360-mcp-server)"
MAX_AUDIO_BYTES = 800 * 1024 * 1024      # refuse absurd downloads
MAX_TRANSCRIBE_SECONDS = 3 * 3600

INDEX_URL = os.environ.get("AJ360_INDEX_URL", "").rstrip("/")
INTERNAL_TOKEN = os.environ.get("AJ360_INTERNAL_TOKEN", "")
LOCAL_DB = os.environ.get("AJ360_INDEX_DB", "video_index.db")
CF_ACCOUNT = os.environ.get("CLOUDFLARE_ACCOUNT_ID", "")
CF_AI_TOKEN = os.environ.get("CLOUDFLARE_AI_TOKEN", "")


# ----------------------------------------------------------------------------
# Arabic-aware normalisation (identical rules in the Worker: normalizeText)
# ----------------------------------------------------------------------------
_TASHKEEL = re.compile(r"[ً-ْٰـ]")


def normalize(text: str) -> str:
    t = _TASHKEEL.sub("", text or "").lower()
    t = re.sub("[أإآٱ]", "ا", t).replace("ى", "ي").replace("ة", "ه")
    return re.sub(r"\s+", " ", t).strip()


def fmt_ts(seconds: float) -> str:
    s = int(seconds)
    return f"{s // 3600}:{s % 3600 // 60:02d}:{s % 60:02d}" if s >= 3600 else f"{s // 60:02d}:{s % 60:02d}"


def parse_ts(value: Any) -> int:
    """'14:30', '1:02:03', 870, '870' → seconds."""
    if isinstance(value, (int, float)):
        return int(value)
    parts = [p for p in str(value).strip().split(":") if p != ""]
    try:
        nums = [float(p) for p in parts]
    except ValueError:
        return 0
    total = 0.0
    for n in nums:
        total = total * 60 + n
    return int(total)


# ----------------------------------------------------------------------------
# SEE: BIF preview frames
# ----------------------------------------------------------------------------
_bif_cache: dict[str, tuple[float, bytes]] = {}


async def fetch_bif(url: str) -> bytes:
    hit = _bif_cache.get(url)
    if hit and time.time() - hit[0] < 1800:
        return hit[1]
    async with httpx.AsyncClient(timeout=60, follow_redirects=True) as client:
        resp = await client.get(url)
        resp.raise_for_status()
        data = resp.content
    if data[:8] != BIF_MAGIC:
        raise ValueError("preview file is not a BIF archive")
    if len(_bif_cache) > 20:
        _bif_cache.pop(next(iter(_bif_cache)))
    _bif_cache[url] = (time.time(), data)
    return data


def parse_bif(data: bytes) -> tuple[int, list[tuple[int, bytes]]]:
    """Returns (interval_seconds, [(timestamp_seconds, jpeg_bytes), ...])."""
    count = struct.unpack("<I", data[12:16])[0]
    multiplier_ms = struct.unpack("<I", data[16:20])[0] or 1000
    index = [struct.unpack("<II", data[64 + i * 8: 72 + i * 8]) for i in range(count + 1)]
    frames = []
    for i in range(count):
        ts, off = index[i]
        end = index[i + 1][1]
        frames.append((int(ts * multiplier_ms / 1000), data[off:end]))
    return max(1, multiplier_ms // 1000), frames


def pick_frames(frames: list[tuple[int, bytes]], start: int, end: Optional[int], max_frames: int):
    inside = [f for f in frames if f[0] >= start and (end is None or f[0] <= end)]
    if len(inside) <= max_frames:
        return inside
    step = len(inside) / max_frames
    return [inside[int(i * step)] for i in range(max_frames)]


def contact_sheet(frames: list[tuple[int, bytes]], cols: int = 3, scale: float = 1.5) -> bytes:
    """Timestamped grid as JPEG. Imported lazily: Pillow only needed here."""
    from PIL import Image as PILImage, ImageDraw

    label_h = 20
    rows = (len(frames) + cols - 1) // cols
    sheet = PILImage.new("RGB", (FRAME_W * cols, (FRAME_H + label_h) * rows), "white")
    draw = ImageDraw.Draw(sheet)
    for i, (ts, jpeg) in enumerate(frames):
        x, y = (i % cols) * FRAME_W, (i // cols) * (FRAME_H + label_h)
        try:
            img = PILImage.open(io.BytesIO(jpeg)).convert("RGB").resize((FRAME_W, FRAME_H))
        except Exception:
            img = PILImage.new("RGB", (FRAME_W, FRAME_H), "gray")
        sheet.paste(img, (x, y + label_h))
        draw.rectangle([x, y, x + FRAME_W - 1, y + label_h - 1], fill="black")
        draw.text((x + 6, y + 4), fmt_ts(ts), fill="white")
    if scale != 1:
        sheet = sheet.resize((int(sheet.width * scale), int(sheet.height * scale)))
    out = io.BytesIO()
    sheet.save(out, format="JPEG", quality=82)
    return out.getvalue()


# ----------------------------------------------------------------------------
# HEAR: decode any audio/video file and transcribe it in chunks
# ----------------------------------------------------------------------------
async def download_media(url: str) -> str:
    if not re.match(r"^https?://", url or ""):
        raise ValueError("audio_url must be an http(s) link to an audio or video file")
    fd, path = tempfile.mkstemp(prefix="aj360-media-")
    size = 0
    headers = {"User-Agent": USER_AGENT}
    async with httpx.AsyncClient(timeout=httpx.Timeout(60, read=300), follow_redirects=True, headers=headers) as client:
        async with client.stream("GET", url) as resp:
            resp.raise_for_status()
            with os.fdopen(fd, "wb") as f:
                async for chunk in resp.aiter_bytes(1 << 20):
                    size += len(chunk)
                    if size > MAX_AUDIO_BYTES:
                        raise ValueError("file is larger than 800 MB")
                    f.write(chunk)
    return path


def decode_to_chunks(path: str, start: int, end: Optional[int]) -> list[tuple[int, bytes]]:
    """16 kHz mono WAV chunks of CHUNK_SECONDS: [(offset_seconds, wav_bytes)]."""
    import av  # PyAV, bundles FFmpeg
    import wave

    rate = 16000
    samples = bytearray()
    with av.open(path) as container:
        stream = next((s for s in container.streams if s.type == "audio"), None)
        if stream is None:
            raise ValueError("the file has no audio track")
        if start:
            container.seek(int(start / stream.time_base), stream=stream)
        resampler = av.AudioResampler(format="s16", layout="mono", rate=rate)
        limit = (end - start) if end else MAX_TRANSCRIBE_SECONDS
        for packet in container.demux(stream):
            for frame in packet.decode():
                for out in resampler.resample(frame):
                    samples.extend(bytes(out.planes[0])[: out.samples * 2])
            if len(samples) >= limit * rate * 2:
                break
    samples = samples[: int(limit * rate * 2)]
    chunks = []
    step = CHUNK_SECONDS * rate * 2
    for i in range(0, len(samples), step):
        buf = io.BytesIO()
        with wave.open(buf, "wb") as w:
            w.setnchannels(1)
            w.setsampwidth(2)
            w.setframerate(rate)
            w.writeframes(bytes(samples[i: i + step]))
        chunks.append((start + i // (rate * 2), buf.getvalue()))
    return chunks


async def _whisper(client: httpx.AsyncClient, wav: bytes, language: str) -> dict:
    body = {"audio": base64.b64encode(wav).decode(), "language": language, "vad_filter": True}
    if INDEX_URL and INTERNAL_TOKEN:
        resp = await client.post(f"{INDEX_URL}/internal/transcribe", json=body,
                                 headers={"x-internal-token": INTERNAL_TOKEN})
    elif CF_ACCOUNT and CF_AI_TOKEN:
        resp = await client.post(
            f"https://api.cloudflare.com/client/v4/accounts/{CF_ACCOUNT}/ai/run/{WHISPER_MODEL}",
            json=body, headers={"Authorization": f"Bearer {CF_AI_TOKEN}"})
    else:
        raise RuntimeError("no transcription backend: set AJ360_INDEX_URL + AJ360_INTERNAL_TOKEN "
                           "(hosted) or CLOUDFLARE_ACCOUNT_ID + CLOUDFLARE_AI_TOKEN")
    resp.raise_for_status()
    data = resp.json()
    return data.get("result", data)


# Phrases Whisper is known to invent over music, applause or silence (learnt
# from subtitled YouTube videos). Segments that are only one of these are dropped.
HALLUCINATIONS = {normalize(p) for p in (
    "اشتركوا في القناة", "اشترك في القناة", "لا تنسوا الاشتراك في القناة", "شكرا للمشاهدة",
    "شكرا على المشاهدة", "ترجمة نانسي قنقر", "نانسي قنقر", "سبحان الله", "موسيقى",
    "Thanks for watching!", "Subscribe to the channel",
)}


def is_hallucination(text: str) -> bool:
    return normalize(re.sub(r"[.!؟?،,]+$", "", text or "")) in HALLUCINATIONS


def transcription_available() -> bool:
    return bool((INDEX_URL and INTERNAL_TOKEN) or (CF_ACCOUNT and CF_AI_TOKEN))


FAILED = "[تعذّر نسخ هذا الجزء]"


async def transcribe_chunks(chunks: list[tuple[int, bytes]], language: str = "ar") -> list[dict]:
    """[{start, end, text, failed?}] with absolute timestamps."""
    sem = asyncio.Semaphore(6)
    async with httpx.AsyncClient(timeout=120) as client:
        async def one(offset: int, wav: bytes):
            async with sem:
                for attempt in range(3):
                    try:
                        res = await _whisper(client, wav, language)
                        break
                    except Exception:
                        if attempt == 2:
                            return [{"start": offset, "end": offset + CHUNK_SECONDS, "text": FAILED, "failed": True}]
                        await asyncio.sleep(2 * (attempt + 1))
                segs = res.get("segments") or []
                if not segs and res.get("text"):
                    segs = [{"start": 0, "end": CHUNK_SECONDS, "text": res["text"]}]
                return [{"start": round(offset + float(s.get("start", 0)), 1),
                         "end": round(offset + float(s.get("end", 0)), 1),
                         "text": (s.get("text") or "").strip()} for s in segs
                        if (s.get("text") or "").strip() and not is_hallucination(s.get("text"))]
        parts = await asyncio.gather(*(one(o, w) for o, w in chunks))
    return [seg for part in parts for seg in part]


# ----------------------------------------------------------------------------
# HEAR the episode itself: the platform's HLS audio, when it is not encrypted
# ----------------------------------------------------------------------------
class ProtectedAudio(Exception):
    """The episode's audio is DRM-encrypted; it is never decrypted."""


def _attrs(line: str) -> dict:
    return {k: v.strip('"') for k, v in re.findall(r'([A-Z0-9-]+)=("[^"]*"|[^,]*)', line.split(":", 1)[1])}


def pick_audio_playlist(master: str, master_url: str) -> str:
    """URL of the audio rendition used by the lowest-bandwidth variant."""
    from urllib.parse import urljoin
    lines = master.splitlines()
    variants = []
    for i, line in enumerate(lines):
        if line.startswith("#EXT-X-STREAM-INF"):
            a = _attrs(line)
            variants.append((int(a.get("BANDWIDTH", "0") or 0), a.get("AUDIO"), lines[i + 1] if i + 1 < len(lines) else ""))
    medias = [_attrs(l) for l in lines if l.startswith("#EXT-X-MEDIA") and "TYPE=AUDIO" in l]
    if medias:
        group = min(variants)[1] if variants else None
        in_group = [m for m in medias if m.get("GROUP-ID") == group] or medias
        chosen = next((m for m in in_group if m.get("DEFAULT") == "YES"), in_group[0])
        if chosen.get("URI"):
            return urljoin(master_url, chosen["URI"])
    if variants:  # audio muxed into the video variants
        return urljoin(master_url, min(variants)[2])
    raise ValueError("no audio in this stream")


def parse_media_playlist(text: str) -> dict:
    """{'encrypted', 'map': (uri, length, offset)|None, 'segments': [(start, dur, uri, length, offset)]}"""
    out = {"encrypted": False, "map": None, "segments": []}
    t, dur, rng, last_end = 0.0, None, None, {}
    for line in text.splitlines():
        line = line.strip()
        if line.startswith("#EXT-X-KEY") and "METHOD=NONE" not in line:
            out["encrypted"] = True
        elif line.startswith("#EXT-X-MAP"):
            a = _attrs(line)
            br = a.get("BYTERANGE")
            if br:
                n, _, o = br.partition("@")
                out["map"] = (a["URI"], int(n), int(o or 0))
            else:
                out["map"] = (a["URI"], None, None)
        elif line.startswith("#EXTINF"):
            dur = float(line.split(":", 1)[1].split(",")[0])
        elif line.startswith("#EXT-X-BYTERANGE"):
            n, _, o = line.split(":", 1)[1].partition("@")
            rng = (int(n), int(o) if o else None)
        elif line and not line.startswith("#") and dur is not None:
            length, offset = (rng or (None, None))
            key = line.split("?")[0]
            if length is not None and offset is None:
                offset = last_end.get(key, 0)
            if length is not None:
                last_end[key] = offset + length
            out["segments"].append((t, dur, line, length, offset))
            t += dur
            dur, rng = None, None
    return out


async def fetch_stream_audio(hls_url: str, start: int, end: Optional[int]) -> tuple[str, int]:
    """Download the audio for [start, end] into a temp file. Returns (path, offset_seconds)."""
    from urllib.parse import urljoin
    async with httpx.AsyncClient(timeout=httpx.Timeout(30, read=180), follow_redirects=True) as client:
        master = (await client.get(hls_url)).text
        audio_url = pick_audio_playlist(master, hls_url)
        pl = parse_media_playlist((await client.get(audio_url)).text)
        if pl["encrypted"]:
            raise ProtectedAudio()
        segs = [sg for sg in pl["segments"] if sg[0] + sg[1] > start and (end is None or sg[0] < end)]
        if not segs:
            raise ValueError("no audio in that range")
        fd, path = tempfile.mkstemp(prefix="aj360-audio-", suffix=".mp4")
        with os.fdopen(fd, "wb") as f:
            async def get(uri, length, offset):
                headers = {"Range": f"bytes={offset}-{offset + length - 1}"} if length is not None else {}
                r = await client.get(urljoin(audio_url, uri), headers=headers)
                r.raise_for_status()
                return r.content
            if pl["map"]:
                f.write(await get(*pl["map"]))
            same_file = all(sg[3] is not None and sg[2].split("?")[0] == segs[0][2].split("?")[0] for sg in segs)
            if same_file:
                # One ranged request for the whole contiguous run of segments.
                first, last = segs[0], segs[-1]
                f.write(await get(first[2], last[4] + last[3] - first[4], first[4]))
            else:
                for sg in segs:
                    f.write(await get(sg[2], sg[3], sg[4]))
        return path, int(segs[0][0])


# ----------------------------------------------------------------------------
# REMEMBER: the index (Worker/D1 when hosted, SQLite locally)
# ----------------------------------------------------------------------------
_SCHEMA = """
CREATE TABLE IF NOT EXISTS video_analysis (
  video_id INTEGER PRIMARY KEY, title TEXT, series TEXT, duration INTEGER, watch_url TEXT,
  summary TEXT, data TEXT, updated_at TEXT);
CREATE TABLE IF NOT EXISTS video_moments (
  id INTEGER PRIMARY KEY AUTOINCREMENT, video_id INTEGER, t_sec INTEGER, kind TEXT, text TEXT, norm TEXT);
CREATE INDEX IF NOT EXISTS idx_moments_video ON video_moments (video_id, kind);
"""


def moments_from_analysis(a: dict) -> list[dict]:
    rows = []
    for c in a.get("chapters") or []:
        rows.append({"t_sec": parse_ts(c.get("start", 0)), "kind": "chapter", "text": c.get("title", "")})
    for p in a.get("people") or []:
        label = p.get("name", "") + (f" — {p['role']}" if p.get("role") else "")
        rows.append({"t_sec": parse_ts(p.get("first_seen", 0)), "kind": "person", "text": label})
    for t in a.get("on_screen_text") or []:
        if isinstance(t, dict):
            rows.append({"t_sec": parse_ts(t.get("at", 0)), "kind": "onscreen", "text": t.get("text", "")})
        else:
            rows.append({"t_sec": 0, "kind": "onscreen", "text": str(t)})
    for t in a.get("topics") or []:
        rows.append({"t_sec": 0, "kind": "topic", "text": str(t)})
    for k in a.get("keywords") or []:
        rows.append({"t_sec": 0, "kind": "keyword", "text": str(k)})
    return [dict(r, norm=normalize(r["text"])) for r in rows if r["text"]]


class VideoIndex:
    def __init__(self):
        self.remote = bool(INDEX_URL and INTERNAL_TOKEN)

    # -- remote ---------------------------------------------------------------
    async def _call(self, method: str, path: str, **kw):
        async with httpx.AsyncClient(timeout=60) as client:
            resp = await client.request(method, f"{INDEX_URL}{path}",
                                        headers={"x-internal-token": INTERNAL_TOKEN}, **kw)
            resp.raise_for_status()
            return resp.json()

    # -- local ----------------------------------------------------------------
    def _db(self):
        db = sqlite3.connect(LOCAL_DB)
        db.executescript(_SCHEMA)
        db.row_factory = sqlite3.Row
        return db

    async def save(self, video: dict, analysis: dict, kinds: list[str], moments: list[dict]) -> dict:
        payload = {"video": video, "analysis": analysis, "kinds": kinds, "moments": moments}
        if self.remote:
            return await self._call("POST", "/internal/index/save", json=payload)
        db = self._db()
        with db:
            if analysis is not None:
                old = db.execute("SELECT data FROM video_analysis WHERE video_id=?", (video["id"],)).fetchone()
                merged = {**(json.loads(old["data"]) if old and old["data"] else {}), **analysis}
                db.execute("""INSERT INTO video_analysis (video_id,title,series,duration,watch_url,summary,data,updated_at)
                              VALUES (?,?,?,?,?,?,?,datetime('now'))
                              ON CONFLICT(video_id) DO UPDATE SET title=excluded.title, series=excluded.series,
                              duration=excluded.duration, watch_url=excluded.watch_url,
                              summary=COALESCE(excluded.summary, video_analysis.summary),
                              data=excluded.data, updated_at=excluded.updated_at""",
                           (video["id"], video.get("title"), video.get("series"), video.get("duration"),
                            video.get("watch_url"), merged.get("summary"), json.dumps(merged, ensure_ascii=False)))
            db.execute(f"DELETE FROM video_moments WHERE video_id=? AND kind IN ({','.join('?' * len(kinds))})",
                       (video["id"], *kinds))
            db.executemany("INSERT INTO video_moments (video_id,t_sec,kind,text,norm) VALUES (?,?,?,?,?)",
                           [(video["id"], m["t_sec"], m["kind"], m["text"], m["norm"]) for m in moments])
        return {"saved": True, "moments": len(moments)}

    async def get(self, video_id: Optional[int]) -> dict:
        if self.remote:
            return await self._call("GET", "/internal/index/get", params={"id": video_id or ""})
        db = self._db()
        if not video_id:
            rows = db.execute("""SELECT a.video_id, a.title, a.series, a.updated_at,
                                 (SELECT COUNT(*) FROM video_moments m WHERE m.video_id=a.video_id AND m.kind='transcript') AS transcript_segments
                                 FROM video_analysis a ORDER BY a.updated_at DESC LIMIT 200""").fetchall()
            return {"videos": [dict(r) for r in rows]}
        a = db.execute("SELECT * FROM video_analysis WHERE video_id=?", (video_id,)).fetchone()
        ms = db.execute("SELECT t_sec, kind, text FROM video_moments WHERE video_id=? ORDER BY kind, t_sec",
                        (video_id,)).fetchall()
        return {"analysis": dict(a) if a else None, "moments": [dict(m) for m in ms]}

    async def search(self, query: str, kind: str, limit: int) -> dict:
        q = normalize(query)
        if self.remote:
            return await self._call("GET", "/internal/index/search", params={"q": q, "kind": kind, "limit": limit})
        db = self._db()
        sql = """SELECT m.video_id, m.t_sec, m.kind, m.text, a.title, a.series, a.watch_url
                 FROM video_moments m LEFT JOIN video_analysis a ON a.video_id=m.video_id
                 WHERE m.norm LIKE ?""" + (" AND m.kind=?" if kind != "all" else "") + " ORDER BY m.video_id, m.t_sec LIMIT ?"
        args = [f"%{q}%"] + ([kind] if kind != "all" else []) + [limit]
        return {"results": [dict(r) for r in db.execute(sql, args).fetchall()]}


index = VideoIndex()
