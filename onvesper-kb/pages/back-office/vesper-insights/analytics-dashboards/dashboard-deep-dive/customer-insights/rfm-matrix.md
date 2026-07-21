> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/vesper-insights/analytics-dashboards/dashboard-deep-dive/customer-insights/rfm-matrix.md).

# RFM Matrix

<figure><img src="/files/kPtVbCLeY4hZwlvAOxnQ" alt=""><figcaption></figcaption></figure>

### Use Cases

This dashboard displays the cumulative revenue generated from orders placed by customers who recently made purchases and have a specific total order count.

This matrix serves as a powerful visualisation tool to understand customer spending behaviours based on order frequency and recency.&#x20;

It assists in recognising actionable patterns, trends, and correlations, thereby guiding effective strategies for customer segmentation, targeted marketing, and optimised pricing strategies to boost revenue and engagement.

### Shortcut Panel

<figure><img src="/files/NpvgWd2DOUqrNlnbqk3L" alt=""><figcaption></figcaption></figure>

Date range for analysis - Longer timeframes may result in longer dashboard load times

<figure><img src="/files/rdGjEPT4Zc3TTQpLPVkP" alt=""><figcaption></figcaption></figure>

Quoted in Default Currency - This will show the values in the local currency of the Realm

Quoted in USD - This will show values in USD.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/vesper-insights/analytics-dashboards/dashboard-deep-dive/customer-insights/rfm-matrix.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
