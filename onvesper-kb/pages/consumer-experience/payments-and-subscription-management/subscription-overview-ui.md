> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/consumer-experience/payments-and-subscription-management/subscription-overview-ui.md).

# Subscription Overview UI

<figure><img src="/files/zLzcYO8FALphb0exO5f2" alt=""><figcaption><p>Current Subscription Details</p></figcaption></figure>

There are various labels that can be included in the Subscription Tab such as:

* Renewal Dates
* Expiry Dates
* Billing Provider
* Licence Pause/Resume Details
* Payments Pending
* Upgrade/Downgrade Details

<table><thead><tr><th width="45.87109375" align="center"></th><th width="227.234375">Label Key</th><th>New Value</th><th>Comment</th></tr></thead><tbody><tr><td align="center">1</td><td>licenseWillExpireOn</td><td>Expires on: {{expiry}}</td><td>User has cancelled licence or licence is set to expire</td></tr><tr><td align="center">2</td><td>licenceWillRenewOn</td><td>Renews on: {{renewal}}</td><td>User has a licence set to renew</td></tr><tr><td align="center">3</td><td>licenceWillExpireTomorrow</td><td>Will expire tomorrow</td><td><p>Confirming this can be updated to:</p><p>Expires on: {{expiry}}</p></td></tr><tr><td align="center">4</td><td>licenceWillRenewTomorrow</td><td>Will renew tomorrow</td><td><p>Confirming this can be updated to:</p><p>Renews on: {{renewal}}</p></td></tr><tr><td align="center">5</td><td>licenceWillExpireToday</td><td>Licence will expire today</td><td><p>Confirming this can be updated to:</p><p>Expires on: {{expiry}}</p></td></tr><tr><td align="center">6</td><td>licenceWillRenewToday</td><td>Licence will renew today</td><td><p>Confirming this can be updated to:</p><p>Renews on: {{renewal}}</p></td></tr><tr><td align="center">7</td><td>paymentPendingInfo</td><td>Payment pending</td><td>User has purchased a licence. This is a temporary state prior to payment being confirmed.</td></tr><tr><td align="center">8</td><td>licencePauseInitiated</td><td>Pauses on: {{date}}</td><td>User has paused licence</td></tr><tr><td align="center">9</td><td>licencePaused</td><td>Resumes on: {{resumeDate}}</td><td>User has resumed licence</td></tr><tr><td align="center">10</td><td>pendingResumeRequested</td><td>Status will update shortly. Please refresh in a few minutes</td><td>User has resumed licence. This is a temporary state prior to payment being confirmed.</td></tr><tr><td align="center">11</td><td>billingRealmName</td><td>Billed through (Realm/Resident)</td><td>Dynamic label updating to where the source of purchase was</td></tr></tbody></table>

&#x20;The ability to display these additional details adds clarity to the user's current subscription purchases. If you wish to have any or all of these labels enabled, please contact your Account Management team.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/consumer-experience/payments-and-subscription-management/subscription-overview-ui.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
