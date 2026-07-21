> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/self-service-live-streaming/navigating-the-ui.md).

# Navigating the UI

When enabled, Live Management is accessed in Back Office via the Content tab

When you open Live Management, you land on the **Events** tab — a table of all your scheduled events showing:

* **Event name** — including the parent Tournament and a unique event ID
* **Status** — e.g. Published, Upcoming... - with a cost indicator where applicable
* **Event start and end times**
* **Actions menu** — accessible via the three-dot icon on the right of each row

At the top of the screen you'll see two key controls:

* **Create New** — starts the creation flow for a new event or tournament
* **Multi-View** — opens the multiplayer monitoring panel. Clicking this gives you three options: Open Tab, Open Picture-in-Picture, or Open Popup Window

**Tabs**

The UI is organised into three tabs:

* **Events** — the primary working view; lists all live events
* **Tournaments** — view of all scheduled Tournaments, each showing the Tournament name, ID, date range, and indicators for Events, Live status, and DRM configuration
* **Cost Estimator** — view estimated costs for your current streams

**Event Row Actions**

Each row in the Events list includes two quick-access icons to the left:

* **Add to Multi-View** — adds the stream to your multiplayer monitoring panel
* **Preview Stream** — opens the stream monitor for that event

The three-dot actions menu on the right of each row provides additional options:

* **Preview stream** — opens the stream monitor
* **Add to multi-view** — adds to the monitoring panel
* **Edit Event** — opens the event for editing
* **Clone Event** — creates a copy of the event
* **Terminate** — shuts down the stream and infrastructure
* **Delete event** — permanently removes the event


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/self-service-live-streaming/navigating-the-ui.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
