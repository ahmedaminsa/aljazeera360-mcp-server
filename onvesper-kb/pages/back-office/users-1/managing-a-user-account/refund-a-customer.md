> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/users-1/managing-a-user-account/refund-a-customer.md).

# Refund a Customer

If you need to refund a customer’s account as they no longer need that subscription than this can be done via the customer’s account. To remove the customer’s subscription you will need to go ‘Customers’ section in Back Office, search for the customer via Username, Card Number, Name or EXID.

<figure><img src="/files/I5sNKA7a5rqXq50Up1Ft" alt=""><figcaption></figcaption></figure>

Click on the Customers name and you will be taken to the customer's account page. Select the ‘Licences’ tab and you will see all the payments that have been made under ‘Event Type’.

Once you have found the payment that you need to refund, select the ‘Confirmed’ button on that particular line of the payment.

<figure><img src="/files/jr4WV6RyE1AXfO3QkRFm" alt=""><figcaption></figcaption></figure>

You will be taken to the ‘Manage Transaction’ section, where you can select to either provide a Partial refund or Full refund to the customer depending on the use case.

<figure><img src="/files/8L3ICslA2fYVfvsLPs3u" alt=""><figcaption></figcaption></figure>

From this area, you will then be taken to a screen which will ask you if you wish to go ahead with the refund of the transaction.

Once you have confirmed the refund of the transaction, in the right-hand corner you will see a notification will pop up confirming that the refund has been successful.

When the subscription has been refunded, if you refresh the page then you will see that the subscription has been refunded.

<figure><img src="/files/hObnu5Wl5UHHTr2DMovq" alt=""><figcaption><p>Example of a refunded transaction</p></figcaption></figure>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/users-1/managing-a-user-account/refund-a-customer.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
