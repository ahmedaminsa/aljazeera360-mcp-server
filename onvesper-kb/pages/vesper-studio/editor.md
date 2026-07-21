> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/vesper-studio/editor.md).

# Editor

The Vesper Studio editor tool allows content managers to create new VOD assets from existing live streams and VOD assets from your catalogue.&#x20;

![Vesper Studio Editor Home Page](/files/-MQBeyOzj9X3Ab8VU6hp)

**Live:** Live Streams available for clipping

**Recently Created:** Recently Created clips

**Videos:** VOD assets available for clipping.

## Clipping From A Live Stream

To clip a Live Stream simply click on the Live area on your home page.&#x20;

![](/files/-MQBfqJt_D8awtTDP6Wk)

You will see a Live Preview Window (RIGHT) and a current progress window (LEFT) which correlates to the point in time on the Live Stream or Video your action cursor is currently located.&#x20;

**Controls**

![](/files/-MQBgVV0dg4533TUCN_I)

To select an area you would like to clip simply seek on the progress bar using your mouse and click on the are you would like to start the new clip from. This point can be changed by clicking in a different area of the bar or by using the hotkeys above.&#x20;

![](/files/-MQBgrYdzW4a2wiu1Vyq)

When you have selected the start and end of the area you would like to clip Press I at the start and O at the end. You can Preview the clip by clicking the Preview button at the bottom of page and view the video prior to exporting. To publish the video click Export and then Create Clip from the Modal.&#x20;

![](/files/-MQBhNyWhADC-dpfoAj5)

Once the clip is created the video will populate in your DVE account in a matter of seconds with the title as listed above. If you wish to change any of the metadata of the clip prior to exporting, close this modal and navigate to the clips dropdown on the middle right of the page.&#x20;

![](/files/-MQBhvJ18lQMT9bh2RJq)

Here you can change the title of the clip prior to exporting. Once finished click export in the bottom right of you screen and create clip.&#x20;

## Clipping From A Pre-Existing VOD Asset

To clip a VOD Asset simply click on the Recently Created or Videos area on your home page.&#x20;

![](/files/-MQBiag6EbJhseEtM15i)

You will see a Progress Window. Unlike the Live clipping function there is no Preview image on the right hand side.&#x20;

**Controls**

![](/files/-MQBgVV0dg4533TUCN_I)

To select an area you would like to clip simply seek on the progress bar using your mouse and click on the are you would like to start the new clip from. This point can be changed by clicking in a different area of the bar or by using the hotkeys above.&#x20;

![](/files/-MQBgrYdzW4a2wiu1Vyq)

When you have selected the start and end of the area you would like to clip Press I at the start and O at the end. You can Preview the clip by clicking the Preview button at the bottom of page and view the video prior to exporting. To publish the video click Export.&#x20;

![](/files/-MQBisb-F4o_A80uF9pS)

You will now have two options:

* New Clip: This will create a brand new VOD asset with the new video you have just clipped.
* Overwrite Clip: This will overwrite the original VOD asset entirely.

Once the clip is created the video will populate in your DVE account in a matter of seconds with the title as listed above. If you wish to change any of the metadata of the clip prior to exporting, close this modal and navigate to the clips dropdown on the middle right of the page.&#x20;

![](/files/-MQBhvJ18lQMT9bh2RJq)

Here you can change the title of the clip prior to exporting. Once finished click export in the bottom right of you screen and create clip.&#x20;


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/vesper-studio/editor.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
