> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/analytics-1.md).

# Analytics \[Legacy]

{% hint style="warning" %}
These analytics tools are being deprecated in favour of [Vesper Insights](/platform-knowledge-base/back-office/vesper-insights.md). These legacy functions will be accessible until they are completely replaced by the Insights systems. You are advised not to build new workflows/dependencies on legacy Analytics
{% endhint %}

The 'Analytics' section is where you are able to find out real-times results of your business and content metrics along with reporting from the platform.

![](/files/-M57ZmlmsZ9uIt0dchnm)

[Business Intelligence Dashboard:](/platform-knowledge-base/back-office/analytics-1/business-intelligence-dashboard-mvp.md) Is where you are able to find out real time results for your business.

[Live Dashboard:](/platform-knowledge-base/back-office/analytics-1/live-dashboard.md) Is where you are able to see real time metrics of your content on the platform.

[Reports:](/platform-knowledge-base/back-office/analytics-1/reports.md) Is where you are able to download our 5 different reports: Transaction, Customer, Promo Code, Licence, VOD and Live Event.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/analytics-1.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
