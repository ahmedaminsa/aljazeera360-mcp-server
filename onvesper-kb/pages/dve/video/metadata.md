> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/dve/video/metadata.md).

# Metadata

Once the video has been uploaded to the DVE platform, you can edit the metadata of your video by selecting **'Edit Metadata'** on the right hand side of the page.

![](/files/-LzhWDd8prK-BR6rl0cf)

The editable metadata fields for a video are as follows:

{% hint style="info" %}
Fields marked with an asterisk (\*) are mandatory and must be completed before you can Save or Publish your video.
{% endhint %}

**Title\***: The name of the video.

**Description**: A high level description of what the video is.

**Language\***: The language that you would like the video to be displayed as, for example: English or Italian. &#x20;

**Status**: Indicates whether the video is in *Draft* or *Published* state. To publish your video, please change the status and click **Save** at the top of the page to update the metadata.

<figure><img src="/files/HNdEl6HIQCFjTXQcW3el" alt=""><figcaption></figcaption></figure>

**Tags\***: The tags are used for the Vesper realm when searching for videos or can be used to allocate the video to a certain row on your platform.

**Playlist**: Shows what playlist the video will show up on in the Vesper realm.

[**Typed Tags**](/platform-knowledge-base/dve/video/typed-tags.md)**:** These are predefined values that correlate to categories or known sources defined by your Project team and relate to a range of categories, asset types, content sources or air dates.

**Geoblocking**: Ability to set Geo-blocking for single videos to not show in certain countries. (see [Geo-Blocking](/platform-knowledge-base/dve/geo-blocking.md))

**Media RSS Content ID**: Upstream delivery content ID from another CMS.

**Mid-roll:** CUE points (in seconds) that will trigger mid-roll ads if dynamic ad insertion is enabled.

[**Subtitles**](/platform-knowledge-base/dve/video/subtitles.md): You can upload subtitles to your video. These must be a SCC, SRT or VTT format.

**DGE Event ID**: The event ID for a video archived from the Streaming Exchange platform (DGE). \
This can be set manually to ensure live -> vod link is maintained.

**External ID**: ID used for stats or other integration purposes.

![Metadata Fields](/files/-LzlDBwgPI4_Wx8awAW8)


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/dve/video/metadata.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
