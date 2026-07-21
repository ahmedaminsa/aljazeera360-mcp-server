> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/vesper-insights/analytics-dashboards/dashboard-deep-dive/retention-analysis/retention-analysis.md).

# Retention Analysis

<figure><img src="/files/ecgfIUFVEnNB60qPvSPG" alt=""><figcaption></figcaption></figure>

### Use Cases

A retention analysis dashboard is a vital tool for businesses aiming to boost customer loyalty and long-term value. This insight empowers companies to implement targeted strategies for improving retention, whether through personalised marketing, product enhancements, or customer support.&#x20;

With real-time tracking, the dashboard facilitates swift adjustments to retention tactics, fostering a proactive approach to customer relationship management and contributing to sustained business growth.

### Shortcut Panel

<figure><img src="/files/KxXzVBmqVs08kN4Aspk0" alt=""><figcaption></figcaption></figure>

Select Subscription Start Date - Longer timeframes may result in longer dashboard load times

<figure><img src="/files/3OeMKmLSiSRHOft04v8u" alt=""><figcaption></figcaption></figure>

View Retention By:

* Subscription Count - The number of subscriptions
* Total Month over Month Percentage - The retention percentage month over month
* Total Monthly Percentage - The total retention percentage based on Month 0.

<figure><img src="/files/HJUTkhtHPB8eygw6yLE8" alt=""><figcaption></figcaption></figure>

Started As Free Trial - Allows you to filter down the view to observe metrics specific to free-trial conversions. Where you want to run analysis exclusively on all users who were successfully converted from a free trial on to a recurring subscription, you can filter this to True.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/vesper-insights/analytics-dashboards/dashboard-deep-dive/retention-analysis/retention-analysis.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
