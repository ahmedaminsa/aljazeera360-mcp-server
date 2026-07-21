> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/licences/customer-payment-flows/card-switching-and-deletion.md).

# Card switching and Deletion

If a customer wishes to switch their payment card for a renewing licence, they can follow these steps:

1. Navigate to the account section of the webapp
2. Chose "payment details" in the account menu
3. Here the customer will see their payment history and stored cards

<figure><img src="/files/FuPcCGWgXwkAwqZ3JnSZ" alt=""><figcaption><p>Viewing payment details</p></figcaption></figure>

4. Using "Add Card" the customer can add a new payment card
5. Once added, the "..." option on the new card can be used to switch licence (or remove the card)
6. After selecting switch licence, the customer can select the licence they wish to move to the new card:

<figure><img src="/files/yEx0TyB8rynUAltvwLxK" alt=""><figcaption><p>Changing the licence card</p></figcaption></figure>

### Deletion

A card can be deleted at any time provided there is not a licence due to renew on that card. After a successful card switch, the old card can be deleted. Cards can also be deleted if a customer has cancelled their subscription and will leave the service at the end of their current period.

### Reactivation after Deletion

Should a customer - who has cancelled their subscription and removed their card - wish to re-activate the pending cancellation licence, they will be presented with an error. They must add a new card and assign it to their pending cancellation licence, then they will be able to reactivate the licence.

These steps can be provided to customers:

1. Go to “payment details” page in account
2. Add a new payment card if one does not exist
3. Once complete, refresh the page
4. After refreshing the page, click the “…” on the card
5. Click “switch licence”
6. In the dropdown which appears, chose your cancelled subscription and then click save
7. Go back to your “subscriptions” page, you will be able to re-activate the licence


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/licences/customer-payment-flows/card-switching-and-deletion.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
