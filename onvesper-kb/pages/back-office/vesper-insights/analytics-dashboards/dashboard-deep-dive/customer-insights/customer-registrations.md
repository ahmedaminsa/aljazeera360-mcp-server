> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/vesper-insights/analytics-dashboards/dashboard-deep-dive/customer-insights/customer-registrations.md).

# Customer Registrations

<figure><img src="/files/3prEP4LPCv1IILGO8NCy" alt=""><figcaption></figcaption></figure>

Register Date - Use date of user registration for date range filtering\
Last Access Date - Use date of user last accessing the platform (login inclusive) for date range filtering\
Last Watch Date - Use date of user last consuming video content for date range filtering\
Last Order Date - Use date of user last purchase action for date range filtering

<figure><img src="/files/Ki0oWqLf6yHjB93mtaY4" alt=""><figcaption></figcaption></figure>

Date range for analysis - Longer timeframes may result in longer dashboard load times

<figure><img src="/files/jn16qJN3YozsEJWUW4hD" alt=""><figcaption></figcaption></figure>

The Customer Insights dashboard contains multiple datasets. By selecting "Yes", the datasets will be joined when performing queries.&#x20;

<figure><img src="/files/iIKkginRFHg60u4ZePNs" alt=""><figcaption></figcaption></figure>

Disabling filters across sheets will prevent the same filters being applied to all of the sheets within the dashboard.&#x20;


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/vesper-insights/analytics-dashboards/dashboard-deep-dive/customer-insights/customer-registrations.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
