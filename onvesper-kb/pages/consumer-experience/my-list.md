> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/consumer-experience/my-list.md).

# My List

Users can now add multiple series to **a system defined group** from the interstitial screen so that they can save the content they're most interested in.

{% hint style="info" %}
This feature replaces Favorites, owing to increased functionality around saving entire series' rather than standalone assets or episodes.
{% endhint %}

### Key Capabilities

* One-Click functionality when adding or removing content.
* Saves entire series & seasons, rather than single assets.
* Offers simple & recognizable features that will be familiar to most end-users.

<div align="left"><figure><img src="/files/iGW6HQwpE371MukmMOfW" alt=""><figcaption><p>'My List' visible in the top menu</p></figcaption></figure></div>

Users will be able to add content to their list from the following areas:

* When hovering over an asset, via clicking on an 'Add to My List' icon on the upper right of the thumbnail
* From a series' homepage via clicking the 'Add to My List' button under the series description
* From the video player, via clicking on the 'Add to My List' icon on the player control bar

<div align="left"><figure><img src="/files/BdMFPj0ANsM6nUYLlM53" alt="" width="563"><figcaption><p>CTA on the series page</p></figcaption></figure></div>

### Device Availability

'My List' will be available on the following devices:

* Web
* Mobile version 8.0
* UTV version 3.10
* Roku version 3.19

### How to Configure

If you wish to have this feature enabled, please contact your Account Management team. Once enabled in your Realm Settings, the 'My List' Menu item can be added to your homepage layouts via the following steps:

In back office, navigate via **Administration > Menus**. Create or Edit an existing Menu  and click 'Next'. Under Step 2, click "Add an Item"

<div align="center" data-with-frame="true"><figure><img src="/files/sfHSZNYpXpgaRLpdVsfa" alt="" width="375"><figcaption></figcaption></figure></div>

#### Menu Item Details

Name the new item "My List", and choose your preferred location. Select "View" and enter "/mylist" under the redirect options.

<div data-with-frame="true"><figure><img src="/files/0576uJq5g8nIdb6ZD06Q" alt="" width="375"><figcaption></figcaption></figure></div>

Finishing adding your new item by selecting the appropriate user and translation settings, and publish your new item to add "My List" to your homepage.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/consumer-experience/my-list.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
