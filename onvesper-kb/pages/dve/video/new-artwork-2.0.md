> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/dve/video/new-artwork-2.0.md).

# New: Artwork 2.0

{% hint style="info" %}
Artwork 2.0 is in early rollout stages. Whilst this system will one day replace the current Vesper images and thumbnails (and documentation on those items) - this page is intended to introduce and help you adopt it.
{% endhint %}

Artwork 2.0 brings extended artwork configuration to Vesper VOD — adding support for multiple art types, up to 5 variants per type, and localisation, so different images can be served in different regions. It replaces the previous single-image-per-type setup and gives you significantly more editorial control over how content is presented across the platform.

## Do I need to move to Artwork 2.0?

Artwork 2.0 is opt-in. Your existing setup remains on the previous version (V1) until you choose to migrate — there is no fixed deadline, and the change is reversible if you need to revert.

That said, Artwork 2.0 is the direction of the Vesper platform. New art types, variants, and localisation support are only available in V2. If you want richer artwork configuration — or if your templates are built to use the newer art types — you will need to be on V2 to take advantage of them.

To enable Artwork 2.0, contact your Account Management team.

## What happens to existing artwork?

Existing artwork is not lost when switching to V2. All images uploaded under V1 are automatically migrated and mapped to their V2 equivalents. Nothing needs to be re-uploaded to maintain what was already there.

The section below explains exactly where each V1 art type maps to in V2.

## V1 to V2 artwork mapping

