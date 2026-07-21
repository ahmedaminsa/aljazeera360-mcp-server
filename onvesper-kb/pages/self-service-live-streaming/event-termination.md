> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/self-service-live-streaming/event-termination.md).

# Event Termination

Once your event has ended, infrastructure must be terminated to stop cost accumulation. Live Management supports both manual termination and automated termination - where at a realm level we can configure that *if an event has passed it's scheduled end-time and there is no active feed being delivered to the endpoint* the platfrom can automatically kill the infrastructure.

### **Manual Termination**

To terminate an event, select **Terminate** from the three-dot actions menu on the event row. You will be prompted to confirm before any action is taken.

{% hint style="success" %}
**Best practice:** Stop the stream at your encoder before terminating in Live Management. While terminating via Live Management will stop the stream on the front end, stopping at the encoder first ensures that the encoder will not continue trying to establish a connection with the endpoint.
{% endhint %}

## **Automated Safeguards**

Live Management includes two optional automated mechanisms to protect against streams being left running unintentionally.

#### **Stream Launcher**

Automatically provisions infrastructure ahead of your event start time, based on a defined lead time  (eg. 30 minutes, 1 hour, 2 hours, or 3 hours before scheduled start time). This ensures infrastructure is ready without requiring manual intervention.

#### **Stream Terminator**

A safety mechanism that automatically shuts down infrastructure when both of the following conditions are met:

* The event's scheduled end time has passed (plus a buffer period)
* No active input feed is detected

For advice on automated safeguards, please discuss with your Account Manager.

{% hint style="warning" %}
**Important:** The Stream Terminator will **not** shut down a stream if it is still active or if the event is still within its scheduled window - both conditions need to be met. Manual termination is required in all other scenarios.
{% endhint %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/self-service-live-streaming/event-termination.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
