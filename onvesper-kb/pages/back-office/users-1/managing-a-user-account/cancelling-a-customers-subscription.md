> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/users-1/managing-a-user-account/cancelling-a-customers-subscription.md).

# Cancelling a Customers Subscription

A customer can cancel their own subscription via the account section.

On the rare occasion that you may need to cancel a customer’s subscription on their behalf, go to the Customers’ section in Back Office, and search for the customer via Username, Name, Transaction ID, Card Number, Exid, Address-Line, or Postal Code.

On the account summary page, navigate to the Licences page.

<figure><img src="/files/l68hjU8ejpOG8ycQsGwv" alt=""><figcaption></figcaption></figure>

In this section, you will see all the subscriptions that the customer has signed up for. On the right-hand side, you will see a button ‘Manage’, when you click on this button you will see two options will appear under the Manage Subscription box.&#x20;

Select the Licence you wish to cancel and press ‘Manage’ to access more options.

<figure><img src="/files/mH58KJm6eths8j6vNeQ6" alt=""><figcaption><p>Manage button on center-right corner</p></figcaption></figure>

<figure><img src="/files/zWoWIsgQ41O2rvChkYzW" alt=""><figcaption></figcaption></figure>

* **Revoke access now**: This will immediately cancel the user’s licence
* **Expire at the end of the current period**: This will revoke access at the end of the customer’s current billing period

After selecting ‘Revoke access now’ and then ‘Cancel Subscription’, a notification will pop up which will confirm that the subscription has been cancelled.

Once the subscription has been cancelled staus against the licence will change.

![](/files/5gDTLxeBnJkwbSdINpTT)


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/users-1/managing-a-user-account/cancelling-a-customers-subscription.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
