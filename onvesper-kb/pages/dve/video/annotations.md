> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/dve/video/annotations.md).

# Annotations

Annotations are used on videos in order to help the viewer jump to certain segments of the video. \
For example, in Football, the viewer can skip to any red cards, goals, or the start or end of the match.

When editing a video in the DVE platform, you can add annotations by clicking the "**Annotate Video**" button located in the "*Edit Video*" section beneath the video preview.

You will know when annotations have been applied to a video as you will notice a thin white line with dots show on the preview of the video.

![](/files/-M-B5rIXB2ud-xJQSpUe)

After you have clicked '**Annotate Video**',  a pop-up box will appear with the video and in the top right hand corner you will notice a '**Create Annotation**' button.&#x20;

![](/files/-M-B7-CfOtJUw41YU1kE)

Once you have selected the '**Create Annotation**' button, another pop-up box will appear in front of the original pop-up box.&#x20;

It is in this new area that you can set a Title for the annotation and Start Time to apply the annotation (It is best to know exactly what time to use beforehand).

![](/files/-M-BARYKyIlw88ReMDAs)

Once you have filled in the Title and Start Time of the annotation, on the left hand side you will notice a Preview Annotation (This is the image that will be used for that particular annotation). \
\
Underneath the Preview Annotation are two boxes:

* **Timestamp Thumb:** This will be the image from the video that matches the Start Time you entered.&#x20;
* **Custom:** We recommend using a custom image for optimal quality. This image will need to be in size 1920 x 1080 and under 1mb.

After selecting which image you will be using, click on the '**Save**' button and you will be taken back to the original pop-up box.&#x20;

Upon opening the preview pop-up, you will observe a thin white line. This line will be dotted with small white markers, each corresponding to the annotations you've newly created.

![](/files/-M-EsIJ-YK3ogcQt_7wv)

When hovering along the white dots, the thumbnail will show up along with the title you entered.

After the video is published, annotations will appear on the video, making it easier to jump to specific sections of the video.

![Video with annotation](/files/-M-F-Np6Dc7AaOa09viF)


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/dve/video/annotations.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
