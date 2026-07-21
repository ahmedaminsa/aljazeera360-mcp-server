> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/vesper-insights/vesper-insights-use-cases/vi-use-case-identify-which-content-is-driving-most-sign-ups.md).

# VI Use Case - Identify which content is driving most sign ups

## Problem Statement

You have acquired a new sports competition to be streamed for free in multiple markets over a series of weekends and want to determine how much customer growth it is generating for your service. How many people are signing up to explicitly watch this content?

## How Vesper Insights can help

You can leverage the First Watch events available in the customer profile to determine what was the first content a user watched right after signing up. This is achieved thanks to Vesper Insights' identification of a registered user's **first** viewing session, which provides details regarding the content watched, the session's duration and the session's origin (location and device).&#x20;

## Implementation

* Go to Insights on Vesper Back Office and select the Customer Insights dashboard.
* Select a date range to monitor new customers on the platform over a determined time period.
* Select 'Is Guest User -> False' to ensure the query returns values for registered users only.
* Apply a 'First Watch' filter under the 'Customer Profile' Dataset, such as 'First Watch Live Content LIKE Champions League' (ensure that the text you enter is present in the live content name)
* Color By 'First Watch Live Content Name'
* List By 'Register Country'

This query will return all new customers registered on the service during the specified date range whose first watched content was a live event containing the string 'Champions League', listed by country of registration.

You can dig deeper into your analysis by creating a cohort of these users and implementing it on the All Watch Data dashboard: this will empower you to monitor what other events these users have been watching ever since their first viewing session, unlocking insights into your customer's watching behavior.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/vesper-insights/vesper-insights-use-cases/vi-use-case-identify-which-content-is-driving-most-sign-ups.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
