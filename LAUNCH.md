# Launch Checklist — Al Jazeera 360 MCP Server

Everything needed to launch, in order. Items marked **[you]** need your
authenticated access (a dashboard login or an interactive OAuth) that automation
can't reach — each is a copy-paste command or a short form. Everything else is
already in the repo.

---

## 0. Pre-flight (already done ✅)

- [x] v2.0.0 code, 24 tools, 3 transports, analytics dashboard
- [x] Tool profiles: 8 core (default) / 24 full (`AJ360_ENABLE_SEO_TOOLS=1`)
- [x] Hosted instance live on Railway
- [x] `server.json` registry manifest (in repo root)
- [x] Marketing content drafted (`marketing/`)
- [x] Disclaimer + Quick Connect in README
- [x] Daily live-check CI workflow

---

## 1. Repo secrets — **[you]** (GitHub UI, 2 min)

So the daily `live-check.yml` live-API job passes.

Go to **repo → Settings → Secrets and variables → Actions → New repository secret** and add:

| Name | Value |
| :--- | :--- |
| `AJ360_API_KEY` | the platform API key (from browser DevTools → Network → any request to `dce-frontoffice.imggaming.com`) |
| `AJ360_REFRESH_TOKEN` | optional — from `localStorage.getItem('dice:refreshToken')` after logging in |

---

## 2. Decide the hosted instance's tool profile — **[you]** (Railway UI, 1 min)

Right now the hosted instance still serves **all 24 tools**. For the public
instance, the 8-tool core profile gives end users better tool selection.

- **To switch it to 8 core tools (recommended for the public URL):** in Railway
  → your service → **Variables**, make sure `AJ360_ENABLE_SEO_TOOLS` is **not
  set** (or `0`), then redeploy.
- **To keep all 24 on the hosted instance:** set `AJ360_ENABLE_SEO_TOOLS=1`.

(Either way, anyone self-hosting controls their own profile via the same var.)

---

## 3. Publish to the official MCP Registry — **[you]** (one-time, ~5 min)

The manifest (`server.json`) is ready. Publishing under the `io.github.ahmedaminsa/*`
namespace just needs you to prove you're that GitHub user.

```bash
# from the repo root
# 1. get the publisher CLI (see github.com/modelcontextprotocol/registry for the latest install)
#    e.g. via Go: go install github.com/modelcontextprotocol/registry/cmd/mcp-publisher@latest
#    or download the binary from the registry repo's releases

# 2. authenticate as your GitHub user (opens browser once)
mcp-publisher login github

# 3. publish
mcp-publisher publish
```

This lists you in the registry that Smithery, Glama, PulseMCP, and others index —
so several directories pick you up automatically afterward.

> After you publish to PyPI (optional, step 5), add a `packages` entry to
> `server.json` and re-run `mcp-publisher publish` to bump the version.

---

## 4. Registry / directory submissions — **[you]** (web forms, ~10 min total)

Most of these read your GitHub repo or the MCP Registry, so submission is mostly
"paste the repo URL and confirm." Pre-filled details below.

| Directory | Where | Notes |
| :--- | :--- | :--- |
| **Smithery** | smithery.ai → Add Server | Connect the GitHub repo; `smithery.yaml` is already in the repo |
| **mcp.so** | mcp.so → Submit | Paste repo URL |
| **Glama** | glama.ai/mcp/servers → Add | Often auto-indexes from the MCP Registry after step 3 |
| **PulseMCP** | pulsemcp.com → Submit a server | Paste repo URL |

**Paste-ready copy for the forms:**

- **Name:** Al Jazeera 360
- **Tagline:** Connect AI assistants to Al Jazeera 360's Arabic streaming catalog.
- **Description:** An MCP server that gives AI tools real-time access to Al Jazeera 360's library — documentaries, podcasts, talk shows, and investigative programs — returning real metadata and direct watch links. Zero-install hosted instance available. 8 core discovery tools plus an optional pro profile with 16 SEO/analytics tools.
- **Category/Tags:** media, video, streaming, arabic, news, search
- **Repo:** https://github.com/ahmedaminsa/aljazeera360-mcp-server
- **Hosted URL:** https://aljazeera360-mcp-server-production.up.railway.app/mcp

---

## 5. (Optional) Publish to PyPI — **[you]** (~15 min)

Gives people `uvx aljazeera360-mcp` for local use.

```bash
pip install build twine
python -m build
twine upload dist/*          # needs a PyPI account + API token
uvx aljazeera360-mcp         # verify
```

Then add a `packages` block to `server.json` and re-publish (step 3).

---

## 6. Marketing — **[you]** (content is written, in `marketing/`)

Suggested sequence over ~1 week:

1. **Day 1 — soft launch:** post `marketing/x-thread-ar.md` (Arabic) + LinkedIn.
   Also r/ClaudeAI (`marketing/reddit.md`).
2. **Day 2:** publish `marketing/devto-post.md` on dev.to / Hashnode.
3. **Day 3 — Show HN:** post `marketing/show-hn.md` Tue–Thu ~9am US Eastern,
   add the first comment immediately.
4. **Day 4:** r/LocalLLaMA + r/SideProject.
5. **Week 2+:** reply to every comment/issue; watch the analytics dashboard fill up.

**Before posting:** try it yourself first (connect the hosted URL in Claude and
run a few queries) so the dashboard isn't empty when the first curious person checks.

---

## 7. Later — the Al Jazeera B2B angle

After ~a month of usage data, the analytics dashboard becomes your pitch deck:
"AI assistants requested your content N times this month; here are tools that
improve your visibility in AI search." Reach out to Al Jazeera with real numbers,
not a cold idea.
