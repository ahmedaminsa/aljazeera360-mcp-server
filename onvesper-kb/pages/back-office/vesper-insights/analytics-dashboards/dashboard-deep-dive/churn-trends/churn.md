> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/vesper-insights/analytics-dashboards/dashboard-deep-dive/churn-trends/churn.md).

# Churn

<figure><img src="/files/81P1SO9OTibnfvAUE0XZ" alt=""><figcaption></figcaption></figure>

### How do we define Churn?&#x20;

Churn rate is the total number of churned licences over a rolling 30 day period divided by total number of active licences over a rolling 30 day period, as decribed in the following formula:

<figure><img src="/files/kw4vXvg6sCszMzoVHPiB" alt=""><figcaption></figcaption></figure>

* **churned events:** any subscriptions end in the period from Day(T-29) to Day(T) will be counted. It is the number of churned subscriptions, not churned customers
* **active subscriptions:** any subscriptions ever active in the period from Day(T-29) to Day(T) will be counted. It is the number of subscriptions, not the customers. A subscription that ends on Day(T-29) will be counted, and a subscription that starts on Day(T) will also be counted.

<figure><img src="/files/aAeW87M6kKqsBRpoaPne" alt=""><figcaption></figcaption></figure>

'Licence End Date' is the date that the user no longer had access to the platform whereas, 'Active Churn Date' is the date at which the user has requested to churn i.e. the user may choose to no longer renew and still have some time remaining on their licence.&#x20;

<figure><img src="/files/Fsem7HUzhJjiSBJolhn9" alt=""><figcaption></figcaption></figure>

Date range for analysis - Longer timeframes may result in longer dashboard load times

<figure><img src="/files/4HNuIfyHbxeVnIZyuRAG" alt=""><figcaption></figcaption></figure>

A user may have multiple licences within their subscription. 'Churned Licences' refer to specific licences that have churned whereas, 'Churned Subscribers' refer to when a user has decided to churn their last active licence and their active licence count has reduced to 0.&#x20;

<figure><img src="/files/Kwi916ds5jioMjlJD5RR" alt=""><figcaption></figcaption></figure>

Is Successfully Converted - Allows you to filter for either all successfully processed payments for analysis if set to "True", or all unsuccessfully processed payments (including pending) if set to "False"


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/vesper-insights/analytics-dashboards/dashboard-deep-dive/churn-trends/churn.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
