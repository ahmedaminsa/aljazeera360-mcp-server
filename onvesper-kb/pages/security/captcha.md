> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/security/captcha.md).

# Captcha

As an additional security layer to reduce the activity of bots and malicious actors against the Vesper purchase flow, a Captcha mechanism is available and is being rolled out for all customers selling Licences on the Vesper platform.

## How does it work?

The captcha provider leveraged by Vesper utilises machine learning and advanced risk analysis to determine if any given request is likely to have been submitted by a bot or a human. A score is given to each request to indicate, on a scale, whether the risk of the given request is high or low.

Vesper's score threshold for risk is being continuously evaluated. It is being set in line with, or more lenient than industry recommendations, in order to ensure there is minimum friction to end-users.

## Which parts of Vesper support Captcha verification?

Captcha is integrated against adding cards to the **payment flow** at present, if you wish to opt-out of this change in the payment flow of your Vesper configuration, please contact your account management team to understand the financial risks.&#x20;

We are exploring increased rollout to other parts of the platform to further protect against malicious actors and increase the session data available for the risk analysis.

## What will my users see?

Vesper has implemented a frictionless captcha system.

No challenges are presented to the end-users, they may observe a small tag indicating that their session is being evaluated for captcha challenge flash onto the screen for a few moments when they add a credit card, but otherwise no changes will be apparent.

<figure><img src="/files/Ob9KVo5W6LHQub35RqCi" alt=""><figcaption><p>Captcha evaluation</p></figcaption></figure>

Bots that attempt to use captcha protected endpoints (e.g. registering a card on the service) will be blocked and prevented from accessing those endpoints.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/security/captcha.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
