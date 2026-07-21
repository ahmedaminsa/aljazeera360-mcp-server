> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/dve/video-processing-pipeline-explained.md).

# Video Processing Pipeline explained

Once a mezzanine asset has been provided, the VOD platform will get to work processing the video and making it available for streaming globally.&#x20;

If you are uploading an asset through the VOD platform's UI, you will be able to track the progress through the pipeline. The table below gives an overview of what the percentages represent.&#x20;

These percentages are not linear, they do not represent *time* (50% does not mean half of the time required has elapsed, it means half of the workload steps are complete). The time spent on a stage (and therefore at a percentage) is dependent on the complexity for the given job.

<table data-header-hidden><thead><tr><th width="249"></th><th></th><th></th></tr></thead><tbody><tr><td><strong>Percentage</strong></td><td><strong>Phase</strong></td><td><strong>Additional Details</strong></td></tr><tr><td>1-2%</td><td>Preparing</td><td> </td></tr><tr><td>3-33%</td><td>Demuxing Phase</td><td>33% means all files have finished. If there are multiple files 20% means the first has finished, (20+13/n)% means the <em>n</em>th file has finished</td></tr><tr><td>34-60%</td><td>Encoding Phase</td><td>There are many encoding jobs the percentage should be a rough indicator as to how many of the jobs have completed. > 55% meaning all jobs have completed.</td></tr><tr><td>61-98%</td><td>Packaging Phase</td><td>There are many packaging jobs. Range is similar to encoding. 98% means all jobs have completed</td></tr><tr><td>99-100%</td><td>Manifest creation Phase and Completion</td><td> </td></tr></tbody></table>

{% hint style="info" %}
If you are using Batch video uploader or the Onboarder API to provide your mezzanine files to Vesper, you will not see this level of detailed progress. The VOD product team are assessing and designing improvements to this feedback loop.
{% endhint %}

## Glossary

**Mezzanine file:** The file you originally uploaded to Vesper.

**Demuxing:** The process of extracting the signals from the mezzanine file (will include decoding the file in question).

**Encoding:** The process of converting the demuxed signal into the multiple renditions (at different bitrates) required for adaptive streaming.

**Packaging:** Segmenting the encoded renditions into chunks for delivery over streaming. Then uploading all outputs to the Content Delivery Network (CDN) to be received by end-users.

**Manifest creation:** Building adaptive streaming manifest(s) using HLS/DASH to deliver the encoded files.&#x20;

## FAQs

#### How long does it take for a VOD to process?

This is heavily dependant on the video Mezzanine file that has been provided, and the configuration for your realm. The length and bitrate of the input file, the number of renditions (bitrates) and packaged versions (HLS, Dash, Downloadable) that need to be created will all affect processing time.

Because of this variability, we can provide this guidance so that content managers and publishers can understand how to plan.

> Vesper operates a zero queue transcoding principle, and all assets begin processing as soon as they are uploaded. Vesper will process the vast majority of all uploaded videos within approximately 80% of the length of the video asset provided. So, a 30 minute HD episode is expected to be available in Draft in approximately 24 minutes. In some rare cases, this processing may encounter issues that will automatically resolve, but take the processing time to 1.5x the length of the video asset. Video resolution directly affects this time, so 4k assets may take longer to process.
>
> You should plan to upload assets at least 1.5x the length of the video before you require them to be published. Should an asset take longer than 2x the length of the the video, and it is urgent, the Vesper helpdesk team will accept a ticket to investigate. Please do not open tickets with helpdesk if it has been less than 2x, we are not able to expedite the processing time.

If you have a business case for faster uploads, or a significant amount of high resolution / high bandwidth content, contact your account management team to discuss Vesper's accelerated video processing pipeline capabilities.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/dve/video-processing-pipeline-explained.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
