> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/dve/video/thumbnails.md).

# Thumbnails

After uploading your video to the DVE platform and entering the required metadata, you will have the option to upload or create a Thumbnail, Cover, and Poster for your video.

<img src="/files/-LzgNX7C_7iEm-7SMjav" alt="Adding a Thumbnail for your video" width="375">

When it comes to setting a Poster, Cover or Thumbnail for the video, the images will need to meet the following requirements:

* Thumbnail = 1920 x 1080
* Cover = 1920 x 1080
* Poster = 1142 x 1600

The images will also need to be in *jpg* format and compressed under 1MB in total size. \
When applying an image for the thumbnail of the video, you have 2 options:

* **Capture As Thumbnail**: This button is found under the video preview, once you get to the frame that you would like to use as the thumbnail then click on the button and confirm. &#x20;

<div align="center" data-full-width="true"><img src="/files/-Lzg_Leepogjbws5i4sB" alt="Confirming that this particular frame will be used for the thumbnail" width="563"></div>

{% hint style="info" %}
Please note! Capture as Thumbnail takes a screen capture of the video playback in your browser and then presents it as an upload. This is not possible with DRM encrypted videos as the capture will be forbidden on many web browsers - resulting in a black rectangle being captured. Therefore this feature is not available for DRM encrypted videos.
{% endhint %}

* **Uploading image for Thumbnail**: Select the **More Options** icon on the *Thumbnail* section, a box will then pop up where you are then able to select an image which can be uploaded and used as the thumbnail.

<img src="/files/-Lzga4Xf2jw7RZsaAgXS" alt="Upload an image for your Thumbnail" width="563">

![Thumbnail showing on the Video List](/files/-LzgaTFk1u04fZ87KxSs)


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/dve/video/thumbnails.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
