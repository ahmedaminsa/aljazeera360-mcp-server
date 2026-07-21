> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/vesper-insights/analytics-dashboards/dashboard-deep-dive/service-reliability-analysis/playback-success.md).

# Playback Success

<figure><img src="/files/VP0gWX3ptAKrHNeaViqR" alt=""><figcaption></figcaption></figure>

View Start - Utilise session View Start timestamp for analytics\
View Eng - Utilise session View End timestamp for analytics

<figure><img src="/files/8HTsjXLpPKKM7SIgUrRq" alt=""><figcaption></figcaption></figure>

Date range for analysis - Longer timeframes may result in longer dashboard load times

<figure><img src="/files/JenewzAt02TUIyWEgebZ" alt=""><figcaption></figcaption></figure>

**Playback Success Score** - Metric based on whether a video played back successfully. A failure that ends playback is a `0`, while a video that plays through without failure is `100`. A view that is terminated by the viewer before playback starts (an “Exit Before Video Start,” or EBVS) is given a score of `50`. EBVS views that occur in less than 1 second is given no score.\
**Playback Failure Percentage** - Metric that gives the percentage of video views that failed to play due to an error.\
**Exits Before Video Start** - Metric that measures the count of viewers that abandon a video before playback (e.g. close the page/app or click the back button)\
**Video Startup Failure Percentage** - Metric of the percentage of video views that experienced an error that prevents the user from seeing the first frame of video


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/vesper-insights/analytics-dashboards/dashboard-deep-dive/service-reliability-analysis/playback-success.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
