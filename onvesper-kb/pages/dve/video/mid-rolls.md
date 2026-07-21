> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/dve/video/mid-rolls.md).

# Mid-Rolls

The Vesper Platform allows residents to incorporate dynamic ad insertion into their content, enabling ads to be triggered at various points: pre-roll (beginning of the video), mid-roll (during the event), or post-roll (end of the video). While pre-roll and post-roll ads can be defined by the video or playback itself, mid-roll ads require specific markers—either SCTE35 markers in a live feed or CUE points in a VOD asset.

For VOD assets, the VOD Vesper Platform (DVE) allows content managers to insert these CUE points that will trigger mid-roll ads when dynamic ad insertion is enabled in the platform.

CUE points can be added in two ways:

* **Individually**: manually insert markers into the VOD metadata. To do this, click *Midrolls* below the video playback window, and then either:

  * Click *Add at Current Time* to use the exact time where you have paused the playback

  <figure><img src="/files/2bC3q6v2k7In9iEDZj1M" alt=""><figcaption></figcaption></figure>

  * Click *+ Add Another* to manually enter the desired breaks (in hours, minutes, and seconds)

  <figure><img src="/files/X3jSqgFMUK1RDFg6ASRm" alt=""><figcaption></figcaption></figure>
* **In Batch**: use the *Batch Upload* tool to add mid-roll points to multiple VOD files at once by including the points in a CSV file. For more details, please refer to the [Updating Batch VOD's](/platform-knowledge-base/dve/batch-video-upload-via-ui/updating-batch-vods.md)

Once the configuration is saved and the integration with the SSP is correct, mid-roll ads will be triggered at the specified points.&#x20;


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/dve/video/mid-rolls.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
