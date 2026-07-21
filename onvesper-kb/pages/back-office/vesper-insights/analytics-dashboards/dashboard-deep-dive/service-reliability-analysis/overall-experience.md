> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/vesper-insights/analytics-dashboards/dashboard-deep-dive/service-reliability-analysis/overall-experience.md).

# Overall Experience

<figure><img src="/files/IaDQkiyLw3tfX1irPpkp" alt=""><figcaption></figcaption></figure>

View Start - Utilise session View Start timestamp for analytics\
View Eng - Utilise session View End timestamp for analytics

<figure><img src="/files/bp3FUomIsb0U3mj3pCjE" alt=""><figcaption></figcaption></figure>

Date range for analysis - Longer timeframes may result in longer dashboard load times

<figure><img src="/files/HCskgy0rqzZl9LTwWlWR" alt=""><figcaption></figcaption></figure>

Overall Viewer Experience is a high-level score from 0 to 100 that measures the QoE (Quality of Experience). Overall Viewer Experience Score is based on four other Viewer Experience Scores, which each describe one of the four elements of video streaming performance: [Playback Success](/platform-knowledge-base/back-office/vesper-insights/analytics-dashboards/dashboard-deep-dive/service-reliability-analysis/playback-success.md), [Startup Time](/platform-knowledge-base/back-office/vesper-insights/analytics-dashboards/dashboard-deep-dive/service-reliability-analysis/startup-time.md), [Smoothness](/platform-knowledge-base/back-office/vesper-insights/analytics-dashboards/dashboard-deep-dive/service-reliability-analysis/smoothness.md) and [Video Quality](/platform-knowledge-base/back-office/vesper-insights/analytics-dashboards/dashboard-deep-dive/service-reliability-analysis/video-quality.md)

<figure><img src="/files/QBVC7xxyUiX7VmFYIUOV" alt=""><figcaption></figcaption></figure>

Disabling filters across sheets will prevent the same filters being applied to all of the sheets within the dashboard.&#x20;


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/vesper-insights/analytics-dashboards/dashboard-deep-dive/service-reliability-analysis/overall-experience.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
