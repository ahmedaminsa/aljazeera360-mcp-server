> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/dve/live-to-vod-archiving.md).

# Live to VOD archiving

When a live event finishes, a temporary asset is created using the video data that was streamed live (essentially a DVR playback). This temporary asset remains available on the CDN (content delivery network) whilst the permanent VOD asset is processed. This is so there is no material loss of access to the content to end users while the permanent asset is processing, allowing end users to have immediate retroactive access to the event. After processing, the permanent asset is clipped so the pre/post-slates are removed and a new VOD asset is generated.&#x20;

The series of events is shown below:

1. Live event ends.
2. Temporary VOD asset generated (**VOD\_ID\_1**) and published on the front end still containing slates – currently playing back from Live Event Archive (DVR)
3. Live event archive completes processing into permanent asset (still **VOD\_ID\_1**) and remains published on front end still containing slates – currently playing back from permanent VOD asset
4. **VOD\_ID\_1** is edited by relevant content management team to clip out the slates and new asset is generated, **VOD\_ID\_2**.&#x20;
5. **VOD\_ID\_1** is unpublished and no longer accessible to end users. **VOD\_ID\_2** is published as a replacement.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/dve/live-to-vod-archiving.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
