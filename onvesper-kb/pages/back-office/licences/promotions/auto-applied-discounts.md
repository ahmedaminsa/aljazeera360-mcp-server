> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/licences/promotions/auto-applied-discounts.md).

# Auto-applied Discounts

The auto-applied discount feature allows you to automatically apply a promotional discount to a licence - ensuring that your end users see the discount applied at checkout without needing to manually enter a promo code.&#x20;

This feature is ideal for executing extensive promotional campaigns, such as seasonal sales or exclusive offers on your products (e.g., Black Friday, Holiday Sales, Limited-time promotions).

This page explains how auto-applied discounts work and how you can configure them to streamline the checkout experience for your end users.

{% hint style="warning" %}

## Key points to know

* **Only one auto-applied discount per licence** - Each licence can only have one auto-applied discount at any time
* **In-App Purchases are not supported** - Auto-applied discounts won't affect purchases made in external or mobile apps.
* **Only supports Generic discounts -** Only **Generic** discount codes can be auto-applied, **Single-use** discount codes **are not supported.**
* **Auto-applied discount configuration can't be edited** - Once a configuration has been created, it cannot be modified. To change it, please delete the existing configuration and create a new one
  {% endhint %}

## How to set up an auto-applied discount

1. Create a [Generic promotion](/platform-knowledge-base/back-office/licences/promotions.md#setting-up-a-promotional-code)
   * Ensure that the Promo code type is marked as "Generic"
2. Navigate to ***Licences > Promotions > Auto-applied discounts***

<figure><img src="/files/4HIZiCJR1i49PJMoZ160" alt=""><figcaption></figcaption></figure>

3. Click on the **"Auto Apply Discounts**" button
4. Enter the **Licence ID** for which the discount should be applied, and the **Promotion ID** of the discount
   * You can find your Licence ID under the ***Licences > Package Licences*** section of the Vesper BackOffice, and the Promotion ID under the ***Licences > Promotions*** section

     <figure><img src="/files/5DinqQ96UQhwMSpcAngo" alt=""><figcaption><p>The Licence ID corresponds to the first number in the sequence</p></figcaption></figure>

     <figure><img src="/files/8ZZFLBrArq85h6kDhqcT" alt="" width="563"><figcaption><p>Location of the Promotion ID</p></figcaption></figure>
5. Click "**Save**" to apply the configuration. The discount will then be automatically applied to all future purchases associated with the selected licence.

### What end users will see

Once an auto-applied discount has been successfully configured for a licence, the discount will automatically appear in the checkout page for any qualifying purchase.

<figure><img src="/files/iG2fXRDej6ZhCl5kBCW5" alt=""><figcaption><p>Example of auto-applied discount at checkout</p></figcaption></figure>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/licences/promotions/auto-applied-discounts.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
