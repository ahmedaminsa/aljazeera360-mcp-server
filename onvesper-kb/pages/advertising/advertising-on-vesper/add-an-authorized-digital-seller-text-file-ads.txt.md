> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/advertising/advertising-on-vesper/add-an-authorized-digital-seller-text-file-ads.txt.md).

# Add an Authorized Digital Seller text file (ads.txt)

[Authorized Digital Sellers for Web, or ads.txt](https://iabtechlab.com/ads-txt/), is an IAB initiative to improve transparency in programmatic advertising, while [Authorized Sellers for Apps, or app-ads.txt](https://iabtechlab.com/wp-content/uploads/2019/03/app-ads.txt-v1.0-final-.pdf), is an extension to the Authorized Digital Sellers standard.&#x20;

You can create your own authorized digital sellers (`ads.txt`) and authorized sellers for apps (`app-ads.txt`) text files to identify who is authorized to sell your inventory. These files are publicly available and crawlable by exchanges, Supply-Side Platforms (SSP), and other buyers and third-party vendors.

After you create the two text files, please reach out to your Account Management team to set up a redirect.&#x20;

Once the redirect has been created, head over to your **Vesper Admin -> Content -> Advertising -> Manage Sellers (tab)**. From there, copy and paste both the ads.txt and app-ads.txt file content and click on save.&#x20;

{% hint style="info" %}
If you do not see the Advertising menu, please reach out to your Account Management team to enable.
{% endhint %}

<figure><img src="/files/jRO4fH0EqqBivF5hpaTH" alt=""><figcaption></figcaption></figure>

Once the redirect is in place, along with the files saved on Vesper Admin, the text files can be accessed on the root of the preferred domain.&#x20;

E.g. (<https://watch.mydomain.co&#x6D;**/ads.txt>\*\*) and (<https://watch.mydomain.co&#x6D;**/app-ads.txt>\*\*).


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/advertising/advertising-on-vesper/add-an-authorized-digital-seller-text-file-ads.txt.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
