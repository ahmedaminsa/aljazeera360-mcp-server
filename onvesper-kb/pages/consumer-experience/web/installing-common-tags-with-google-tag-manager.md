> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/consumer-experience/web/installing-common-tags-with-google-tag-manager.md).

# Installing Common Tags With Google Tag Manager

[Here's](https://support.google.com/tagmanager/answer/6102821?hl=en) Google's overview on Google Tag Manager to get you started.&#x20;

To get your Google Tag Manger setup code added to your Endeavor Streaming web app, please reach out to your Account Manager and provide your GTM ID (GTM-xxxxxx) and the Google Tag Manager Setup code to continue.&#x20;

#### 1. How to add Meta Pixel with Google Tag Manager on your web app&#x20;

If you're using Google Tag Manager to manage tags for your website, you can add your Meta Pixel to your Google Tag Manager account to measure and optimize the results of your Facebook advertising.&#x20;

[Here's](https://www.facebook.com/business/help/1021909254506499) Meta's walk through guide on how to install your Meta Pixel through Google Tag Manager.&#x20;

#### **2. How to implement OneTrust Consent Management Platform on your web app**

{% hint style="warning" %}
The OneTrust consent banner **will not work** if your users have any form of software that prevents GTM from running (such as Ublock or some specific web browsers).
{% endhint %}

The preferred and recommended approach of implementing OneTrust CMP would be to provide the production script to your Account Management team by following the directions [here](/platform-knowledge-base/consent-management-platforms/onetrust/configure-onetrust.md). However, you may implement OneTrust via GTM tag by following OneTrust guidelines outline on their website [here](https://my.onetrust.com/s/article/UUID-d81787f6-685c-2262-36c3-5f1f3369e2a7?language=en_US).&#x20;


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/consumer-experience/web/installing-common-tags-with-google-tag-manager.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
