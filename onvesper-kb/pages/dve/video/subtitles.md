> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/dve/video/subtitles.md).

# Subtitles

Vesper supports uploading subtitles for videos in a SCC, SRT or VTT format. Depending on your encoding presets, subtitles will be associated with the video in one of two ways.

To verify which method is being utilised by your VOD content, please contact your account management team.

### Side car Subtitles

The file is separated from the video and video manifest. It is provided to the player at playback and the player displays on-screen text according to the current position of the playback head.

This method is fast to make edits, as it does not require the subtitles to be part of video content in any way. However, it is not compatible with Server Side Ad Insertion (SSAI), or certain playback methods (such as Apple AirPlay). If the video is manipulated and elongated at delivery to the consumer (e.g. an SSAI ad has been injected at the beginning or middle of the content), the timestamps of the subtitles cannot be updated, so they would be shown out of sync with the content.

### Embedded Subtitles

The subtitles file is read and embedded into the video manifest which will be delivered to any video players in a widely supported standard.

As the subtitles are part of the manifest, the timing of display will be correctly updated with any manifest edits (such as SSAI ad insertion). The embedded subtitles are also supported by more device types and players.

Any updates to the subtitles require edits to the manifest, which in turn may require a re-transcode of the video content. This means that to edit subtitles or include new subtitles in the Vesper VOD UI, a new [Content Source](/platform-knowledge-base/dve/video/video-content-sources-management.md) must be created. We recommend that all subtitles are defined and uploaded with an asset when it is first uploaded to Vesper VOD - to reduce costs.

With Embedded subtitles, you are able to utilise the advanced features discussed in [Subtitle Variants](/platform-knowledge-base/dve/video/subtitles/subtitle-variants.md).

{% hint style="info" %}
If you need to switch from side-car to embedded subtitles - please contact your platform account manager to discuss the process.
{% endhint %}

### Burned-in Subtitles

{% hint style="danger" %}
These subtitles are not part of the Vesper product or delivery. Vesper cannot burn-in subtitles, nor can they be edited. The term is defined here only to delineate it from the term "Embedded" subtitles.
{% endhint %}

Subtitles could be burned-in (or rendered) to the video content uploaded to the Vesper platform. In this way they become part of the video content. This is sometimes used for forced-narrative subtitles when the content producer wants to include stylized translations (see the John Wick franchise for examples).


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/dve/video/subtitles.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
