> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/content/content-management/segmentation.md).

# Hero Segmentation

## Introduction

Hero Segmentation enables content managers to display customised banners to users based on specific criteria such as geographic regions, entitlements, partitions, devices or user authentication status. This feature enhances the user experience by ensuring the content displayed is relevant to their preferences and access rights.

## Back Office configuration

1. On Vesper Back Office, go to Content -> Content Management ->  Home (or any new or existing section).
2. Select **+** on the top right side to create a new Hero (or edit an existing one).
3. Give your segment a descriptive name; this is not user-facing and will help you keep track of your heroes.
4. Select the Segmentation Format. By default, it will be 'Custom'. For guidance on how to use a Geo-Template or a Geo-Policy instead, please read [this](https://docs.onvesper.com/platform-knowledge-base/back-office/content/content-management/geo-templates-and-geo-policies-on-vesper-back-office).&#x20;
5. By default, you can segment by all the available options on Vesper, which will be detailed below.

## Segmentation options

### Segment by Schedule

<figure><img src="/files/lunFxSmK53prb29gdE9g" alt=""><figcaption><p>A hero scheduled for a weekend </p></figcaption></figure>

Content managers can create a hero and schedule it be published during a predefined time window. This flexibility allows teams to strategise their content delivery ahead of time.

This method of segmentation is very useful for clients featuring live content outside of standard business hours, such as sports, since they can schedule the hero to be taken offline once the live events are concluded.

One the hero configuration is completed, the UI will display the start and end times of the Hero, which can be amended at any time should the time window need to be shortened or extended.

<figure><img src="/files/TmDyF52frYxbrBMS5xmt" alt=""><figcaption><p>Scheduled hero</p></figcaption></figure>

### Segment by Partitions&#x20;

See document [here](https://docs.onvesper.com/platform-knowledge-base/~/revisions/SZJs5bLGsYWhPfAqKYZq/back-office/content/content-management/optional-partitions) for more information about partitions.&#x20;

Content managers can target hero images by partitions.&#x20;

For example - As a content manager I would like users who chose their favourite team as "England" to be served an "England flag" for the hero image, and those that chose "Italy" as their favourite team to be served an Italian flag.&#x20;

**Segment Hero by Partition:**

Follow the steps noted above ("Back office configuration").&#x20;

When choosing this option;&#x20;

<figure><img src="/files/0TfAZt6wdYuajRCJJs4F" alt=""><figcaption></figcaption></figure>

Enter in the "Abbreviation" and then select the team that you would like to use.&#x20;

{% hint style="info" %}
NOTE: you will have input ALL three letters for your abbreviation before the tram will appear.&#x20;
{% endhint %}

This method of segmentation creates a personalised look and feel to the user based on the "Partition" (or favourite team) that is chosen. See the front end experience for the example outlined above.

Picking Italy as your favourite team you will be presented with the below;&#x20;

<figure><img src="/files/WLNCQQfhJeoasEOxn6ES" alt=""><figcaption></figcaption></figure>

Picking England as your favourite team you will be presented with the below;&#x20;

<figure><img src="/files/CcymmYCRZRidRjAJDGu3" alt=""><figcaption></figcaption></figure>

### Segment by Audience and Cohorts

<figure><img src="/files/5ayNwKqxWegE3A6rbcvU" alt=""><figcaption><p>Restricting a hero to guest users only</p></figcaption></figure>

Content managers can target heroes to guest (or, unauthenticated) users.&#x20;

This method of segmentation is very useful to serve guest users with a tailored banner highlighting the benefits of signing up or registering to the platform rather than showcasing specific content.&#x20;

Additionally, content managers can upload tailored heroes to three user cohorts managed by the Vesper platform:

* New Users (bnu) - users that have just signed up or registered to the platform can be targeted with a hero, perhaps welcoming them to the service.
* Winbacks (bwb) - if your platform has any subscription services, these are former users that at one point churned and made their way back to the platform. These users can be targeted with a hero acknowledging their return.
* Super User (bsu) - your most engaged users can be targeted with content targeted to them, perhaps highlighting new seasons or series to binge.&#x20;

### Segment by Geography

<figure><img src="/files/yOtZsGRVyqILGWgHTLMd" alt=""><figcaption><p>Hero displayable in Spain and the UK</p></figcaption></figure>

Content managers can target heroes to be displayable in selected territories only, choosing between allowing or blocking locations. This feature is very useful when your platform serves a global audience and multiple rights deals are in place based on location.&#x20;

End users accessing the platform outside of the marked territories will be served a generic hero.&#x20;

### Segment by Device

<figure><img src="/files/G3Dc4aEGnr8kruvsDRgc" alt=""><figcaption><p>Hero available on mobile phones</p></figcaption></figure>

Content managers can target heroes to be displayable on selected devices, providing different creatives that generate increased user engagement across their preferred method of consumption.

This feature can leverage your knowledge of how users interact with their devices to access a streaming platform. For example, mobile users might prefer a curated image cleared from any text and logos owing to the mobile's small screen size, whilst browser users might prefer banners with more metadata, which will assist them in determining if the content fits their preferences.&#x20;

### Segment by licence

<figure><img src="/files/u9ZfFDfVOZHALm29jVDA" alt=""><figcaption><p>Apply a hero to a licence</p></figcaption></figure>

Content managers can target heroes to be displayable to end-users that have attained one or more predefined licences. They can target licences at an individual level or they can target an entire licence family. This is useful if you're looking to showcase new content dropped for consumption under a particular licence, such as a subscription package.

{% hint style="info" %}
Universal Users will **always** see the default hero.
{% endhint %}

Combining multiple segmentations will enrich the content offering provided to your user base. If you wish to provide multiple segments and complex targeting, then familiarity with the segmentation priority rules applied on Vesper is recommended. Read more at [Content Segmentation Priority and rules](/platform-knowledge-base/back-office/content/content-management/content-segmentation-priority-and-rules.md).


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/content/content-management/segmentation.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
