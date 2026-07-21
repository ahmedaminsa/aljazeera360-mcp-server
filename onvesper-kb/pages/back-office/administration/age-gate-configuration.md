> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/administration/age-gate-configuration.md).

# Age Gate Configuration

## Background

An age gate is one tool that can be deployed as part of compliance with local laws regarding minors on online platforms, for example, COPPA in the U.S.

**COPPA** (Children’s Online Privacy Protection Act) is a US law that protects children under the age of 13. Under this law, websites that may have children as users should verify that users are above the age of 13 before collecting any personal information, and should refrain from storing PII or passively tracking any information for users under 13.

## Who Should Use This Feature?

This feature will be most pertinent to:

* Current Residents with content geared toward children
* Current Residents with graphic or adult content
* Current Residents with users in the US&#x20;

## How to Configure&#x20;

Reach out to your Account Management team with the minimum age you wish to apply to your service.&#x20;

The format should be in **years** and **months**. For example, 13 years and 6 months or 13 years and 0 months.&#x20;

To set the age restriction per region, provide your Account Management team with the age restriction per region. If there are no geo-specific age restrictions, it will default to the age limit you decide for all regions.&#x20;

Example:&#x20;

* USA - 13 years, 0 months
* France - 16 years, 0 months
* Rest of World - 10 years, 0 months

## Known Limitations <a href="#end-user-experience" id="end-user-experience"></a>

Age gate configurations are not available for mobile applications (iOS/Android mobile). If you're interested in requesting prioritization of this feature, please reach out to your Account Management team.&#x20;

## End-User Experience <a href="#end-user-experience" id="end-user-experience"></a>

If you input an age that is under the minimum requirement, the end user will receive a generic error message indicating that the platform was not able to create their account.&#x20;

<figure><img src="/files/wBtRVcHHEqR6iKaZjynW" alt=""><figcaption><p>Note that generic error messages are recommended to avoid revealing the minimum age required</p></figcaption></figure>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/administration/age-gate-configuration.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
