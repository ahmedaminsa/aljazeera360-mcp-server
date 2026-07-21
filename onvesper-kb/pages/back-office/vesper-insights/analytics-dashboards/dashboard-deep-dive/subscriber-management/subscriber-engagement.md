> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/vesper-insights/analytics-dashboards/dashboard-deep-dive/subscriber-management/subscriber-engagement.md).

# Subscriber Engagement

<figure><img src="/files/R4yLKHD3juicXFZlJMUR" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/IPSzrJAxaNMf3Y4wcp1N" alt=""><figcaption></figcaption></figure>

**What is an engaged subscriber?**

An engaged subscriber is someone who has watched content and has an active licence during the reporting period.

### Use Cases

The Subscriber Engagement sheet allows you to understand how many users with active subscriptions each period are watching content that same period. This allows you to determine viewership peneration.

### Shortcut Panel

<figure><img src="/files/hiN2Qtn9noKBTCyiAQ6N" alt=""><figcaption></figcaption></figure>

Date range for analysis - Longer timeframes may result in longer dashboard load times

<figure><img src="/files/0kNikLvKLQg8mNR7RX6C" alt=""><figcaption></figcaption></figure>

Is Successfully Converted - Allows you to filter for either all successfully processed payments for analysis if set to "True", or all unsuccessfully processed payments (including pending) if set to "False"


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/vesper-insights/analytics-dashboards/dashboard-deep-dive/subscriber-management/subscriber-engagement.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
