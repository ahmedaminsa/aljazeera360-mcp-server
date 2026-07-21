> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/vesper-insights/vesper-insights-use-cases/vi-use-case-reward-your-super-users.md).

# VI Use Case - Reward your super users

## Problem Statement

You want to identify the users most engaged with your platform to target them with a tailored marketing campaign that will reward their loyalty (for example: early bird discount for event tickets).

## How Vesper Insights can help

You can leverage the native Endeavor cohort for superusers (bsu) and collect their email addresses for 3rd party marketing if they have agreed to receive marketing emails. You can then introduce this cohort of most receptive users to other areas of your business with a revenue opportunity, such as e-commerce.&#x20;

## Implementation

* Go to Insights on Vesper Back Office and select the All Watch Data dashboard.
* Select a date rage to monitor the superusers over a determined time period.
* Add one filter to focus on watching sessions carried over by super users (bsu) via using the 'Cohorts' Field and setting it up to 'bsu'.&#x20;
* Apply
* Create a new cohort with your results and give it a descriptive name, such as 'superusers January'.
* Navigate to the Customer Insights dashboard.
* Import the cohort of superusers created on the All Watch Data dashboard.
* Add one filter to determine which users from the cohort gave consent to receive marketing emails via using the 'Customer Profile' dataset, the 'Consent Resident Marketing' or 'Consent Email Marketing' set to 'True'.&#x20;
* Apply
* You now have a list of superusers over a determined time period that have been given consent to receive marketing emails.&#x20;
* Download a report and use the emails to set up an external email campaign that will expose your most engaged users with your suite of marketable options. &#x20;


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/vesper-insights/vesper-insights-use-cases/vi-use-case-reward-your-super-users.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
