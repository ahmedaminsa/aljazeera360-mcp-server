> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/vesper-insights/vesper-insights-use-cases/vi-use-case-identify-your-peak-concurrency-viewership.md).

# VI Use Case - Identify your peak concurrency viewership

<figure><img src="/files/KEkYYdDE7opTfblnlbhx" alt=""><figcaption><p>Peak concurrency of watchers over the course of a 3-day long competition</p></figcaption></figure>

## Problem statement

You wish to create more data-driven content on your social feeds to increase exposure to your streaming platform during one of your flagpole competitions, delivered as a daily long stream containing back-to-back events.

## How Vesper Insights can help

You can leverage the Viewership Concurrency dashboard to monitor the Average Minute Audience (AMA) and Peak Concurrency during weekends where your flagpole competition takes place.&#x20;

Thanks to the visual chart, which allows for the metrics to be broken down hourly, you can decipher which match within the competition drove the highest watcher engagement.

You can then use that information to generate content on your social feeds, focusing on the action taking place at the time fans flocked to the platform to watch concurrently.

You can also use this data to strategise the upload of shoulder content to keep watchers engaged after the live event is over.&#x20;

## Implementation

* Go to Insights on Vesper Back Office and select All Watch Data dashboard.
* Select Viewership Concurrency tab.
* Select Viewership Date&#x20;
* View Usage By 'Peak Concurrency of Views'
* List by 'Content Name'
* View by Hour on main chart
* Apply
* See the concurrency peaks broken down by LIVE and VOD and by the hour, where you'll see which hour saw most users concurrently watching, as well as viewer engagement gaps between live and vod events that might need content scheduling addressing.&#x20;


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/vesper-insights/vesper-insights-use-cases/vi-use-case-identify-your-peak-concurrency-viewership.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
