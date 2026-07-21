> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/consumer-experience/payments-and-subscription-management/renewal-notifications.md).

# Renewal Notifications

{% hint style="info" %}
See also [Checkout Consent Management](/platform-knowledge-base/back-office/administration/user-consent-management/checkout-consent-management.md) which is often enabled with this feature
{% endhint %}

Vesper features a tool that allows the sending email notifications to users about upcoming subscription renewals. This supports compliance with the **California Auto-Renewal Law**, which requires, starting **July 1, 2025**, that users on annual (or longer) subscriptions receive advance renewal notices.

To set up and enable this feature, please coordinate with your **Platform Account Manager**

## What Can Be Configured

1. **Email Templates**

There are two types of email notifications that can be customized:

* **Renewal Reminder:** notifies users of an upcoming renewal

<details>

<summary>Templated Copy </summary>

Subject: Your subscription for \[licence name] will renew on \[renewal date]

Body:

Hi \[Customer name],

This is a reminder that your subscription for \[licence name] will renew.

You’ll be automatically charged as described below to the payment method provided unless you cancel at before then.

You can cancel at any time by going to your account page.

\--Membership information--

Next payment: \[amount]

Payment date: \[date]

All pricing is accurate as at the date of this e-mail. Pricing is subject to change and may have increased. Please visit your account to see up-to-date pricing information. This renewal notification is not an invoice.

</details>

* **Renewal Confirmation**: confirms when a renewal has been processed

<details>

<summary>Templated Copy </summary>

Subject: Your subscription has renewed

Title: Your subscription for \[Licence name] has successfully renewed.

Body:

Dear \[Customer name]

Your subscription for \[Licence name] has successfully renewed.

\[Manage your account]

– Membership information –

Customer Name:

Customer Address\
Purchase ID:

Membership: \[ID]

Sub total: \[amount]

Tax: \[amount]

Discount: \[amount]

Total: \[amount]

Payment method: \[Payment method]

Billing date:

The payment will show up on your statement as “\[value]“

</details>

2. **Notification Schedule**

You can define multiple renewal notifications and set different schedules for each renewal cycle. For example, you can have separate schedules for monthly, quarterly and annual subscriptions.

Additionally, you can target notifications by **country and U.S. state**, allowing for region-specific compliance.

## How It Works

Once your email templates are finalized and your schedules are configured, users will begin receiving:

* A **renewal reminder** according to the defined schedule
* A **renewal confirmation** after the renewal has been processed

{% hint style="info" %}
If there isn’t a schedule that matches a user’s exact subscription cycle, the system will use the next closest option. For example, if a resident sets up schedules for monthly and quarterly renewals but not for annual, users on annual plans will receive renewal notifications based on the quarterly schedule
{% endhint %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/consumer-experience/payments-and-subscription-management/renewal-notifications.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
