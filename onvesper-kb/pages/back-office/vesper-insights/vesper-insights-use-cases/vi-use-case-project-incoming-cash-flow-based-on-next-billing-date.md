> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/vesper-insights/vesper-insights-use-cases/vi-use-case-project-incoming-cash-flow-based-on-next-billing-date.md).

# VI Use Case - Project incoming cash flow based on next billing date

<figure><img src="/files/Aj8kQTllvWr2tnAU8Dne" alt=""><figcaption><p>Next billing dates over the next 30 days for monthly and annual subscribers</p></figcaption></figure>

## Problem Statement

You want to quickly identify how many subscribers are due for renewal within the following days, weeks, or months, detailed on a ready-made comprehensive graph breaking down the number of expected renewals per day.

## How Vesper Insights can help

The Order Management dashboard within Vesper Insights can showcase future orders for users currently subscribed to a licence with a recurring billing cycle. Knowing when subscribers are due to renew their services can help you predict revenue, which can, in turn, aid with planning investments on your platform.&#x20;

Additionally, monitoring the next billing dates can boost your marketing spending as you target upsells (such as an annual licence to a monthly subscriber) to customers due to the renew soon.

## Implementation

* Go to Insights on Vesper Back Office and select the Order Management dashboard.
* On the Shortcut section on the left hand of the dashboard, select **Date Field for Analysis -> Next Billing Date**
* Still on the Shortcut section on the left hand side of the dashboard, select a **Date Range -> Next X time**&#x20;
* Apply a filter of **Licence Type Is Subscription**&#x20;
* Hit Apply
* A graph will display all the dates within the specified date range that a user is due to renew their subscription


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/vesper-insights/vesper-insights-use-cases/vi-use-case-project-incoming-cash-flow-based-on-next-billing-date.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
