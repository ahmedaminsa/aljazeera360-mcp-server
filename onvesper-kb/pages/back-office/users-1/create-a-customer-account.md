> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/users-1/create-a-customer-account.md).

# Creating User Accounts

To create a new user account, go to the '*Customers*' section in the Back Office. In the top right-hand corner, on the same line as the customer search bar, you will find a button labeled '*Create Customer*'.

<figure><img src="/files/x0Nybyc9sl0SeAYFq3ko" alt=""><figcaption></figcaption></figure>

Click on ‘*Create Customer'*. A small pop-out window will appear on the screen - allowing you to enter the email address of the customer as well as the role that will be assigned to them.

<figure><img src="/files/i1bAVGMHs5nG5P2NJoLV" alt=""><figcaption></figcaption></figure>

The roles that you can choose from are:

* **Customer:** Standard user
* **Overflow (Tier 1):** Can reset the password (via email tool only), view the summary tab, Activity History, View watch history,  View Licenses/Transactions and View payment methods
* **Agent (Tier 2):** Same permissions as Overflow, and in addition, is able to Suspend users, create reset password links, Manage Licence (cancellations etc)
* **Supervisor (Tier 3):** Same permissions as Agent and in addition is able to view other users, add/disable Agent (Tier 2) accounts, change the default payment method, delete payment methods
* **Resident (Tier 4):** Same permissions as Supervisor as well as able to use the ‘Actions’ tab on customers, Add Content (Heros/Rows/Sections), Create Promo Messages, Create Users, Create Customers, Make someone VIP/Universal, GDPR Delete, Download Reports, See BI Dashboard, See Licences tab

After entering the relevant details and selecting the allocated role for the customer please click *save*.

Once the account is created, the customer will receive an email that will ask them to finish off the registration process (validate the email and enter a new password).

The new customer account created will now show on your platform as well as on Back Office, which means you make any changes to the account right away if needed.

![](/files/MVorHP5P7sYJ00m0P0BH)


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/users-1/create-a-customer-account.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
