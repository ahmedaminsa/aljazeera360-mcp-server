> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/content/content-management/creating-rows/premiere-vod.md).

# Premiere VOD

{% hint style="warning" %}
Premiere VODs are not compatible with Roku devices older than Roku OS 15.0 (released October 2025). Due to this limitation, premiere VODs are not recommended for use if your customer base is heavily reliant on Roku devices.
{% endhint %}

Premiere VOD is a premium feature that allows end users to experience a video as a live-streamed event, where viewers watch together in real time - similar to YouTube's Premiere functionality.

Vesper provides tools in the Back Office and VOD platforms to help residents set up Premiere VOD experiences in their apps.

{% hint style="info" %}
Please contact your Platform Account Manager to enable this premium feature
{% endhint %}

## Step-by-Step Setup <a href="#step-by-step-setup" id="step-by-step-setup"></a>

### Prepare your VOD Asset in Vesper VOD

* Go to the Vesper VOD platform and locate the VOD file you want to premiere
* Set the **active content source** to a ***NO Playback*** source to keep the video inactive until scheduled
* Create a **new content source** by uploading the video intended for the premiere
* Schedule the Premiere:

  <div data-full-width="true"><figure><img src="/files/MGZ3PUTph58zpoovyLqB" alt="" width="293"><figcaption></figcaption></figure></div>

  * Navigate to the **Scheduled Releases** section
  * Select ***Premiere*** as the release type
  * Set the future date and time for the premiere event
  * Choose the appropriate content source for the premiere event
  * Optionally, specify a release location to schedule different times by region
  * Save the release schedule
* Add the **tag** that will be used to surface this VOD in the dedicated Premiere VOD row
* Save the changes

### Create a Premiere VOD Row in Vesper Back Office

* Go to the ***Content Management*** section in the Vesper Back Office
* Click **Create New - Row**
* Select the ***Countdown Trailer Row*** template

<figure><img src="/files/QZvj5S0djDL53OWLMTg8" alt="" width="286"><figcaption></figcaption></figure>

* Enter the **tag** used to identify the Premiere VOD
* Save and confirm the configuration

## User Experience

Once set up, users will see a new dedicated row on web, mobile and TV apps featuring upcoming Premiere VODs. This row includes:

* Large-format cards
* Thumbnail image
* Video metadata
* Countdown timer

<figure><img src="/files/hxbrIbjvM5Xeph25jGOX" alt=""><figcaption></figcaption></figure>

Metadata is fully localized, so end users will see the description in their selected language (if provided in the VOD metadata).

### Premiere Playback

* Clicking or tapping the Premiere card will take users to an **interstitial page** with a countdown
* When the premiere begins, users are automatically directed to the live-viewing experience
* During playback, viewers can **rewind** but **cannot fast-forward** beyond the current live point

<figure><img src="/files/xtUFPhcPn0M6KitHhaEO" alt=""><figcaption></figcaption></figure>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/content/content-management/creating-rows/premiere-vod.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
