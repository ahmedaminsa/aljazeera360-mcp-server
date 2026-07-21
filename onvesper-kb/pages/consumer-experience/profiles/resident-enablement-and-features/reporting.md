> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/consumer-experience/profiles/resident-enablement-and-features/reporting.md).

# Reporting

Reporting dashboard can be found under "Insights".&#x20;

### Reporting&#x20;

Reporting has been updated to include reporting on customer (account owner), profile ID, and profile type.

* All Watch Data has been updated to be broken down by profile type (adult vs. kids)
* Underlying Watch Data has been updated to include profile ID, profile type, and whether the profile is the default profile.
* Customer Insights will allow you to identify how many profiles (and how many child profiles) an account has; utilize the List by/Color by function on Total User Profiles or Total User Profiles Child
* All reporting related to subscription management, churn, etc will continue to be reported out on the Customer (Account Owner) level, as payments for services still exist at the account level (not at the profile level)


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/consumer-experience/profiles/resident-enablement-and-features/reporting.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
