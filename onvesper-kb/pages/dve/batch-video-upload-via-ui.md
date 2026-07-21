> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/dve/batch-video-upload-via-ui.md).

# Batch Video Upload via UI

Using our user-friendly interface, you can upload up to 1000 videos directly onto our Vesper VOD UI. This self serve UI includes a status page to indicate if there are any issues with the video so you can take action. The tooling will also allow you to bulk update or delete files.

**What you'll need to upload your video:**

**1.** Access to our Video Platform 'Vesper VOD'\
**2.** A CSV listing of your videos and metadata as specified in this document\
**3.** Files stored locally, on a S3 bucket\*, or via a publicly accessible HTTP/HTTPS link\
\
\*If you're using an Endeavor Streaming owned S3 bucket, please be aware that files stored there will automatically expire after 90 days. To avoid losing any assets, ensure they are uploaded from the S3 bucket to the Vesper VOD platform within this 90-day window

<figure><img src="/files/xvJPK29GEAppdfRv5HTM" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
If you do not have a Vesper VOD account, please reach out to your Client account management team (PM/TAM/Sales Engineer)
{% endhint %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/dve/batch-video-upload-via-ui.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
