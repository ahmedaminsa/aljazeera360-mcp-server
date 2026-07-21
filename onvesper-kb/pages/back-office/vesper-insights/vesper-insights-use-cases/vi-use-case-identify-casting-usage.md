> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/vesper-insights/vesper-insights-use-cases/vi-use-case-identify-casting-usage.md).

# VI Use Case - Identify Casting Usage

## Use Case

Users often cast content from their mobile devices to larger screens using Google Chromecast or Apple AirPlay protocols. Vesper Insights enables you to track how many users are utilizing this feature. This data can help you decide whether to expand your portfolio by supporting additional TV devices or leverage the high mobile usage to promote other app experiences, such as gaming, graphs, dashboards, and more.

## Dashboard

To view data by **Remote Played** on the dashboard:

* Go to Insights on Vesper Back Office and select the [All Watch Data](/platform-knowledge-base/back-office/vesper-insights/analytics-dashboards/dashboard-deep-dive/all-watch-data.md) dashboard
* In the **List by** dropdown, select **Remote Played**
* You can choose to view data for users who cast content (**True**) or those who did not (**False**)
* Use the **View Usage By** dropdown to select whether you'd like to analyze total hours of usage or the number of unique users who cast content
* Click **Apply** to view the results


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/vesper-insights/vesper-insights-use-cases/vi-use-case-identify-casting-usage.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
