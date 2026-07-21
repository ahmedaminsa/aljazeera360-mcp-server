> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/dve/batch-video-upload-via-ui/uploading-batch-vods.md).

# Uploading Batch VOD's

Follow the steps below to efficiently upload your VOD content in bulk:

1. [**Prepare your videos assets**](/platform-knowledge-base/dve/batch-video-upload-via-ui/uploading-batch-vods/prepare-your-video-assets.md)**:** Your videos must be organized in a CSV file format. This file should include specific fields necessary for the upload process. Ensure all required information is accurately filled out for each video.
2. [**Upload your batch**](/platform-knowledge-base/dve/batch-video-upload-via-ui/uploading-batch-vods/upload-your-batch.md)**:** Once your video assets are properly organized, proceed to create your batch. This involves uploading your videos (if they're stored locally) and the CSV file previously created.
3. [**Review and approve your batch**](/platform-knowledge-base/dve/batch-video-upload-via-ui/uploading-batch-vods/review-and-approve-your-batch.md): Ensure that all actions on your VOD assets are accurate and approve them.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/dve/batch-video-upload-via-ui/uploading-batch-vods.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
