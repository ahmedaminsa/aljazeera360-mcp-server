> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/users-1/managing-a-user-account/suspending-a-customer-account.md).

# Suspending A Customer Account

{% hint style="warning" %}
Suspending a user prevents the user from accessing their account. Suspending a user does not revoke/cancel the user's license.&#x20;

The suspended user will continue to be renewed and billed on their license. &#x20;
{% endhint %}

If you need to stop a customer from accessing your platform, a Realm user with Admin privileges can suspend the customer’s account.

To suspend a customer’s account you will need to go ‘Customers’ section in Back Office, search for the customer via the values below:

<figure><img src="/files/kNIQyYSmAZcZSubU8jD4" alt=""><figcaption></figcaption></figure>

Click on the customer’s name and you will be taken through to account page.&#x20;

On the right-hand side click on the actions button then select ‘Suspend’.

<figure><img src="/files/inSOQDNKLWs34dREWJxl" alt=""><figcaption></figcaption></figure>

After selecting ‘Suspend’, in the right-hand corner of the page a notification window will pop up which states that the suspending of the customer account has been successful. You will also see a "Suspended" marker on the profile.&#x20;

<figure><img src="/files/CjOqX9AUUISbwW0KBrbU" alt=""><figcaption></figcaption></figure>

Once applied if you search for the customer again the state will now be Suspended.

Now if the customer tries to log in they will be unable to and will see the message “An Error Occurred. Please Try Again”, they will keep seeing this message until you revoke suspension on the customer’s account.

![](/files/usabGVU4RA5FdmfdT8fw)

### REVOKE SUSPENSION <a href="#revoke-suspension" id="revoke-suspension"></a>

To revoke a suspension, follow the steps above to find the customer’s account and to go into the account page, click the Actions button again for the drop-down menu to appear and select ‘Remove Suspension’.

<figure><img src="/files/dCih3D8bdUVaQ1EqT7rq" alt=""><figcaption></figcaption></figure>

You will see the notification pop up on the right-hand side letting you know that the Updated Users Status was successful. The "Suspended" marker will also be removed from the profile.&#x20;

This will mean that the customer is no longer blocked from accessing the service and can log in as normal.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/users-1/managing-a-user-account/suspending-a-customer-account.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
