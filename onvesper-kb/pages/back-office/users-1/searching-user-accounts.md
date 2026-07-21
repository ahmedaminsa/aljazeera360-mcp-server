> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/users-1/searching-user-accounts.md).

# Searching User Accounts

You can search for a customer/realm user by providing one of the following options: **Username, Name, Card Number** (You will need the last 4 digits of the customer’s card number and the expiry date) or **EXID**.

<figure><img src="/files/BovC0fjnuhw1yB6bit4p" alt=""><figcaption></figcaption></figure>

When you search for a customer/realm user, you will see 6 columns, ID, NAME, EXID, ROLE, STATE, CREATED.

* **ID**: Customer’s email address
* **NAME**: The name of the customer
* **EXID:** External ID assigned to the customer
* **ROLE:** Role assigned to the customer
  * **Customer:** Standard user
  * **Overflow (Tier 1):** Is able to reset the password, view the summary tab, Activity History, View watch history,  View Licenses/Transactions and View payment methods
  * **Agent (Tier 2):** Same permissions as Overflow, however, is able to Suspend users, Manage Licence, change the default payment method
  * **Supervisor (Tier 3):** Same permissions as Agent as well as able to view other users, add/disable agent, delete a payment method
  * **Resident (Tier 4):** Same permissions as Supervisor as well as able to use the ‘Actions’ tab on users.
* **STATE**: Shows whether a customer is active or inactive
* **CREATED**: The date on which the account was created


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/users-1/searching-user-accounts.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
