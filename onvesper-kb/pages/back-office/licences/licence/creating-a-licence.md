> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/licences/licence/creating-a-licence.md).

# Creating a Licence

In Back Office, click licence, package licence and create on the right hand side.

### Section 1 - Add Licence Metadata&#x20;

Give the licence a title and description then click confirm.

You can select whether or not your license has a specific CTA type or is hidden and amend the label here

### Section 2 - Set Licence Availability&#x20;

**Set your licence availability date,** this is how long customers can keep accessing content on this licence.

**Set your purchasable date** - This is how long it appears in the checkout flow for customer to purchase..

**Set your display rules** -standard checkout flow = visible on checkout page, behind locked content = if you click on an asset with a padlock and will be presented with a licenc&#x65;**.**

**Allow locked content to be visible to guest users** =If guest access is enabled, a user can click on    an asset with a padlock and will be presented with a licenc&#x65;**.**

**Select your Licence Purchase Countries -** Which countries the licence will be available to purchase in. (whitelist means its available, blacklist is not available).

Note: For "free" licences, the purchasable restriction has little impact. It will define whether a free licence can be visually seen in a checkout flow for "purchase", but any customers in a region defined in Section 6 will be granted a free licence.

**Purchasable Devices -** Set which devices you can purchase the licence on, then click confirm

**License restrictions** - Restrict what licences should no-longer be acquirable if this licence has been acquired. If a free licence is restricted then access to that licence will be removed. Enter an licence numerical id individually or as comma-separated list.

### **Section 3 - Define type of licence**&#x20;

**Licence Type -** Is this a subscription, Rental, PPV or Free licence

**Free Trial -** if a free trial is offered on the licence, select yes and state the number of days.

**Enable subscription pause & resume -**&#x74;ick yes if you would like customers to be able to  pause their licence (subscription only)

**IAP Support & Codes** - If offering in app purchases, add the codes here.

### Section 4 - Set Licence Family&#x20;

Licence Family - if this is a subscription you can add a family to create an upgrade/downgrade path. (NB the family needs to be created first via licence family section).

Rank - add the rank the subscription licence should have. remember an annual must have a greater rank than a month. e.g. monthly rank = 10, annual rank = 20.

### Section 5 - Add content to licence

**Restrict VOD** - This defines which video-on-demand content will be available to watch on that licence. Typically this managed by Tags. e.g. 'premium'. The licence will then show all videos that have the tag of 'Premium' (tags are added to videos via a separate system in the Video Exchange.) Alternatively, answering "no" here will make your entire VOD library available to owners of this licence.

**Restrict Live Content** - This defines which live content available to watch on that licence. If you have an annual pass for example you may just want to say 'no' to make all live content available. This then unlocks all live content on the platform to that licence access to all tournaments.&#x20;

Alternatively, you could select "yes" to restrict live content completely. After restriction, if you want to open just one live event, or a tournament defined within Vesper then you'd then just add the ID for that tournament or event. If you're creating a PPV it could be a singular event, you'd add that ID. &#x20;

{% hint style="info" %}
*Example:* You have defined a "guest" licence that sets out what content should be shown to free/unregistered users. That licence normally restricts access to all Live content and only shows certain VODs tagged with "free". If you wanted to make a single live event available to those free users, you would add that live event ID here (contact content operations to confirm live event IDs, or find them in the URL of your upcoming live event).
{% endhint %}

### **Section 6 - Define Usage Restriction**

**Licence content availability (e.g. EU portability)** - Countries in which users should be able to **use** this licence to access content. For a paid licence, this setting determines whether it can this be purchased in one country and viewed in another e.g. purchased in the UK and viewable in Paris. For free licences, it determines which countries are granted the free licence.

**Device availability (device whitelist/blacklist) -** What devices you want the the licence to be played on. e.g. allowed on Web and Mobile but not allowed on TV apps.

**Playback concurrency -** This is how many video playback sessions a single user can have at any time. They can be logged into as many devices as they want - the concurrency check is only run when consuming video content.

### Section 7 - Add pricing per territory&#x20;

Set the currency, price, region & tax in this section. \
**Licence SKUs (global pricing & currencies)** -  Currency that the licence will sold in and if Tax is inclusive or exclusive.

* £8.99 | UK | Tax Inclusive | Is Default&#x20;
* $9.99 | USA, Canada | Tax Exclusive&#x20;
* €9.99 | Spain, Germany, France | Tax Inclusive

When you want to add another price click the + once complete click confirm and save the licence. If no price is configured for a specific country, the platform will use price and currency defined by default.

### IAPs

For details on how to configure IAPs, please see: [In-app purchase (IAP)](/platform-knowledge-base/consumer-experience/payments-and-subscription-management/in-app-purchase-iap.md)

### Notes

* Certain licence fields, such as the title or description, can be modified while the licence is active and live
* Platform users cannot change an active licence from tax-exclusive to tax-inclusive (or vice versa); this would require engineering work
* Vesper Insights displays the licence title as it was when the licence was created, and does not show any changes


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/licences/licence/creating-a-licence.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
