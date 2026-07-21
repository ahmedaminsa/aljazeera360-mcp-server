> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/consumer-experience/interstitial-pages/series-interstitial-title-logo-and-full-screen-background-image.md).

# Series Interstitial: Title Logo & Full Screen background image

The **Title Logo on the Interstitial** feature allows Vesper customers to replace the default text title shown on interstitials with a custom logo asset. This provides a branded, visually rich experience for VOD, serie and seasons. It is supported on Vesper web and TV interfaces.

Before reading this page, it's a good idea to ensure you are fully familiar with the creative options in [Image and VOD Specifications](/platform-knowledge-base/dve/image-and-vod-specifications.md#images-creatives).

{% hint style="info" %}
The information below may need to be translated if you are using [New: Artwork 2.0](/platform-knowledge-base/dve/video/new-artwork-2.0.md). Speak to your account management team for more assistance.
{% endhint %}

By default, interstitial pages on Vesper use the **Title Image (series)** or **Thumbnail** **(VOD)** which is expected to carry any visual branding about the current title.

You may instead chose to set up your interstitial to (1) use the **Cover** **Image** as a background for your interstitial and (2) use the **Title Logo** on the interstitial.

These two capabilities are **mutually exclusive** and independent of each other. However they work best when combined.

<figure><img src="/files/ZFoJHFzVVf33CEHsVtUg" alt=""><figcaption><p>Example of the interstitial page when both Title Logo (the Breaking Bad logo) and Cover image background are enabled</p></figcaption></figure>

To configure these capabilities, contact your Account Manager. You should also ensure you are setting up your VOD catalogue with the required creative assets as laid out in [Image and VOD Specifications](/platform-knowledge-base/dve/image-and-vod-specifications.md#images-creatives).

### Cover Image as a background

When enabled, the **cover image** is displayed as a background to the interstitial page. This works best with photography or images that do not contain branding. A portion of the image will be unobscured to spotlight the cover image as seen in the screenshot above.

### Title Logo

When enabled, if a **Title logo** exists for a given series or VOD, it will be used instead of the text. This works best with stylised, branded show/movie names. It will be rendered over the top of the cover image and any gradients if enabled, as shown in the top left of the image above.

### FAQs

#### What options to I have if my content is already in Vesper VOD and not all of my assets have these creatives?&#x20;

If Cover image is not available, the platform will fall back to using Thumbnail in the background. However we would recommend that you prioritise setting up a cover image for all of your content.

If Title logo is not available, the platform will fall back to using the normal text representation.

**Recommendation:** Should you wish, you can request that your account manager sets up logic on your interstitial page so that the cover image *will only be shown* if there is a **Title Logo** available. If configured in this way, then any time a **Title Logo** is not available, the page will fall back to the default display using **Title Image**. Using this configuration will allow you to update your existing assets in your own time

#### How will this look on mobile apps?

As of publication, there is no suitable way to provide a full-bleed **Cover image** which will work well on a portrait / mobile view. This is a known limitation which will be addressed in future.

**Title Logo** will be supported on mobile, it will simply take the place of the text in the existing mobile app's [interstitial page](/platform-knowledge-base/consumer-experience/interstitial-pages.md) design.

**Recommendation:** It is possible for the interstitial page to employ responsive design/breakpoint logic such that the cover image will never be used for the mobile apps (or mobile web). You can also request that the Title Logo is never used on the mobile breakpoint if you prefer the current look for the interstitial screen on mobile screens. Ask your Account Manager about the options here.

#### Can this apply to VOD interstitial as well?

Yes, however there are some limitations to consider. A title logo will work well for movies or standalone content (such as documentaties), however it is less appropriate if a user lands on a VOD interstitial for an episode of a series. There are options available here but they may require a more in-depth data strategy, discuss with your Account Manager for more details.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/consumer-experience/interstitial-pages/series-interstitial-title-logo-and-full-screen-background-image.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
