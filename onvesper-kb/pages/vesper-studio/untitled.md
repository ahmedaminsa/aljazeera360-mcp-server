> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/vesper-studio/untitled.md).

# Overview

[**Vesper Studio**](https://studio.onvesper.com) is the native, browser-based, fully integrated clipping and Virtual Live Linear channel creator tool provisioned to each Vesper resident (you).&#x20;

The Vesper Studio platform capabilities include:

* [**Editor**](/platform-knowledge-base/vesper-studio/editor.md): Self-service clipping tool that allows a content manager to clip from a livestream or VOD asset to create new VOD assets that will automatically populate in your DVE CMS.&#x20;
* [**Broadcaster**](/platform-knowledge-base/vesper-studio/broadcaster.md)**:** Self-service Virtual Live Linear channel creator. This tool allows you to create fully integrated live channels for your realm from existing VOD assets from your video catalogue in the DVE.&#x20;

You can access Vesper Studio to make edits via this URL: <https://studio.onvesper.com/>. Your account manager will have set you up as a resident for that realm and you’ll have received an email asking you to set a password. The login for this tool is the same as you use for Back Office.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/vesper-studio/untitled.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
