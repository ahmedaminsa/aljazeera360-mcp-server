> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/consumer-experience/watchlists.md).

# Watchlists

### Introduction

When scrolling through content, end users can tick any video-on-demand they're interested in watching later or saving for a specific occasion and include it in various watchlists serving as their personally curated content catalogue.

Watchlists differ from ‘Favorites’ because a user can create multiple user-curated collections rather than a single collection of stand-alone assets. Users can create various watchlists full of content to suit a specific occasion or mood.

Users will be able to create a new watchlist from the following areas:

* From a new menu item reserved for Watchlists
* When hovering over an asset, via clicking on an 'add to watchlist' icon on the bottom right of the thumbnail
* From an interstitial page containing a CTA to add content to a watchlist
* From the video player, via clicking on an 'add to watchlist' icon on the player control bar

Users can rename, remove and share their watchlists from the Watchlist menu item; they can also reorder the assets within each watchlist by clicking and dragging them to a new position.

{% hint style="info" %}
Watchlists **replace** Favorites owing to their increased capabilities; after enabling Watchlists, content previously marked as Favorite will be lost.
{% endhint %}

\ <br>

<figure><img src="/files/ih3EMsYVv33BfYOPHYir" alt=""><figcaption><p>Watchlists menu (Web view)</p></figcaption></figure>

### Device Availability

Watchlists are available in the following stock devices:

* Web
* Mobile
* UTV Smart & Connected TV\*

{% hint style="info" %}
\*Watchlists can be updated but not created on this device.
{% endhint %}

### Content Availability

Watchlists can contain the following content types:

* Individual VOD assets
* Playlists
* Seasons
* Series

{% hint style="info" %}
You can mix and match different types in a single watchlist.
{% endhint %}

If you wish to have this feature enabled, please contact your Account Management team.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/consumer-experience/watchlists.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
