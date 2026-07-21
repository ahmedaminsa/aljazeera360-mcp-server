> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/vesper-insights/analytics-dashboards/dashboard-deep-dive/subscriber-management/active-subscribers.md).

# Active Subscribers

<figure><img src="/files/p2RIyiCNP6dtbBrpTBkP" alt=""><figcaption></figcaption></figure>

The date range for analysis sets the period of time you're investigating. **To understand the current state of subscribers, set the date range to today.**&#x20;

By extending the date range beyond today, ie to the last 30 days, the KPI metric (Displayed beneath List By and Color By) will show a unique count of all EXIDs that have had an active subscription within the stipulated date range. The main visual will show how that unique count is broken down by time, as below.

<figure><img src="/files/Pe3WL4vxdhNTAb3ewSUd" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/g94Xckocbgn1rM8l0qSD" alt=""><figcaption></figcaption></figure>

Filter by Unique Subscribers (who can individually own many licenses, Recurring + PPV for example)\
Filter by Unique Licenses (individual purchases of which several can be attributed to a single Subscriber)

<figure><img src="/files/NlVX4FmvPnKsdjTYrurB" alt=""><figcaption></figcaption></figure>

Is Successfully Converted - Allows you to filter for either all successfully processed payments for analysis if set to "True", or all unsuccessfully processed payments (including pending) if set to "False"


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/vesper-insights/analytics-dashboards/dashboard-deep-dive/subscriber-management/active-subscribers.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
