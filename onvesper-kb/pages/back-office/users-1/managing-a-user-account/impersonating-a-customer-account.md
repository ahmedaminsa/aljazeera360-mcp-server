> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/users-1/managing-a-user-account/impersonating-a-customer-account.md).

# Impersonating A Customer Account

As a resident, you can impersonate a customer’s account to see if you can replicate an issue they are having or to view permissions applied to their account.

To impersonate a customer’s account, navigate to **Back Office -> Users -> Customers**, and search for the customer via **Username, Name, Transaction ID**, **Card Number**, **EXID**, **Address-Line** or **Postal Code**.

<figure><img src="/files/7z3eivoA3cK6NkEbN86F" alt=""><figcaption></figcaption></figure>

Select the customer name and you will be taken through to the Summary page where you can select IMPERSONATE button from the bottom menu.

<figure><img src="/files/AoZWO1FlPhoWo6TpmueR" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
If you are impersonating a customer in a different region, please connect your VPN to that territory.
{% endhint %}

A separate window tab will open once you’ve successfully logged in as that user and you’ll be notified (see image below).

![](/files/k9UN2TPlNmqzqNxi0Yjt)

{% hint style="warning" %}
Once you finished your investigation, make sure to log out as the user who you have been impersonating by clicking **Account -> Logout.**&#x20;
{% endhint %}

<figure><img src="/files/oUU4jxZAkcfnoYOLpNgy" alt=""><figcaption></figcaption></figure>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/users-1/managing-a-user-account/impersonating-a-customer-account.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
