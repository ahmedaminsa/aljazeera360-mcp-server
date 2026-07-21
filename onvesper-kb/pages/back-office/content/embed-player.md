> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/content/embed-player.md).

# Embed Player

Enabling the Embed Player feature on your realm will require approval from your Commercial Account Manager and config work from your Technical Account Manager. Once this has been completed, you can proceed with [Embed Player Config](/platform-knowledge-base/back-office/content/embed-player/embed-player-config.md)

The Embed Player allows residents to stream both VOD and live events outside of the platform’s native environment by embedding a video player directly onto any webpage they choose. This makes it easy to extend reach and integrate content into external sites, blogs, or partner pages.

Key characteristics:

* **Flexible placement** — can be embedded on any webpage.
* **Open access** — content must be free to view, without geo-blocking restrictions.
* **Seamless streaming** — supports both on-demand and live video playback.
* **Consistent branding** — player retains platform’s look and feel across external sites.

This feature is particularly useful for promotional campaigns, free previews, or broad audience engagement where you want maximum accessibility without limiting viewers by geography or paywall.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/content/embed-player.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
