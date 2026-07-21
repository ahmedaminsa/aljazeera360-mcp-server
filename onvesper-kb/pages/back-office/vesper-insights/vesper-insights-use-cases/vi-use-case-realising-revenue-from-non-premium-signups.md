> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/vesper-insights/vesper-insights-use-cases/vi-use-case-realising-revenue-from-non-premium-signups.md).

# VI Use Case - Realising revenue from non-premium signups

<figure><img src="/files/UXvGJOXbI3mcso4LHfpd" alt=""><figcaption></figcaption></figure>

## Problem Statement&#x20;

One of the residents on the Vesper Platform saw stagnant MoM growth in subscribers, and requested data to help with decision making on how to grow the business.&#x20;

## How Vesper Insights can help

Reviewing a 6 month time period, we noticed in Vesper Insights that this resident saw over 12,000 users create an account on the platform but did not convert to paid subscribers.

## What Actions Were Used to Deliver Value

A segment was be created in Vesper Insights that qualifies all users that did not make a purchase into an email marketing campaign with the goal of getting users to complete the final step in the journey. After 2-3 sends with no conversion, we sent another email with a 10% discount to these users in the hopes of giving these interested users the final incentive they may need to complete their transaction. We were able to convert 10% of free users through our non-discounted marketing journey, generating over $74,000 in additional revenue. We also acquired an additional 5% of subscribers who did not previously successfully convert with the 10% discount, gaining an additional \~$33,000 in additional revenue. Overall, we were able to generate more than $100,000 in additional revenue by identifying these qualifying users in Vesper Insights.

## Implementation

* Within the Shortcut panel, select the following from each drop down menu:
  1. Data Field for Analysis: Register Date
  2. Select a Date Range: Relevant date range to your desired target (e.g. non-premium users older than 1 month)
  3. Join Analysis Results Across Datasets: No
* Create the following filter:
  1. Customer Profile – Total Licence Count\
     **OPERATOR**: BETWEEN\
     **VALUES**: 0 AND 0
* Create a segment with these criteria (alternatively directly export this selection of users for a one-off campaign)

With these criteria you will be able to find the number of people who are yet to convert to a paid subscriber. From there, you can create a [Segments](/platform-knowledge-base/back-office/vesper-insights/analytics-dashboards/dashboard-controls/segments.md) with this list of users who have never made a purchase and enter them into an email journey (users will always fall out of inclusion in a segment once they no longer qualify, in this case after making any purchase allowing consistent monitoring of this state over time).


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/vesper-insights/vesper-insights-use-cases/vi-use-case-realising-revenue-from-non-premium-signups.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
