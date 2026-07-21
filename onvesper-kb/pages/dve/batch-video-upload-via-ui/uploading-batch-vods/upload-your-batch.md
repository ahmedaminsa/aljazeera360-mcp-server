> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/dve/batch-video-upload-via-ui/uploading-batch-vods/upload-your-batch.md).

# Upload your batch

## Create your new batch

* Sign in to [Vesper VOD](https://vod.onvesper.com/?#/login)&#x20;
* Select 'Batch Processes' from the top bar navigation menu
* Select 'Create New Batch Process'&#x20;
* Give the 'Batch' a unique name e.g. "VOD Upload 1\_08112023"
* Choose the default language (defaults to realm default language)
* Select 'Next'

<figure><img src="/files/vW8z2Sj3XWuFryv1BkFj" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
If you do not have a Vesper VOD account, please reach out to your Client account management team (PM/TAM/Sales Engineer)
{% endhint %}

## Upload local assets *(optional step)*&#x20;

* If you've referenced assets within your csv file that are stored locally on your machine, you'll need to drag and drop these into your batch from your desktop
* Select 'Next'

{% hint style="info" %}
If all files referenced in your .csv file are available via S3 bucket or a public HTTP/HTTPS link you can ignore this step by selecting 'Next'
{% endhint %}

<figure><img src="/files/jDUb890PdrkUwM5qiZ5q" alt=""><figcaption></figcaption></figure>

## Upload your CSV file

* Download the CSV template and populate the fields
* Once ready upload the CSV
* Select 'Review & Approve'

<figure><img src="/files/kQrFvxOapyrzOQlrxxvV" alt=""><figcaption></figcaption></figure>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/dve/batch-video-upload-via-ui/uploading-batch-vods/upload-your-batch.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
