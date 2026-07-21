> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/advertising/advertising-on-vesper/configuring-vesper-to-call-your-ssp.md).

# Configuring Vesper to call your SSP

This guide will explain how to set up CSAI advertising on Vesper. It assumes that you already have a Supply Side Provider (such as Google Ad Manager) configured, and have generated a VAST tag. Note that the same setup steps and configuration UI are used for SSAI advertising, however SSAI requires the Endeavor Streaming team to stand up a significant amount of additional infrastructure, so you must contact your Account Manager first to initiate that process and understand the costs associated.

## Basic setup

Once enabled, Vesper back office will present a new section under "Content" : "Advertising".

<figure><img src="/files/44vGliVkSORqrNzhPayg" alt=""><figcaption><p>The advertising configuration menu</p></figcaption></figure>

Upon entering this section of back office, you will likely be greeted by this screen, showing no configuration present:

<figure><img src="/files/LUGmYQFecMwwTqrzyZP1" alt=""><figcaption></figcaption></figure>

If you have a VAST or VMAP tag ready to go, you can very quickly test that tag using CSAI ad technologies.

Click create new ad config, and get started.&#x20;

1. Give your configuration a name
2. Chose Insertion Type (CSAI)
3. Select the Device(s) you wish to apply this configuration to (Browser)
4. Set the Stream Type (VOD)
5. Enter the VMAP or VAST URL into the box\*

{% hint style="info" %}
**Important:** For VOD advertising, you must use a VMAP (a playlist) if you wish to provide mid rolls or post rolls, as the VMAP format specifies where the adverts should appear. If you are only able to provide a VAST URL for VOD, then pre-rolls are the only supported advertising format
{% endhint %}

If you're using Google Ad Manager and are unsure how to generate a tag, try their documentation here: <https://support.google.com/admanager/answer/1181016?hl=en>

The sample configuration should look something like this:

<figure><img src="/files/GpUHbHqpugAqUUGL5Mr8" alt=""><figcaption><p>Example configuration</p></figcaption></figure>

You can immediately test the VAST tag you have been given by your SSP by clicking "Launch Player" (make sure you have turned off any ad blocker on your browser!). If your SSP is returning adverts you will immediately see them

<figure><img src="/files/a8F2MduF0uPrWWJIZOIN" alt=""><figcaption><p>A test advert from Google</p></figcaption></figure>

If you save this configuration, you will now be showing adverts on all your VOD content (assuming adverts is enabled for the licence you are testing with, see: [Basic targeting: Licences](/platform-knowledge-base/advertising/advertising-on-vesper/targeting/basic-targeting-licences.md)).&#x20;

### Adding more devices & Configurations

You can chose to check all of the options on the left hand side of this view to enable VOD adverts for every supported device.

<figure><img src="/files/pc4aLOPC3bGEbBHaBZWt" alt=""><figcaption></figcaption></figure>

Alternatively, if you wish to use a different tag for different devices (to simplify your SSP-side targeting) this is possible by adding multiple tag configurations.

Endeavor Streaming recommends that you have as few configurations as possible to ensure maintenance is simplified. Ideally that would mean you only need 3 configurations to achieve the maximum capability of the Vesper Platform:

1. VOD VMAP, all devices
2. Live VAST Pre roll, all devices
3. Live VAST Mid roll, all devices

Note that whilst it is possible to have multiple tag configurations, it is not possible to have multiple tags that would apply in the same scenario. For instance, these two tags can co-exist:

1. VOD VMAP, Browser & Embedded Player
2. VOD VMAP, iPhone & Android

However trying to save this second tag will be rejected:

1. VOD VMAP, Browser & iPhone
2. <mark style="color:red;">VOD VMAP, Browser & Android</mark>

This will fail because you have now introduced two VOD VMAP configurations for web browsers.

{% hint style="info" %}
Note: due to a current stitcher limitation for SSAI, a pre roll ads are served on all devices if they are configured for any device. While we work on a resolution, residents can adjust their ad server settings to ensure that pre roll ads are not delivered to specific devices.
{% endhint %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/advertising/advertising-on-vesper/configuring-vesper-to-call-your-ssp.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
