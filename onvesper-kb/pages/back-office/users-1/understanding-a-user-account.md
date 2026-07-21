> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/users-1/understanding-a-user-account.md).

# Understanding a User Account

Once you have searched for the customer, click on the account name and you will be taken through to the ‘*Summary*’ page, where you will be presented with 6 tabs:

* **Summary** – Contains the basic information such as the email, name, preferred name, EXID, Address, and the signup date
* **Activity History** – Shows the login activity of the customer including dates and times.
* **Licences** – Shows all the details about the customer’s subscription. Here, you can see the name of the subscription, status of the subscription, type of subscription, payment method, the date of purchase, and the end date.
* **Watch History** – Shows which videos the customer has watched, along with details for the watched videos.
* **Notifications** – Customer-focused push notification. A notification will be sent to this specific customer.
* **Payment Methods** – This displays the card(s) that a customer used to sign up for the platform. An admin will be able to delete the customer’s credit card information if they have signed up via Web.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/users-1/understanding-a-user-account.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
