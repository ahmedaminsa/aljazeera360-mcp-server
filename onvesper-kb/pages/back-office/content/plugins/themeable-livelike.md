> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/content/plugins/themeable-livelike.md).

# Themeable LiveLike

The Vesper platform has enabled some capabilities in the Back Office letting residents change a set of few color variables to customize even more the gaming experiences powered by LiveLike.

These changes are applied to both Web and Mobile applications indifferently and they do not require new app builds.

Colors that can be actioned:

| Customize Theme            | Value (Hex Code) |
| -------------------------- | ---------------- |
| Background color           | #3cdd17          |
| Primary color              | #7ef7ef          |
| Secondary Background color | #7fe2ab          |
| Terciary Background color  | #06145e          |
| Text color                 | #7d72bd          |
| Correct answer color       | #9ce7b3          |
| Incorrect answer color     | #b13b6d          |
| Selected color 1           | #8d82d7          |
| Selected color 2           | #0d0352          |

<figure><img src="/files/fRlOD44aY0O9uNfyADbb" alt=""><figcaption><p>Example of themeabled LiveLike experience on mobile</p></figcaption></figure>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/content/plugins/themeable-livelike.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
