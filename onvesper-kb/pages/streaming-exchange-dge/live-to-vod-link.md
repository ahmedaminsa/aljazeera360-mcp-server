> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/streaming-exchange-dge/live-to-vod-link.md).

# Live to VOD link

A live event on the platform will have a unique link such as: *myservice.com/live/**123456***

This unique link helps your customers get directly to the livestream, and can be used in marketing, social media, or other web content. \
But what if your customer couldn't watch live and wants to catch up?

Each live event can have a single VOD linked to it so that when a customer hits an old live event link, they are automatically re-directed to the on-demand version. This works whether your customer comes from the web, or if they are following an app deep link (through a push notification).

If your live event is automatically archived to the Video Exchange - **there's nothing you need to do**, it will be automatically linked to the Streaming Exchange ID.

However, if you want to manually link a VOD to a live event, that is also possible, using the metadata in the video exchange: [Metadata](/platform-knowledge-base/dve/video/metadata.md).

<figure><img src="/files/pES1vVX4pGQDZvPdb5Tv" alt=""><figcaption><p>Setting the DGE Event ID</p></figcaption></figure>

Simply set the "DGE Event ID" in the VOD metadata to match the live event ID (123456 in the example above). The link will then be established for all customers who hit the old *myservice.com/live/123456* link.

#### Why would I need to do this manually?

If you've used [Vesper Studio](/platform-knowledge-base/vesper-studio/untitled.md) and clipped the original live -> vod archive into a new VOD asset, or if you clipped the original live event straight into a VOD asset to speed up the process, you need to instruct the system as to which VOD to use.

You can also use this feature to direct to a "highlights" video that has been editorially produced rather than a full event re-run.

#### What happens if I give multiple VODs the same DGE live event ID?

The VOD which most recently had the Live event ID added to it will be the one used in the Live -> VOD link. This means you can overwrite the original archive with a clipped version if you prefer, without needing to edit the archived VOD asset's metadata.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/streaming-exchange-dge/live-to-vod-link.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
