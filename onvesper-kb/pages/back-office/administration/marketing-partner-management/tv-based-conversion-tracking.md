> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/administration/marketing-partner-management/tv-based-conversion-tracking.md).

# TV-based conversion tracking

TV-based conversion tracking is the most straightforward functionality that Marketing Partner Management unlocks, as it is automatically enabled for all Vesper clients without any additional configuration.

## Tracking the conversion&#x20;

The TV conversion reporting is always on and tracks user sign-ups and conversions when the user is driven from the TV to the web to complete the navigation using the QR Code or PIN system.

The attribution window (the timeframe when to count conversion) for TV-based conversions is **24 hours**.&#x20;

## Reporting metrics

The Referral Partner Name and Campaign Name will appear in [Vesper Insights](/platform-knowledge-base/back-office/vesper-insights.md) reporting and will **match the TV or console from which the user navigated.**

Example:&#x20;

An end-user downloads the app onto Apple TV, navigates from the TV app to the web via a QR Code or PIN and completes a new user signup. The following will appear in the reporting:

* REFERRAL\_PARTNER\_NAME = Apple TV
* REFERRAL\_CAMPAIGN\_NAME = Apple TV
* REFERRAL\_ID = apple\_tv


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/administration/marketing-partner-management/tv-based-conversion-tracking.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
