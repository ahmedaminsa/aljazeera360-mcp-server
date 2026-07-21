> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/vesper-insights/faqs/segments-vs-cohorts-whats-the-difference.md).

# Segments vs Cohorts: What's the difference?

[Segments](/platform-knowledge-base/back-office/vesper-insights/analytics-dashboards/dashboard-controls/segments.md) allow you to monitor a set of criteria for users who fall into/out of validity\
e.g. all users who watched a VOD of a tentpole event in the past month so they can be contacted with marketing for tickets of the next upcoming event.

[Cohort](/platform-knowledge-base/back-office/vesper-insights/analytics-dashboards/dashboard-controls/cohort.md) allow you to monitor a static set of users across time and dashboards.\
e.g. all users who purchased a PPV package on your application could be added to a cohort; this specific cohort of users could offer insight into the content most likely to onboard new purchases based on which content is the most popular in this cohort over the course of the next 6 months.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/vesper-insights/faqs/segments-vs-cohorts-whats-the-difference.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
