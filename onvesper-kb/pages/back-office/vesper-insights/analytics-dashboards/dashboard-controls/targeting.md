> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/vesper-insights/analytics-dashboards/dashboard-controls/targeting.md).

# Targeting

<figure><img src="/files/2NxlAtxJbBqB5hj9bOqU" alt=""><figcaption></figcaption></figure>

Targets are delivery locations for Segments of user data. Delivery of user data can be one off delivery events, or scheduled to recur at a regular cadence e.g. every hour or every 6 hours or daily during weekends (every Friday, Saturday and Sunday).

<figure><img src="/files/Hx9hMzXMPW51J2bLxmK8" alt=""><figcaption></figcaption></figure>

For a configured target to be public to your team, the underlying segment must also be publicly editable.

<figure><img src="/files/UWfQECZN2KLYFgLoqyih" alt=""><figcaption></figcaption></figure>

Targeting destinations will need to be configured for you by Deltatre. Please contact your CAM/TAM to begin the configuration process.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/vesper-insights/analytics-dashboards/dashboard-controls/targeting.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
