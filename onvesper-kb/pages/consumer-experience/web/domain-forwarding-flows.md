> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/consumer-experience/web/domain-forwarding-flows.md).

# Domain Forwarding Flows

When an end user navigates to a resident URL, the experience can vary depending on the desired navigation flow.

#### Scenario 1 - End User always lands on resident landing page

In this flow, when the user navigates to the resident URL, the user reaches the resident controlled landing page. This can allow for a more marketing oriented user experience where the user is obligated to pass through a page before reaching the Vesper Web application **regardless of authentication status.**

<figure><img src="/files/79nvkfATQAH2AOoO18bt" alt=""><figcaption><p><br><mark style="background-color:orange;"><strong>Unauthenticated users destination can be specified, i.e. /home for guest access residents, /login or /signup or an external URL such as the landing page</strong></mark></p></figcaption></figure>

#### Scenario 2 - Dynamic Authentication status forwarding

In this flow, when the user navigates to the resident URL, the users authentication status is checked immediately by the Vesper Web application. The Vesper Web application will then forward the user to their appropriate desination. This allows for less friction to already authenticated users in their journey to access content and has no impact to the unauthenticated user journey. **This scenario requires that the resident autoforward requests to their URL directly into the Vesper Web application controlled subdomain URL to allow authentication status checking to take place.**

<figure><img src="/files/iYwE5gKlbGnrmFqL7IK7" alt=""><figcaption><p><br><mark style="background-color:orange;"><strong>Unauthenticated users destination can be specified, i.e. /home for guest access residents, /login or /signup or an external URL such as the landing page</strong></mark></p></figcaption></figure>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/consumer-experience/web/domain-forwarding-flows.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
