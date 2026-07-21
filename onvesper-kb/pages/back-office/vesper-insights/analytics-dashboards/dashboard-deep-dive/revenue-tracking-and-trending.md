> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/vesper-insights/analytics-dashboards/dashboard-deep-dive/revenue-tracking-and-trending.md).

# Revenue Tracking and Trending

<figure><img src="/files/IO5CJkvhDU2DTUnNkKCA" alt=""><figcaption></figcaption></figure>

Settlement date - date the users order was settled, primarily relevant to payment processes with an interval between ordering and settling, e.g. SEPA Direct Debit\
Transaction date is the date that the user actually placed the order.&#x20;

<figure><img src="/files/yHi8kkMR6Z0QIxF2CigJ" alt=""><figcaption></figcaption></figure>

Date range for analysis - Longer timeframes may result in longer dashboard load times

<figure><img src="/files/Zmp3gap5btZwIfEQy0OO" alt=""><figcaption></figcaption></figure>

Default currency is the default currency of the realm (as pertains to domicility of managed payment provider account)\
Local currency is the currency of purchaser\
Quoted in USD - Displays all pricing in USD (with exchanges performed daily at date specific rates) i.e. the transactions made on 10th March 2023 will be converted with the exchange rate as set on 10th March 2023, likewise the 11th etc.&#x20;

<figure><img src="/files/osuPKugbXb5iLmEycNRR" alt=""><figcaption></figcaption></figure>

Filter for revenue events in specific currency types

<figure><img src="/files/k4ibBmpuclVMvHsmNj1v" alt=""><figcaption></figcaption></figure>

Whenever aggregation is set to **"Quoted in Default Currency"**, the total will be displayed in the realm’s default currency. Otherwise, it will be shown in USD.

<figure><img src="/files/WrfTai2rAW9ho4yWwuFR" alt=""><figcaption></figcaption></figure>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/vesper-insights/analytics-dashboards/dashboard-deep-dive/revenue-tracking-and-trending.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
