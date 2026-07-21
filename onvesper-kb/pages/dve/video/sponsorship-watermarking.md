> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/dve/video/sponsorship-watermarking.md).

# Sponsorship Watermarking

Video Exchange provides the option to add a "watermark" to specific VOD content. These watermarks are displayed over the video player by Vesper front ends during playback as images on the user interface.

This functionality is designed to allow you to build a playlist or group of videos that are sponsored by a partner. You can either leave the watermarks associated to the video, or remove/edit them in future if your sponsor changes or a deal ends.

## Configuring a watermark

Watermarks are part of our VOD metadata. You can add them in the video page below other image data (e.g. Thumbnail, Cover, Poster).

<figure><img src="/files/0xZxiEYLJqTdwdUc2fvH" alt=""><figcaption><p>Add watermark option</p></figcaption></figure>

When clicking add watermark, you will be shown your site's library of existing watermarks. This allows you to re-use any previously configured watermarks quickly, and assign them to your video.

<figure><img src="/files/WKid7NuWKGB7silzm9Er" alt="" width="293"><figcaption></figcaption></figure>

## Create a new watermark

To upload a new watermark, select the Upload option, and provide an asset (see tips below for more details). Our UI recommends 250x250 PNG images, but the size is at your discretion.

Once you've uploaded a new watermark, you can set positioning and scaling properties in the screen below.

<figure><img src="/files/bdcoKH5rrvUgEHSXQcm1" alt="" width="443"><figcaption><p>A preview window will playback your video content to demonstrate how your scaling will be applied</p></figcaption></figure>

The preview provided here is indicative only, it does not guarantee final position, as watermarks are rendered relative to the video player size, not the video content itself. If you need to guarantee position, Endeavor Streaming always recommends producing your video content with watermarks embedded in the video content.

### Scaling & Positioning

#### Watermark position:

* **Top-left**: Render relative to the top left of the video player
* **Top-right:** Render relative to the top right of the video player
* **Bottom-left**: Render relative to the bottom left of the video player
* **Bottom-right:** Render relative to the bottom right of the video player

#### Scale type & percentage

Defines how the video player should scale the image. The percentage value is the % of the screen space available on the browser or mobile device (so 25% would be a quarter of the available space). Scale type defines whether that is 25% of the available vertical space, or 25% of the available horizontal space.

* **Height**: Render the image as x% of the available *vertical* space
* **Width:** Render the image as x% of the available *horizontal* space

For wide image assets, we'd recommend using "width" as the scale type. For images that are taller than they are wide, use "height".

You only need to decide this once, after these properties are set, they will be saved against this watermark, and applied again when you chose this watermark from your library.

### Localised Watermark <a href="#localised-watermark" id="localised-watermark"></a>

Additional watermarks can now be created for localisation purposes, this introduces:

* Localisation support for watermarks, enabling a VOD to display different watermarks in different countries.
* Support for additional metadata *(watermark/sponsorship URL)*, is optional and, when available, is displayed in the info tray on Web, where users can navigate to it. *(this metadata isn’t rendered on Mobile or TV)*

#### To configure a localised watermark <a href="#to-configure-a-localised-watermark" id="to-configure-a-localised-watermark"></a>

* Click “Manage Watermark“ or "Add VOD Watermark“ from the drop-down in the Watermark section which exposes the Watermark Library where watermarks can be configured as outlined in [**Create new watermark**](#create-a-new-watermark) above.
* To update which countries where this watermark will be available click 'Show Country Selector' and search for or select a country from the drop down menu:<br>

  <figure><img src="/files/k0V86bzfXqBcHBp6BGcu" alt=""><figcaption></figcaption></figure>
* By checking the “Default Localisation“ checkbox, you can specify whether the configured localisation should be presented as the default (fallback) if a country does not have a watermark assigned.
* There is also the ability to add different locations within the same watermark where different metadata / logo can be displayed depending on region, to do this click the Add button and again configure your metadata / logo:

<figure><img src="/files/bWN29BvAFdeIpGvKsm3r" alt="" width="295"><figcaption></figcaption></figure>

## Customer Watermark

Vesper has the ability to add a customer specific watermark which is set at an account level which would subsequently be applied to all VOD's in the customer's catalogue. Should you wish to implement this please speak to your Platform Account Manager.

## Tips and best practices

It's advised to create your watermark image asset with around 65% opacity, so that it is visible but not overbearing.

As the watermarks are dynamically rendered on each of the Vesper front ends, the positioning is not guaranteed to be identical across platforms.&#x20;

If you need the watermark to appear in a specific location on the video (for example, away from in-video graphics, scores etc) you are advised to include some transparent pixels as padding in the image that's uploaded.

One option is to provide a 1920 x 1080 PNG with the watermark asset in the expected position, and then set scaling to 100% of width. Depending on the rendered video size this will not guarantee exact position, but it can be helpful to visualise before upload.

## FAQs&#x20;

#### Why doesn't my watermark show when using casting devices?

Apple AirPlay and Google Chromecast provide significantly less control over the video player experience. Due to technical limitations we are unable to render custom interface elements over playback on these platforms.

If you require the watermark to always be visible, please provide it as part of the video asset which is uploaded to video exchange.

Watermarks cannot be created using the Onboarder API or Batch support. However, a watermark created in Vesper VOD can be referenced/assigned to a VOD using the Onboarder API or Batch support.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/dve/video/sponsorship-watermarking.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
