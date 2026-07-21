> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/consumer-experience/theming-and-customisation/animated-splash-screens.md).

# Animated Splash screens

Vesper supports an animated splash screen experience across several of the consumer experience applications. The animated splash screen will render immediately after the initial static logo is first shown by the operating system, whilst the app loads in the background.

When the animated splash screen feature is used, the entire animation will play out to the end user - so if the animation is 10 seconds long, the end user will see all 10 seconds of the animation. If the app loads within this time, once the animation is complete the user will be taken to the first page of the application. If the application is still loading after the animation completes, the splash screen will stay static on the last frame of the animation until the application has fully loaded.

We **recommend** that animations be no more than 4 seconds long so as not to delay the user's entry to the app experience.

Once you've read this guide and produced an animation, contact your Platform Account Manager. They will be able to start the process and include the animation in a future build of your Vesper apps.

## Formats

#### Lottie (Mobile & Connected TV)

To use animated splash screens on Mobile and Connected TV devices Vesper, we require a [Lottie](https://lottiefiles.com/) format of animation built with Vectors only. This format of animation is lightweight, does not require loading a video playback engine, and will not negatively impact the loading of the applications.&#x20;

Note the "vector only" restriction is important, using images inside a Lottie animation of any kind dramatically enlarges the size and render complexity of the animation such that it will not perform well on Android, Android TV and Fire TV devices.

#### Video (Web TV)

For Web TV, we utilise a video for splash screen animations. These platforms allow the use of a HTML `<video>` tag which is also lightweight and can be rendered without impacting performance. Lottie animations do not perform well on these platforms' hardware + rendering engines, so a WebM video file is required. Alternatively you can provide an MP4 for Endeavor Streaming to convert into WebM.

## Recommendations

Full list of recommendations:

* Between 2 and 4 seconds long
* High frame rate (60 fps)
* Lowest possible file size (to ensure no impact on app load)

## Specifications

See below for the supported devices and formats.

**General Lottie specifications:** max file size 500KB, use of vectors only (no image data)

**General MP4 specifications:** max file size 1.2MB

**General WebM specifications:** max file size 200KB

<table><thead><tr><th width="191.34375">Device</th><th width="107.55859375">Format</th><th width="220.3671875">Device specific Restrictions</th><th>Recommended Ratio*</th></tr></thead><tbody><tr><td>iOS (mobile)</td><td>Lottie</td><td>Shared across mobile</td><td>9:19</td></tr><tr><td>Android (mobile)</td><td>Lottie</td><td>Shared across mobile</td><td>9:19</td></tr><tr><td>iPadOS (tablet)</td><td>Lottie</td><td><strong>Optional Shared across tablet:</strong> provide an animation designed for portrait + horizontal rendering if not using a "square" ratio as below<br><strong>Otherwise</strong> shared across tablet + mobile</td><td>3:4 (portrait)<br>4:3 (landscape)</td></tr><tr><td>Android (tablet)</td><td>Lottie</td><td>" As above</td><td>3:4 (portrait)<br>4:3 (landscape)</td></tr><tr><td>TvOS</td><td>Lottie</td><td>Shared across Connected TVs</td><td>16:9</td></tr><tr><td>Android TV</td><td>Lottie</td><td>Shared across Connected TVs</td><td>16:9</td></tr><tr><td>Fire TV</td><td>Lottie</td><td>Shared across Connected TVs</td><td>16:9</td></tr><tr><td>Samsung Tizen</td><td>WebM</td><td>Shared across Web TVs</td><td>16:9</td></tr><tr><td>HiSense Vidaa</td><td>WebM</td><td>Shared across Web TVs</td><td>16:9</td></tr><tr><td>Vizio</td><td>WebM</td><td>Shared across Web TVs</td><td>16:9</td></tr><tr><td>LG WebOS</td><td><span data-gb-custom-inline data-tag="emoji" data-code="274c">❌</span></td><td>No support</td><td></td></tr><tr><td>PlayStation</td><td><span data-gb-custom-inline data-tag="emoji" data-code="274c">❌</span></td><td>No support</td><td></td></tr><tr><td>Xbox</td><td><span data-gb-custom-inline data-tag="emoji" data-code="274c">❌</span></td><td>No support</td><td></td></tr><tr><td>Roku</td><td><span data-gb-custom-inline data-tag="emoji" data-code="274c">❌</span></td><td>No support</td><td></td></tr></tbody></table>

\*Ratio is only applicable if you are providing a "full screen" animation. If you are animating say, a simple logo in the centre of the screen, provide a square aspect ratio to support all screen sizes.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/consumer-experience/theming-and-customisation/animated-splash-screens.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
