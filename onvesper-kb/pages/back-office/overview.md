> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/overview.md).

# Overview

The [**Vesper Back Office**](https://backoffice.onvesper.com) is a browser-based, fully integrated customer and content management tool provisioned to each Vesper resident (you).&#x20;

The Vesper Back Office platform capabilities include:

* [**Content**](/platform-knowledge-base/back-office/content/content-management.md): Self-service tooling that gives a platform content manager the ability to easily edit hero images and associated CTAs, configure content rows, and publish across a suite of client applications at the touch of a button.
* [**Notifications**](/platform-knowledge-base/back-office/content/notifications.md)**:** In-app promotional message tooling.
* [**Users**](/platform-knowledge-base/back-office/users-1.md)**:** A natively integrated customer support tool to help you understand who’s consuming content on your platform .
* [**Reporting**](/platform-knowledge-base/back-office/analytics-1.md)**:** Insights into the Customer behaviour through dashboards and reporting.

You can access Back Office to make edits via this URL: <https://backoffice.onvesper.com>. Your account manager will have set you up as a resident for that realm and you’ll have received an email asking you to set a password.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/overview.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
