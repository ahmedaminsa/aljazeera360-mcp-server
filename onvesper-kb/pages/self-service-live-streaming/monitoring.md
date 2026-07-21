> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/self-service-live-streaming/monitoring.md).

# Monitoring

Live Management provides built-in tools for monitoring your streams both before and during broadcast, without needing to leave the Live Management screen.

**Single Stream Preview**

To monitor an individual stream, select **Preview stream** from either the quick-access icon on the event row or the three-dot actions menu. This opens a player panel on the right-hand side of the main screen, allowing you to view the stream alongside your event list.

The preview player indicates whether the stream is currently in a published state — giving you a quick visual confirmation of what your viewers are seeing.

**Multi-View Monitoring**

If you need to monitor multiple streams simultaneously, use the **Multi-View** button in the top right of the screen. This allows you to open the multi-stream player in one of three ways:

* **Open Tab** — opens Multi-View in a new browser tab
* **Open Picture-in-Picture** — floats the player over your current screen
* **Open Popup Window** — opens Multi-View in a separate browser window

To populate the Multi-View panel, select **Add to multi-view** from the icon in the top right of screen or the three-dot actions menu on indivdual events.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/self-service-live-streaming/monitoring.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
