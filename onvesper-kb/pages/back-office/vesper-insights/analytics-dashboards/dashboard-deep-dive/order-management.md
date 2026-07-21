> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/vesper-insights/analytics-dashboards/dashboard-deep-dive/order-management.md).

# Order Management

<figure><img src="/files/IXzK7me2TTyRasqiZsZx" alt=""><figcaption></figcaption></figure>

**Use Cases**

An order management dashboard serves as a vital tool for users, enabling them to streamline and optimise their entire order process. With real-time visibility into order status and customer data, this dashboard empowers businesses to efficiently track and manage various licence types. \
\
It also facilitates data-driven decision-making by providing insights into sales trends, customer behaviour, and supplier performance. Additionally, it enhances customer service through the ability to quickly address inquiries and issues, ultimately leading to improved customer satisfaction and increased revenue.

<figure><img src="/files/50n442MmbudvMidiI272" alt=""><figcaption></figcaption></figure>

**Order date** - date a user initiated a payment order by checking out for a license\
**Settlement date** - date the users order was settled, primarily relevant to payment processes with an interval between ordering and settling, e.g. SEPA Direct Debit

<figure><img src="/files/Tkwg9OeZpvDHtQxJGSnm" alt=""><figcaption></figcaption></figure>

**Date range for analysis** - Longer timeframes may result in longer dashboard load times

<figure><img src="/files/F9JgOaIoZXVIB3lkMq1f" alt=""><figcaption></figcaption></figure>

**View Totals As** - Totals can be viewed as either the total number of orders or the total number of unique customers making purchases, useful for differential analysis where recurring and one-off purchases can both be made on your application

<figure><img src="/files/SrWLi8UZDjW5lLKy1ZqY" alt=""><figcaption></figcaption></figure>

**Is Successfully Converted** - Allows you to filter for either all successfully processed payments for analysis if set to "True", or all unsuccessfully processed payments (including pending) if set to "False"

<figure><img src="/files/9vnyilZljojuYCFJB43o" alt=""><figcaption></figcaption></figure>

**Allows to filter for orders that originated from the Vesper Platform** - this is relevant where you have historically migrated payments into the Vesper platform and the first "order" received would be a renewal. Where you would like to filter out migrated payments to observe new user update you would set this to "True". Or alternatively if you exclusively want to observe the inverse subset of users, this can be set to "False"

<figure><img src="/files/bUyb7Qrz6PkmFCV0JciH" alt=""><figcaption></figcaption></figure>

**Started As Free Trial** - Allows you to filter down the view to observe metrics specific to free-trial conversions. Where you want to run analysis exclusively on all users who were successfully converted from a free trial on to a recurring subscription, you can filter this to True


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/vesper-insights/analytics-dashboards/dashboard-deep-dive/order-management.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
