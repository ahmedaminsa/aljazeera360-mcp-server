> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/vesper-insights/analytics-dashboards/dashboard-deep-dive/subscriber-management/subscription-tenure.md).

# Subscription Tenure

**What is subscription tenure?**

Subscription tenure is the length of time a subscriber has held an active subscription/license, measured from their subscription start date to the current date (or to their cancellation date, if no longer active).

**Use Cases**

The Subscription Tenure sheet allows you to understand how long your subscriber base has been subscribed, helping you assess retention strength and identify how much of your audience is new versus long-standing.

<figure><img src="/files/CYmNja0ryUXbSeyYDLlq" alt=""><figcaption></figcaption></figure>

**Shortcut Panel**

<figure><img src="/files/h2NoQBSmpdM1KjR7HRhs" alt="" width="135"><figcaption></figcaption></figure>

* **Select Subscription Date** – Date range filter for analysis, based on subscription start date. *Longer timeframes may result in longer dashboard load times.*
* **View Tenure Trend By** – Allows you to select the metric used to visualize the tenure trend (e.g. Median Tenure vs Average Tenure).
* **Realm selection** – Allows you to filter the analysis to one or more specific realms (e.g. dce.sandbox).
* **Is Successfully Converted** – Allows you to filter for either all successfully processed payments for analysis if set to "True", or all unsuccessful ones (e.g. revoked, expired, pending) if set to "False". See [#successfully-converted-filter](#successfully-converted-filter "mention")
* **Started As Free Trial** – Allows you to filter for subscribers who started as free trial, subscribers who did not, or all data.
* **License Status** - Allows you to filter based on the license status (e.g. active, active churn, cancelled, revoked etc.)

#### **Successfully Converted filter**&#x20;

Filter to True for clean reporting on active, successfully paying subscribers — this bucket is reliable and unaffected by other data noise. \
Be cautious using False as a "failed conversions" metric on iOS/Android: when an already-active subscriber generates extra purchase receipts (e.g. restore-purchase flows, duplicate receipt delivery), those duplicates get revoked, and the revocation itself logs as False — even though the subscriber is valid and paying. So False can be inflated by receipt noise rather than genuine payment failures on these platforms.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/vesper-insights/analytics-dashboards/dashboard-deep-dive/subscriber-management/subscription-tenure.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
