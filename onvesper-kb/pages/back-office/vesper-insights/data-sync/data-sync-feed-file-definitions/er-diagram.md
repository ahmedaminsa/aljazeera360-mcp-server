> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/vesper-insights/data-sync/data-sync-feed-file-definitions/er-diagram.md).

# ER Diagram

<figure><img src="/files/lDPUzSvWGtMCVat2sdgz" alt=""><figcaption></figcaption></figure>

Due to the asynchronous nature of the events that is received into our DWH, primary keys and foreign keys are not enforced. They are followed as a guide to understand the relationship between data entities and to enrich related entities with more data. While some events may arrive before others causing one entity to be created before it’s dependent related entity is created, it is expected that it will eventually arrive and that these constraints will become consistent.

You should plan your ingestions of the data sync feeds with this note in mind.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/vesper-insights/data-sync/data-sync-feed-file-definitions/er-diagram.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
