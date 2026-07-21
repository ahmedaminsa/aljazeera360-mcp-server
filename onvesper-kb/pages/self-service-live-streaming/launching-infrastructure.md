> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/self-service-live-streaming/launching-infrastructure.md).

# Launching Infrastructure

Before a stream can go live, infrastructure must be launched for the event. This spins up the cloud components needed to ingest and transcode your stream, and is managed at the individual event level.

**How Infrastructure is Launched**

Infrastructure can be launched in two ways:

* **Automatically** — based on a pre-configured lead time set for your account (e.g. 3 hours before the event start time). No action is required from you
* **Manually** — by selecting **Launch** from the three-dot actions menu on the event row in the Events list

{% hint style="info" %}
**Important:** Cost accumulation begins from the moment infrastructure is launched, whether triggered automatically or manually. You are responsible for costs from this point onwards.
{% endhint %}

**Event Status: Upcoming → Provisioned**

Once launched, the event status changes from **Upcoming** to **Provisioned**. At this point the stream is ready to receive an input feed.

**Retrieving Input Details**

Once an event is live (status: **Published**), you can retrieve the connection details needed to send your input feed. Select **View input info** from the three-dot actions menu to open the Input Details panel, which displays connection information for Zixi, SRT & RTMP protocols - it is important to retrieve the correct details for your chosen delivery method.

| Protocol | Details provided                     |
| -------- | ------------------------------------ |
| **Zixi** | Server URL, Stream Key, Full Details |
| **SRT**  | Server URL, Stream Key, Full Details |
| **RTMP** | Server URL, Stream Key, Full Details |

You can toggle **Show Port Information** within the panel to display or hide port numbers alongside the connection details, this may be significant depending on the encoder being used.

Endpoint details can then be used to establish the ingest connection.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/self-service-live-streaming/launching-infrastructure.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
