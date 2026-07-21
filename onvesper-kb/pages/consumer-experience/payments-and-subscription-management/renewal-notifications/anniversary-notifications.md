> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/consumer-experience/payments-and-subscription-management/renewal-notifications/anniversary-notifications.md).

# Anniversary Notifications

Vesper features a tool that allows you to send an annual reminder to your paying subscribers. This is a useful tool to help you comply with certain auto-renewal laws, such as California’s Enhanced Automatic Renewal Law.

This notification is separate from and does not replace the standard renewal reminder notification that are sent before each billing cycle. It is sent on the anniversary of the user's paid membership starting.

## How To Configure

Please speak to your dedicated **Account Manager** to configure the notification&#x20;

<details>

<summary>Templated Copy </summary>

Subject: Your Annual Subscription Reminder for \[realm\_name]

Title: Your Annual Subscription Reminder for \[realm\_name]]

Body:

Dear {{customerName}},

This is your annual reminder about your {{#licenceLocalisedName:localised}} subscription.

We hope you've been enjoying {{realm\_name}} over the past year!&#x20;

We are sending this annual reminder to keep you informed about your ongoing service and its terms.

You can cancel at any time by going to your {{realm\_domain}}.

\--- MEMBERSHIP INFORMATION ---&#x20;

Membership: {{licenceLocalisedName:localised}}

Amount of Each Charge: {{skuPrice:money}}

Next Payment: {{renewalChargeAmountDetails.total}}

All pricing is accurate as at the date of this e-mail. Pricing is subject to change and may have increased. Please visit your account to see up-to-date pricing information. This notification is not an invoice.

&#x20;This payment will show up on your statement as "Dice Tech".

</details>

\
NB// The email can accommodate for paused subscriptions aswell&#x20;

## Important Notes

* Who Gets the Email: This notification is sent to users who have a managed payment subscription that has been *active for at least one year.*
* Anniversary reminders can be set up for any length of subscription, monthly, annual, 6 monthly - the e-mail will still be sent on the anniversary of the user starting their paid subscription.
* Paused Subscriptions: A user with a paused subscription will still receive this anniversary email.
* Supported Subscriptions: This feature is currently limited to managed payments only and does not support in-app purchases (IAP).


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/consumer-experience/payments-and-subscription-management/renewal-notifications/anniversary-notifications.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
