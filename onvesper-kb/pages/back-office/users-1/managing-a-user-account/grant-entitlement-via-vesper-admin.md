> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/users-1/managing-a-user-account/grant-entitlement-via-vesper-admin.md).

# Grant Entitlement via Vesper Admin

### Introduction

Ability to specifically grant access to a customer and define which licence you want to grant access to and for how long.&#x20;

### Actions&#x20;

1. Navigate to Vesper Admin > Users > Customers
2. Search user in the search bar&#x20;
3. Click on the user so that you open up their customer summary&#x20;
4. Click on "Grant Access" and the following pop up will appear

<figure><img src="/files/aipqhQ1OC1UCxYWhw5jb" alt=""><figcaption></figcaption></figure>

5. Type in the licence ID you wish to grant access to&#x20;
6. Select Expiry Date - The date in which this will no longer have access to this licence
7. Click Save&#x20;

This user will now have access to the service via this licence.&#x20;


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/users-1/managing-a-user-account/grant-entitlement-via-vesper-admin.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
