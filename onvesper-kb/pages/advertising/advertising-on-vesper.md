> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/advertising/advertising-on-vesper.md).

# Advertising on Vesper

The Vesper platform can be configured to provide linear advertising for VOD and Live videos. This section will outline basic configuration and concepts of advertising.

{% hint style="info" %}
**Important:** Vesper is not a provider of advertising technology. The platform can integrate with almost every Supply-Side Provider (SSP) utilising Client-Side (CSAI) technologies. Vesper is also partnered with Server-Side (SSAI) stitching providers who support several SSPs.

In order to advertise on Vesper, you must have a Supply-Side Provider (SSP) to own managing your advertising inventory. Vesper has no advertising inventory management capabilities.&#x20;
{% endhint %}

### Self Serve Ad Configurations

Within the Advertising section of Vesper Back Office, users can now create and manage their own ad configurations through a simple and intuitive interface. To begin, navigate to the Advertising tab and click on “Create Ad Configuration.” From there, users can specify configuration details such as the platform, ad server URL, and fallback behaviour. The interface supports device-level targeting, making it possible to tailor ad delivery strategies for specific platforms like Android TV, iOS, or Roku. Once saved, the configuration becomes immediately available for use across events or content libraries, giving residents full control over how and where ads are served.

<figure><img src="/files/m2DO57AnRdCwuDK0HOeD" alt=""><figcaption></figcaption></figure>

### Glossary

Getting started with advertising? Here are some definitions you need to know.

<table><thead><tr><th width="227">Term</th><th>Definition</th></tr></thead><tbody><tr><td>Supply-Side Provider (SSP)</td><td>Responsible for managing advertising inventory (the adverts themselves and rules for how to target them). Can manage sponsorship, house advertising, bumpers and programmatic advertising to the highest bidder</td></tr><tr><td>Client-Side Advertising (CSAI)</td><td>The front end application/web app pauses or stops the primary video content, to instead switch to playing a seperate advertising video stream. All logic is managed on the client side, leveraging customer's devices for lower costs, but is easier to block and requires rebuffering.</td></tr><tr><td>Server-Side Advertising (SSAI)</td><td>Adverts are dynamically stitched into the content video stream served to each user.</td></tr><tr><td>Consent Management Platform (CMP)</td><td>The EU and most US states require a consent management platform to be installed on any platform serving <em>personalised</em> adverts. If you are planning to use programmatic and personalised adverts you will likely need a consent management platform so that a customer can opt-out of such tracking. Vesper currently supports <a data-mention href="/pages/vFu532mRZfZv1JpXug3R">/pages/vFu532mRZfZv1JpXug3R</a> as a CMP.</td></tr><tr><td>Video Ad Service Template (VAST) ad tags</td><td>Template for structuring ad tags that serve ads to video players using an XML schema. You can read more about the IAB standard here: <a href="https://www.iab.com/guidelines/vast/">https://www.iab.com/guidelines/vast/</a>.</td></tr><tr><td>Video Multiple Ad Playlist (VMAP)</td><td>The IAB XML specification used to describe the structure of the ad inventory insertion. VMAPs can be thought of as the playlist of VAST tags that accompanies a VOD, explaining at what time to play an advert pod, and how many ads will be in that pod. You can read more about the IAB standard here: <a href="https://www.iab.com/guidelines/vmap/">https://www.iab.com/guidelines/vmap/</a>.</td></tr></tbody></table>

### Supported devices

This list must reflect all the devices vs stream types, ad insertion modes available in the platform currently in Production environment.

* :white\_check\_mark: - Supported
* :x: - Not supported
* :clock1: - In progress
* *blank* - Not planned **yet**

| **Device Types** | **CSAI**             | **SSAI**             |
| ---------------- | -------------------- | -------------------- |
| BROWSER          | :white\_check\_mark: | :white\_check\_mark: |
| EMBEDDED\_PLAYER | :white\_check\_mark: | :white\_check\_mark: |
| IOS\_PHONE       | :white\_check\_mark: | :white\_check\_mark: |
| IOS\_TABLET      | :white\_check\_mark: | :white\_check\_mark: |
| APPLE\_TV        | :white\_check\_mark: | :white\_check\_mark: |
| ANDROID\_PHONE   | :white\_check\_mark: | :white\_check\_mark: |
| ANDROID\_TABLET  | :white\_check\_mark: | :white\_check\_mark: |
| ANDROID\_TV      | :white\_check\_mark: | :white\_check\_mark: |
| CHROMECAST       | :x:                  | :white\_check\_mark: |
| FIRE\_TV         | :white\_check\_mark: | :white\_check\_mark: |
| FIRE\_TABLET     | :x:                  | :white\_check\_mark: |
| ROKU             | :x:                  | :white\_check\_mark: |
| SAMSUNG\_TV      | :x:                  | :white\_check\_mark: |
| LG\_TV           | :x:                  | :white\_check\_mark: |
| PS4              | :x:                  | :x:                  |
| PS5              | :x:                  | :white\_check\_mark: |
| XBOX             | :x:                  | :x:                  |
| HISENSE          | :x:                  | :white\_check\_mark: |


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/advertising/advertising-on-vesper.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
