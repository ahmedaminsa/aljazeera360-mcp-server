> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/users-1/managing-a-user-account.md).

# Managing a User Account

Once you have searched for the customer, click on the account name and on the top right-hand corner of the summary page, you will find the ‘Actions’ tab.

There are six actions you can apply to your customer’s account:

* **Suspend** – The customer will no longer have access to your platform.
* **Make VIP** – Gives customer access to all content on your platform
* **Make Universal** – Gives customer access to content without the use of a VPN
* **Impersonate** – Allows support to visualise/use the resident’s site as if it were the user
* **Reset Password** – Reset password for the specific customer
* **Create Reset Link** – Creates a Reset password link which can be sent to the customer
* **GDPR Delete** – Deletes a customer’s personal data in accordance with GDPR regulations\*

{% hint style="info" %}
\*Only Endeavor Streaming can GDPR delete a customer, please raise a support ticket for this.
{% endhint %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/users-1/managing-a-user-account.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
