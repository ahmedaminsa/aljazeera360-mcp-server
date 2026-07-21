> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/content/content-management/creating-hero-images/card-style-hero.md).

# Card-Style Hero

<figure><img src="/files/DXoxug1AEU9rIxeIE9jC" alt=""><figcaption><p>Card-Style Hero with Badges</p></figcaption></figure>

## Feature Overview

The **Card Style Hero (or Skinny Hero)** feature introduces a new visual layout option for heroes, designed to provide a more compact presentation for featured content. This layout is ideal for promotional content, channel highlights, or visually rich hero areas that blend imagery, text, and branding in a single, cohesive component.

### How to Configure

If you wish to have this feature enabled, please contact your Account Management team. Once enabled, the Card-Style Hero option will be available when creating/editing a hero in the back office.

&#x20;The Card-Style Hero item can be added to your homepage layouts via the following steps:

In back office, navigate via **Content > Create New > Hero**. Select **Card-Style Hero** as the Hero type.

<figure><img src="/files/5lyxCzHjHyg9cy7ziNeU" alt=""><figcaption></figcaption></figure>

### Card-Style Hero Options

<table data-full-width="false"><thead><tr><th>Field</th><th>Description</th><th>Notes/Behaviour</th></tr></thead><tbody><tr><td><strong>Background Image</strong></td><td>The main image used in the hero.</td><td>Applies to all devices. <strong>Portrait sized images are not supported on mobile.</strong></td></tr><tr><td><strong>Background Colour</strong></td><td>The background colour that blends into the hero area</td><td>Used to create a smooth visual gradient or fallback.</td></tr><tr><td><strong>Title</strong></td><td>Configurable text field for the main title.</td><td><strong>Bold</strong> and <strong>Italic</strong> styling only.</td></tr><tr><td><strong>Description</strong></td><td>Optional text field appearing below the title</td><td><strong>Bold</strong> and <strong>Italic</strong> styling only. <strong>Not displayed on mobile devices.</strong></td></tr><tr><td><strong>Tagline</strong></td><td>Optional text field used as a promotional line</td><td>Always appears in <strong>bold.</strong></td></tr><tr><td><strong>Channel Logo</strong></td><td>Upload the channel or brand logo associated with the hero</td><td>Positioned within the hero layout.</td></tr><tr><td><strong>Title Image</strong></td><td>Upload a graphic version of the title (e.g., movie or series logo)</td><td>Overrides the text title </td></tr><tr><td><strong>Primary CTA</strong></td><td>Defines the action taken when the user selects the hero</td><td><strong>CTA buttons are not shown on this hero style</strong> - the action is triggered on click/tap.</td></tr><tr><td><strong>Badges</strong></td><td>Configure up to 3 badges for promotional or content purposes</td><td>Useful for highlighting new, exclusive, or trending content.</td></tr></tbody></table>

Note: **Animated Heroes** are **not supported** with the Card Style Hero layout.

### Device Availability

The Card-Style Hero will be available on the following devices:

* Web
* Mobile - v8.0
* UTV Smart & Connected TVs - v3.11


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/content/content-management/creating-hero-images/card-style-hero.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
