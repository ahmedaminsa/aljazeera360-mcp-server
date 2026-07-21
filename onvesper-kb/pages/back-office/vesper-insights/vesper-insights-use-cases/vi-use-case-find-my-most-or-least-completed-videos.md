> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/vesper-insights/vesper-insights-use-cases/vi-use-case-find-my-most-or-least-completed-videos.md).

# VI Use Case - Find my most (or least) completed Videos

## Problem Statement

Vesper Insights makes finding your "most viewed" (by view count) and "most total hours watched" (across all users) VODs easy to identify, but what if you're concerned that customers are watching the first minute of your content, and then bouncing off?

How do you filter out customers that bounced after the introduction of a video, and how do you find the content which customer's are most engaged with and watching to the end - so that you can commission more content of that quality?

## How Vesper Insights can help

Using the [Content Viewership](/platform-knowledge-base/back-office/vesper-insights/analytics-dashboards/dashboard-deep-dive/all-watch-data/content-viewership.md) dashboard, you are able to apply filters that make doing watch percentage analysis much simpler.

Add a filter using the Field "Video Completion Rate" to improve the quality of the data you are working with. For example, by filtering video completion rate to greater than 1-5% (depending on your average content length), you will filter out any watch sessions that immediately "bounced" off the VOD.

<figure><img src="/files/cgVd7pNCiXFLujJS9CDl" alt=""><figcaption><p>This Filter would remove all user sessions that only watched the first 5% of a video</p></figcaption></figure>

If you now want to find which VOD content has the best completion rate for your users, set up a filter and your dashboard according to the screenshot below:

<figure><img src="/files/1MSC0fReoWYJygTTzC0s" alt=""><figcaption><p>Number of unique accounts that watched the content through to at least 90% completion</p></figcaption></figure>

This setup will show you which content has the most unique customers watching the video through to completion. Using 90% as completion is fairly generous, we would recommend using 95% for more accuracy but advise ***against*** 100% as customers might roll off before the credits of a Video.

If you have Seasons and Series configured ([Collections & Series](/platform-knowledge-base/dve/curating-grouped-content/collections-and-series.md)) you will also be able to view this data by Series or Season title

<figure><img src="/files/hHvYz9QjVlVVKrAZA8Xv" alt=""><figcaption><p>If you have configured Series, you can now identify how many users have completed multiple episodes of a given series.</p></figcaption></figure>

Note that whilst this gives you a great insight into the series that your customers are watching complete *episodes* of, it does not tell you how many customers have completed the series itself.

{% hint style="info" %}
Adding "Video Completion Rate" filters will remove all live sessions, as completion rate is only available for VOD content.
{% endhint %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/vesper-insights/vesper-insights-use-cases/vi-use-case-find-my-most-or-least-completed-videos.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
