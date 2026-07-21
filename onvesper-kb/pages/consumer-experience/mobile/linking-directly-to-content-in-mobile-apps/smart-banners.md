> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/consumer-experience/mobile/linking-directly-to-content-in-mobile-apps/smart-banners.md).

# Smart Banners

Vesper Web app can support Smart Banners. When configured, any user visiting the web application on a mobile device's web browser will be shown a banner that will link them to their respective app store to download the mobile app.

<figure><img src="/files/K8Akty38UGg0A9PgcKGD" alt=""><figcaption><p>Android Smart Banner example</p></figcaption></figure>

<figure><img src="/files/D8RX2jLB9OVdVK12rtIg" alt=""><figcaption><p>Apple Smart Banner example</p></figcaption></figure>

If configured, these banners will show on any page of the Vesper web application, until dismissed by the end user.

Please consider your preferred user onboarding/subscription journey before enabling these banners, as they will drive app installs and likely encourage users to sign up and subscribe directly through the app if you have enabled In App Purchases.

Contact your Account Manager to enable smart banners on your Vesper web app.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/consumer-experience/mobile/linking-directly-to-content-in-mobile-apps/smart-banners.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
