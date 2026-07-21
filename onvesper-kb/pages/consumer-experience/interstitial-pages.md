> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/consumer-experience/interstitial-pages.md).

# Interstitial Pages

Interstitial pages are a platform feature that offers end users a sneak peek at content prior to viewing. These pages act as the entry point to the video player, highlighting essential details about programs such as descriptions, genres, trailers, ratings, and additional information. This allows consumers to ensure that the content aligns with their preferences. These pages are an effective instrument for encouraging viewers to explore videos and igniting interest in upcoming releases or popular content.

This powerful capability enables residents to showcase not just video details such as languages, subtitles, or content ratings, but also highlights like the director or actors in a film, or the teams and players in a sports game. The details shown on interstitial pages are composed using the video description and its metadata set up on VOD Vesper. Consult [Typed Tags](/platform-knowledge-base/dve/video/typed-tags.md) for instructions on how to add this data (and localise it if applicable). Once your VOD library is populated with this metadata, you can define an interstitial template to choose the information you want to display.

<figure><img src="/files/TN7J77MUKcKLblHRfycE" alt=""><figcaption></figcaption></figure>

Interstitial pages display dynamic calls-to-action tailored to the specific scenario. They serve as a potent marketing, enticing guest users to sign up to watch specific content. For registered users, these pages let users start watching the asset but also facilitate adding it to their [Watchlists](/platform-knowledge-base/consumer-experience/watchlists.md) or Favourites. Furthermore, if a particular subscription or license is necessary to access the content, users are directed to the purchase page. These capabilities make interstitial pages a strong feature for enhancing platform engagement and usage.

To activate this feature, reach out to your Account Manager to set your template.

## Customising interstitial pages

As templated pages, Vesper supports customisation of the user interface shown to end users for each realm.

Below is a list of known and supported customisations. All customisation requests should be raised with your account management team as they are not currently self-serviceable. Other customisations may be possible, or could be made possible with a change to the platform — contact your account management team to enquire further.

### Artwork & Visual

* [Series Interstitial: Title Logo & Full Screen background image](/platform-knowledge-base/consumer-experience/interstitial-pages/series-interstitial-title-logo-and-full-screen-background-image.md)

### Layouts

* [Series Interstitial: Vertical list view of episodes](/platform-knowledge-base/consumer-experience/interstitial-pages/series-interstitial-vertical-list-view-of-episodes.md)
* [Series Interstitial: Tabbed navigation](/platform-knowledge-base/consumer-experience/interstitial-pages/series-interstitial-tabbed-navigation.md)
* [Series Interstitial: Season selector](/platform-knowledge-base/consumer-experience/interstitial-pages/series-interstitial-season-selector.md)

### Content

* Enabling and displaying [Participants](/platform-knowledge-base/dve/video/participants.md)
  * With or without profile pictures (if such data is unlikely to be available)
* Showing [Related Content](/platform-knowledge-base/consumer-experience/related-content.md)
* Providing content ratings and localised typed tag values
* Showing subtitle and audio languages available

### Styling

* Text Size & Colour: Most text properties and colours can be adjusted on Web & TV, for example if you wish to make the header text smaller, or use a different colour for your typed tag data
* Tag Styling: Your typed tag data can be styled to look more like a "tag" with a coloured background
* Spacing: The spacing between many elements can be increased or decreased on Web & TV


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/consumer-experience/interstitial-pages.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
