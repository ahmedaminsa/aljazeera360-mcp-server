> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/content/content-management/back-office-glossary-of-creatives.md).

# Back Office - Glossary of creatives

Use this glossary to start building your creative strategy when managing content via the Vesper Back Office platform.

{% hint style="info" %}
All creatives should be under 1MB in size.
{% endhint %}

| Creative             | Description                                                                  | Dimensions                                                               | Notes                                                                                                                                                                                                                               |
| -------------------- | ---------------------------------------------------------------------------- | ------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Hero                 | Large static banner image prominently placed on top section of the Home page | 1920x1080 .jpeg                                                          | You can reduce the image using a compressing tool such as TinyJPG or Squoosh; alternatively, you can export an image with optimised quality using your preferred photo editing software (Adobe Photoshop or Sketch are recommended) |
| Hero Title Image     | An image used as a title on a hero; it supersedes the title text             | 640x480 .png                                                             | Creative must have a transparent background                                                                                                                                                                                         |
| Hero Channel Logo    | An image used as a logo on a hero                                            | 250x250 png                                                              | Creative must have a transparent background                                                                                                                                                                                         |
| Navigation carousel  | A row displaying existing sections within the application                    | 500x500 .jpeg for static image; video 300x300 MP4 with no audio channels | You can add a video on hover, which will play when users hover over the static image                                                                                                                                                |
| Featured row         | A row containing a background creative                                       | 1920x601 .jpeg                                                           | n/a                                                                                                                                                                                                                                 |
| In-line playlist row | Background image for an in-line playlist row                                 | 1920x466 .jpeg                                                           | n/a                                                                                                                                                                                                                                 |


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/content/content-management/back-office-glossary-of-creatives.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
