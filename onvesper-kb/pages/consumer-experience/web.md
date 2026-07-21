> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/consumer-experience/web.md).

# Web

- [Domain Forwarding Flows](https://docs.onvesper.com/platform-knowledge-base/consumer-experience/web/domain-forwarding-flows.md)
- [Link to a licence or pre-applied promotion in checkout](https://docs.onvesper.com/platform-knowledge-base/consumer-experience/web/link-to-a-licence-or-pre-applied-promotion-in-checkout.md): Details of how to link to specific licence, promotions, and other content in the Vesper web application
- [Link to a moment within a video](https://docs.onvesper.com/platform-knowledge-base/consumer-experience/web/link-to-a-moment-within-a-video.md)
- [Installing Common Tags With Google Tag Manager](https://docs.onvesper.com/platform-knowledge-base/consumer-experience/web/installing-common-tags-with-google-tag-manager.md): Google Tag Manager is a tag management system that allows you to quickly and easily update measurement codes and related code fragments collectively known as tags on your website or mobile app.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/consumer-experience/web.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
