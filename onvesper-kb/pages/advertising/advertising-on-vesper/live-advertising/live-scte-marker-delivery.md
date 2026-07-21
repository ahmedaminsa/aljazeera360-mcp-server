> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/advertising/advertising-on-vesper/live-advertising/live-scte-marker-delivery.md).

# Live: SCTE Marker Delivery

## Live: SCTE Marker Delivery

* SCTE markers should be delivered under a separate PID in the MPEG-TS feed if ads are meant to be supported.
* Only `splice_insert()` and `time_signal()` commands are supported.

### Splice Insert

* `splice_insert()` commands are used to signal "splice" events were new content, such as ads, should be inserted into a presentation
* If the feed carries multiple tiers of ads (network, provider, local etc.) they each should use unique `program_id` attribute of the `splice_insert()` command. We will need to be provided which `program_id` value should be used for digital ad delivery for each channel.
* `splice_insert()` commands should use `event_id` attribute to distinguish different ad events within the feed.
* if a `splice_insert()` OUT command has the `duration` attribute set it will be used for returning back into network feed, unless a corresponding `splice_insert()` IN command with a matching `event_id` attribute is sent before. In such case the `duration` attribute will be ignored.
* if a `splice_insert()` OUT command is provided without `duration` attribute there *must* be a corresponding `splice_insert()` IN command sent to signal when to return back to network feed.

### Time Signal

* `time_signal()` commands are used to signal that the ad stitcher should begin prefecting ads for an upcoming break
* Different `Segmentation UPID Type` can be filtered to limit which types trigger prefetches
* The `segmentation_upid` contains metadata about upcoming breaks, e.g:
  * `"segmentation_upid": "{"type" : "next", "pid" : 012345, "genre" : news}"`


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/advertising/advertising-on-vesper/live-advertising/live-scte-marker-delivery.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
