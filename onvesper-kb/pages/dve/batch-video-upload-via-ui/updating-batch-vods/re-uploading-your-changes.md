> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/dve/batch-video-upload-via-ui/updating-batch-vods/re-uploading-your-changes.md).

# Re-uploading your changes

1. Once the changes have been made and saved you need to navigate back to the “Batch Processing” section within Vesper VOD.
2. Click “New Batch Process” in the top right hand corner

<figure><img src="/files/8neCy5VutpALHJAKkjzY" alt=""><figcaption><p>New Batch Process </p></figcaption></figure>

3. This will take you through the following steps;
   1. Title / Language&#x20;
      1. Name - Of Batch
      2. Default Language - Of your service
   2. Uploading VOD's
      1. You can ignore this section as you are not uploading any new VOD’s to the service
   3. Updating VOD's
      1. Upload your saved file
      2. Click “Review and Approve”
   4. Review and Approve&#x20;
      1. This will show you the breakdown of your doc;
         1. Errors - If you receive any errors please reach out to your TAM
         2. Create - No VOD’s created in this scenario (Please refer to the previous section "Uploading Batch VOD's to go through this)&#x20;
         3. Update - The number of VOD’s you updated - Note, if you did not remove the VOD’s that you were NOT updating from the sheet then they will still be updated according to the UI, but the metadata will remain the same.
         4. Delete - No VOD’s deleted

<figure><img src="/files/wrRODJjj3rRveyxS3huk" alt=""><figcaption><p>Review and Approve </p></figcaption></figure>

9. One you are happy, Click approve (bottom right)
10. And you file / updates will start processing

Once complete, It is best just to open up one of the VOD’s you updated and check that the tag has been added.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/dve/batch-video-upload-via-ui/updating-batch-vods/re-uploading-your-changes.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
