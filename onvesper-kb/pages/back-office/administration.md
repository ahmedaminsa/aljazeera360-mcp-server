> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/administration.md).

# Administration

The ‘Administration’ section of Dice Admin is where you are able to find the Audit section of the platform to be able to see the history behind the actions taken on your platform.

<figure><img src="/files/M3eDNkSD4myZS7D9iCbI" alt=""><figcaption></figcaption></figure>

[Menus](/platform-knowledge-base/back-office/administration/deprecated-menu-items.md): This is where you can configure the navigation menus of your application(s).

[Audit](/platform-knowledge-base/back-office/administration/audit.md): This is where you track the audit history of the platform.

[IP Overrides](/platform-knowledge-base/back-office/administration/ip-overrides.md): This is where you can temporarily override our Vesper System's geolocation resolution for debugging and testing purposes.

[Show EXIDs](/platform-knowledge-base/back-office/administration/exid-injection.md): This section explains how to configure EXID Injections, enabling you to identify pirated streams from external sources.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/administration.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
