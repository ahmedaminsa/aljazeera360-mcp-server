> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/vesper-insights/analytics-dashboards/dashboard-deep-dive/service-reliability-analysis/startup-time.md).

# Startup Time

<figure><img src="/files/Q2rcGiFXqNvi7qlYnSK0" alt=""><figcaption></figcaption></figure>

View Start - Utilise session View Start timestamp for analytics\
View Eng - Utilise session View End timestamp for analytics

<figure><img src="/files/r9TQYpoWFUxyCAuRwyDj" alt=""><figcaption></figcaption></figure>

Date range for analysis - Longer timeframes may result in longer dashboard load times

<figure><img src="/files/7v5CpiW1KU2pYkbeGc4T" alt=""><figcaption></figcaption></figure>

**Startup Time Score** - Longer startup times mean lower scores, while shorter startup times mean higher scores.\
\
Following metrics are broken into 2 analytics groupings:

* Median (50th Percentile) – Helps understand a typical experience (half are better than this number, half are worse)
* 95th Percentile – Helps understand what a poorer experience is like on your applications, while excluding outliers and happening frequently enough (at least 1 in 20 views).<br>

**Video Startup Time** - measures the time that the viewer waits for the video to play after the page is loaded and the player is ready\
**Player Startup Time** - measures the time from when the player is first initialized in the page to when it is ready to receive further instructions.\
**Page Load Time** - measures the time from the initial user request for a page to the time when the video player is first initialized.\
**Aggregate Startup Time** - combines Page Load Time, Player Startup Time, and Video Startup Time to show the total time a viewer waits for a video to play after requesting to watch the video on the previous screen or page.\
**Seek Latency(sec)** - measures the average amount of time that viewers wait for the video to start playing again after seeking to a new time.\
**Video Startup Preroll Request Time** - measures the total amount of Video Startup Time that is spent making ad requests, waiting for the ad responses, and parsing the VAST/VMAP response.\
**Video Startup Preroll Load Time** - measures the total amount of Video Startup Time that is spent making ad requests, waiting for the ad responses, and parsing the VAST/VMAP response.\
**Requests for First Preroll** - measures the number of ad requests that are made up to the point of preroll ad playback beginning.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/vesper-insights/analytics-dashboards/dashboard-deep-dive/service-reliability-analysis/startup-time.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
