> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/content/content-management/content-segmentation-priority-and-rules.md).

# Content Segmentation Priority and rules

## Introduction

Content managers leveraging the Vesper platform can segment and target their content to cohorts of users via segmentation policies.

These policies have a **priority order**, which is as follows:

1. <mark style="background-color:blue;">Audience & Cohorts</mark>
2. <mark style="background-color:green;">Geography</mark>
3. <mark style="background-color:red;">Device</mark>
4. <mark style="background-color:orange;">Licence</mark>
5. <mark style="background-color:purple;">Schedule</mark>

When a user visits the site or app, the system will evaluate the available segments, matching them in the above order.

{% hint style="info" %}
If two segments match the exact same criteria, Vesper will prioritise the **most recently** **created** segment (modifying an old segment will not put it to the front of the queue).&#x20;
{% endhint %}

## Example scenario

{% hint style="info" %}
The below scenario is complex for illustration purposes. When applying segmentation, simplicity via creating as few segments as possible is the preferred approach to avoid unexpected results.&#x20;
{% endhint %}

*I am promoting a pay-per-view event on browser. The event must not be available for purchase on mobile because I am not using In-App-Purchases. Additionally, the event should be blocked in France owing to an already existing broadcast deal in the region.*

Here are the actions that *could* be taken:

1. Create a first hero and apply segmentation for <mark style="background-color:blue;">Audience & Cohorts</mark> -> Restrict Audience to Guest Users, segmentation for <mark style="background-color:red;">Device</mark> -> Browser and with a Call-To-Action (CTA) stating 'Sign Up to Buy Here'.
2. Create a second hero and apply segmentation for <mark style="background-color:red;">Device</mark> -> Browser and with a Call-To-Action (CTA) stating 'Buy Here'.
3. Create a third hero and apply segmentation for <mark style="background-color:orange;">Licence</mark> -> PPV Licence and with a Call-To-Action (CTA) stating 'Watch Here'.
4. Create a fourth hero and apply segmentation for <mark style="background-color:green;">Geography</mark> -> Allow France and promote something completely unrelated to the PPV.
5. Create a fifth hero and apply segmentation for <mark style="background-color:red;">Device</mark> -> Android Phone & iOS phone and promote something completely unrelated to the PPV.
6. Leave a Generic hero with no segmentation to ensure there is a fallback for users that do not fit any of the above criteria.&#x20;

Once complete, these are my segments:

<table data-header-hidden><thead><tr><th width="115"></th><th></th><th></th><th></th><th></th><th></th></tr></thead><tbody><tr><td>Generic</td><td><mark style="background-color:blue;">Guest Browser (1st hero)</mark></td><td><mark style="background-color:red;">Browser (2nd hero)</mark></td><td><mark style="background-color:orange;">Purchased licence (3rd hero)</mark></td><td><mark style="background-color:green;">France (4th hero)</mark></td><td><mark style="background-color:red;">Mobile apps (5th hero)</mark></td></tr></tbody></table>

### Segmentation priority policies in action

#### Customer A

*Customer A is a guest user on a web browser.*

Customer A will be shown the <mark style="background-color:blue;">Guest Browser 1st hero</mark>, which targets guest users on browser.&#x20;

#### Customer B

*Customer B is a guest user on an Android app.*

Customer B will be shown the <mark style="background-color:red;">Mobile Apps 5th hero</mark>, which targets Android apps. Even though they are a guest user, they don't qualify for the first hero because they are not visiting the platform from a browser.

#### Customer C

*Customer C is a guest user from France on a web browser.*

Customer C will be shown the <mark style="background-color:blue;">Guest Browser 1st hero</mark>, which targets guest users on browser.&#x20;

Even though the PPV should not be seen in France, Audience & cohorts policies are prioritised over Geography.&#x20;

To fix this, the first hero should also contain segmentation by <mark style="background-color:green;">Geography</mark>.

#### Customer D

Customer D is a logged in user from France that has purchased the PPV

Customer D will be shown the France 4th hero, which targets users in France, since segmentation by geography is prioritised over segmentation by licence.

#### Customer E

Customer E is a logged in user from the UK on a web browser that has purchased the PPV

Customer E will be shown the <mark style="background-color:green;">Browser 2nd hero</mark>, which targets users on web browser, since segmentation by device is prioritised over segmentation by licence.&#x20;

{% hint style="info" %}
In this example, the <mark style="background-color:orange;">Purchased licence 3rd hero</mark> will never be shown because the segmentation by device always take precedence.&#x20;
{% endhint %}

#### Licence blocking VS Segmentation behaviour

Our licence structure supports [device‑level Usage Restrictions](/platform-knowledge-base/back-office/licences/licence/creating-a-licence.md#section-6-define-usage-restriction). When a licence restricts a specific device, it does not grant any entitlement on that device.

<figure><img src="/files/az8t1vsgKXM6Qxcq6jun" alt="Device usage restrictions" width="479"><figcaption><p>Device Usage restrictions configuration</p></figcaption></figure>

For example, if a licence restricts Xbox, owning that licence provides no content entitlement **on Xbox**. Users on Xbox will only be able to watch content if another licence they own explicitly grants access on that device.

However, segmentation behaves differently.

If a hero is configured to target owners of a specific device, **the hero will still be displayed**, even if that licence restricts the targeted device.

**Use case:**

I am selling two subscription tiers: Basic and Premium.

The basic licence restricts Xbox devices, and only Premium licence users are entitled to watch content on Xbox.

To encourage upgrades, I want Xbox users on the Basic tier to be prompted to upgrade to the Premium licence to access content.\
\
A hero segment is created that targets owners of the **Basic** licence on Xbox devices (see example below), and the hero slide prompts said users to upgrade to the **Premium** licence.

<figure><img src="/files/nODIyI3uePg8kDQfrXly" alt=""><figcaption></figcaption></figure>

**Result:** \
Although the **Basic** licence restricts Xbox, hero segmentation still applies, and the hero is shown to Xbox users who own the **Basic** licence.

<figure><img src="/files/nCxyB3sTTUCtjhHDvtSm" alt=""><figcaption></figcaption></figure>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/content/content-management/content-segmentation-priority-and-rules.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
