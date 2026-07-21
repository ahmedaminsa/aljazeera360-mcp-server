> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/dve/video.md).

# Video

Once you have logged into the [DVE platform](https://vod.onvesper.com), the first page that you will see will be the *Videos* page.&#x20;

Here you can see a list of the videos which have been uploaded to the platform and using the navigation bar on the videos page you can see the different stages that the video will sit in.

<figure><img src="/files/31puAA3oeXX0xbIQlsts" alt=""><figcaption></figcaption></figure>

## How to upload a video

If you ever need to upload videos to the DVE, there are two easy options you can follow:

### Upload Video

You can use on the **Upload** / **Upload Video** buttons on the right hand corner of the platform. Once you click, a pop out box will appear in the middle of the page. Here you can either Drag and Drop the video in the box, or you can select videos on your computer to be uploaded. Supported formats are *avi*, *mp4*, *mpeg*, *mov*.

Once the video(s) are uploaded, their metadata is available for edition:

<figure><img src="/files/iwTItdHqkKqL8HVVcLVM" alt=""><figcaption><p><em>Upload Video</em> process diagram</p></figcaption></figure>

### Create New Video

You can click on the **+ (Create New Video)** button next to *Upload Video.* Then, the following side window will pop out:

<figure><img src="/files/d9RkLJFBfSAqKz3UptLS" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/oOmYxsL6py9WQLpomWis" alt=""><figcaption><p><em>Create New Video</em> pop up window</p></figcaption></figure>

You will be able to:

* Provide localised metadata
* Specify the playback type
* Configure video artwork
* Add tags & typed tags to the video asset

The main difference between the two described options is that the first (historic) option allows users to   fill the metadata once the video is uploaded, while the new version allows users to do everything at once. On top of that, the *Create New Video* option lets users create VOD assets using only metadata: title, description and thumbnail, allowing users to upload the video later on. Check the next subpages for more details on the [Metadata](/platform-knowledge-base/dve/video/metadata.md).

This option is helpful for pre-populating or scheduling video-on-demand (VOD) content. You can create assets without an associated video (using just metadata and artwork), and then add the video content later through the *Manage Source* function. You can also benefit from the *scheduling* feature to publish the video in the future. For more information about *sources* and *scheduling*, refer to [Video Content Sources Management](/platform-knowledge-base/dve/video/video-content-sources-management.md) and [Scheduling Releases](/platform-knowledge-base/dve/video/scheduling-releases.md).

**Understanding your Video**

On the *Videos* page, you'll find the following fields just above your list of videos:

* **Title:**  Video Name                                                                                                                        &#x20;
* **Modified:** Date the video was modified                                                                                           &#x20;
* **Duration:** Length of the video                                                                                                                &#x20;
* **Status:** Draft, Processing, Error or Published

### Video Status &#x20;

The navigation bar on the *Videos* page gives the stage your videos are at on the platform.

**All:** Displays all videos on the platform, regardless of their status, including drafts, processing, or errors.

**Published:** Shows you all published videos in the DVE. Once published, these appears on the platform for your users to watch.&#x20;

**Draft:** Shows all the videos which are waiting on being published, you may need to add on related metadata or thumbnails. Once done, you can publish the video which will make it live on the platfor&#x6D;**.**

**Processing:** Shows all the videos which are currently being uploaded to the DVE. This should only take around 5 - 15 minutes. If the video is still in this queue after around 15 minutes then it would be best to log a ticket with your B2B customer support team.

**Error:** Shows all the videos which experienced an error during processing. If you have an issue, please see the [Video Error Reporting](/platform-knowledge-base/dve/video-error-reporting.md) section.

**Last 7 Days:** Shows all the videos which have been uploaded to the platform over the past 7 days.

**Last 24 Hours:** Shows all the videos which have been uploaded to the platform over the past 24 hours.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/dve/video.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
