> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/content.md).

# Content

The ‘Content’ section of Back Office is an area that allows you (Resident) to manage how your content is presented to customers as well as the creation of Promo notifications.

<figure><img src="/files/j2hkcF0NmyG760Rr8hxv" alt=""><figcaption></figcaption></figure>

There are a whole host of creative controls that you have as a resident to help bring your content to life including:

* [Content Management](/platform-knowledge-base/back-office/content/content-management.md): This is where you can manage how your content is presented on your platform for customers to consume.
* [Notifications](/platform-knowledge-base/back-office/content/notifications.md): This is where you are able to create and have a Promo code notifications on your realm for customers to see when they go onto your platform.
* [Advertising](/platform-knowledge-base/advertising/advertising-on-vesper.md): This section will guide you through configuring advertising for your application(s).
* [Embed Player](/platform-knowledge-base/back-office/content/embed-player.md): This section will guide you through setting up and configuring our embed player for insertion into your own website.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/content.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
