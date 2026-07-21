> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/self-service-live-streaming/cost-tracking.md).

# Cost Tracking

Live Management includes a Cost Estimator that gives you a real-time view of your estimated live streaming for each event.

**Accessing the Cost Estimator**

The tool is accessed via the **Cost Estimator** tab at the top of the main screen.

**What it Shows**

The Cost Estimator displays a running estimate of costs based on:

* How long the event has been active
* The per-hour cost for the specific delivery&#x20;

As infrastructure runs, the estimated cost updates in real time, giving you an at-a-glance view of your current spend.

{% hint style="info" %}
**Please note:** The Cost Estimator is intended as an illustrative guide only. Figures displayed are estimates and are not guaranteed to match your final invoice. For billing queries, contact your Commercial Account Manager.
{% endhint %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/self-service-live-streaming/cost-tracking.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
