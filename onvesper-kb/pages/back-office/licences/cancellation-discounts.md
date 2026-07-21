> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/licences/cancellation-discounts.md).

# Cancellation Discounts

Cancellation Discounts are supported on the Vesper Platform to reduce churn.

They allow you to offer a promotional discount to end users when they attempt to cancel their ACTIVE licence.

This page explains how you can set up and manage Cancellation discounts for your end users

<img src="/files/BCM3JatF5juNpo13YV8s" alt="Example of an Image-based cancellation discount (Shown when the viewport > 768px)" width="440">

When an end-user clicks on CANCEL on the Account > Subcription page on Web, they will be presented with a one-time discount offer. For example: "Get 20% off your next two months".&#x20;

Once redeemed, the discount will be automatically applied to their next billing cycle(s) without further user interaction.

You can configure both image-based and text-only cancellation discounts.

<figure><img src="/files/22wfQ3CooI7mwzj8nT5w" alt=""><figcaption><p>Text-only cancellation discount (Shown when the viewport &#x3C; 768px or no image is set)</p></figcaption></figure>

### **Eligibility Criteria** - In order to benefit from a Cancellation Discount, the following must apply:

* The user has an active, renewing licence
* The user must not have previously redeemed a cancellation discount for that licence before
* Their active licence is included in the Cancellation discount campaign configuration
* They meet the minimum number of renewals specified in the campaign settings
* They must not be located in a country that has been blacklisted from the campaign
* They must not already have an active discount applied to their next billing cycle  (even if that discount comes from a different promotional campaign)

### **Application of the discoun**t - If the user accepts the discount:

* It will be applied to their next renewal
* It will not be carried over if they subsequently decide to up/downgrade
* It will be lost if they are subsequently cancelled immediately or revoked. And they will not be eligible to redeem it again.

## How to set up a Cancellation Discount <a href="#set-up-instructions" id="set-up-instructions"></a>

1. On Vesper Back Office, go to ***Licences > Promotions***
2. Go to the ***Cancellation Discounts*** tab
3. Click the "Add Cancellation discount" button&#x20;

<figure><img src="/files/AkG0tKPCDj1XbCqH2zMP" alt=""><figcaption></figcaption></figure>

4. Configure the **Promotion Metadata:**

<figure><img src="/files/N3ES0McM5QDWpcWK8B6M" alt=""><figcaption><p>Promotion Metadata</p></figcaption></figure>

* **Promotion name** - Internal name used for reference (Non-visible to End users)
* **Localised title** - Title shown to end-users if no image is uploaded or on smaller screens (< 768 px)
* **Localised description** - Description shown under the title if no image is uploaded or on smaller screens (< 768 px)
* **Additional notes** - Internal notes for reference only.
* **Image guidelines:**

  * Image size - Must be 600x680px
  * Content/text in the image has to use a maximum of 70% (480px) of it, on the top
    * Do not include any important content/text in the bottom 30%, since the buttons on the UI will be included here
  * The bottom 30% must be a light colour as a transparent button with black foreground will be used for “Cancel”
  * Include a margin of minimum 35px on each side + top

  *Note: If an image is uploaded, it will be displayed when the user clicks **Cancel** on desktop (viewport > 768px)*

  *On smaller screens (viewport < 768px), the Localised title and Description will be shown instead.*

5. Configure the **Promotion Availability**:

   <figure><img src="/files/8uIAX8psVCCtYySoJ3k9" alt=""><figcaption><p>Promotion Availability</p></figcaption></figure>

   * **Status toggle -** ![](/files/RtB2HN6jTUFaSVXeQXer) - :warning: You must toggle this ***on*** for the cancellation discount to become active and available to end users
   * Set the **Start Date** and **End Date** of the Cancellation discount campaign.
   * Set the **Promotion country restrictions** where applicable
   * Set the **Minimum number of renewals -** Users must have renewed this number of times to qualify for the discount
6. Configure the **Type of Promotion:**

   <figure><img src="/files/bmEE7O5N9aiqYIPTrvfE" alt=""><figcaption></figcaption></figure>

   * **Discount type** - Currently, only *Percentage* discounts are supported
   * **Periods** - Define the number of renewal periods the discount will apply for if accepted
7. Configure the **Customer Eligibility**

   <figure><img src="/files/2EFNtxIXMBrjX8i1Ttpu" alt=""><figcaption></figcaption></figure>

   * Enter the **Licence ID(s)** for which this cancellation discount should be available
     * Only eligible end users associated with these licences active will be able to see and redeem the Cancellation discount when attempting to cancel their subscription
8. **Save** the configuration

After saving, your cancellation discount campaign will appear in the list of campaigns within the *Cancellation Discounts* tab.

<figure><img src="/files/BqCNDmeTTii9CimCAT7d" alt="" width="342"><figcaption><p>Cancellation discount campaign</p></figcaption></figure>

## Reporting

In order to see how many people have claimed your cancellation discount code, navigate to;&#x20;

1. Reports&#x20;
2. Downlaods&#x20;
3. Download New&#x20;
4. Search "Cancellation Redemption Report"&#x20;
5. Generate a report for your chosen period

This will give you the following date;&#x20;

* CUSTOMER\_EXID - Unique identifier for the customer
* LICENCE\_RID - Unique identifier for the licence associated with the discount
* CLAIMED\_DATE - The date when the user accepted the offer
* DISCOUNT\_ID - The unique identifier for the discount
* DISCOUNT\_NAME - The name of the licence associated with the discount
* DISCOUNT\_TYPE - The type of discount the user accepted
* TOTAL\_DISCOUNT\_PERIOD - Denotes how many times the offer was redeemed
* REMAINING\_DISCOUNT\_PERIOD - Denotes the number of times the user can still use the offer


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/licences/cancellation-discounts.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
