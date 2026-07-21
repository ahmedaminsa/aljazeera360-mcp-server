> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/consumer-experience/payments-and-subscription-management.md).

# Payments & Subscription Management

- [Apple and Google Pay (wallets)](https://docs.onvesper.com/platform-knowledge-base/consumer-experience/payments-and-subscription-management/apple-and-google-pay-wallets.md): Introduction to digital wallets as additional payment methods.
- [In-app purchase (IAP)](https://docs.onvesper.com/platform-knowledge-base/consumer-experience/payments-and-subscription-management/in-app-purchase-iap.md): Guide on how to create your IAPs for Apple, Google, Amazon and Roku platforms.
- [Renewal Notifications](https://docs.onvesper.com/platform-knowledge-base/consumer-experience/payments-and-subscription-management/renewal-notifications.md)
- [Discount notification](https://docs.onvesper.com/platform-knowledge-base/consumer-experience/payments-and-subscription-management/renewal-notifications/discount-notification.md)
- [Anniversary Notifications](https://docs.onvesper.com/platform-knowledge-base/consumer-experience/payments-and-subscription-management/renewal-notifications/anniversary-notifications.md)
- [Subscription Overview UI](https://docs.onvesper.com/platform-knowledge-base/consumer-experience/payments-and-subscription-management/subscription-overview-ui.md): The Subscription Overview UI feature creates a summary of the user's licence status at the top of their account page.
- [Checkout Experience](https://docs.onvesper.com/platform-knowledge-base/consumer-experience/payments-and-subscription-management/checkout-experience.md): This page describes the checkout experience on the Vesper Platform.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/consumer-experience/payments-and-subscription-management.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
