> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/consumer-experience/interstitial-pages/series-interstitial-tabbed-navigation.md).

# Series Interstitial: Tabbed navigation

Tabbed navigation organises the content on an interstitial page into distinct tabs, separating episodes, related content, and participants into their own views. This makes it easier for users to explore the different types of content associated with a title without everything competing for space on a single scrolling page.

It is available on Web, TV, and Mobile.

{% hint style="info" %}
To enable tabbed navigation on your interstitial pages, contact your account team.
{% endhint %}

### Available tabs

| Tab             | Description                                                                                                                                                    |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Episodes        | The episode list for the current season or series. This tab is shown first and opens by default.                                                               |
| Related Content | Other content related to the current title, displayed in a list format. See [Related Content](/platform-knowledge-base/consumer-experience/related-content.md) |
| Participants    | Cast, crew, or other participant data associated with the content. See [Participants](/platform-knowledge-base/dve/video/participants.md).                     |

Tabs are only shown if the relevant content exists. For example, if no participants have been configured for a title, the Participants tab will not appear.

### Notes

* The Episodes tab is always first and selected by default. The system has been designed to allow this to change if requested - at the time of publishing no use cases for changing that default have been identified.
* Related content is displayed in list format within its tab
* Tabs work alongside the [Series Interstitial: Vertical list view of episodes](/platform-knowledge-base/consumer-experience/interstitial-pages/series-interstitial-vertical-list-view-of-episodes.md) — when both are enabled, the episode list within the Episodes tab uses the vertical list layout


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/consumer-experience/interstitial-pages/series-interstitial-tabbed-navigation.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
