> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/content/content-management/home.md).

# Home & Browse

The landing page that your customers will see is the ‘Home’ section.

There are two main components on this page:

### 1. [HERO](/platform-knowledge-base/back-office/content/content-management/creating-hero-images.md)&#x20;

This is a large static web banner image that will be prominently placed on top section of the ‘home’ page. You are able to change the title, description and link an asset that corresponds with the hero messaging.

### 2. [ROWS](/platform-knowledge-base/back-office/content/content-management/creating-rows.md)

A row is formed from videos, playlists, upcoming events, live events or automated assets from the content API that are either automated or curated via tags or playlists. In Vesper Back Office, you can create your rows and can choose the row image, title, type of row, description and associated tags.

<figure><img src="/files/aJxhwGxkl55gihnnKnnX" alt=""><figcaption><p>Example of Home section</p></figcaption></figure>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/content/content-management/home.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
