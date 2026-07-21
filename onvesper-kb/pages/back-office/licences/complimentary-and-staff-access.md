> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/licences/complimentary-and-staff-access.md).

# Complimentary & Staff Access

### Scenario

You want to be able to offer complimentary access to your streaming service for your employees and vendors for a set period of time.

### Key Asks&#x20;

1. Offer complimentary access to your service to Employees and Vendors
2. Access using a 100% promo code without having to enter any card details
3. Retain control over how long the users have access for
4. Ensure that they don’t get charged once their complimentary access has been terminated.
5. Ensure that the licence is NOT visible to all other customers

### Solution&#x20;

1. Set up a **monthly licence** with the following configuration;
   1. Subscription
   2. Billing period – Monthly
   3. Hidden from the checkout flow
   4. Hidden from behind locked content
   5. Purchasable
2. Set up a **promo code**
   1. Single use (to avoid the code being distributed)
   2. Associated with the licence above
3. **Backend configuration** (contact your B2B helpdesk to request this configuration)\
   \&#xNAN;*Contact your B2B helpdesk address with the following template, using your 4 digit unique licence ID:*\
   \
   Hi Helpdesk, \
   \
   I am configuring a new licence (licence ID *xxxx*) to be redeemable only through promotional codes. Please ensure that all managed payment providers are disabled for licence ID *xxxx*, allowing only "Zero value basket" as a payment method.\
   \
   Thanks,\
   \&#xNAN;*name*
4. Step 3 above ensure that it will never be possible for someone else to purchase the licence unexpectedly. Access will be restricted through promo codes. Your staff can then access the licence with a direct licence link, follow the instructions on this page to make one: [Link to a licence or pre-applied promotion in checkout](/platform-knowledge-base/consumer-experience/web/link-to-a-licence-or-pre-applied-promotion-in-checkout.md)

### Alternative Solution/granting extended access

If you would prefer not to have time-based access (i.e. a monthly subscription), you can chose to either:

1. In Step 2 above, provide a promo code that grants multiple, or infinite free periods (e.g. 12 periods of a monthly licence would be a 1 year access promo code)\
   \
   OR<br>
2. You can use a "PPV" type licence which unlocks all content to grant access to your service indefinitely through this method. Please note that this will require you/your team to manually review customers with access through this licence and suspend any that should no longer have access through back office.

### Payment Details Refresh

Payment details refresh – This is a churn prevention tool that is enabled on Vesper by default. Because users who get access to this complimentary licence will NOT have a Credit Card associated with their account they will fall into the bucket of users that get notified to add a card. The concern here is that if users add a CC to their account before their next renewal and their complimentary access has terminated then will they get charged at the next renewal.

To prevent this issue you must contact helpdesk and request that all payment providers from the licence there will NO risk of the user getting charged even if they do add a card. That said, there are a couple of things to be aware of on the UI when users are in this state;

* Email – Notifying them to “update their CC” – This is just a service email that takes the user to their account page – No risk here
* Payment Details Refresh UI (See below) – Navigating to their account page they will see the CTA “Update payment details” however, clicking on this CTA will still NOT allow them to add a CC (see below) – No risk here

<figure><img src="/files/bZA2QdwiTpyjNoZHsZR5" alt="" width="156"><figcaption><p>Payment Details Refresh UI </p></figcaption></figure>

<figure><img src="/files/mQFj8tqAJfJvGK6RzaPn" alt="" width="188"><figcaption><p>No payment providers except for Zero Value Basket</p></figcaption></figure>

* Payment details section – With in the “payment details” section of the accounts page a user will be able to “add a card”. If a user chooses to do so a card will be added but NO payment will be taken as the card is not associated with that specific licence nor are there any available payment providers for that licence

&#x20;

&#x20;

&#x20;


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/licences/complimentary-and-staff-access.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
