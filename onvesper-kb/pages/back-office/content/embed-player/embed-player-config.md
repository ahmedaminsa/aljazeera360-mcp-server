> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/content/embed-player/embed-player-config.md).

# Embed Player Config

{% hint style="warning" %}

* Embed player requires the content to either be available for guest users or have an embed player specific "free" license configured for granting access see [Licences Types & Guides](/platform-knowledge-base/back-office/licences/licence.md#licence-types)
* Embed player does not support geo-restricted content&#x20;
  {% endhint %}

Once commercial approval has been received from the CAM team and the Embed Player has been enabled by your TAM, you should be able to access the Embed Config menu.&#x20;

Head to your Vesper Admin account and select **Embed Player Configurations** from the **Content** nav bar.

<figure><img src="/files/NXKJ0qjJQRERQryyb0w1" alt=""><figcaption></figcaption></figure>

Once you click on **Create Embed Config** on the top right of the page, you will be presented with the below config page:

<figure><img src="/files/ocuncCO7Nkt5PdUeHh9x" alt=""><figcaption></figcaption></figure>

A logo can be uploaded per config created and will appear on the player as shown below

<figure><img src="/files/yv1i8q34Y1P9DfrIY5q5" alt=""><figcaption></figcaption></figure>

Settings that modify the behaviour of the playback experience:

* `Logo Display Type` - The duration at which we display the Logo
  * **Persistent**: Display the logo throughout the duration of the video
  * **Ephemeral**: Display the logo whenever the playback controls are displayed
* `Logo Position` - The position to display the logo
  * **Top Right**
  * **Top Left**
* `Autoplay` - Settings that modify the behaviour of the playback experience
  * **Yes**: Autoplay without changing the volume
  * **No**: Disables Autoplay and content is loaded when pressing ‘play’
  * **Muted**: Autoplay muted
  * **Any**: try auto play with volume, on failure (e.g. when blocked by browser settings) mute and try again
* `Sticky Player Location` - The location of the Embed Player iFrame attached to the webpage
  * **Top Right**
  * **Top Left**
  * **Bottom Right**
  * **Bottom Left**
  * **Disabled**
* `Poster Frame`
  * Show content poster (live) or thumbnail (vod) before playback begins
* `Playback Speed`
  * Enable option under settings cogwheel play control for amending the playback speed
* `Picture-in-Picture`
  * Enable option to pop out player into mini player while the embedded page is active
* `ChromeCast`
  * Enable option to cast content
* `FF & Rewind`
  * Enable FF & Rewind Player controls
* `Quality Selection`
  * Enable option to select quality of playback
* `Time Display`
  * Enable numerical display of playback time next to progress bar
* `Unmute CTA`
  * Changes the appearance of the "Pause" button to an "Unmute CTA" for Autplayed content:

<figure><img src="/files/xlR52RF5iFxnRZCUGejM" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Sticky players allow you to scroll up and down the page away from the area containing the embedded player.
{% endhint %}

<br>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/content/embed-player/embed-player-config.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
