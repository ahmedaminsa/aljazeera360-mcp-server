> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/licences/promotions/promo-code-reports.md).

# Promo code reports

Once you've set up a promotion, there are 2 ways to get data on how successful it has been. The simplest option is the Promo Code report.

The promo code report is generated daily at 00:00 UTC, and can be downloaded in the report section of Back Office.

Inside the report you will see the following information:

<figure><img src="/files/WEjTcuHzD8GZBPzddHWv" alt=""><figcaption><p>Sample promotion code report</p></figcaption></figure>

Using this report, you can identify the number of codes that have been redeemed for each of your promotions, the codes themselves (if generic), the promotion running time, and all restrictions.

The number of redeemed codes is the number that have been entered by your customers. That is: if a customer has entered a code which will apply to their **next** billing cycle (i.e. next month is 30% off), then that will be counted in this number. The same is true of customers that are using a promotional code but are currently in a free trial, they will show in this count.\
If the customer does not complete the transaction (cancels their trial or cancels the account), this number will be reduced accordingly.

### Measuring promo code transactions

The Transaction report contains information about every transaction that has occurred through the last 31 days, and is generated every 6 hours.&#x20;

In that report, there are columns for "VOUCHER", "VOUCHER NAME" and "VOUCHER CODE". Using the "VOUCHER" column as a filter for **true** will allow you to identify the number of your transactions in that 31 days which have been discounted by a promotion.

For more information on Vesper reports, see our data pages: [Vesper Data Exports](https://docs.onvesper.com/platform-knowledge-base/vesper-data-exports/)


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/licences/promotions/promo-code-reports.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
