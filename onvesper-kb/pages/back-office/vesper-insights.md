> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/vesper-insights.md).

# Vesper Insights

Vesper Insights is a fresh set of tools crafted by the Vesper Data Services group. These tools empower both technical and non-technical employees of our Residents to engage in the data analysis journey independently, eliminating the need for assistance from IT experts or specialized data analysts.

This solution enables business users, marketers, and other non-technical individuals to swiftly access data in almost real-time. They can bring forth their inquiries, uncover novel insights, take actionable steps based on these newfound revelations, and attain outcomes that fuel business expansion.

Currently, Vesper Insights is comprised of four main feature sets:

* Analytics Dashboards: A compilation of dashboards that consolidate data from the entire platform. These dashboards can be customized through sorting and filtering options, and the data can subsequently be exported to CSV files.
* Self-Service Reports: Users can access desired data on-demand or through scheduled reports, providing flexibility in obtaining information.
* User Targeting: The ability to generate dynamic Segments and Cohorts, enhancing comprehension of user behaviour and the efficacy of marketing tactics.
* Data Sync: Allows you, our customers, to extract a complete copy of all data sets, updated with deltas on a daily basis, to empower your own analytics and insights.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/vesper-insights.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
