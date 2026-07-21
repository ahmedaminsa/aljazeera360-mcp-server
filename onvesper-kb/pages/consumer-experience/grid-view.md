> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/consumer-experience/grid-view.md).

# Grid View

{% hint style="warning" %}
An MVP for the grid view is now available for customer use. We will continue to iterate on this functionality to increase the use cases for the feature.
{% endhint %}

The Grid View is a new way for customers to browse through all content available on your streaming platform in an organised and efficient manner.&#x20;

This view consolidates all content into a single page, making it easier to explore and discover new titles without the need to scroll through specific genres individually.

<figure><img src="/files/Mh61JzQ2c0Purmledn0m" alt=""><figcaption><p>Grid view - filtered to show "Series"</p></figcaption></figure>

## Filters

On the top right, users can find filters that can be used to narrow down content.

There are two types of filters:

* **Customer-defined filters:** These filters uses Typed tags that have been set up on the Vesper VOD platform. To learn more about Typed tags, please click [here](/platform-knowledge-base/dve/video/typed-tags.md).\
  \
  If you’d like one of your typed tags to be used as filter, please reach out to your Account Manager to get these set up. <br>
* **Content Type**: This allows the user to filter the results by Content Type (Series, Season, VOD or Playlist.&#x20;

<figure><img src="/files/8sW4fjEemtWZ43388dJ6" alt=""><figcaption><p>Filters</p></figcaption></figure>

The **Customer-defined** filters use OR conditions. From the example in the screenshot above, this means that if a user selects *Comedy* and *Sports*, the Grid View will display all content that falls under either genre.

## Sorting

Next to the filters icon, users can sort the content in the following ways:

* Date published (newest) **\*Default\***
* Date published (oldest)
* Alphanumeric order:
  * A - Z: Sorts content from A to Z.
  * Z - A: Sorts content from Z to A.

## Enabling Grid View

{% hint style="warning" %}
Grid View requires the enhanced Vesper Search Engine to be enabled in order to work properly.

Please reach out to your Account Manager to confirm that this search engine has been enabled.
{% endhint %}

The Grid View can be enabled via the [Menu configuration](/platform-knowledge-base/back-office/administration/deprecated-menu-items.md) in Vesper Back Office as a ‘View’ of /Grid.&#x20;

The Display Name can be changed to anything - for example, you may wish to replace any existing "Browse" menu item with this function.

<figure><img src="/files/CfqzCeV38jTFQZw6CRFC" alt=""><figcaption><p>Setting up Grid view in the menu config</p></figcaption></figure>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/consumer-experience/grid-view.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
