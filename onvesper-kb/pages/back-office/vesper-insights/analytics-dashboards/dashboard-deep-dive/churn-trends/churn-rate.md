> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/vesper-insights/analytics-dashboards/dashboard-deep-dive/churn-trends/churn-rate.md).

# Churn Rate

<figure><img src="/files/uhwKXl8Kgh9ncAVfKoIy" alt=""><figcaption></figcaption></figure>

Date range for analysis - Longer timeframes may result in longer dashboard load times

<figure><img src="/files/PEjjnvdTlV0tsJUW9X1D" alt=""><figcaption></figcaption></figure>

As previously described on [Churn](/platform-knowledge-base/back-office/vesper-insights/analytics-dashboards/dashboard-deep-dive/churn-trends/churn.md), this will display the churn rate on either a licence level or a subscriber level. A user may have multiple licences within their subscription. 'Churned Licences' refer to specific licences that have churned whereas, 'Churned Subscribers' refer to when a user has decided to churn their last active licence and their active licence count has reduced to 0.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/vesper-insights/analytics-dashboards/dashboard-deep-dive/churn-trends/churn-rate.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
