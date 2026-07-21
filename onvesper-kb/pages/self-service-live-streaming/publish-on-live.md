> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/self-service-live-streaming/publish-on-live.md).

# Publish on Live

Live Management supports two publishing modes:&#x20;

#### Auto-publish (default):&#x20;

The stream will go live once the connection has been established and the feed is being delivered.

#### Manual publish:&#x20;

Manual publish allows you to send and monitor your stream before making it available to viewers. This is useful for:

* Validating audio and video quality before broadcast
* Testing your feed in advance of the scheduled start time
* Resetting the DVR window before the public stream begins

When Manual Publish is enabled, the stream is ingested and visible within the monitoring panel but is **not** published to end users. When you are satisfied the feed is healthy, you can push it live using the **Publish Live** control, which appears below the preview window.

### **Resetting the DVR**

A **Reset DVR** control is available within the stream preview panel. When triggered, it clears the existing buffer and starts a fresh playback window from that point forward.

This can be used at any point, but may be specifically needed as part of the Manual Publish flow, to ensure end users can not scrub back to any content that played out before the publish time.

{% hint style="warning" %}
**Important:** Infrastructure and CDN costs apply during preview.&#x20;
{% endhint %}

{% hint style="info" %}
**Note:** Manual Publish is an optional configuration that must be set up in advance and once enabled applied to all events - there are no existing safeguards against an operator not publishing. Speak to your Account Manager if you'd like to discuss using Manual Publish.
{% endhint %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/self-service-live-streaming/publish-on-live.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
