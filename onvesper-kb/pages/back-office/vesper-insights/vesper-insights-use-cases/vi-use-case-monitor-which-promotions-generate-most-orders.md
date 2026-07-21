> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/vesper-insights/vesper-insights-use-cases/vi-use-case-monitor-which-promotions-generate-most-orders.md).

# VI Use Case - Monitor which promotions generate most orders

## Problem Statement

You want to track how many orders are being initialised via a promotion as a metric against their conversion success rate.

## How Vesper Insights can help

You can leverage promotion related events present on the Order Management dashboard to determine how many orders were initialised thanks to the application of a promotion, or voucher code. When compared with the total orders received including those not using a voucher code, you can determine the success rate of the promotion.

## Implementation

* Go to Insights on Vesper Back Office and select Order Management dashboard.
* On Orders, select the date range you wish to inspect.
* You can choose between seeing Totals as Total Orders (same customer potentially making multiple orders) or Unique Customers.
* Add one filter to focus on one licence you want to inspect by using the 'Licence Name' field.
* Add one filter to focus on the orders where a voucher was implemented by using the 'Is Voucher Used' field.
* Apply
* Compare the total of orders fitting the criteria with the number of orders received for the same licence without a voucher implementation to get a voucher success rate.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/vesper-insights/vesper-insights-use-cases/vi-use-case-monitor-which-promotions-generate-most-orders.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
