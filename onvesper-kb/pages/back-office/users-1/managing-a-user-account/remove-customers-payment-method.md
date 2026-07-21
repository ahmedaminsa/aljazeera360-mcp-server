> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/users-1/managing-a-user-account/remove-customers-payment-method.md).

# Remove Customers Payment Method

To remove the customer payment method you will need to go ‘Customers’ section in Back Office.

<figure><img src="/files/Gz54VLHT5fglBy0XprKz" alt=""><figcaption></figcaption></figure>

Search for the customer via Username, Name, Transaction ID, Card Number, Exid, Address-Line or Postal Code.

Select the customer’s name and you will be taken through to the account page.&#x20;

On the account page next to 'Payments Methods’ please select 'View All’ option. &#x20;

<figure><img src="/files/FffPO7t485daKpIUuYiv" alt=""><figcaption></figcaption></figure>

In this section, you will see all the Credit Cards that the customer has linked to their own account.

After selecting the card you wish to remove, go to the three dots in the right-hand side corner and action ‘Delete Card’ button.

<figure><img src="/files/YMlMipZ9meKQVWcniYNS" alt=""><figcaption></figcaption></figure>

Once you have deleted the card a notification will appear in the top right-hand corner of the page indicating that the customer’s credit card information has been deleted from the system and the platform entirely.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/users-1/managing-a-user-account/remove-customers-payment-method.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
