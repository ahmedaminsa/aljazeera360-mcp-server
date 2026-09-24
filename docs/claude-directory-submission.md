# Claude Connectors Directory — submission kit

Ready answers for each step of Anthropic's submission portal
(<https://claude.ai/admin-settings/directory/submissions/new>).
Requirements checked against <https://claude.com/docs/connectors/building/submission>
and the [pre-submission checklist](https://claude.com/docs/connectors/building/review-criteria), September 2026.

## Prerequisites — must be done by Al Jazeera 360 (not the code)

| # | Requirement | Why | Status |
|---|---|---|---|
| 1 | Submit from a **Claude Team or Enterprise organization**, as an Owner (or an Enterprise role with the *Directory* permission) | The portal lives in organization settings; individual plans can't submit | ⬜ |
| 2 | **Al Jazeera 360 approval** to publish an official connector to its catalog | Checklist: "Your server must call your own first-party APIs, or APIs you legitimately proxy"; the Compliance step includes a first-party API acknowledgment | ⬜ |
| 3 | **Custom domain on aljazeera360.com**, e.g. `mcp.aljazeera360.com` → the Cloudflare Worker | "The MCP server domain should match your service." Today it is `aljazeera360-mcp.ahmed-26d.workers.dev` | ⬜ |
| 4 | Platform provider (Deltatre / Vesper) OK for the API key's use by the connector | Data-handling step asks whether the API is yours, proxied with permission, or third-party | ⬜ |
| 5 | Support mailbox that answers (currently `support@aljazeera360.com` in the privacy policy) | Support contact is a required listing field | ⬜ |
| 6 | 3–5 PNG screenshots, ≥1000 px wide, of the interactive view inside Claude, cropped to the app response (no prompt) | Required for MCP Apps | ⬜ |

After the domain is set: add it to `AJ360_ALLOWED_HOST` in `deploy/cloudflare/wrangler.jsonc`, redeploy, and update `server.json` `remotes[0].url` (bump `version` → the MCP Registry updates itself).

## Already met by the server

- Remote, `https://`, streamable HTTP, no authentication needed (public catalog).
- All 26 tools have a `title` and `readOnlyHint: true`; none write data; names ≤ 28 chars.
- No catch-all API tool; every tool calls a fixed endpoint.
- Tool descriptions describe behaviour only (no instructions to Claude).
- Inputs are validated and bounded; errors return messages, not bare 500s.
- Privacy policy: <https://aljazeera360-mcp.ahmed-26d.workers.dev/privacy> (lists exactly what is logged; 180-day automatic deletion is implemented).
- Documentation: <https://aljazeera360-mcp.ahmed-26d.workers.dev/docs> and the GitHub README.
- Open source (MIT).

**Recommended before submitting:** deploy the directory endpoint with the **core profile** (10 tools, `AJ360_ENABLE_SEO_TOOLS` unset). The 16 SEO/analytics tools are for the content team, and a focused toolset reviews and behaves better for the public.

## Portal answers

### Connection
- URL: `https://mcp.aljazeera360.com/mcp` (after prerequisite 3)
- Transport: Streamable HTTP
- Users: **Universal URL**

### Listing
- **Server name:** Al Jazeera 360
- **Tagline** (≤55): `Watch and explore Al Jazeera 360's Arabic programmes` (51)
- **Categories:** Media & Entertainment · News · Education
- **Description** (≤2,000):

  > Al Jazeera 360 brings Al Jazeera's Arabic streaming platform into Claude. Ask in Arabic or English to find documentaries, investigations, talk shows and podcasts — Al Daheeh, Ma'a Tamim, Al Jazeera Documentary, Atheer, AJ+ Arabic and more — and Claude answers from the live catalog.
  >
  > In Claude, results appear in an interactive view in Al Jazeera 360's own design: the home page's editorial banners and rows, programme pages with every season and episode, and episode details with duration and publish date. Watch opens the official Al Jazeera 360 player.
  >
  > What you can do:
  > • Search the catalog by topic, programme or presenter
  > • Browse trending content and each channel's latest episodes
  > • Open a programme and see all its seasons and episodes
  > • Get the details and watch link of any episode
  >
  > The connector is read-only, needs no account, and only reads the public catalog.

- Documentation URL: README or a help page on aljazeera360.com
- Privacy policy URL: `https://mcp.aljazeera360.com/privacy`
- Support contact: `support@aljazeera360.com`
- Icon: the official AJ360 logo (square PNG)
- Slug: `aljazeera-360` (permanent)

### Use cases
- Primary: discover and watch Al Jazeera 360 programmes from inside Claude.
- Prerequisites for users: none (no account needed; some episodes ask for free sign-in on the site to watch).
- Data: **reads only**.

### Authentication
- **No authentication.**

### Data handling
- API: Al Jazeera 360's own platform API (Vesper/Deltatre), used with Al Jazeera 360's permission (prerequisites 2 and 4).
- Personal health data: no. Sponsored content: no.

### Test & launch
- Test account: not needed; every tool works without sign-in.
- Steps for the reviewer: add the URL as a connector, then try the example prompts below.

### Example prompts (≥3, different tools)
1. `Show me what's trending on Al Jazeera 360` → trending view
2. `ابحث في الجزيرة 360 عن وثائقيات عن غزة` → search
3. `Open the programme «ما الجدوى؟» and list its episodes` → series + episodes
4. `What are the latest Al Jazeera Documentary episodes?` → latest episodes
5. `Play the latest episode of Al Daheeh` → player / watch link

### Allowed link URIs
- `https://www.aljazeera360.com` (owned by Al Jazeera, so allowed only when Al Jazeera submits)

### Compliance
Seven acknowledgments; none conflict (no financial transactions, no AI media generation, no conversation-data collection beyond tool arguments, public docs available).

## Known limitation to mention
Playback inside the chat depends on the host. The Claude iOS app blocks embedding the official player (verified with `run_diagnostics`), so there the view shows a *Watch on Al Jazeera 360* button instead.
