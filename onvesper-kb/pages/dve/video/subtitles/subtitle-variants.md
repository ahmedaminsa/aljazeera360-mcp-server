> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/dve/video/subtitles/subtitle-variants.md).

# Subtitle Variants

Vesper supports defining multiple subtitle tracks per audio language. This supports a use case where customers may want the spoken words on screen to be transcribed, but not want full subtitles intended for the deaf and hard of hearing.

All of the capabilities defined in this page require [Subtitles](/platform-knowledge-base/dve/video/subtitles.md#embedded-subtitles) to function. Defining types of subtitle including forced narrative is implemented on Vesper in a standards based approach in the manifest. Therefore the logic cannot be applied to side car subtitles. It is also important to define all types of subtitles when the content is first uploaded to Vesper VOD to avoid the need to upload a new [Content Source](/platform-knowledge-base/dve/video/video-content-sources-management.md) in order to make edits.

Vesper's typed subtitle definitions are as follows:

#### Regular type

Also known as **Subtitles**. Translate/transcribe spoken dialog only, no additional text on screen to convey other audio cues.

Intended for viewers who **can hear the audio** but may not understand the language.

#### Closed Captions type

Also known as **Subtitles for Deaf and hard of hearing** \[SDH]. Provide text representation of all important information in the audio track - for example:

‣ sound effects (e.g. *\[door creaks]*)\
‣ speaker identification\
‣ non-speech audio

Intended for viewers who **deaf or hard of hearing** but may not understand the language.

#### Forced-Narrative type

Subtitles will only appear on screen when a language other than the primary audio language is being spoken. The subtitles are forced on to ensure the narrative details are not lost.

One forced narrative subtitle can be defined per language (i.e. 1 is the forced narrative track for English audio, one is the forced narrative track for Spanish audio).

These subtitles are played back on the player side provided that:

* Normal subtitles are set to ‘off’
* Audio language has a forced subtitle text track uploaded through the DVE

## Defining subtitle type

### In Vesper VOD UI

When first uploading videos or content sources to Vesper VOD, you are able to upload subtitles text track and define:

* **Subtitle Name** - Name displayed in the player for the end user\*
* **Subtitle Language** - Defines the language of the subtitles e.g. English if the subtitles are for consumers who read English.
* **Subtitles Type** - Regular, Closed Caption, Forced

{% hint style="info" %}
\*It’s important to note that users will see the subtitle name in the player, therefore it’s important to define the subtitle type in the subtitle name when using multiple types for one video
{% endhint %}

Vesper's recommends labelling of subtitles when using multiple files in one of the following conventions.

{% tabs %}
{% tab title="Convention 1" %}

* **Regular:** English
* **Closed Captions:** English (SDH)
  {% endtab %}

{% tab title="Convention 2" %}

* **Regular:** English
* **Closed Captions:** English (Full)
  {% endtab %}

{% tab title="Convention 3" %}

* **Regular:** English (CC)
* **Closed Captions:** English (SDH)
  {% endtab %}
  {% endtabs %}

<figure><img src="/files/V4nwrhxVr4pKeryFITZq" alt=""><figcaption><p>Subtitle names will be validated for uniqueness</p></figcaption></figure>

<figure><img src="https://media-cdn.atlassian.com/file/72e81060-11c7-402f-93f1-029b4b2906c2/image/cdn?allowAnimated=true&#x26;client=bb71b883-e5f3-4ed7-a708-24c04f742e6a&#x26;collection=contentId-4834328984&#x26;height=125&#x26;max-age=2592000&#x26;mode=full-fit&#x26;source=mediaCard&#x26;token=eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJiYjcxYjg4My1lNWYzLTRlZDctYTcwOC0yNGMwNGY3NDJlNmEiLCJhY2Nlc3MiOnsidXJuOmZpbGVzdG9yZTpjb2xsZWN0aW9uOmNvbnRlbnRJZC00ODM0MzI4OTg0IjpbInJlYWQiXX0sImV4cCI6MTc3MDk4NjMwOSwibmJmIjoxNzcwOTgzNDI5LCJhYUlkIjoiNjEwOTQ1MzhlYjdhZWYwMDY5ZWE2ZGVmIiwiaHR0cHM6Ly9pZC5hdGxhc3NpYW4uY29tL2FwcEFjY3JlZGl0ZWQiOmZhbHNlfQ.I3LF3olJaI2jkzeFlcb5tEUgY0kbyFIxzU8k86vgoZw&#x26;width=576" alt=""><figcaption><p>Ability to create multiple subtitles with different types e.g. regular, CC and SDH</p></figcaption></figure>

### Forced Narrative subtitles in Vesper VOD UI

The option to include a forced narrative subtitle will be provided when you first upload content to Vesper VOD.

<figure><img src="/files/kkqYGWQFpc1wgYPPCieZ" alt=""><figcaption><p>Initial video upload with audio track and forced narrative subtitles</p></figcaption></figure>

Once the initial audio track is uploaded, additional audio tracks can be uploaded along with forced subtitle for each audio track.

<figure><img src="/files/MdrOxrFVzPbRecSgSDCA" alt=""><figcaption></figcaption></figure>

When forced subtitles are defined for available audio tracks, the forced subs are shown automatically during playback on sync with the audio track. Whenever a subtitle language is active, the forced subtitles are not shown.

### Editing typed subtitles in Vesper VOD UI

After an embedded subtitles content version has been made available, you are no longer able to add new embedded subtitles to that version.

Instead, make use of the [Video Content Sources Management](/platform-knowledge-base/dve/video/video-content-sources-management.md#clone-source) option to adjust subtitles, or add new supported audio languages.

## Batch & Onboarder API

All types of subtitle are defined in the same way for both batch and onboarder API, by assigning a "type" property when the asset is first contributed.

To provide subtitle definitions in batch, see: [Prepare your video assets](/platform-knowledge-base/dve/batch-video-upload-via-ui/uploading-batch-vods/prepare-your-video-assets.md), under the subtitle definition.

To provide subtitle definitions using the Onboarder API, refer to the subtitles.typeId field in the Upsert and Patch endpoints at [Content Onboard APIs](https://docs.onvesper.com/build/vod-apis/apis/content-onboard-apis). The mapping is provided below for reference:

<table><thead><tr><th width="226.65625">ID</th><th>Mapping</th></tr></thead><tbody><tr><td>1</td><td><a href="#regular-type">Regular</a></td></tr><tr><td>2</td><td><a href="#closed-captions-type">Closed-Captions</a></td></tr><tr><td>4</td><td><a href="#forced-narrative-type">Forced</a></td></tr></tbody></table>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/dve/video/subtitles/subtitle-variants.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
