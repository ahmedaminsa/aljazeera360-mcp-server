> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/vesper-insights/analytics-dashboards/dashboard-deep-dive/churn-trends/churn-tenure.md).

# Churn Tenure

<figure><img src="/files/wmTkU8uTcwMVTo18hFDp" alt=""><figcaption></figcaption></figure>

**Use Cases**

A churn tenure dashboard is a valuable analytics tool for users looking to understand and mitigate customer churn, which is the rate at which customers discontinue their engagement with a product or service. This dashboard displays a range of critical metrics related to customer retention, such as customer tenure, churn rates, and reasons for churn, over specific time periods.&#x20;

By providing a clear visualisation of these data points, it allows companies to identify patterns, customer segments at risk, and the factors contributing to attrition.&#x20;

<figure><img src="/files/OJW98puhhbrrgrIpiw4S" alt=""><figcaption></figcaption></figure>

'Licence End Date' is the date that the user no longer had access to the platform whereas, 'Active Churn Date' is the date at which the user has requested to churn i.e. the user may choose to no longer renew and still have some time remaining on their licence.&#x20;

<figure><img src="/files/z5gMRhgmhKE0cYNiESb1" alt=""><figcaption></figcaption></figure>

Date range for analysis - Longer timeframes may result in longer dashboard load times

<figure><img src="/files/vVdI37jHRICnqRbtcJf8" alt=""><figcaption></figcaption></figure>

Medium tenure and average tenure are measures of the time that users spend subscribed to the platform.&#x20;

* Median tenure finds the middle value, where half have shorter durations, and half have longer durations, providing a balanced perspective.&#x20;
* Average tenure calculates the sum of all tenures divided by the number of people, offering a  average tenure.&#x20;

The key difference is that average tenure is sensitive to outliers, while medium tenure is less influenced by extreme values, making it a better choice for a more representative measure of typical tenure.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/vesper-insights/analytics-dashboards/dashboard-deep-dive/churn-trends/churn-tenure.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
