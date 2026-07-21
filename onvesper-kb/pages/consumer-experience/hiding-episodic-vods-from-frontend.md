> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/consumer-experience/hiding-episodic-vods-from-frontend.md).

# Hiding Episodic VODs from Frontend

## Feature Overview

Utilize this feature for a more streamlined and curated browsing experience for the end user.&#x20;

This feature provides minimal redundancy/repetition in thumbnail content in your realm's content discovery areas, by helping define if Single Episodes, [Seasons](https://docs.onvesper.com/platform-knowledge-base/dve/curating-grouped-content/playlists), or only top-level titles ([Series](https://docs.onvesper.com/platform-knowledge-base/dve/curating-grouped-content/collections-and-series) and/or Standalone Movies) are made visible to your users.

This is a realm-level feature, configured via realm settings in Back-Office.

### Device Availability:

* Web, Mobile, TV, Roku

### Configuration: Episodic Content Policy

This will define the visibility of episodic VOD content types across search and various front-end rows. Contact your platform account manager to request a change to this setting.

| Available Values            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Show All**                | Default Vesper behaviour. All content types (Series, Seasons, Episodes, Standalone VODs) appear in search and rows. Users can search for and directly access episodes. No filtering is applied.                                                                                                                                                                                                                                                                                                                                                                                 |
| **Show Series Only**        | <p>Only the <em>Series</em> is returned in search results. Episodes and Seasons are filtered out of most rows, with the exception of <a href="https://docs.onvesper.com/platform-knowledge-base/back-office/content/content-management/creating-rows/title-rows-mixed-content"><em>Title Rows</em></a><em>, Continue Watching, Related Content, and Continue Watching Rows.</em></p><p></p><p>Rows already configured that have episodes or seasons, will have the episodes or seasons removed</p><p></p><p>Note: standalone VODs will also appear in search such as movies</p> |
| **Show Series and Seasons** | <p>Both <em>Series</em> and <em>Seasons</em> appear in search results. Episodes are filtered out of most rows, with the exception of <a href="https://docs.onvesper.com/platform-knowledge-base/back-office/content/content-management/creating-rows/title-rows-mixed-content"><em>Title Rows</em></a><em>, Continue Watching, Related Content, and Continue Watching Rows.</em></p><p></p><p>Rows already configured that have episodes, will have the episodes removed.</p><p> </p><p>Note: standalone VODs will also appear in search such as movies</p>                     |

### Notable Feature Interactions

#### Search

* Configurable by the *Episodic Content Policy*.
* To filter episodes and seasons out of search results the *Episodic Content Policy* setting needs to be set to **Show series only**

#### Continue Watching

* Not affected by the *Episodic Content Policy*.
* If a user is mid-way through an episode, that episode continues to appear in *Continue Watching*.
* With the new *Continue Watching* configuration, the user will be taken to the **Series Interstitial**, displaying the **series artwork** on the thumbnail.

#### **Related Content**

* Not currently tied to the *Episodic Content Policy*.
* Only **Series**, **Playlists**, and **Standalone** **VODs** are ever returned.
* Episodes and Seasons will never appear as related content.
* For more on **Related Content** see [here](https://docs.onvesper.com/platform-knowledge-base/consumer-experience/related-content)

#### Recommendations

* Not currently tied to the *Episodic Content Policy*.
* Logic for enabled realms:
  * If **Episode** selected → return **Series**.
  * If **Standalone VOD** selected → return **Standalone VOD**.
  * If **Trailer VOD** selected → return **Series**, **Playlist**, or **Standalone VOD** depending on the associated content.
* Note: *Standalone VODs* may belong to a playlist, but the returned result will always match the trailer’s associated standalone VOD.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/consumer-experience/hiding-episodic-vods-from-frontend.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
