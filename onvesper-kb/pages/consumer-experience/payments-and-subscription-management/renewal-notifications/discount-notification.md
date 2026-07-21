> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/consumer-experience/payments-and-subscription-management/renewal-notifications/discount-notification.md).

# Discount notification

Vesper Features a tool that allows the sending of e-mail notifications prior to a discount ending. This means we can send a notification to customers who have previously claimed a discount on their subscription, prior to the discount ending, warning them that their next renewal will be full price.

To set up an enable this feature, please coordinate with your **Platform Account Manager**&#x20;

## What Can be Configured&#x20;

You can define;&#x20;

1. Which users this applies to based on their billing frequency e.g Monthly vs Annual users&#x20;
2. Target notifications by country / state&#x20;
3. Define the number of days prior to the discount ending that you would like this notification to be delivered. For example; I would like users to receive this notification 7 days prior to the discount ending.&#x20;

## Email Template&#x20;

The email template will include;&#x20;

1. Old Price&#x20;
2. New Price&#x20;
3. When the price change will take place&#x20;

See example below;&#x20;

<figure><img src="/files/OKfvridufZ6t6ArbFUos" alt=""><figcaption></figcaption></figure>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/consumer-experience/payments-and-subscription-management/renewal-notifications/discount-notification.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
