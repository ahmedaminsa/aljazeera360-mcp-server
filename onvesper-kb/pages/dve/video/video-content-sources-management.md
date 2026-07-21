> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/dve/video/video-content-sources-management.md).

# Video Content Sources Management

*Video Content Sources* have been enabled to help content owners to manage multiple video versions of a VOD asset.&#x20;

It is important to highlight the distinction between VOD and content: the VOD's playback is determined by its content source. A single VOD can have multiple contents (each version identified by a unique content ID), but only one content is *active* for playback at any given time.

The *active* content ID for a given VOD can be seen on the video top bar. Beside this information, two buttons enables users to manage the video content sources:

<figure><img src="/files/IgeZOIyGSsohskNBryc6" alt=""><figcaption><p>Video Top Bar identifying the current active content ID of the VOD. New source button highlighted.</p></figcaption></figure>

## New Source

The *New Source* button allows users to create a new content source. The following window will pop out to choose the new video, audio or subtitles:

<figure><img src="/files/w3GhZNYKrVnXeb81I11G" alt="" width="563"><figcaption></figcaption></figure>

## Manage Sources

The *Manage Sources* button displays the different content sources added to the VOD, letting users to self serve the management of the *active* content at any moment:

<figure><img src="/files/K7sGGvLuzsaRpq2Gh3lK" alt=""><figcaption><p>Manage Content Sources</p></figcaption></figure>

The platform allows a second option to swap the VOD's active content by clicking on the active ID (top bar menu) which triggers a dropdown menu showing the different content sources available in the VOD. With a simple click on the desired source ID, the platform will make it the active source.

<figure><img src="/files/TH7QHE83aW4XKc7uPvWq" alt=""><figcaption></figcaption></figure>

## Clone Source

<figure><img src="/files/wYVhE8ByEOVoAqyKDUJs" alt=""><figcaption></figcaption></figure>

If you need to make edits to metadata which is embedded in the content source, such as [Subtitle Variants](/platform-knowledge-base/dve/video/subtitles/subtitle-variants.md), the best approach is to clone a given content source.

After you click the clone button, you will be presented with an interface where you are able to add new audio tracks, and new typed subtitles.

<figure><img src="/files/kJfAUJ5ZERd07ZyG7m4C" alt=""><figcaption><p>Clone source modal</p></figcaption></figure>

After you have defined the subtitles to be used with the newly cloned content version, the pipeline will carry out the necessary processing. The video itself will not be re-muxed or encoded, as these changes only need affect the manifest. The cloning process, with new audio or subtitle tracks, will take less time than uploading a new content source.

{% hint style="info" %}
This option will only be functional if the source you are cloning was already encoded using a VOD preset that supports embedded closed captions.

If you need to switch from side-car to embedded subtitles - please contact your platform account manager to discuss the process.
{% endhint %}

## Example Use cases

* The initial published version of the VOD could be a trailer that is automatically scheduled to be replaced with the final version of the asset.
* The initial published version of the VOD might be the raw recording of a game, which can be replaced with the final edited version.
* You may initially make content available in a single language with embedded subtitles, then offer new audio languages and their associated subtitles at a later date.

Visit [Scheduling Releases](/platform-knowledge-base/dve/video/scheduling-releases.md) for more information on this topic.

\ <br>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/dve/video/video-content-sources-management.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
