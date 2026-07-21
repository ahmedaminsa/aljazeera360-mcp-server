> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/dve/curating-grouped-content/collections-and-series.md).

# Collections & Series

{% hint style="info" %}
Collections are **manually** ordered groupings of Playlists (e.g. Playlist1, Playlist4, Playlist3, Playlist8, Playlist2)

Series are **numerically** ordered groupings of Seasons (e.g. Season1, Season2, Season3, Season4)
{% endhint %}

Once your Playlist/Season is published it can be grouped with others within a a Collection/Series. To start, navigate to the Collections section of the VOD platform and select Create.

<figure><img src="/files/5HvZcwwUtvMrCtmY6Blz" alt=""><figcaption></figcaption></figure>

Fill in the metadata to create

<figure><img src="/files/EHwevM618U72JNpU98Pe" alt=""><figcaption></figcaption></figure>

**Title\***: The name of the Collection/Series

**Description**: A high level description of the video.

**Language\***: The language that you would like the video to be display as, for example: English or Italian.

**Tags\***: The tags are used for the Vesper platform when searching for videos or can be used to allocate the video to a certain row on Vesper. &#x20;

**Cover Image\***: This image will be the complete background image when the user is consuming the on the DVE. The image dimensions should be 1920x1080 .jpg no larger than 1mb in total size.&#x20;

**Thumbnail Image\***: This image will be used in displaying the grouped content on the Vesper realm. The image dimensions should be 640x704 .jpg no larger than 1mb in total size.&#x20;

**Title Image**: This image will be displayed when a Row Type of "List of Shows" is selected in Row Creation.

**Poster Image**: This image will be displayed if a List of Shows or Playlists type of row is created and Poster Type is selected.&#x20;

**Collection Logo: Coming Soon**

**Content Owner Logo: Coming Soon**

**External ID:** A video ID, type string (e.g. 12345a, playlist\_1, season\_10). When batch uploading VOD assets or utilizing Onboarder API, this field will be required.&#x20;

<figure><img src="/files/D3jpHIF5FB9r87B1wVLo" alt=""><figcaption></figcaption></figure>

**Typed tag**: User facing tags that have a structure of key:value, for example adsTag:SHOW or adsTag:HIDE (note, these must be set prior to being available for allocation)

**Content Rating:** The rating defined by the content standard your offering adheres to. This is specified per country based on the rating agency that maintains the standard. To specify multiple different regions press the 3 dots and add country

<figure><img src="/files/oKJTH4ja13SmqnePIkip" alt=""><figcaption></figcaption></figure>

Once created the Collection/Season will need content populated. Select your created collection and manage the content by adding playlists/seasons

<figure><img src="/files/pDP85zrHdfQkv2HM3GdQ" alt=""><figcaption></figcaption></figure>

You will then be able to select which playlists/seasons are considered part of this collection.

<figure><img src="/files/HGB11jWQviDaAEZOxmY8" alt=""><figcaption></figcaption></figure>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/dve/curating-grouped-content/collections-and-series.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
