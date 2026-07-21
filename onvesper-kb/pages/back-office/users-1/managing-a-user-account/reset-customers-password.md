> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/users-1/managing-a-user-account/reset-customers-password.md).

# Reset Customers Password

In the ‘Customers’ section in Back Office, search for the customer via Username, Name, Transaction ID, Card Number, EXID, Address - Line 1, or Postal code.

<figure><img src="/files/Wit8MW1aHYmdZI9yr5oA" alt=""><figcaption></figcaption></figure>

Click on the customer’s name to navigate to the account page.

Select 'Reset Password' and a successful notification will trigger an automated reset password email to your customer.

<figure><img src="/files/FV5YvkUU7HZlokIEAuMA" alt=""><figcaption></figcaption></figure>

The customer will then receive an email similar to the below, from here they just need to click on the ‘Reset Password’ button to reset their password. If you would like to change the text for the reset password email please speak to your account manager.

![](/files/HReF1A0f9IlDGbYpDEOt)

You also have an option to create a password reset link to share by selecting  'Create Reset Link'.

<figure><img src="/files/AG6Egg3TeCEPFa5YN65W" alt=""><figcaption></figcaption></figure>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/users-1/managing-a-user-account/reset-customers-password.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
