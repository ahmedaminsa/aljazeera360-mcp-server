> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/consumer-experience/television/roku.md).

# Roku

## Closed Captions

### Where can I enable Closed Captions?

To maintain a clean display and avoid overloading the screen with icons, Roku's apps group functionalities into a sidebar activated by pressing the (**\***) options button on the remote. This sidebar allows users to easily enable or disable Closed Captions.

<figure><img src="/files/kGFTV2RF9bSEQt4boL9q" alt="" width="563"><figcaption></figcaption></figure>

## Time Outs

### App Timeout Due to Inactivity

Roku devices feature a setting called **Bandwidth Saver**, which, when enabled, causes apps to time out after 4 hours of inactivity. To prevent this from happening, you can disable the feature by going to **Settings** > **Network** > **Bandwidth Saver** and turning it off.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/consumer-experience/television/roku.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
