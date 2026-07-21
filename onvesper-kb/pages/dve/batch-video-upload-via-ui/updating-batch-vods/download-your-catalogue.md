> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/dve/batch-video-upload-via-ui/updating-batch-vods/download-your-catalogue.md).

# Download your Catalogue

To do this follow the instructions below:

**Vesper VOD**

1. Login to Vesper VOD (<https://vod.onvesper.com/?#/login>)
2. Navigate to the “Batch Processing” tab

<figure><img src="/files/ekL655Psg1GXEKpF4nlk" alt=""><figcaption><p>Batch processing tab</p></figcaption></figure>

3. In the top right hand corner hit the “Download Catalogue(s)”

<figure><img src="/files/jA4hoZBtE8XW3aONxNPT" alt=""><figcaption><p>Download Catalogue(s)</p></figcaption></figure>

4. Make sure you hit "Generate New"

<figure><img src="/files/FIwIHsKLeTUmnLpY7SuV" alt=""><figcaption><p>Generate a new file </p></figcaption></figure>

{% hint style="info" %}
IMPORTANT: This is super important otherwise you are at risk of downloading an old version of your catalogue and overriding changes that you have made in the past.&#x20;
{% endhint %}

4. This will download your video entire catalogue into a csv
5. Open the CSV


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/dve/batch-video-upload-via-ui/updating-batch-vods/download-your-catalogue.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
