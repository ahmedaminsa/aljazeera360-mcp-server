> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/dve/curating-grouped-content/playlists.md).

# Playlists & Seasons

Once the video has been published, you have the ability to add the video into a playlist or season on the DVE and that will reflect on your Vesper realm.&#x20;

{% hint style="warning" %}
Playlists will need the VOD content ordered manually whereas a Season will always utilise the Episode Number for ordering VOD content.

While curation on the VOD platform is the same for both Playlists & Seasons, they are visually represented in different manners on front ends.\
\
Seasons must be associated with a Series. A Season created without a Series will not be displayed correctly on your platform.\
Playlists can exist independently and do not require association with a Series or Collection.

Please review [Playlists/Seasons Carousels](/platform-knowledge-base/back-office/content/content-management/creating-rows/curating-grouped-content/playlists-seasons-carousels.md) to select how your content will be displayed on the front end.
{% endhint %}

To add a video to playlist/season or create a playlist/season, you will need to go to 'Playlists' section. Once here you will see a list of all the playlists which have already been created.

![](/files/-LzkvF4gAMSX52pjc0wC)

### Creating a Playlist/Season

To create a playlist/season, you will just need to select the 'Create New' button on the right hand side of the page.

<div data-full-width="false"><figure><img src="/files/bIZFUdz8sdLXdPtO83UL" alt=""><figcaption></figcaption></figure></div>

Once selected a pop up box will show up on the screen and you will need to fill out all the \* mandatory sections.

<figure><img src="/files/mJ273182F222SWQsc02E" alt=""><figcaption></figcaption></figure>

**Title\***: The name of the video

**Description**: A high level description of the video.

**Language\***: The language that you would like the video to be display as, for example: English or Italian.

**Tags\***: The tags are used for the Vesper platform when searching for videos or can be used to allocate the video to a certain row on Vesper. &#x20;

**Cover Image**: This image will be the complete background image when the user is consuming the on the DVE. The image dimensions should be 1920x1080 .jpg no larger than 1mb in total size.&#x20;

**Thumbnail Image\***: This image will be used in displaying the grouped content on the Vesper realm. The image dimensions should be 640x704 .jpg no larger than 1mb in total size.&#x20;

**Title Image**: This image will be displayed when a Row Type of "List of Shows" is selected in Row Creation.

**Poster Image**: This image will be displayed if a List of Shows or Playlists type of row is created and Poster Type is selected.&#x20;

![Once all the details have been filled in](/files/-Lzl1OxIeZWGz0KSwi7q)

#### **External ID**

A video ID, type string (e.g. 12345a, playlist\_1, season\_10). When batch uploading VOD assets or utilizing Onboarder API, this field will be required.&#x20;

&#x20;![](/files/D3jpHIF5FB9r87B1wVLo)

**Typed tag**: User facing tags that have a structure of key:value, for example adsTag:SHOW or adsTag:HIDE (note, these must be set prior to being available for allocation)

**Content Rating:** The rating defined by the content standard your offering adheres to. This is specified per country based on the rating agency that maintains the standard. To specify multiple different regions press the 3 dots and add country

<figure><img src="/files/oKJTH4ja13SmqnePIkip" alt=""><figcaption></figcaption></figure>

### Adding/Managing Videos

Once you have filled in the required fields and added in the thumbnail and cover image, you can then look to start adding videos into the playlist.

To add videos into a playlist, you will need to click on the desired playlist. Select **'Manage'** button on the right hand side and a drop down list will appear with the following options;

**Edit** **Metadata**: Ability to make changes to the title, description, tags, language and creative of the playlist itself.

**Manage** **Videos**: Add or remove videos from the playlist.

**Delete**: This deletes the playlist but not the videos included within the playlist.

![](/files/-Lzl2SVEYzaWlIIKG-Du)

After selecting '**Manage Videos',** you will see a box slide up from the bottom of the screen and it will show the list of videos already added to the playlist.&#x20;

You can see that they are added to the playlist via the box with a green tick in it on the left hand side, just before the thumbnail/title of the video.

If you would like to remove the video then you will just need to select the same box so that the box is blank and the green tick is no longer shown.

![Videos on the Playlist](/files/-LzkyWK6s1gfmjrw1DDJ)

To add more videos to the playlist, you can search for either the full title name of the video or you can use certain words/tags to see what videos show in the results.&#x20;

When you have the videos that you would added to the playlist, then you will just need to select the empty box next the video so that a green tick will appear.&#x20;

Once you have made the changes you would like with either adding or removing videos from the playlist, select the '**Save Changes**' button.

![Searching for Videos to add](/files/-LzkydTQMc4AeGPgDczL)


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/dve/curating-grouped-content/playlists.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
