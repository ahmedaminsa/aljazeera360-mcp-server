> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/consumer-experience/web/link-to-a-moment-within-a-video.md).

# Link to a moment within a video

Vesper web supports linking directly to a timestamp within a live or VOD video. To achieve this, simply add a "t" URL parameter to the Vesper link:

```
t=60
```

The value is the time in seconds to pre-seek to. So in the example above, the video will start at one minute in.

Full URL examples:

```
https://www.mygreatvesperstreamingservice/video/12345?t=60

https://www.mygreatvesperstreamingservice/video/12345?utm=xyz&t=60
```

#### In live events

This feature is also supported on the live video player (/live/12345) - however the behaviour will depend on the DVR window assigned to the live event.

The timecode is always relative to the start time. So, if your live event started 90 minutes ago, and you want to link to something that happened at the 60 minute mark you can use `t=3600`. For this to work, you must have a full 90 minute DVR window, in other words, your users would be able to rewind to the beginning of the event.

If, in the example above, your event was 3 hours long, but you only had a 90 minute DVR window, then after the DVR window is exceeded, that `t=3600` would shift to being relative to the beginning of the DVR window that is available.

This may serve a use case you have in mind, but in general we recommend against using this parameter for live events, given that the default experience is always to join the content live.

### Link to a moment of a VOD with Embed Player

If you are using the [Embed Player](/platform-knowledge-base/back-office/content/embed-player.md) to embed a VOD on a third party site, you can specify a timecode to start at using the `s=` parameter. This parameter is the "start at" parameter but accepts the same seconds value as referenced above on this page.

```
s=60
```

Add this parameter into the URL of your embed iframe, as in the example below, which will start 10 seconds into the video:

<pre class="language-html" data-overflow="wrap"><code class="lang-html">&#x3C;iframe src="https://doris-embed.diceplatform.com/player/2/index.html?r=dce.showcase&#x26;c=31&#x26;v=898398&#x26;t=vod<a data-footnote-ref href="#user-content-fn-1">&#x26;s=10</a>" title="Embed player" width="560" height="315" frameborder="0" allow="autoplay; encrypted-media; picture-in-picture;" allowfullscreen>&#x3C;/iframe>
</code></pre>

[^1]: This is the added parameter


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/consumer-experience/web/link-to-a-moment-within-a-video.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
