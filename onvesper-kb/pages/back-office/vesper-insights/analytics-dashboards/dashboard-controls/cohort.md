> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/vesper-insights/analytics-dashboards/dashboard-controls/cohort.md).

# Cohort

<figure><img src="/files/CEBZc2mXWDKDX76tvtRi" alt=""><figcaption></figcaption></figure>

A cohort of users is a static grouping of users that can be defined after filtering on your current dashboard. For example, today I can filter my dashboard for all users who signed up in the past 24 hours (perhaps during/after a high traffic live event). If I create a cohort from these users, I can return after a month and load the cohort to observe their behaviour.

<figure><img src="/files/t6EPvkGirJt3ZZqiAEZF" alt=""><figcaption></figcaption></figure>

Selecting Public will make the cohort you have created visible to other team members for use and editing.

You are able to use pre-existing cohorts to create additional cohorts.&#x20;


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/vesper-insights/analytics-dashboards/dashboard-controls/cohort.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
