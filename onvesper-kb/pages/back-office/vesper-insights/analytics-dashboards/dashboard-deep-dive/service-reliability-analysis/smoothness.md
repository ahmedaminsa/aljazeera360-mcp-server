> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/vesper-insights/analytics-dashboards/dashboard-deep-dive/service-reliability-analysis/smoothness.md).

# Smoothness

<figure><img src="/files/EwZzMReSb1aFEzHAOY0T" alt=""><figcaption></figcaption></figure>

View Start - Utilise session View Start timestamp for analytics\
View Eng - Utilise session View End timestamp for analytics

<figure><img src="/files/NwbF2osxZUgKKlrCTMxh" alt=""><figcaption></figcaption></figure>

Date range for analysis - Longer timeframes may result in longer dashboard load times

<figure><img src="/files/6HmQwEe4d6ppWIep44rE" alt=""><figcaption></figcaption></figure>

**Smoothness Score** - measures the amount of rebuffering a viewer sees when watching video. A higher Smoothness Score means the viewer experiences less rebuffering, while a lower score means a viewer sees more rebuffering.\
**Rebuffer Percentage(%)** - measures the volume of rebuffering that is occurring across the platform.\
**Rebuffer Frequency** - Rebuffer Frequency measures how often rebuffering events happen.\
\
Following metrics are broken into 2 analytics groupings:

* Median (50th Percentile) – Helps understand a typical experience (half are better than this number, half are worse)
* 95th Percentile – Helps understand what a poorer experience is like on your applications, while excluding outliers and happening frequently enough (at least 1 in 20 views).

**Rebuffer Duration** - the amount of time in seconds that viewers wait for rebuffering per video view.\
**Rebuffer Count** - the number of rebuffering events that happen during video views.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/vesper-insights/analytics-dashboards/dashboard-deep-dive/service-reliability-analysis/smoothness.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
