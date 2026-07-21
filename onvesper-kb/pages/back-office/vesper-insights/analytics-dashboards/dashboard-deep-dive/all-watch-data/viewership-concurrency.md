> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/vesper-insights/analytics-dashboards/dashboard-deep-dive/all-watch-data/viewership-concurrency.md).

# Viewership Concurrency

<figure><img src="/files/XZ0DT52dbwNJUpfpjNjo" alt=""><figcaption></figcaption></figure>

Date range for analysis - Longer timeframes may result in longer dashboard load times

<figure><img src="/files/qTdS83DRPzq1SX8JQpdS" alt=""><figcaption></figcaption></figure>

Peak Concurrency shows the max number of concurrent views per minute for the duration chosen

Average Concurrency shows the average number of concurrent views per minute for the duration chosen.&#x20;

**How is concurrency calculated?**&#x20;

The following diagram shows how peak concurrency is calculated using the orignal timestamps of the viewer whilst viewing content.

<figure><img src="/files/dcKkG8u3iDMitvbMk6mU" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/aOdWtyePsUFyVXzqhn8O" alt=""><figcaption></figcaption></figure>

Filter data set by type of video being watched (Live/VOD)


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/vesper-insights/analytics-dashboards/dashboard-deep-dive/all-watch-data/viewership-concurrency.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
