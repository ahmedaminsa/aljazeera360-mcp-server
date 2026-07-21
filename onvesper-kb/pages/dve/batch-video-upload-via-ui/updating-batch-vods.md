> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/dve/batch-video-upload-via-ui/updating-batch-vods.md).

# Updating Batch VOD's

Follow the step below to efficiently update multiple VOD assets at the same time:

{% stepper %}
{% step %}

### [**Download your Catalogue**](/platform-knowledge-base/dve/batch-video-upload-via-ui/updating-batch-vods/download-your-catalogue.md)

Start by downloading your current video catalogue in CSV format to get the latest state of your VOD assets.
{% endstep %}

{% step %}

### [**Edit your CSV**](/platform-knowledge-base/dve/batch-video-upload-via-ui/updating-batch-vods/editing-your-csv.md)

Make the necessary edits to your CSV file to update your VOD assets as needed, or flag rows for deletion using the `delete` column.
{% endstep %}

{% step %}

### [**Re-upload your changes**](/platform-knowledge-base/dve/batch-video-upload-via-ui/updating-batch-vods/re-uploading-your-changes.md)

Once your edits are complete, re-upload the catalogue file so that your changes can be processed.
{% endstep %}
{% endstepper %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/dve/batch-video-upload-via-ui/updating-batch-vods.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
