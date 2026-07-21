> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/administration/ip-overrides.md).

# IP Overrides

IP Override is a debugging tool available on Vesper Admin that allows you to temporarily override the Vesper system's geolocation resolution. You can leverage this tool to impersonate a region and debug block rules for elements such as live events or segmented hero images on your platform without relying on a VPN.

To access this tool, go to **Vesper Admin -> Administration -> IP Overrides -> Create an IP Override**.&#x20;

<figure><img src="/files/r0D1MO7s9F3Lnkl471KF" alt=""><figcaption></figcaption></figure>

You need to specify the following mandatory information:

* Your current IP (you can use <https://whatismyipaddress.com/>, for example).
* The country to impersonate.
* The duration of the override (minimum one day, but you can immediately remove the IP override after you no longer need it).

You can add the following optional information:

* The city to impersonate.
* The postcode to impersonate.
* The most specific division or host part of the address.&#x20;
* The least specific division or highest level in the address hierarchy.
* Whether the IP override should be detected as part of a VPN service or a hosting provider.

{% hint style="success" %}
You'll need to do a hard refresh on your browser once you reopen the front-end domain, then log out/log in for the changes to come into effect. This includes mobile/tv apps, where a log out/log in is the fastest way to apply changes.
{% endhint %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/administration/ip-overrides.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
