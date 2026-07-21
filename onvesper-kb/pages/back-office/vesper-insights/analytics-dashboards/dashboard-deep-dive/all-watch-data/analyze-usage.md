> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/vesper-insights/analytics-dashboards/dashboard-deep-dive/all-watch-data/analyze-usage.md).

# Analyze Usage

<figure><img src="/files/M3IYRI8axYPXkqGBOa5W" alt=""><figcaption></figcaption></figure>

Filter watch data by timestamp at Start or End of watch sessions

<figure><img src="/files/BW7CNYaiGwtiMtgFam6J" alt=""><figcaption></figcaption></figure>

Date range for analysis - Longer timeframes may result in longer dashboard load times

<figure><img src="/files/QMO8wEhjIr9CdYUzHj6b" alt=""><figcaption></figcaption></figure>

Hours Viewed - Aggregated total view session length in hours\
Number of Unique Users - Count of unique viewers that have viewed content\
Avg Hours Viewed per User - The average number of viewed hours per user, as defined by the number of users within the selected date range. \
View Count - Total number of view sessions for specified time period\
Avg Hours per View - Average view session length in hours\
Avg View per User - Average number of view sessions per user on your platform\
Minutes Viewed - Aggregated total view session length in minutes

<figure><img src="/files/53InxvmZA2Au0BK2Q3vC" alt=""><figcaption></figcaption></figure>

Disabling filters across sheets will prevent the same filters being applied to all of the sheets within the dashboard.&#x20;


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/vesper-insights/analytics-dashboards/dashboard-deep-dive/all-watch-data/analyze-usage.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
