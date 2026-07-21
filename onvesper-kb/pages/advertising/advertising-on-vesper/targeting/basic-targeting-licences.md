> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/advertising/advertising-on-vesper/targeting/basic-targeting-licences.md).

# Basic targeting: Licences

The most common form of advertising targeting is to only show ads to a cheaper tier of your subscription. Or, to only show ads to "free" users or logged out users.

To achieve this targeting, head to the "Licences" page in Vesper back office.

<figure><img src="/files/lDtNbyq4EVPsHDC6BpDj" alt=""><figcaption><p>Only one of these licences will display adverts</p></figcaption></figure>

The "Ads" icon in the overview demonstrates whether advertising is enabled for this licence. If enabled, then the Vesper platform will make requests to your SSP for adverts. If disabled **no such requests will be made**, advertising will be completely disabled for users who own that licence.

To edit this setting, simply edit your licence, head to section 3 of the editor "Define Type of Licence" and chose to enable or disable Advertising support

<figure><img src="/files/2xsYzC8MAah7Ob7PHvRT" alt=""><figcaption><p>The toggle for enabling adverts</p></figcaption></figure>

That's it! you can completely disable adverts for certain users with this method.

{% hint style="warning" %}
**Important!** By default, the "VIP" licence that is assigned to VIP users will not show adverts. If you are testing your adverts capability please make sure you are using a regular user and not a VIP user.
{% endhint %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/advertising/advertising-on-vesper/targeting/basic-targeting-licences.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
