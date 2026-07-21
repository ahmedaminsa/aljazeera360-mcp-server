# Onvesper (Vesper) Knowledge Base — Local Mirror

A local, offline mirror of the official **Onvesper / Vesper** platform documentation
(`https://docs.onvesper.com/platform-knowledge-base`). Vesper is the OTT/streaming
platform and CMS (by **Deltatre**) that powers **Al Jazeera 360** (aljazeera360.com).

> **Attribution & takedown:** all documentation content under `pages/` is
> © Deltatre / Onvesper, mirrored unmodified from the publicly accessible
> official docs solely to power AI-assisted operations for the Al Jazeera 360
> platform (a Vesper resident). No ownership is claimed. If you represent
> Deltatre and want this mirror removed, open an issue and it will be taken
> down promptly — `refresh.sh` can always rebuild it locally instead.

This folder is the knowledge source for the [`onvesper-expert`](../.claude/agents/onvesper-expert.md)
subagent. Ask that agent things like *"how do I create a hero slide?"* or
*"explain licence family upgrades"* and it will search here first.

## Layout

```
onvesper-kb/
├── README.md            ← you are here (navigation + platform map)
├── pages/               ← every doc page as clean Markdown, mirroring the site URLs
│   ├── _master.md       ← the docs' own master index page
│   ├── back-office/…
│   ├── dve/…
│   └── …
└── _sources/
    ├── llms.txt         ← official flat index (page list + one-line descriptions)
    └── _urls.txt        ← the URL list used to build this mirror
```

**URL ↔ file mapping:** a page at
`docs.onvesper.com/platform-knowledge-base/<path>` is mirrored at
`onvesper-kb/pages/<path>.md`.

## How to use

- **Find a topic by keyword:** grep across the mirror, e.g.
  `grep -ri "geo-block" onvesper-kb/pages/` or search `_sources/llms.txt`.
- **Read a page:** open the matching `.md` under `pages/`.
- **Get the latest / a missing page:** append `.md` to the live URL, or query the docs
  dynamically:
  `https://docs.onvesper.com/platform-knowledge-base/<path>.md?ask=<question>&goal=<goal>`

## Platform map (9 areas)

| Area | Folder | What it covers |
|------|--------|----------------|
| **Back Office** | `pages/back-office/` | Admin at `backoffice.onvesper.com`: content management (heroes, rows, sections, segmentation), notifications, embed player, plugins, **users** (customer support), **Vesper Insights** (analytics + Data Sync feeds), administration, **licences** (subscriptions, promotions, payment flows, gifting), legacy analytics |
| **Self-service Live Streaming** | `pages/self-service-live-streaming/` | Schedule, launch infra, publish-on-live, monitor, cost tracking, terminate live events |
| **DVE — Video Exchange** | `pages/dve/` | VOD system: metadata, artwork, subtitles, typed tags, mid-rolls, trailers, thumbnails, geo-blocking, batch upload, image/VOD specs, video processing pipeline, live-to-VOD archiving |
| **Vesper Studio** | `pages/vesper-studio/` | Content creation/production: editor, broadcaster |
| **DGE — Streaming Exchange** | `pages/streaming-exchange-dge/` | Live/linear channels, virtual live-linear, live-to-VOD, automated archiving from EPG |
| **Service Emails** | `pages/service-emails/` | Transactional / service email behaviour |
| **Advertising** | `pages/advertising/` | SSP config, ads.txt, ad targeting (basic/advanced, macros, functions), VOD ads, live ads (SCTE/SSAI) |
| **Consumer Experience** | `pages/consumer-experience/` | End-user apps: web, mobile (push/deeplinks), TV (Roku, PIN/QR), theming, payments & subscriptions, profiles/parental controls, search, watchlists, interstitials |
| **Payment Recovery / Security / Consent** | `pages/payment-recovery.md`, `pages/security/`, `pages/consent-management-platforms/` | Dunning; CAPTCHA + DRM; OneTrust cookie consent |

## Key vocabulary

- **Resident** — a client tenant (Al Jazeera 360 is a resident). **Realm** — a branded
  instance/environment; many settings are per-realm.
- **DVE** = Deltatre Video Exchange (VOD). **DGE** = Deltatre Streaming Exchange (live/linear).
- **Licence** — a subscription/entitlement product. **Licence family** — models
  upgrade/downgrade paths between plans.
- **Row / Hero / Section** — merchandising building blocks of the app's home/browse UI.
- **Typed tags** — structured, schema'd video metadata (vs free tags).
- **SSAI / SCTE-35** — server-side ad insertion for live streams.

## Refreshing this mirror

Re-run the downloader to pull the latest docs:

```bash
cd onvesper-kb
BASE="https://docs.onvesper.com/platform-knowledge-base"
curl -sL "$BASE/llms.txt" -o _sources/llms.txt
while IFS= read -r path; do
  [ -z "$path" ] && continue
  out="pages/${path}.md"; mkdir -p "$(dirname "$out")"
  curl -sL --retry 2 "$BASE/${path}.md" -o "$out"
done < _sources/_urls.txt
```

To also refresh the **page list** itself (in case new pages were added), re-download the
sitemap and rebuild `_sources/_urls.txt`:
`curl -sL "$BASE/sitemap-pages.xml"` (strip the URL prefix from each `<loc>`).

*Source: official Onvesper documentation. Mirror built for the Al Jazeera 360 project.*
