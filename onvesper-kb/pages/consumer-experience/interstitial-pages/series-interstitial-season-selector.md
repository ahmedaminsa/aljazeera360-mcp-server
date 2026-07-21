> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/consumer-experience/interstitial-pages/series-interstitial-season-selector.md).

# Series Interstitial: Season selector

The season selector on interstitial pages allows users to switch between seasons of a series. By default Vesper supports platform-specific implementations of the selector to provide a more native experience on each device type — for example, a dropdown on web versus a modal on TV.

{% hint style="info" %}
To configure the season selector for your interstitial pages, contact your account team.
{% endhint %}

The selector replaces the usual implementation approach:

{% tabs %}
{% tab title="Web Dropdown" %}

<figure><img src="/files/Twt2VCUcuAf6k6tfpqkm" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Tab/Pill (Default)" %}

<figure><img src="/files/14WkIB7pN9KRxCXqGU1Q" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

## Platform implementations

<table><thead><tr><th width="307.85546875">Platform</th><th>Season selector style</th></tr></thead><tbody><tr><td>Web</td><td>Dropdown</td></tr><tr><td>TV</td><td>Call-to-action button that opens a modal with a scrollable list of seasons</td></tr><tr><td>Mobile</td><td>Action sheet</td></tr></tbody></table>

On season interstitial pages, the selector appears below the title or title logo. On series interstitial pages, it appears nested within the episode tab.

If only one season exists for a series, the selector is hidden and replaced with text.

## Configuring the label

The season selector label is configurable and can include dynamic values. You can include the following parameters in the label text:

* `{season-name}` — the name of the season
* `{episode count}` — the number of episodes in the season

For example, a label configured as `{season-name} ({episode count})` would render as `Season 1 (8)`.

Your account team can configure this label to match the language and format required for your platform, including for multi-language or RTL layouts.

## Season list pagination

The list of seasons displayed in the selector (whether in the dropdown, modal, or action sheet) loads 25 seasons at a time. As users scroll to the bottom of the list, the next 25 seasons load automatically. This is a platform-level behaviour to ensure performance across large catalogues.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/consumer-experience/interstitial-pages/series-interstitial-season-selector.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
