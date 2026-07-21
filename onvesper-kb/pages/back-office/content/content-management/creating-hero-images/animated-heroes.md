> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/content/content-management/creating-hero-images/animated-heroes.md).

# Animated Heroes

Animated Hero's allows you to surface content in the hero section of your service. Content will playback automatically when the user lands on the page, allowing you to showcase a specific piece of content, promote an upcoming season or give a sneak preview to an exciting new series.&#x20;

{% embed url="<https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LvKlMqUAgpPfEFkrjiJ%2Fuploads%2FBWLtkCj7XbFvtCjMNEfu%2Fcropped_video%20(9).mp4?alt=media&token=c92460f4-8d3b-44ce-b39e-2964db30baac>" %}

## User Experience&#x20;

The user will access the service and land on the home page. The Background image will display for 2 seconds, before the chosen video begins to playback.&#x20;

**After 1 Minute;**&#x20;

If the video in the animated hero is the same as the video linked in the CTA then the animated hero will transition into a full screen video playback.&#x20;

If the video in the animated hero does not mirror that linked in the CTA, then the animated hero will transition back to the background image and transition to the next hero carousel (in the event there are multiple hero carousels available).&#x20;

**Video Unavailable;**&#x20;

In the event the VOD or Live asset is unavailable to the user (due to geo blocking rules, licence permissions or the asset is scheduled in the future), the video will not playback within the animated hero section and the background image will continue to display.&#x20;

## How to Configure&#x20;

### 1. Create a Hero Image&#x20;

[Create a hero image](https://docs.onvesper.com/platform-knowledge-base/back-office/content/content-management/creating-hero-images/heroes-best-practices). Then in Step 2 "Customise Hero";&#x20;

* TICK "Animated Hero"

<div data-full-width="true"><figure><img src="/files/EUW7EgPaEYqY3HONRZEj" alt=""><figcaption></figcaption></figure></div>

* An additional pop up will appear (see below) to add;
  * Animated Background Type&#x20;
    * Live&#x20;
    * VOD&#x20;
  * Event&#x20;
    * Search for the event (you can also search for Trailers here)&#x20;

<figure><img src="/files/8Kn1RBe2R9CL6FAJ3fSx" alt=""><figcaption></figcaption></figure>

* Click "Next" and "Publish" Hero&#x20;

### 2. Licence Configuration&#x20;

Given that this feature allows for content to playback in the hero image, we want to ensure this doesn’t impact the concurrency limits already set for your service. Therefore, we have added an additional setting within the licence section to accommodate for this.

[Create a Licence](https://docs.onvesper.com/platform-knowledge-base/back-office/licences/licence/creating-a-licence). Then in step 6 "Define Usage Restrictions"&#x20;

* Set "Autoplay Concurrency" to X
  * We advise that this is set to the same limit as the playback concurrency for consistency, but this is up to your discretion.&#x20;

<figure><img src="/files/uE6mIA6fh1n7jAimMErL" alt=""><figcaption><p>Autoplay concurrency</p></figcaption></figure>

### 3. Realm Setting&#x20;

To manage audio and playback settings for this specific feature please reach out to your dedicated Account manager.&#x20;

The options available are as follows;&#x20;

Auto play behaviour;&#x20;

* VIDEO\_ONLY - Video will display without audio&#x20;
* AUDIO\_AND\_VIDEO - Video will display with audio

### 4. User Settings

As an End-user, you also have the ability to set your autoplay settings under the "Preferences" section on the "My account" page.&#x20;

NOTE: This will override the settings set at the realm level.&#x20;

<figure><img src="/files/MOVMELFo2YwGqOEJoCGv" alt=""><figcaption></figcaption></figure>

## Reporting&#x20;

User views as part of the animated hero feature will be included as part of the overall view count for this specific asset.&#x20;

&#x20;


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/content/content-management/creating-hero-images/animated-heroes.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
