> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/consent-management-platforms/onetrust/publish-script-for-web.md).

# Publish Script for Web

{% hint style="info" %}
This guide is intended to assist you with the initial setup of OneTrust Cookie Banner, a product not owned or operated by Endeavor Streaming. While we strive to ensure the accuracy and relevance of the information provided based on our experience with the product, you should consult the official documentation provided by OneTrust or contact their customer support for detailed instructions, updates and additional support.
{% endhint %}

After you have assigned a Geolocation Rule Group to a domain, you can publish your script in the Scripts tab. It can take up to 4 hours for changes in the script to appear on your site after Endeavor Streaming has included it in the script header of your site.

Follow the below steps within the OneTrust dashboard or watch this tutorial from OneTrust [here](https://my.onetrust.com/s/article/UUID-2808c7da-40a4-28f9-7a91-20fdedde45f8?topicId=0TO1Q000000sseOWAQ):

| Action                                                                                                                                                               | Visual                                                              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| <ol><li>On the left-side menu, go to Integration -> Scripts. Select the domain to be published and click 'Publish Production'.</li></ol>                             | <img src="/files/XFQ9PF9KCQrDPr4FRoNr" alt="" data-size="original"> |
| <ol start="2"><li>After entering the published model, you'll be provided with both testing and production scripts.</li></ol>                                         | <img src="/files/AureTQIc4qHBnGk7DOZO" alt="" data-size="original"> |
| <ol start="3"><li>Copy the production scripts and send them over to your Endeavor Streaming representative; they'll include it in the header of your OTT. </li></ol> | <img src="/files/cse2o6xMYgAdM7wD198D" alt="" data-size="original"> |


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/consent-management-platforms/onetrust/publish-script-for-web.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
