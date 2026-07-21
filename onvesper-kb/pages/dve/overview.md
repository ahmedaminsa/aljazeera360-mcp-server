> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/dve/overview.md).

# Overview

[**Video Exchange (DVE)**](https://vod.onvesper.com) is designed to make transforming your video archive into a highly-consumable, intelligently managed online library of content. Our simple, intuitive video management interface allows for self-service localisation, metadata augmentation and can be integrated as a standalone service for your websites, apps and any other part of your digital ecosystem that could benefit from flawless on-demand video playback. The Video Exchange (DVE) platform capabilities include:

* [**Videos**](/platform-knowledge-base/dve/video.md): Editorially managing VOD content for your Vesper Realm
* [**Playlists**](/platform-knowledge-base/dve/curating-grouped-content/playlists.md)**:** Helping compilation management and distribution of your large VOD Catalogue
* [**Collections**](/platform-knowledge-base/dve/curating-grouped-content/collections-and-series.md)**:** A collection of playlists listed in a chronological format. eg Seasons within a show.
* [**Analytics**](/platform-knowledge-base/back-office/analytics-1.md)**:** A natively integrated analytics tool to help you understand how your content is being consumed, by who, where and on what device.
* [**Geo-Blocking**](/platform-knowledge-base/dve/geo-blocking.md)**:** Providing a tool to distribute your content in specific regions or blocking against distribution in restricted regions.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/dve/overview.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
