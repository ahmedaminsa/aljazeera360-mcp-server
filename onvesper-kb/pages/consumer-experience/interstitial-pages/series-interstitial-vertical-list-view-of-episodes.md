> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/consumer-experience/interstitial-pages/series-interstitial-vertical-list-view-of-episodes.md).

# Series Interstitial: Vertical list view of episodes

The vertical list view is an alternative episode layout for season and series interstitial pages. Instead of the default horizontal bucket layout, episodes are presented in a single vertical scroll — making it simpler to browse through all available content, particularly with a touch interface or mouse scrollwheel.

This layout also surfaces richer episode metadata directly in the list, giving users more context before they tap or click to watch.

It is available on Web, TV, and Mobile.

<figure><img src="/files/gJRwsZsHin9rxYt5llRv" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
To enable the vertical list view on your interstitial pages, contact your account team.
{% endhint %}

## What's shown in the list

Each episode card in the vertical list can display the following metadata:

* Episode title
* Episode number
* Description
* Duration
* Thumbnail
* Publish date
* Watch progress (if the user has started watching)

## Available actions

The following actions can be shown alongside each episode, depending on platform:

| Action                        | Web | TV | Mobile |
| ----------------------------- | --- | -- | ------ |
| Add to Watchlist / Favourites | ✓   | —  | ✓      |
| Share                         | ✓   | —  | ✓      |
| Download                      | ✓   | —  | ✓      |

{% hint style="info" %}
Watchlist and Favourites availability also depends on your realm's episodic content policy setting. If your configuration is set to series-only or seasons-and-series watchlisting, those actions will not appear in the episode list view.
{% endhint %}

## Platform notes

* **Web** and **TV** — the vertical list view is an opt-in alternative to the existing horizontal bucket layout
* **Mobile** — a vertical episode list is already the default on mobile; this configuration aligns Web and TV to match
* The layout applies to both season and series interstitial pages, as well as playlists

## Metadata configuration

Episode numbering in the list is driven by a configurable label. Your account team can set this up using the `episodeTitleWithEpisodeNumber` label, which formats as `{{episodeNumber}}. {{title}}` by default. You can also choose to hide this number entirely if preferred.

The episode count shown in the season selector label is also configurable — see [Series Interstitial: Season selector](/platform-knowledge-base/consumer-experience/interstitial-pages/series-interstitial-season-selector.md) for details.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/consumer-experience/interstitial-pages/series-interstitial-vertical-list-view-of-episodes.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
