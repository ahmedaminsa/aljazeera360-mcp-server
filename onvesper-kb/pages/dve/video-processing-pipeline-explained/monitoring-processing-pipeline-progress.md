> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/dve/video-processing-pipeline-explained/monitoring-processing-pipeline-progress.md).

# Monitoring Processing Pipeline Progress

<figure><img src="/files/j7wc1f2tl0rjZcUHKcSH" alt=""><figcaption><p>Old VOD UI</p></figcaption></figure>

<figure><img src="/files/6soc54W5FnzutFYbiK51" alt=""><figcaption><p>New VOD UI</p></figcaption></figure>

Each uploaded VOD moves through the following stages in sequence (as described in [Video Processing Pipeline explained](/platform-knowledge-base/dve/video-processing-pipeline-explained.md)):&#x20;

**1. Initialisation** \
This is where the VOD record is created and registered in the platform. Prepackaging logic is also triggered if relevant, preparing the system for asset ingestion.&#x20;

**2. Demuxing** \
The uploaded asset is split into separate video and audio streams. This is necessary to allow encoding, which works independently on audio and video tracks.&#x20;

**3. Encoding** \
The video and audio tracks are transcoded into multiple renditions at different bitrates and resolutions according to your configured encoding presets. This ensures adaptive streaming works across varying device types and network conditions.&#x20;

**4. Packaging** \
The encoded renditions are wrapped into delivery formats such as HLS and DASH. Audio and video are also packaged separately, following modern streaming standards. Any download-to-go configurations will also be packaged here.

**5. Manifest Creation** \
Master playlists and manifests are generated to tell the player which renditions are available and how to access them.&#x20;

**6. Saving Processing Results** \
The final step involves saving the VOD metadata and linking all generated assets so that the content becomes accessible in the DVE and available for playback or further workflows.&#x20;

Each job within each pipeline stage includes:&#x20;

* Job name and parameters (e.g. bitrate, resolution)&#x20;
* Timestamps for created, started, and completed&#x20;
* Duration&#x20;
* Status (Scheduled/Processing/Completed/Failed)&#x20;
* Job ID (with copy function)&#x20;

<figure><img src="/files/ivijK23U5rUPrJ5wbzIK" alt=""><figcaption><p>View overall stage progress</p></figcaption></figure>

<figure><img src="/files/L9SzE5RhcWk7hH0oUD0H" alt=""><figcaption><p>Expand each step for a detailed view</p></figcaption></figure>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/dve/video-processing-pipeline-explained/monitoring-processing-pipeline-progress.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
