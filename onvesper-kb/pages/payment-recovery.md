> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/payment-recovery.md).

# Payment Recovery

## Introduction &#x20;

This feature has traditionally been known as "Payment Details Refresh". This feature specifically targets those users who are currently active on the service but have no chargeable card associated with their account. Therefore, they will churn at their next renewal if no action is taken.&#x20;

It allows residents to enable a UI prompt and a series of notifications to encourage the user to take action to update their card details.&#x20;

There are a number of reasons as to why users can be in this state;&#x20;

1. Zero basket checkout - They have received a 100% promo code allowing them to purchase a licence without having to input valid card details. To remain having access to the service once the promo code has expired the user will have to update their credit card details.&#x20;
2. Invalid credit card information - This can range from, Insufficient funds, lost credit card, invalid CVC, card expired etc.&#x20;
   1. Note; For these users, this is only picked up at the point we attempt to take payment.&#x20;

## User Experience&#x20;

The experience for the users comes in 2 parts;

### 1. The user interface&#x20;

If a user into this classification (i.e you do not have a chargeable payment method associated with your account) then you will be presented with a prompt on your licence within your account section. Additional CTAs will appear that will say "Update payment details" or "Pause subscription".&#x20;

See below for an example;&#x20;

<figure><img src="/files/wSzSFQ8sS000PRqWD9Eo" alt=""><figcaption></figcaption></figure>

### 2. Email Notifications&#x20;

In addition to the above UI change, the user will also receive an email notification prompting them to update their payment details.&#x20;

See example email below;&#x20;

<figure><img src="/files/e6J9e8qhNeR7EWXh1Pli" alt=""><figcaption></figcaption></figure>

## Set Up Steps;&#x20;

Please work with your Platform account manager to set this feature up.&#x20;

You will need to provide the following information;&#x20;

1. Email copy for the above email&#x20;
2. Targeted licence - For which licence does this apply to
3. Email Cadence - When would you like the emails sent
   1. X number of days before renewal&#x20;
   2. On the day of renewal&#x20;
   3. X number of days after the renewal&#x20;
4. Grace period - We have the ability to determine how long you would like the grace period to be for these users. I.e if they don't update their CC details and the transaction fails, how long will they remain having access to the service before we remove access all together.&#x20;


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/payment-recovery.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
