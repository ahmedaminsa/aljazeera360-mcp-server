> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/licences/customer-payment-flows/free-trial-eligibility-checks.md).

# Free Trial Eligibility Checks

Free Trial Eligibility Checks (FTEC's) are checks that are performed to see whether or not a customer has taken a free trial previously.

If a customer has taken a free trial previously, on any license, they will fail these check and can be denied further free trials if the platform has been configured to deny free trials depending on FTEC pass/fail.

We use envelopes (which are essentially a hash of 2 or more user data points) as the comparison point. If this comparison point exactly matches a previous instance, the free trial eligibility check will fail.

For example, **CC\_LAST4\_NAME** is a hash string created from the stored data of the customers last 4 numbers of the credit card and the customers full name. If this combination of data points have been previously used to take advantage of a free trial, the FTEC will fail.

if any single one of the below "envelope" checks comes back as previously existing, the FTEC will fail **(the active set of FTEC "envelopes" can be any subset of the below set)**

1. USER\_EXID
2. CONTACT\_EMAIL
3. ADDRESS\_NAME
4. IP\_NAME
5. PAYPAL\_ACCOUNT
6. CC\_LAST4\_NAME

These envelopes translate into:

1. Existing user is system (EXID already used a free trial)
2. Contact Email has previously taken a free trial (this is functionally the same as the EXID check but an extra layer to ensure users are less likely to avoid FTEC)
3. Full name & Billing address&#x20;
4. Full name and IP address &#x20;
5. Paypal account &#x20;
6. Full name & last 4 digits of the credit card&#x20;


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/licences/customer-payment-flows/free-trial-eligibility-checks.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
