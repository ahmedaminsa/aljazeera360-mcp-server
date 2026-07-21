> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/consumer-experience/payments-and-subscription-management/checkout-experience.md).

# Checkout Experience

## Overview

Our checkout flow consists of the following steps;&#x20;

1. Create login&#x20;
2. Select a plan&#x20;
3. Checkout&#x20;

Note: It is possible to change the order of 1 & 2 (e.g have Select a plan first and then create a login). If you would like to do this, then please reach out to your account manager.&#x20;

#### 1. Create login&#x20;

<figure><img src="/files/cGgMMrugoCWHXkDISJJ9" alt=""><figcaption></figcaption></figure>

#### 2. Select a plan&#x20;

<figure><img src="/files/iLSfmtEClCsakB5QnTXj" alt=""><figcaption></figcaption></figure>

#### 3. Checkout&#x20;

<figure><img src="/files/ZhrEhfbSt9czeH2XUT8x" alt=""><figcaption></figcaption></figure>

There are number of key capabilities within this flow that enable a really smooth and seamless checkout experience.&#x20;

## Key Capabilities&#x20;

1. Simple access - Ability to access the sign up flow in multiple ways, driving customers through the checkout flow&#x20;
2. Seamless customer experience - Making sure that the checkout flow is as easy as possible to use to maximise customer acquisition&#x20;
3. Consistent brand experience - Ability to customise the look and feel according to your brand's identity
4. Integrated payment providers - A number of payment providers integrated into the checkout flow to enable faster checkout&#x20;

#### Simple Access&#x20;

The sign up flow can be accessed via multiple routes, driving customers thorough the purchase flow and increasing customer acquisition. The access routes are as follows;&#x20;

1. /signup - Navigating to [www.realm.com/signup](http://www.realm.com/signup) will take you directly to the sign up flow. This has significant SEO functionality and can be optimised on Google search, ultimately increasing awareness for your service. See [here](https://docs.onvesper.com/platform-knowledge-base/back-office/content/content-management/sections/adding-seo-metadata-to-sections) for more information.&#x20;
2. Locked content - If a user was to access the home page of your service (either directly via the URL or clicking "Home" during the sign up flow) without having bought a subscription, then we will "Lock" all content on your service. Clicking on a locked piece of content will direct the user back through the checkout flow.&#x20;

<details>

<summary>Locked Content </summary>

<figure><img src="/files/ftfXzROulhr8Q9CSq6s7" alt=""><figcaption></figcaption></figure>

</details>

#### Seamless Customer Experience&#x20;

Once you have navigated to the sign up page you will be taken through the checkout flow to allow a user to purchase a licence and gain full access to the service.&#x20;

As noted above there are three key steps;

1. Create an account&#x20;
2. Purchase a licence&#x20;
3. Checkout&#x20;

There are a number of capabilities within these steps that make for a really seamless experience including;&#x20;

1. **Email Spell check** - This can be configured on or off, but if "on" a pop up will appear under the email box if your email domain looks wrong. This is to avoid any misspelt emails and risk customers not being able to log back into their account.&#x20;

<details>

<summary>Email Spell Check </summary>

<figure><img src="/files/fYpOPHvWeolIOV1extc1" alt=""><figcaption></figcaption></figure>

</details>

2. **Checkout experience on one single page** - Card details, billing details, payment summary & "pay and subscribe" are all on one single page. Meaning customers don't have to click multiple times and jump through multiple steps to pay for their subscription, reducing friction in the flow.&#x20;

<details>

<summary>Checkout </summary>

<figure><img src="/files/kjAFqYmXU87KBYfkdmrg" alt=""><figcaption></figcaption></figure>

</details>

3. **Stripe link** - For a faster checkout experience, stripe link will automatically pull through your email (from the account creation page) and with the addition of your mobile number and full name, it will mean that for any future payments using this card you can simply use email, name and number to checkout in future. This will pop up as soon as your card details have been completed. Making for a much faster checkout experience.&#x20;

<details>

<summary>Stripe link </summary>

<figure><img src="/files/dahevsOvUhHc4KztEmtg" alt=""><figcaption></figcaption></figure>

</details>

4. **Ability to navigate to "Home" at any point -** The "Go to Home" CTA remains in the top right hand corner of the page throughout the experience allowing customers to jump into the home page of the service at any point. NB// If content is locked behind a licence, then jumping to home prior to purchasing a subscription will mean all content will be locked (See above).&#x20;
5. **Appropriate legal text available** - Legal text can be placed throughout the checkout experience to ensure that you are compliant with any obligations you might have, giving you increased flexibility to showcase this copy, without the customer having to leave the checkout flow. See example below. The copy appearing in this particular example can be changed via our labels architecture.&#x20;

<details>

<summary>Example Legal text</summary>

<figure><img src="/files/NvUPOhymHzrrD9OOpzJU" alt=""><figcaption></figcaption></figure>

</details>

6. **Pre-populated fields -** We have a number of fields that will automatically populate to ensure the user doesn't have to input details more then once. These include;&#x20;
   1. Billing Address - If using Google or Apple wallet, we will automatically populate the billing address on the checkout page.&#x20;
   2. Stripe Link - We will automatically pull in the email address from your "Account creation" page to populate the email address used for Stripe link.&#x20;
   3. Country - The "Country" Filed in the checkout section of the flow is pre-populated based on the users IP address.&#x20;

#### Consistent Brand Experience&#x20;

If you navigate to the following section in our knowledgebase you can review all the options we have around theming and customisation for out checkout flow - [Checkout & Account page Customisation](/platform-knowledge-base/consumer-experience/theming-and-customisation/checkout-and-account-page-customisation.md)&#x20;

#### Integrated payment providers&#x20;

Ability to pay with;&#x20;

1. Stripe (Debit / Credit Card)&#x20;
2. Paypal&#x20;
3. Apple Wallet&#x20;
4. Google Wallet&#x20;

To set up Google / Apple wallet please see here for more information - [Apple and Google Pay (wallets)](/platform-knowledge-base/consumer-experience/payments-and-subscription-management/apple-and-google-pay-wallets.md)&#x20;

## Summary&#x20;

The checkout flow plays a fundamental role in customer acquisition. It is therefore vital that we ensure the experience is consistent with other services in market and is as easy as possible to navigate through. This is why we are constantly making iterations and updates to the flow in order to maximise customer acquisition and minimise churn.&#x20;


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/consumer-experience/payments-and-subscription-management/checkout-experience.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
