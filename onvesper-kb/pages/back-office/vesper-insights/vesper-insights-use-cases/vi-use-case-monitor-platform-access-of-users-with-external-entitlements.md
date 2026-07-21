> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/vesper-insights/vesper-insights-use-cases/vi-use-case-monitor-platform-access-of-users-with-external-entitlements.md).

# VI Use Case - Monitor platform access of users with external entitlements

## Problem Statement

To increase exposure of your service to another business' established customer base, you choose to  leverage external platform entitlements, allowing users to acquire a Vesper entitlement **outside** of the Vesper platform. One example could be partnering with a bank to provide their customers with free access to your streaming service for as long as they remain customers of said bank.

Whilst you have created an external dashboard to monitor how many users have acquired that entitlement, you want to monitor how many of those users are making the journey back to Vesper so you can analyse and compare platform access between internal and external entitlement to determine what's generating more traffic on your service.

## How Vesper Insights can help

Vesper Insights allows you to monitor access to the Vesper platform from users that have obtained an external entitlement, thanks to this information being included in the user's authentication token.&#x20;

There are various values you can choose to monitor from:

| Value                         | Definition                                                                                                                                | Example      |
| ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| Entitlement External Value    | String that the external provider will pass on to Vesper via the integration which designates their externally acquirable entitlement.    | BankFreePass |
| Entitlement Provider ID       | Three-letter value ID set by you, which identifies the externally acquirable entitlement provider.                                        | BOG          |
| Entitlement Internal Group ID | Upon creation of the three-letter value ID above, Vesper will automatically generate a three-letter internal group ID acting as a cohort. | AAA          |
| Entitlement Provider Name     | Easily identifiable name set by you, which initiates the external acquirable entitlement integration.                                     | Bank         |

## Implementation

* Go to Insights on Vesper Back Office and select the Customer Insights dashboard
* Within Customer Insights, select the User Access History tab
* Filter, list by or color by any of these values (for more granular search, you can combine these values):
  * Entitlement External Value
  * Entitlement Provider ID
  * Entitlement Internal Group ID
  * Entitlement Provider Name


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/vesper-insights/vesper-insights-use-cases/vi-use-case-monitor-platform-access-of-users-with-external-entitlements.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
