> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/dve/curating-grouped-content.md).

# Curating Grouped Content

<table data-view="cards"><thead><tr><th></th><th></th><th></th><th data-hidden data-card-cover data-type="files"></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td>Playlists &#x26; Seasons</td><td></td><td></td><td><a href="/files/UFgPkcZ9vpNi36DhRI4C">/files/UFgPkcZ9vpNi36DhRI4C</a></td><td><a href="/pages/-LzNIJh8tg3RP1_CNj7I">/pages/-LzNIJh8tg3RP1_CNj7I</a></td></tr><tr><td>Collections &#x26; Series</td><td></td><td></td><td><a href="/files/dwcsRvo6wartKPG9fpTA">/files/dwcsRvo6wartKPG9fpTA</a></td><td><a href="/pages/aBAHPPTTzAOBUvuxlpfB">/pages/aBAHPPTTzAOBUvuxlpfB</a></td></tr><tr><td>Display &#x26; Watch order</td><td></td><td></td><td><a href="/files/PQygcU9jLXJsWvKB5u1g">/files/PQygcU9jLXJsWvKB5u1g</a></td><td></td></tr></tbody></table>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/dve/curating-grouped-content.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
