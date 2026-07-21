> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/licences/promotions.md).

# Promotions / Promo Codes

{% hint style="warning" %}

* To use a promo code, **the final charge after applying the discount must exceed $0.50 or £0.30.** This requirement is in place due to restrictions from payment providers on processing transactions below these amounts.
  * **Exception**: If applying your promo code reduces the total cost to 0, this minimum charge does not apply, and the promo code can still be redeemed.
* Promo codes can only be applied one at a time during checkout.&#x20;
* Promo codes are only redeemable on web.&#x20;
  {% endhint %}

Promo codes can be generated within Back Office under **Licences -> Promotions**. Promo codes can be used to offer discounts on subscriptions or something that is only new subscriptions.

## Promo code types

1. [**Generic**](#generic-code) – One standard code used for the entire campaign (often used for Affiliate partnerships)
   * Generic promo codes can be re-used once expired, for example running a Black Friday campaign every year for a 1 week redemption period with the same code e.g. BLACKFRIDAY50
2. [**Single-use** ](#single-use-codes)– Each code is different across the board (often used for competitions)
   * If you're running a promo campaign using Single-use promo codes, please note that there is a limit of 235,000 codes per promotion. Should you require more Single-use codes, additional promotions will need to be created.

## Setting up a promotional code

{% stepper %}
{% step %}

### Add Promotion Metadata

* Title - mandatory
* Description - optional
  {% endstep %}

{% step %}

### Add Promotion Availability

* Start and End Date of when you want the promotion to last
* GeoBlocking Restrictions can restrict customers based in certain countries to be able to redeem the promo code
  {% endstep %}

{% step %}

### Add Promotion Type

* Need to state the code type
  * Single - state number of codes required OR
  * Generic - name of code which will be given to customers to redeem e.g. XMAS19
* Redemption Limit - need to state how many promo codes can be redeemed
* Need to state the Discount Type
  * Percentage - up to 100%
  * Amount - you can add multiple amounts against different currencies
  * Discount Periods - You can set more than one discount period on the campaign by clicking the + e.g. if this is a promo against a monthly license you may want your monthly user to have more than one discount period. such as:
    * 100% off on the first month,
    * 50% off second month
    * 25% off third month
  * Recurring - this means that the user will continue to recur at that discount amount for the duration of the license lifetime or until the user decides to cancel.
    {% endstep %}

{% step %}

### Customer Eligibility

* Need to associate a promo code to a licence e.g. what licence will get the discount
  * \*Click on enter after typing the license ID&#x20;
* If a licence is within a family, you need to select the customer type e.g. Inactive users with no subscription, Upgrading/active subscribers and All - see [examples below](#customer-type)
  {% endstep %}
  {% endstepper %}

#### Customer Type

* **All** - This promo-code can be redeemed by all end-users, providing they pass the eligibility check.&#x20;
* **Inactive Users** - This promo-code can be redeemed by end-users who do not currently own an ACTIVE or TRIAL ACTIVE paid licence within the same licence family, providing they pass the eligibility check.
* **Upgrade** (Family ID 123) - This promo-code can be redeemed by end-users who already have an ACTIVE or TRIAL ACTIVE paid licence, and are upgrading to another licence within the same licence family, providing they pass the eligibility check.

### Direct links with pre-applied promo codes

If you'd like to pass a promotional code directly to new customers through e-mail or similar marketing, you can copy a direct link to your promotion from the promotional edit screen. See the example below where there are 2 promotions available. One uses single use codes, the other is a generic code:

{% tabs %}
{% tab title="Generic Code" %}

<figure><img src="/files/VBPEAjqF5jwcSvv1etEk" alt=""><figcaption><p>"Copy Promo URL" for generic code</p></figcaption></figure>

A generic code will give you a promo URL similar to this:

```
https://mystreamingservice.com/purchase?licences=3292%2C1396&voucher=HALFOFF
```

Where the voucher is generic "HALFOFF" and will work for anyone.
{% endtab %}

{% tab title="Single Use Codes" %}

<figure><img src="/files/2r2GZaie1SKbdvDdQS2C" alt=""><figcaption><p>"Copy Template URL" for single use codes</p></figcaption></figure>

Single use promotion codes will provide a URL like the following:

```
https://mystreamingservice.com/purchase?licences=3292%2C1396&voucher=_REPLACE_
```

Where you would need to use another tool to replace `_REPLACE_` with the single use code.
{% endtab %}
{% endtabs %}

These links will automatically be generated to deeplink directly to the licences for which the promotions are applicable, and users following them will see the promotion already applied - removing the need for those users to copy and paste that promo code into the checkout flow.

For more on the purchase deeplink flow, see [Link to a licence or pre-applied promotion in checkout](/platform-knowledge-base/consumer-experience/web/link-to-a-licence-or-pre-applied-promotion-in-checkout.md)

{% hint style="warning" %}
Before using this feature for the first time, please validate the URL that has been generated! If it is using an unexpected domain, contact your account manager for a fix.
{% endhint %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/licences/promotions.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
