> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/dve/video/scheduling-releases.md).

# Scheduling Releases

{% hint style="warning" %}
[Interstitial pages](/platform-knowledge-base/consumer-experience/interstitial-pages.md) are required in order to use Scheduled Releases. They are necessary to provide a CTA location that displays the pending state for videos which are upcoming. For more information, please reach out to your Account Manager.
{% endhint %}

Expanding on the self-service functionality for managing new content sources, users can also plan the release of content sources. This enables users to establish a timeline for a new content source to become the active playback for a VOD. Through the DVE, users can organize three types of content releases:

* **General release**: corresponds to the initial release of a content
* **Audio release**: involves adding an audio track for playback
* **Subtitle release**: involves adding a subtitle track for playback

The *scheduling* feature can be found at:

* Video List View: click on the three dot menu and then on "Schedule a Release"

<figure><img src="/files/EuhKEoccui4EiwuRMkVG" alt=""><figcaption></figcaption></figure>

* Video Detail Page: at the bottom VOD page, click on "Schedule New"

<figure><img src="/files/PMUISj3N0b2IELoCIxzJ" alt=""><figcaption></figcaption></figure>

Either option will open the following pop up window:

<figure><img src="/files/6jz8tISAGfKtXXPglW3i" alt="" width="435"><figcaption></figcaption></figure>

To schedule a content source release, users must specify the release type, release time, and localized name. Optionally, if desired, they can select a different content source and set the audio and subtitles included in the release.

Once the configuration is saved, the content source modification is scheduled. The details are displayed in the Video Detail Page:

<figure><img src="/files/eOIzlP1n0Y40K25kwrEj" alt=""><figcaption><p>Scheduled Releases information</p></figcaption></figure>

The *Scheduled Releases* section displays the content source release name, source ID, release schedule status, release date, audio and subtitle languages *(if specified)* and a preview of the release. If users require to modify or delete the scheduled release, they can do that by clicking on "Edit Metadata" at the top of the Video Detail Page, and then go back to the proper scheduling section.

{% hint style="info" %}
**Note:**

* The content source release scheduling feature **does not** **publish** the video at the scheduled time, **it changes the VOD sources**
  * For example, if the video is in *draft* state when an updated is scheduled, it will stay in *draft* state at the scheduled time unless manually released
* For scheduling a VOD publication, please visit the *Publish Date* which can be accessed via Edit Video Actions<br>
  {% endhint %}

### UI Presentation

#### Interstitials and buckets

After configuring a Schedule, a badge will appear on the content thumbnail and relevant seasons or playlists, indicating upcoming new content, subtitles, or audio.

<figure><img src="/files/FUBS5Rq7r1mJliETFido" alt=""><figcaption><p>Upcoming content badges</p></figcaption></figure>

If you wish to change the badge labels, submit a request to your helpdesk or platform account manager. The labels available are shown below:

| key                             | default value               |
| ------------------------------- | --------------------------- |
| releaseState\_PLANNED           | Released in `{{days}}` days |
| releaseState\_PLANNED\_singular | Releasing Tomorrow          |
| releaseState\_PLANNED\_today    | Releasing Today             |
| releaseState\_RECENT            | New release                 |
| releaseState\_WAITING           | Coming soon                 |

#### The schedule page, and search

A dedicated view is available to display all upcoming releases to your end users. \
This view can be added to your [Navigation menu](/platform-knowledge-base/back-office/administration/menu-items.md) and works across all devices.

<figure><img src="/files/iVKGJMkhDlt3euyF83BH" alt=""><figcaption><p>The /releases page</p></figcaption></figure>

To enable this, please add a "View" menu item that points to `/releases` (see example below)<br>

<figure><img src="/files/PixPe7NriesFRn6dURVH" alt="" width="375"><figcaption></figcaption></figure>

The releases/schedule page will show a "badge" that uses the name of a scheduled release (in it's localised/translated form). That badge can be used to indicate the type of the new release (for example is it a new episode, or a new translation of an existing episode?), or can be named in any way that suits expressing your content.

The same badging system (utilising the name of the scheduled release) is used in search results.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/dve/video/scheduling-releases.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
