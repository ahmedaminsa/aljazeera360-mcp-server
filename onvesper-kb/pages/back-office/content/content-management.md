> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/content/content-management.md).

# Content Management

There are a whole host of creative controls that you have as a resident to help bring your content to life including:

* [Home & Browse](/platform-knowledge-base/back-office/content/content-management/home.md) – The landing & secondary pages that your customers will see and can be fully customised to suit your needs.
* [Hero Images](/platform-knowledge-base/back-office/content/content-management/creating-hero-images.md) – The hero image is often the first visual element a visitor encounters and shows the headline content.
* [Create Rows ](/platform-knowledge-base/back-office/content/content-management/creating-rows.md)– The rows or buckets that all your Live and VOD content assets will sit in and be presented to your customers.
* [Manage your content](/platform-knowledge-base/back-office/content/content-management/managing-your-content.md) – Pin, edit & customise your heroes & rows, bringing the most important content to the top.
* [Segmentation](/platform-knowledge-base/back-office/content/content-management/segmentation.md) – Create separate heroes and rows per geo-location or device for targeted content delivery.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/content/content-management.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
