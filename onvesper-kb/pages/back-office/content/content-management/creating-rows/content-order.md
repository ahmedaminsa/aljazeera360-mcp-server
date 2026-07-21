> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/content/content-management/creating-rows/content-order.md).

# Content Order

Within Back Office *Content managers* have the ability to sort the content in different ways. This page is an extension of [Step By Step Row Creation Guide](/platform-knowledge-base/back-office/content/content-management/creating-rows/step-by-step-row-creation-guide.md) Step 3, Customize Content section.

Usually *Content managers* want to display a specific category of video assets in each *Row*. The Backend Office enables that, letting to choose the correct type of content. A drop-down list shows the different categories grouped in *Automated* and *Curated* options (for more information about these categories [Creating Rows](/platform-knowledge-base/back-office/content/content-management/creating-rows.md)):

<div align="left"><figure><img src="/files/xNozDRLK35FAQdV9JuRG" alt=""><figcaption></figcaption></figure> <figure><img src="/files/etdMLRFTbFLSM75MrWJg" alt=""><figcaption></figcaption></figure></div>

*Automated* (live events) types are automatically sorted, thus, Content providers do not have any control (more details in [Live Event Rows and Tournament Filter](/platform-knowledge-base/back-office/content/content-management/creating-rows/live-event-rows-and-tournament-filter.md)). However, on the *Curated* (VOD) content (*Playlists* and *Tagged items*), Content managers are allowed to apply the following sorting (Create/Edit a Row > Customize Content):

<figure><img src="/files/G3dDHwg8jLknXfdbdFpg" alt=""><figcaption></figcaption></figure>

* Alphabetical (A-Z): sorts content in alphabetical order (from A to Z)
* Alphabetical (Z-A): sorts content in reversed alphabetical order (from Z to A)
* Created (ascending): sorts content based on the content creation date from the oldest to the newest
* Created (descending): sorts content based on the content creation date from the newest to the oldest
* Publish Date (ascending): sorts content based on the content publication date from the oldest to the newest
* Publish Date (descending): sorts content based on the content publication date from the newest to the oldest

Worthy to mention the difference between *Creation* and *Publication* dates. The *Creation* date is triggered when a video asset is added to the DVE. But this asset remains in draft until a content manager decides to *publish* it. Both fields can share the same date when they are uploaded and directly published. In other cases, as in onboarding processes, when batch of videos are uploaded at once, the same date can be also set in both fields to ease the process. But those fields can also differ: a video asset can be created and scheduled for a future publication (admin support can use "Edit Video Actions" in DVE - see screenshots below), or can be created and its publication date set in the past when that happened prior to the asset upload (only for onboarded content):

<figure><img src="/files/VBcBcOIAhk5Ou3AfVLKo" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/Rvab1VKPde23yih0WKMN" alt=""><figcaption></figcaption></figure>

Notes:

1. Once a video is published the last published date field can only be updated by admin support, not by content managers. This edit action for this field only exists as a failsafe in case a content manager accidentally un-publishes/republishes a video
2. Publish date for already existing videos (prior to 2023) are backfilled with the existing Creation Date

## **Recent Update to "New" Rows**

Previously, the "New" row type would only display the latest videos published to the platform without any option for further curation. Now, content managers have more control over these rows.

* Content managers can now add specific tags to "New" or "Recently Added" rows for better targeting and personalization.
* For example, you can now create a "Recently Added Movies" row for anything tagged "movie" or a "Recently Added Comedies" row for items tagged "comedy."
* How it works:

  * When creating or editing a row of the type "New," you will now see a field to add associated tags.

  <figure><img src="/files/8HRT10UB1EVgukc7TTFk" alt="" width="563"><figcaption></figcaption></figure>

  * Once saved, these tags are then applied rendering the row on the UI.&#x20;

  <figure><img src="/files/g1RLgsGObz2pGVgiMxis" alt="" width="563"><figcaption></figcaption></figure>

  * These tags are then applied when the row is rendered on the UI.&#x20;

  <figure><img src="/files/uvCO7Ij5IOSntnIAPJpt" alt="" width="563"><figcaption></figcaption></figure>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/content/content-management/creating-rows/content-order.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