When you move from V1 to V2, your existing images are carried across as follows. See also [Image and VOD Specifications](/platform-knowledge-base/dve/image-and-vod-specifications.md#images-creatives) for examples and guidelines.

### Videos

| V1 Art Type                          | V2 Art Type            | Variant | Notes                                                  |
| ------------------------------------ | ---------------------- | ------- | ------------------------------------------------------ |
| Thumbnail (16:9)                     | Thumbnail (Landscape)  | v1      | Direct equivalent                                      |
| Poster (2:2.8)                       | Poster (Legacy)        | v1      | Direct equivalent                                      |
| Cover (16:9)                         | Thumbnail (Landscape)  | v2      | Card hover / secondary state use case — see note below |
| Cover (16:9)                         | Interstitial Landscape | v1      | Background / interstitial use case — see note below    |
| Title Image (16:9)                   | Thumbnail (Landscape)  | v3      |                                                        |
| Title Logo / Title Text Image (16:9) | Title Logo Landscape   | v1      |                                                        |

### Playlists and Collections

| V1 Art Type                   | V2 Art Type                     | Variant | Notes                                                  |
| ----------------------------- | ------------------------------- | ------- | ------------------------------------------------------ |
| Small Cover / Thumbnail (1:1) | Thumbnail (Square) (Legacy)     | v1      | Direct equivalent                                      |
| Cover (16:9)                  | Thumbnail (Landscape)           | v2      | Card hover / secondary state use case — see note below |
| Cover (16:9)                  | Interstitial Landscape          | v1      | Background / interstitial use case — see note below    |
| Poster (2:3)                  | Poster (Legacy)                 | v1      | Direct equivalent                                      |
| Title Image (16:9)            | Thumbnail (Landscape)           | v3      |                                                        |
| Title Logo (16:9)             | Title Logo Landscape            | v1      |                                                        |
| Content Owner Logo (1:1)      | Publisher / Content Origin Logo | v1      |                                                        |
| Logo Image (4:3)              | Box Art (Series)                | v1      |                                                        |

{% hint style="info" %}
**A note on Cover**

In V1, a single Cover image served two overlapping purposes: it was used as a card hover state and as an interstitial background. In V2, these are separated into distinct art types — Thumbnail (Landscape) v2 and Interstitial Landscape — giving you independent control over each use case.

The existing Cover image is mapped to both automatically on migration, but you can update them independently to serve different creative for each context.
{% endhint %}

## What to check after enabling V2

For most Vesper customers, existing artwork carries across automatically and content continues to display as before. A few things worth reviewing after the switch:

**Cover images** — if you previously used Cover for two different creative purposes (hover state vs interstitial background), you can now upload separate images for Thumbnail (Landscape) v2 and Interstitial Landscape respectively. Until you do, both will show the same migrated image.

**Title Image** — If your Vesper configuration is heavily utilising this image type, you need to be fully aware that in V2 it maps to **Thumbnail (Landscape) v3**. If you were not using it before, no action is needed.

**New art types** — any V2 art types not present in V1 (e.g. Thumbnail Portrait, Box Art Movies, Sponsor Landscape) will be empty until you upload images for them. These are not required — they only need to be populated if your templates are configured to use them.

## Enabling Artwork 2.0

Artwork 2.0 requires a one-time configuration update. Contact your account team to enable it for your organisation.

When enabled, a default set of 5 art types is pre-selected:

* **Thumbnail (Landscape)** — 16:9
* **Interstitial Landscape** — 16:9
* **Box Art (Series)** — 4:3
* **Poster (Legacy)** — 2:2.8
* **Thumbnail (Square) (Legacy)** — 1:1.1

The two legacy types exist to support customers whose creative assets were produced in older, non-standard dimensions. They remain fully supported.

Additional art types can be enabled or defaults removed to match your specific use case. If a required art type is not available, contact your account team to request it.

### API documentation

If you are onboarding content programmatically, the following API references cover artwork fields under V2:

{% tabs %}
{% tab title="Video" %}

* [V2](https://docs.onvesper.com/build/vod-apis/apis/content-onboard-apis/upsert-video-api/v2#art)
* [Patch Video API](https://docs.onvesper.com/build/vod-apis/apis/content-onboard-apis/patch-video-api#art)
  {% endtab %}

{% tab title="Playlist/Season and Collection/Series" %}
{% hint style="info" %}
Not yet available, please check back soon
{% endhint %}

{% endtab %}
{% endtabs %}

## Supported art types

Art types are defined by their aspect ratio, not a fixed location in the app. Each type has a suggested use case (e.g. card row, interstitial page, logo slot), but you are free to use any art type wherever the aspect ratio fits your template.

You will only see the art types enabled for your configuration — familiarity with the full list below is not required. It is provided as a complete platform reference.

| Art Type                      | Aspect Ratio | Recommended Size | Default Enabled            | Description                                                                              |
| ----------------------------- | ------------ | ---------------- | -------------------------- | ---------------------------------------------------------------------------------------- |
| Thumbnail (Landscape)         | 16:9         | 1920×1080        | :white\_check\_mark:       | Landscape image for content row cards                                                    |
| Interstitial Landscape        | 16:9         | 1920×1080        | :white\_check\_mark:       | Landscape image for interstitial pages                                                   |
| Box Art (Series)              | 4:3          | 1024×768         | :white\_check\_mark:       | Landscape image for content row cards                                                    |
| Poster (Legacy)               | 2:2.8        | 1142×1600        | :white\_check\_mark:       | Portrait image for content row cards — legacy dimension, supported for existing creative |
| Thumbnail (Square) (Legacy)   | 1:1.1        | 640×704          | :white\_check\_mark:       | Square image for content row cards — legacy dimension, supported for existing creative   |
| Thumbnail (Portrait)          | 2:3          | 1280×1920        | :heavy\_multiplication\_x: | Portrait image for content row cards                                                     |
| Thumbnail (Square)            | 1:1          | 1080×1080        | :heavy\_multiplication\_x: | Square image for content row cards                                                       |
| Interstitial Portrait         | 2:3          | 1280×1920        | :heavy\_multiplication\_x: | Portrait image for interstitial pages                                                    |
| Box Art (Movies)              | 3:4          | 768×1024         | :heavy\_multiplication\_x: | Portrait image for content row cards                                                     |
| Sponsor Landscape             | 16:9         | 1280×720         | :heavy\_multiplication\_x: | Landscape image of the sponsor for the asset                                             |
| Title Logo Landscape          | 16:9         | 1920×1080        | :heavy\_multiplication\_x: | Landscape title logo image for interstitial pages                                        |
| Title Logo Portrait           | 2:3          | 1000×1500        | :heavy\_multiplication\_x: | Portrait title logo image for interstitial pages                                         |
| Publisher/Content Origin Logo | 1:1          | 250×250          | :heavy\_multiplication\_x: | Square image of the publisher or content origin logo                                     |

## How to manage artwork

{% stepper %}
{% step %}

### Navigate to the artwork section

On any entity page (e.g. a video detail page), the artwork section lists all art types that have at least one image associated. Select an art type from the list to view and manage its details.
{% endstep %}

{% step %}

### Upload artwork

Click **Upload Artwork** to open the upload flow. This is the same entry point for both single and bulk image uploads.

Once an image is uploaded, the following fields are required:

* **Artwork Type** — the art type as enabled in your configuration
* **Variant** — which of the 5 variants this image represents (defaults to Variant 1 for single uploads)
* **Language** — the locale this image targets (defaults to Global, meaning it displays across all regions; a specific locale can be selected where region-targeted artwork is required)

{% hint style="info" %}
**Tip:** Name your file using the convention `artwork-type|variant-number|locale` (e.g. `thumbnail-landscape|variant-1|en-GB`) and these fields will be auto-filled on upload.
{% endhint %}
{% endstep %}

{% step %}

### Validation

Once the required fields are provided, the system validates that:

* The image dimensions match the specifications of the selected art type

If the image doesn't match the expected aspect ratio, a warning is shown. The upload won't be blocked, but the image may be automatically resized or cropped to fit.
{% endstep %}

{% step %}

### Managing variants, localisation, and existing artwork

From the artwork detail view, you can:

* Toggle between variants to see what's configured for each
* Add region-specific images by selecting a locale and uploading an image for that language
* Delete, replace, or add additional images per variant and locale
* See all configured art types listed in the artwork panel, with a preview image, ratio, variant count, and image count shown for each
* Delete individual images or entire art types (confirmation required before deletion)
* Upload new images at any time to update what's already configured
  {% endstep %}
  {% endstepper %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/dve/video/new-artwork-2.0.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
