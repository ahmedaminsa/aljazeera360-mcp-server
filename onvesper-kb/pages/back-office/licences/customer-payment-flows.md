> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/licences/customer-payment-flows.md).

# Customer Payment Flows

Customers when purchasing a license on the Vesper Platform. These can fall into a number of scenarios which are described below.

### **Standard Flow**

In the standard flow, using Stripe to checkout, a user will:

1\. Initiate first payment event by attempting to buy a licence | Payment status: UNCONFIRMED

*a)*. First Payment events are **not** the same as renewal payment events and as such are not considered eligible for a smart retries if the payment fails).\
\&#xNAN;*b)*. Users in an UNCONFIRMED state are not reported on via analytics reports.\
\&#xNAN;*c)*. Users are afforded a brief grace period of access to the platform while their payment processes and in an UNCONFIRMED state, usually 10 minutes in length, and the payment processing is much faster such that we know if they will continue to have access or not (successful or unsuccessful payment).

![](/files/5oe7eE3d4FIZZ3GS3hR5)

2\. This is processed by the payment provider and we are sent a confirmation of successful first payment | PAYMENT\_STATUS in reports: CONFIRMED

a.) CONFIRMED events are only ever emitted for First Payment type payment events.

![](/files/oOICCTeS9WvQrkA2Qrd2)

3\. In the diagram below, the user renews for 2 periods (as defined in the licence, daily, weekly, monthly etc.) | PAYMENT\_STATUS in reports: RENEWAL\
a). The users value in the AUTO\_RENEWAL column is as TRUE in the Customer Summary report as we have recorded a licence cancellation event.

![](/files/gPUHw9AOOOL5SqlM9jpV)

4\. Between their 2nd and potential 3rd renewal the user decides to cancel their licence. | Payment status in reports: RENEWAL

a). The users value in the PAYMENT\_STATUS column remains as RENEWAL in the Transaction Report as the last transactional event recorded for the user was a RENEWAL.\
b). The users value in the AUTO\_RENEWAL column changes from TRUE to FALSE in the Customer Summary report as we have recorded a licence cancellation event.

![](/files/BlOjdiFw1ZyAG6Di4rEp)

5\. The license expires as requested by the user, no payments are taken and no future payments will be taken unless the user re-subscribes.

a). The users is no longer present in the Transaction Report as their licence has now expired and they no longer have entitlement to licensed content.\
b). The users value in the LICENCE\_STATUS column changes to EXPIRED in the Customer Summary report as we have recorded a licence cancellation event.

![](/files/uqWM4X7PRxLQ7tGrEKKW)

### **Downgrade Flow**

In a downgrade flow, using Stripe to checkout, a user will:

1. Initiate first payment event by attempting to buy a licence | Payment status: UNCONFIRMED

![](/files/LgaPvBL5q5Slsf2b4AkN)

2\. This is processed by the payment provider and we are sent a confirmation of successful first payment | PAYMENT\_STATUS in reports: CONFIRMED

![](/files/XqYRDnZK3eEOA4nzE1Na)

3\. In the diagram below, the user renews for 1 period (as defined in the licence, daily, weekly, monthly etc.) | PAYMENT\_STATUS in reports: RENEWAL

![](/files/x0Ck8LCpSqUYIlNcv8Um)

4\. User requests to downgrade their license (e.g. from Annual to Monthly) | PAYMENT\_STATUS in reports: RENEWAL\
\
a.) Users can only downgrade/upgrade within a licence family. Subscription Licences that are in a seperate licence family are considered a new purchase.&#x20;

![](/files/VK3IfFYDZBMdi2i72XQE)


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/licences/customer-payment-flows.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
