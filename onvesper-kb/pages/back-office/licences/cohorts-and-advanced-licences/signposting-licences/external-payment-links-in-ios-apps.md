> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/licences/cohorts-and-advanced-licences/signposting-licences/external-payment-links-in-ios-apps.md).

# External Payment Links in iOS Apps

Apple has recently updated its App Store Guidelines to allow apps to include external payment links following the latest developments in the *Epic v. Apple* case. This change enables app developers to direct users outside the App Store to complete purchases in the US market, in full compliance with the new policy.

The goal of this page is to guide residents who want to take advantage of this using Vesper's capabilities. It outlines how to drive users from their iOS apps to platform web apps to promote external offers and increase revenue. This can be further enhanced using Vesper's Marketing Partner Management to track conversions of those iOS in-app license cards that lead users to purchase passes via the webapp.

### Step-by-Step Setup

#### **Create an External License Provider**

To justify redirecting iOS users to an external checkout flow, you must first create an External License Provider.

* Contact your Platform Account Manager to create it
* Only two fields are required:
  * **Provider Name**: e.g., `IOS`
  * **Internal Provider ID**: e.g., `IOS`

**Create a Signposting License**

Set up a license that will be displayed to iOS users, encouraging them to purchase via the web:

* **License Metadata**:
  * Write a simple message to differentiate the pass
  * Customize the CTA title to clearly distinguish this license card from in-app purchase options
* **License Availability**:
  * Enable **"Standard Checkout Flow"** and **"Behind Locked Content"**
  * Set **"Allow Locked Content to be Visible to Guest Users"** to **Yes**
  * Under **Purchasable Devices**, allow only **iPhone** and **iPad**
  * Set **Licence purchase countries**, allow only US (recommended due to the Epic v Apple court case only applying to the US)
* **License Type**:

  * Select **Free License**
  * Set **External License Provider** to **Yes**, and choose the provider you created earlier
  * In the **Acquisition URL**, enter the link to your purchase flow or specific license(s). Example URLs:

    * `https://endeavorstreaming.com/purchase`
    * `https://endeavorstreaming.com/purchase?licences=1000`
    * `https://endeavorstreaming.com/purchase?licences=1000,2000`
    * `https://endeavorstreaming.com/purchase?licences=1000,2000&esrefid=a2f66ed6-5a3f-4fa8-a206-e3a53763a69d`\
      \&#xNAN;*(the last example includes a Marketing Referral Campaign ID for conversion tracking)*

    To create a referral campaign ID, follow the steps outlined here: [Marketing Partner Management](/platform-knowledge-base/back-office/administration/marketing-partner-management.md). Once set up, copy and paste the suffix at the end of the main purchase URL, as shown above.

  Example:

<figure><img src="/files/bgFkzmmGVdInSnVsHyw9" alt=""><figcaption></figcaption></figure>

* **Skip License Family Setup**

  You don’t need to assign this license to any family
* **Do Not Grant Content Access**

  This license is only for signposting; users will gain access through their standard paid licenses purchased via the web

#### **Link Signposting License to Paid Licenses**

To ensure the signposting license disappears once a user makes a purchase:

* Go to your paid license(s), click **Edit**
* In **Step 2: License Availability**, add the **signposting license ID** to **License Restrictions**

<figure><img src="/files/eZgcgiXii9zBs5Jjo9kr" alt=""><figcaption></figcaption></figure>

This ensures that once a user purchases a license, the signposting card is no longer shown—avoiding any confusion.

All set! If the configuration has been set up correctly, the Order Management data in Vesper Insights will confirm that those purchases were driven by your new iOS signposting license, thanks to the Marketing Partner Referral you created.

&#x20;

{% hint style="warning" %}
When redirected to your web app, the end user will be required to sign in or sign up to complete the purchase if they haven’t already logged in on the mobile web
{% endhint %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/licences/cohorts-and-advanced-licences/signposting-licences/external-payment-links-in-ios-apps.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
