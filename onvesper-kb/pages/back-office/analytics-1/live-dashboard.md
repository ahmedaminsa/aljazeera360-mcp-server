> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/analytics-1/live-dashboard.md).

# Live Dashboard

Under the Analytics drop-down you will notice an option called Live Dashboard, this is where you are able to get real time metrics of the content on your platform. This dashboard provides real-times metrics of the content being consumed on your platform at that time.

![Live Dashboard](/files/-M57ZmlmsZ9uIt0dchnm)

When selected you will taken to Live Dashboard where once loaded your will see that it will populate with real time metrics from your platform.

![](/files/-M58-AN_eLL3QgdvNfcw)

**Total Concurrency:** This will show you the total numbers of users who are currently active on your platform at that time.

**Live Concurrency:** This will show you the total number of active users who are currently watching a live event on your platform at that time.

**VOD Concurrency:** This will show you the total number of active users who are currently watching a video on your platform at that time.

**Live Events:** This will show you the most popular viewed live events on your platform at that time.

**On Demand Videos:** This will show you the most popular viewed videos on your platform at that time.

**Top Devices:** This will show you the top 5 most used devices to view the content on your platform at that time.

**Top Countries:** This will show the top 5 countries who are currently active on your platform at that time.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/analytics-1/live-dashboard.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
