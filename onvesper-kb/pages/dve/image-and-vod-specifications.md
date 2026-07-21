> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/dve/image-and-vod-specifications.md).

# Image and VOD Specifications

The Video Exchange (DVE) has a series of specifications across the platform. Here's a quick summary below.

### Video/Audio

{% tabs %}
{% tab title="Video" %}

| Dimension          | Value                     |
| ------------------ | ------------------------- |
| Dimension          | 1920×1080                 |
| Format             | MPEG4                     |
| Codec              | h.264                     |
| Bitrate            | 11808 kbps                |
| Bitrate Mode       | Constant                  |
| Framerate          | 25/30 fps                 |
| Format Profile     | High/4.1                  |
| Scan Type          | Progressive/De Interlaced |
| Chroma Subsampling | 4:2:0                     |
| File Size          | Less than 128 GB          |
| {% endtab %}       |                           |

{% tab title="Audio" %}

| Audio Codec   | AAC      |
| ------------- | -------- |
| Audio Bitrate | 128kbps  |
| Bitrate Mode  | Constant |
| Sample Rate   | 48.0 KHz |
| {% endtab %}  |          |
| {% endtabs %} |          |

### Images / Creatives

Specifications and recommendations are provided in the table; see under table for usage and general guidelines.

{% hint style="info" %}
The **Artwork 2.0** column shows the equivalent art type in the updated system. See [New: Artwork 2.0](/platform-knowledge-base/dve/video/new-artwork-2.0.md) for full details on migrating to the new artwork system.
{% endhint %}

<table><thead><tr><th width="100">Image for</th><th width="120.45703125">Artwork 2.0 equivalent</th><th width="121.3828125">Size + Aspect Ratio</th><th width="256.875">Purpose</th><th width="149.28515625">Example</th></tr></thead><tbody><tr><td>Poster</td><td>Poster (Legacy) — v1</td><td>1142 x 1600 (5:7 OR 2:3**)</td><td>"Print poster" that highlights the Title. Best used for consistent representation of both series and movies on editorially curated content rows that have been set to "poster" display.</td><td><img src="/files/JVr9ltly1UaZFyR6gTLT" alt="" data-size="original"></td></tr><tr><td>Cover</td><td>Thumbnail (Landscape) — v2 (card hover)<br><br>Interstitial Landscape — v1 (background/interstitial)<br><br>See <a href="https://app.gitbook.com/o/-Lu4VWsQtr5guXJ4j8MW/s/-LvKlMqUAgpPfEFkrjiJ/~/edit/~/changes/854/dve/video/new-artwork-2.0#playlists-and-collections">note on Cover</a></td><td>1920 x 1080 (16:9)</td><td>Photography/image that can be used in background of UI pages.</td><td><img src="/files/GXjyAlUg8g6nalXrnO79" alt="" data-size="original"></td></tr><tr><td>Title Image</td><td>Thumbnail (Landscape) — v3</td><td>1920 x 1080 (16:9)</td><td>Alternative representation of branded artwork (like poster), that will be used for Series &#x26; Seasons in 16:9 UI locations including search and section rows. <strong>Not presently used for VODs</strong> but it is recommended to include for future use cases.</td><td><img src="/files/gq3OyZYglKHlYrM5Uwex" alt="" data-size="original"></td></tr><tr><td>Title Logo</td><td>Title Logo Landscape — v1</td><td>1920 x 1080 (16:9)</td><td>Transparent background image of the Title's logo that can be shown on interstitial pages. It will most often be seen overlaid on top of the <strong>Cover</strong>.</td><td><img src="/files/fSt28GIADNDUiWCHTfog" alt="" data-size="original"></td></tr><tr><td>Thumbnail</td><td>Thumbnail (Landscape) — v1</td><td>1920 x 1080 (16:9)</td><td><p>Required, thumbnail representing the video. Used in interstitial pages to represent episodes in a list, as well as for all VOD content in search results and on editorially curated content rows that are not configured to use the poster.</p><p>For episodes this will likely be a key scene from the episode. For standalone VODs and Movies, you are recommended to still include branding if applicable (similar to title image).</p></td><td><img src="/files/shiECRuG0EVsAvZV9R1C" alt="" data-size="original"><img src="/files/jeWmOospgu7boV5q90Cc" alt=""></td></tr><tr><td>Playlist Card Thumbnail</td><td>Thumbnail (Square) (Legacy) — v1</td><td>640 x 704</td><td>Card that will be used on section pages when showing multiple playlists in a single rail.</td><td><img src="/files/raegFPr4yjuQ0lw3VT5N" alt="" data-size="original"></td></tr></tbody></table>

\*\* Whilst the default is 5:7, Posters can be shown as 2:3 across the platform. Contact your account manager if you wish to adjust this setting.

When considering your artwork and creatives, the general guideline is:

You should apply branding (i.e. stylised text as logos) to **Posters** and **Title Images**. The same goes for **Title Logo** as it is, by nature, the stylised text. It is *optional* to also include some kind of branding in Thumbnail assets — we recommend avoiding the corners (particularly top left and top right) for creative, as platform metadata can be rendered over those locations.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/dve/image-and-vod-specifications.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
