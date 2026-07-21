> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/consumer-experience/theming-and-customisation.md).

# Theming & Customisation

Welcome to the theming homepage of the Vesper knowledgebase.

This section will highlight any customisation and theming features of the platform (either newly launched or always present) to help our customers better represent their brand identities through the Vesper consumer applications.&#x20;

The sub-pages of this section will explore in-depth customisation options, or try the links below which will highlight pages elsewhere in this knowledgbase that allow you to theme the experience.

#### Installed app iconography, Fonts & Basic Colours

* Refer to [Onboarding Documentation](https://docs.onvesper.com/platform-knowledge-base/client-onboarding-documentation/)/ "Consumer Experience" for initial onboarding decisions on branding your apps&#x20;

#### Content management

* Use the [Menu items](/platform-knowledge-base/back-office/administration/menu-items.md) to set custom iconography for your app menus
* [Sponsorship Logo Placements](/platform-knowledge-base/back-office/content/content-management/sponsorship-logo-placements.md)and [Sponsorship Watermarking](/platform-knowledge-base/dve/video/sponsorship-watermarking.md) can help activate a sponsorship deal
* Use [Animated Heroes](/platform-knowledge-base/back-office/content/content-management/creating-hero-images/animated-heroes.md), logo branded [Creating Hero Slides](/platform-knowledge-base/back-office/content/content-management/creating-hero-images.md) as well as themed thumbnails for VOD content
* For more personalisation, try a subtle patterned [Custom Background Sections​](/platform-knowledge-base/back-office/content/content-management/sections/custom-background-sections.md)on your home page or sub section pages

#### Templated pages

There are customisation options available on newer Vesper pages which are templated. These are:

* [Interstitial Pages](/platform-knowledge-base/consumer-experience/interstitial-pages.md#customising-interstitial-pages)
* [Search](/platform-knowledge-base/consumer-experience/search.md)

For more options click through the "next" button below.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/consumer-experience/theming-and-customisation.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
