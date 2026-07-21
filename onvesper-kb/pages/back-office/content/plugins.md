> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/content/plugins.md).

# Plugins

The Vesper platform empowers residents to integrate customized experiences into their applications seamlessly, without requiring additional effort on the Vesper platform's end. Once enabled, plugins become fully self-service: residents have the flexibility to create, manage, and remove them as needed.

Residents are allowed to integrate this external customizations thanks to our **iFrames** support, which are view spaces within the Mobile, Web, or both applications simultaneously in which a resident can inject their own content.

<figure><img src="/files/HoinQFHyU9HLF6eGC9OO" alt=""><figcaption><p>Example of an iFrame over an ad insertion</p></figcaption></figure>

In addition, we have integrated **LiveLike** into the Vesper platform, letting residents add games, quizzes, polls, predictors, chats and other experiences powered by the third party into their mobile and web apps.

<figure><img src="/files/I1uh67rwncczN2NVqOLa" alt=""><figcaption><p>Example of a LiveLike experience integration</p></figcaption></figure>

Once the setup is completed at the LiveLike dashboard, the configuration in the Vesper Back Office is simple and self-service. Residents may enable these experiences under specific content or under menu item. Restrictions can be applied to licenses, devices, locations, and languages.&#x20;

For more information about these capabilities, please talk to your Account Manager.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/content/plugins.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
