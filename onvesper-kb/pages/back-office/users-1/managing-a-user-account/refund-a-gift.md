> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/users-1/managing-a-user-account/refund-a-gift.md).

# Refund a Gift

To refund gift purchase, you need the gifter's email. Use this email to search for the user in the Vesper Back Office and process the refund.

{% hint style="warning" %}
Please note that gifts purchased before September 2023 can't be refunded through Vesper Back Office.

For assistance with refunds for these purchases, please contact our Helpdesk.
{% endhint %}

1. First, search for the user who sent the gift using their email address in the Users search bar. \
   If the gifter has an account on your streaming platform, their email will appear. \
   If they gifted the license as a Guest, their ID will look similar to the example below.

<figure><img src="/files/12xjHDqd39nQ0kzqz73s" alt=""><figcaption></figcaption></figure>

2. Select a guest user and confirm their user details

<figure><img src="/files/1JaF8eyvE1Emoq5s3fMU" alt=""><figcaption></figcaption></figure>

3. Navigate to the **Gift Purchases** tab, find the gift you wish to refund, click the ellipsis on the right, and select "View Invoice"

<figure><img src="/files/rkU9kQh2gYzXxmxlcobi" alt=""><figcaption></figcaption></figure>

4. Click on the *"Issue Refund"* button

<figure><img src="/files/TEbuAyYv7Y5a3966XBC8" alt=""><figcaption></figcaption></figure>

You can then issue a refund to the gift purchaser.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/users-1/managing-a-user-account/refund-a-gift.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
