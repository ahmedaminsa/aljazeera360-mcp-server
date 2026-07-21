> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/vesper-insights/analytics-dashboards/dashboard-deep-dive/service-reliability-analysis/video-quality.md).

# Video Quality

<figure><img src="/files/SJtkdtu1posxTbHVr26P" alt=""><figcaption></figcaption></figure>

View Start - Utilise session View Start timestamp for analytics\
View Eng - Utilise session View End timestamp for analytics

<figure><img src="/files/kfDn2jRUgogtlkOHKWZf" alt=""><figcaption></figcaption></figure>

Date range for analysis - Longer timeframes may result in longer dashboard load times

<figure><img src="/files/yLKEZjEksNxxReFslckK" alt=""><figcaption></figcaption></figure>

Video Quality Score - measures the visual quality a user sees by comparing the resolution of a video stream to the resolution of the player in which it is played.\
\
Following metrics are broken into 2 analytics groupings:

* Median (50th Percentile) – Helps understand a typical experience (half are better than this number, half are worse)
* 95th Percentile – Helps understand what a poorer experience is like on your applications, while excluding outliers and happening frequently enough (at least 1 in 20 views).

Weighted Average Bitrate - the time weighted average of the indicated bitrates that a viewer experiences during a video stream.\
Live Stream Latency (BETA) - measures the time it takes from when a camera captures an action in real life to when viewers of a live stream see it happen on their screen.\
Request Latency Median - measures the average time to first byte for media requests, that is the time from when the request is initiated to the time when the first byte of data is received from the server.\ <br>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/vesper-insights/analytics-dashboards/dashboard-deep-dive/service-reliability-analysis/video-quality.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
