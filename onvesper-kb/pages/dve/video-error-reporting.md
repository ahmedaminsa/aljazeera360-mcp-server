> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/dve/video-error-reporting.md).

# Video Error Reporting

Upon completion of a video upload in the [Video Exchange (DVE)](https://vod.onvesper.com/), if any errors occur, the Content Management System (CMS) will notify the user.

This error will also be displayed in two locations:

1. On the Main video dashboard, under "*Status*":

![](/files/-M4EkjInBAqR1LGBLgEw)

2\. On the Video Asset page itself, under "*Status*" as well:

![](/files/-M4El5_T5e7ua5FmzKa6)

If a user experiences an error on upload, please complete the following steps:

1. Make sure that the video export settings of the asset are as previously advised on the [VOD Specifications Documentation](https://app.gitbook.com/@endeavor-streaming/s/knowledge-base/~/drafts/-M4EjNXGo1i29FdgUdnu/dve/image-and-vod-specifications).
2. Navigate to the video asset page that has errored on the DVE.
3. Copy the full url in the navigation bar at the top of the browser: \
   \&#xNAN;*e.g. <https://dve.imggaming.com/#/videos/131650>*
4. Email **<platformteam@diceplatform.com>** with the video asset url that has errored, and one of our team will get back to you shortly with troubleshooting steps.&#x20;


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/dve/video-error-reporting.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
