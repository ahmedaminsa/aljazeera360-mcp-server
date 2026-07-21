> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/users-1/managing-a-user-account/edit-customer-information.md).

# Edit Customer Details

If you ever need to make any changes to a customer’s account such as their name, email address or address. To make these changes you need to go to the ‘*Customers*’ section in Back Office, search for the customer via Username, Card Number, Name or EXID.

Click on the customer’s name and you will be taken to the Customer's account page. On the right-hand side of the page, you will see under the ‘*User Actions*’ button another option called ‘*Edit Details*’.

<figure><img src="/files/MaeaGf2UbWMlWC2ivckz" alt=""><figcaption></figcaption></figure>

After selecting the ‘*Edit Details*’ button you will be given the option to make changes to the following sections:

* Full Name
* Preferred Name
* Email
* Username
* Phone Number
* Date of Birth
* Billing Address

Amend the details as necessary, click *save* and you will see a notification appear that confirmed the change has been made.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/users-1/managing-a-user-account/edit-customer-information.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
