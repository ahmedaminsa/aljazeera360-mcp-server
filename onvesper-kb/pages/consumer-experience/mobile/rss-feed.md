> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/consumer-experience/mobile/rss-feed.md).

# RSS Feed

Vesper allows you to integrate your RSS feed into your mobile and web apps, letting your platform users to stay updated on any news regarding your organization.&#x20;

{% hint style="warning" %}
Enabling an RSS feed on your platform requires some engineering work, so please consult with your Platform Account Manager to align expectations&#x20;
{% endhint %}

Vesper is primarily focused on the delivery of your video catalogue, therefore support for RSS is limited to the RSS 2.0 standard. Please validate your RSS feed using an online validator first, such as <https://www.rssboard.org/rss-validator/>.  The current support for RSS feeds has the following requirements and limitations:

#### Supported

* Text and image only (not videos or rich media)

* Images should include the title, URL, and link subfields, such as:
  * \<image>

    \<title>NYT > World News\</title>

    \<url>[https://static01.nyt.com/images/misc/NYT\_logo\_rss\_250x40.png\</url](https://static01.nyt.com/images/misc/NYT_logo_rss_250x40.png%3c/url)>

    \<link>[https://www.nytimes.com/section/world\</link](https://www.nytimes.com/section/world%3c/link)>

    \</image>
  * \<media:content url=<http://cms.pbr.com/media/18568193/joao-ricardo-vieira-740x416.jpg> type="image/jpeg" medium="image"> \</media:content>

* Valid markdown
  * pubDate: used to identify when a new item should be added
  * title: the title of the article
  * body: if no body is provided, we will link to another page if a URL is provided

#### Unsupported

* Content updates: our database adds new content but does not review existing items. Therefore, changes to previously posted articles will not take effect
* Article management: removing an item from the RSS feed does not automatically remove it from our database

Examples:

<div align="left"><figure><img src="/files/KcWjnlqo1Hxhc28RezEp" alt="" width="375"><figcaption></figcaption></figure> <figure><img src="/files/kuVIwiJGzkaZqh0IAvFL" alt="" width="375"><figcaption></figcaption></figure></div>

Please note that the best user experience for the RSS feed will be on mobile. You can decide whether to display it in the web app as well, and where, by using the menu configurator ([Menu items](/platform-knowledge-base/back-office/administration/menu-items.md)).


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/consumer-experience/mobile/rss-feed.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
