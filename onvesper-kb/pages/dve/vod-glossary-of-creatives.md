> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/dve/vod-glossary-of-creatives.md).

# VOD - Glossary of creatives

Use this glossary to start building your creative strategy when managing content via the Vesper VOD platform.

{% hint style="info" %}
All creatives should be under 1MB in size.
{% endhint %}

| Creative           | Description                                                                          | Dimensions      | Notes                                                                                                                                                                                                                 |
| ------------------ | ------------------------------------------------------------------------------------ | --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Video Thumbnail    | A cover for a video asset in landscape mode                                          | 1920x1080 .jpeg | n/a                                                                                                                                                                                                                   |
| Video Cover        | A thumbnail background image appearing when hovering over it on web                  | 1920x1080 .jpeg | n/a                                                                                                                                                                                                                   |
| Video Poster       | A cover for a video asset in portrait mode                                           | 1142x1600 .jpeg | n/a                                                                                                                                                                                                                   |
| Video Watermark    | A small logo appearing at the top left or top right of a video asset during playback | 250x250 .png    | Watermarks are rendered relative to the video player size, not the video content itself. If a position must be guaranteed, Endeavor Streaming recommends producing your video content with watermarks embedded in it. |
| Playlist Thumbnail | Cover of a playlist in square mode                                                   | 640x704 .jpeg   | n/a                                                                                                                                                                                                                   |
| Playlist Cover     | Background creative for a playlist                                                   | 1920x1080 .jpeg | n/a                                                                                                                                                                                                                   |
| Playlist Poster    | Cover of a playlist in portrait mode                                                 | 1142x1600 .jpeg | n/a                                                                                                                                                                                                                   |
| Playlist Title     | Cover of a playlist in landscape mode                                                | 1920x1080 .jpeg | n/a                                                                                                                                                                                                                   |


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/dve/vod-glossary-of-creatives.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
