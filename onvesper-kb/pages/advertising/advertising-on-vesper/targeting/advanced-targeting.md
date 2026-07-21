> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/advertising/advertising-on-vesper/targeting/advanced-targeting.md).

# Advanced targeting

Using [Advertisement Macros](/platform-knowledge-base/advertising/advertising-on-vesper/targeting/advanced-targeting/advertisement-macros.md) you can introduce *most* commonly requested business logic for advertising using your Supply side provider (SSP).

## Example Scenarios

Endeavor Streaming cannot provide an exhaustive list of advertising macro configurations or business logic as that will depend on your own business goals. However the most common requests which can be supported with appropriate Supply side logic include:

1. Show adverts only on certain VODs / specific adverts for certain VODs
2. Show adverts only on a particular live event / live tournament
3. Show *more* adverts to "unpaid/free" users, and less to "purchased" customers
4. Show specific adverts to **guest** users encouraging them to sign up
5. Show specific adverts only to a specific paid tier of subscribers

All of the above require passing data from the Vesper platform into the SSP, so that you can enter targeting rules and logic on the SSP that will determine what adverts are shown to the user (or if **none** should be returned to this specific instance).

## Recommended Macros

If you've no idea where to start, and you're using Google Ad Manager as your SSP, you can follow the rest of this guide to make Vesper data available in Google Ad Manager.

This section will outline Endeavor Streaming's commonly recommended Key Value Pairs in Google Ad manager, and provide copyable examples that can be appended to your VAST URL's cust\_params to pass this data to Google Ad Manager.

### Setting up Google Ad Manager

{% hint style="info" %}
This guide is intended to assist you with the setup of Google Ad Manager, a product not owned or operated by Endeavor Streaming. While we strive to ensure the accuracy and relevance of the information provided based on our experience with the product, you should consult the official documentation provided by Google, or contact their customer support for detailed instructions, updates and additional support.

Google documentation references:

* [Key Values](https://support.google.com/admanager/answer/1080597?hl=en\&ref_topic=2480647\&sjid=5008909078582620775-EU)
* [VAST ad tag Parameters](https://support.google.com/admanager/answer/10678356?hl=en\&sjid=5008909078582620775-EU\&visit_id=638469854623469693-278989826\&ref_topic=10684636\&rd=1)
  {% endhint %}

To utilise these parameters, you must add these values in Google Ad Manager under “Inventory → Key-Values” as shown in the screenshot below.

You can set the "Display-name" to anything you like, but the targeting key must match exactly in order to use the examples provided later in this page.

<figure><img src="/files/ONdZLjzkaKWGXFUrzGtl" alt=""><figcaption><p>Configured keys ready to receive data from Vesper</p></figcaption></figure>

### Key Value Pairs

#### Common keys used for both live and VOD:

*licenceId*: To allow for specifying that ads should not be delivered for customers with certain *paid* licences

*streamType*: So that you have the option to run a single Ad Unit with multiple line items targeted at vod or live

*entitlement*: To easily determine “paid” users from “free” users

*videoId*: For targeting ads at a specific video/event

*guest*: To specifically determine your “guest” users who are not yet signed in

#### **Live only keys:**

*tournamentId*: For targeting ads at all events in a DGE “tournament”

#### **VOD only keys:**

*tags***:** All DVE tags which have been assigned to the video, for targeting ads at a “group” of VOD assets (see [Managing ads through tags](/platform-knowledge-base/advertising/advertising-on-vesper/vod-advertising/managing-ads-through-tags.md))

&#x20;

### Sample custom parameters

For VOD VMAPs, make sure your VAST tag includes these cust\_params. If you don't have any cust\_params in your URL, you an copy and paste this into your URL in Vesper's Advertising section

{% code overflow="wrap" %}

```url
&cust_params={{#url_enc}}videoId={{content.video.id}}&streamType={{content.streamType}}&tags={{content.video.tags}}&licenceId={{user.licenceIds}}&entitlement={{user.purchasedEntitlement}}&guest={{user.jwt.isGuest}}{{/url_enc}} 
```

{% endcode %}

For Live tags (pre or mid roll), make sure your VAST tag includes these cust\_params. If you don't have any cust\_params in your URL, you an copy and paste this into your URL in Vesper's Advertising section

{% code overflow="wrap" %}

```url
&cust_params={{#url_enc}}videoId={{content.event.id}}&streamType={{content.streamType}}&tournamentId={{content.event.tournamentId}}&licenceId={{user.licenceIds}}&entitlement={{user.purchasedEntitlement}}&guest={{user.jwt.isGuest}}{{/url_enc}}
```

{% endcode %}

## Further logic

You will notice above that each of the custom parameters above have the "key" name, followed by curly braces "{{ }}". These are advertising macros which will be dynamically replaced by Vesper at runtime, when your customers start watching videos. For a full list of available macros that allow further business logic, see [Advertisement Macros](/platform-knowledge-base/advertising/advertising-on-vesper/targeting/advanced-targeting/advertisement-macros.md).


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/advertising/advertising-on-vesper/targeting/advanced-targeting.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
