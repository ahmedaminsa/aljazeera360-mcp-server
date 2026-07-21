> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/consumer-experience/continue-watching-updates.md).

# Continue Watching Updates

Continue Watching allows users to resume playback from where they left off. Previously the continue watching row has contained single standalone VOD assets that don't have any context to their "Parent" content - the series and season to which they are associated with.  These changes will allow that association to be made, improving the customer experience and making it far more aligned with other existing streaming services in market.&#x20;

## Key Capabilities&#x20;

The updates made can be broken down into the following;&#x20;

1. Improved Navigation - Navigate to the series or season from the continue watching row&#x20;
2. Next Episode - Easily pick up the next episode in the series you were watching
3. Parent Context - Clearly understand which series or season the content is related to&#x20;

### 1. Improved navigation&#x20;

The continue watching row will display the episode or movie that you have previously been watching. Clicking on this piece of content will now take you to the "Parent" interstitial page to which this content is associated with, whether that be a series, a season. \`This interstitial page will also contain a "continue watching" CTA allowing you to easily click on the episode or movie that you were watching within that series or season.

{% tabs %}
{% tab title="Continue Watching Row" %}

<figure><img src="/files/RKpQb6fn8HVGhrpqDGVf" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Interstitual Page" %}

<figure><img src="/files/dWr5ZkoOwVECxzVw2IIB" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

### 2. Next Episode & Next Season

Now that the assets included in the continue watching row have context with the relevant "Parent" content, we can now allow end users to seamlessly transition to the next episode in that season.&#x20;

For example, If a customer clicks on Ep 1 - Breaking bad from the continue watching row, once they have finished watching this asset they will seamlessly transition to Ep 2 - Breaking bad, allowing users to binge through their favourite season.

This extends to returning sessions as well. If customers completed Ep 2 last watch session, then return to the app the next day, Ep 3 will be waiting for them in their continue watching row.

If there are multiple seasons in a series, then customers will automatically get taken to the first episode of the next season once they have finished the prior episode. For example, once they finished S1:E10 (last episode in the season) then you will be automatically taken to S2:E1. If season 2 isn't available on the service yet, then episode 1 will appear there as soon as it is published, further encouraging engagement for customers that have engaged with earlier seasons.

<figure><img src="/files/Ul6unbxXpquApPdDVeb8" alt=""><figcaption></figcaption></figure>

Note that customers will need to make sure that "Auto-play" is enabled in their profile / preferences to automatically watch the next episode when their current one finishes. If this profile setting is disabled, a CTA will appear on screen for the user to chose to start watching the next episode when the current one finishes.

### 3. Parent Context&#x20;

All VOD's and Movies can now have the relevant "Parent" name incorporated in the title. Allowing the user to have context on the associated series or season the asset is associated with.&#x20;

For example - For a single VOD asset the title would be;&#x20;

1. **Previously**; Pilot
2. **Now;** Breaking Bad | S1: E1

<figure><img src="/files/wpupawdoqlh3LsPbyWNv" alt=""><figcaption></figcaption></figure>

This behaviour is optional, and can be configured on your realm as you see fit. There are 3 new labels associated with this display. If you wish the formatting to be different on your service please contact your account manager or helpdesk and request a label change.

<table><thead><tr><th width="182.5390625">Label</th><th>Default Value (en-US)</th><th>Example</th></tr></thead><tbody><tr><td>playlistContextTitle</td><td><code>{{playlistTitle}}</code> | <code>{{contentTitle}}</code></td><td>2025 Highlights | Top Goals</td></tr><tr><td>seriesContextTitle</td><td><code>{{seriesTitle}}</code> | S<code>{{seasonNumber}}</code>:E<code>{{episodeNumber}}</code></td><td>Breaking Bad | S01:E05</td></tr></tbody></table>

If you wish to opt out of this new formatting, you can request that all these labels be set to: `{{contentTitle}}` to maintain the existing experience where only the title is shown.

#### 3.1 Series or Season Title Image

Part of the parent context changes will, by default, show the Series or Season [**Title Image** ](/platform-knowledge-base/dve/image-and-vod-specifications.md#images-creatives)for any episode content which is part of a series. This is to re-enforce the association (combined with the `seriesContextTitle` label) that when a user clicks the card they will be navigated to the series/season interstitial.

This behaviour is optional. If you would prefer for your episodic content in the continue watching rail to still show the episode thumbnail - please contact your account manager and the configuration can be scheduled.

<figure><img src="/files/GktcPb668k0MGO1ZVX4q" alt=""><figcaption></figcaption></figure>

## Known Behaviour & Constraints&#x20;

* The continue watching row will ONLY show single episodes and movie content, rather than the overall series. However, series assets will be used when such a parent is identified.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/consumer-experience/continue-watching-updates.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
