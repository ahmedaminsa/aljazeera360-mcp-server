> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/dve/curating-grouped-content/display-and-watch-order.md).

# Display & Watch order

<figure><img src="/files/PQygcU9jLXJsWvKB5u1g" alt=""><figcaption></figcaption></figure>

The Display Order and Watch Order settings are configurable within both the Playlist/Series and Collection/Season pages of the Vesper VOD UI.&#x20;

These values allow content managers to decide the order that consumers engage with both the episodes of a season, or the seasons of a series,

**Display order** is the order that a the seasons or episodes will be shown on the UI. If you want to show your consumers the newest content first (useful for sports highlights or topical news content), set this value to **descending**. If you prefer to show your consumers the order in chronological order (great for content you want your consumers to binge through the whole series), set the value to **ascending**.

**Watch order** gives even further granular control, allowing content managers to specify the playback direction when a consumer finishes a video. If you want customers to start with your newest content and then consume older content when they finish the latest one, set this to **descending**. If you want customers to instead be shown that there is new content to watch when a new episode is released, leave this value as **ascending**.

{% hint style="info" %}
Watch order will impact Vesper web's interface when a user engages with content through a season or playlist directly.

Watch order requires a further update to the Vesper platform to introduce a fully featured continue watching user experience that supports playing through a series and always offering the consumer the next episode. This functionality is expected in Q3 2025.
{% endhint %}

By default, both settings are set to Ascending across all entities.

To update either setting:

1. Navigate to the desired Playlist or Collection.
2. Select the relevant configuration option.
3. Choose Ascending or Descending based on the desired content behaviour.

### Examples

The examples below illustrates how these changes appear in the Vesper VOD UI and the Vesper web application.

#### **Ascending Order**

<figure><img src="/files/7Cy3ikCzTH6lcS9PwTQr" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/jyusUfjM0H3S2cOgQXzU" alt=""><figcaption></figcaption></figure>

#### **Descending Order**

<figure><img src="/files/GBLbIEs8isMUDU10X5M1" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/gTFyym5deF9rDqOP3PkZ" alt=""><figcaption></figcaption></figure>

### Batch edits and Onboarder API

These properties are available on the Vesper Onboarder API if you wish to set them during content onboarding or edit from a third party asset management system.

Please refer to your Vesper Onboarder API docs for details on how to set these properties.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/dve/curating-grouped-content/display-and-watch-order.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
