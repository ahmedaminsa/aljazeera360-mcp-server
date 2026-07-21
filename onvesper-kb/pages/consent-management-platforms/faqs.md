> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/consent-management-platforms/faqs.md).

# FAQs

## Frequently Asked Questions

<details>

<summary><strong>What is cookie consent?</strong></summary>

Cookie consent is the consent shown to the user before activating cookies and trackers on a website.

It helps uncover hidden website cookies and trackers, configure branded banners and measure and optimize consent rates for maximum opt-ins.

<img src="/files/2gtsnRCiu4J3DuV90ZOG" alt="" data-size="original">&#x20;

&#x20;          *Click the image to enlarge*

</details>

<details>

<summary><strong>What is Cookie Law?</strong></summary>

The Cookie Law was designed to protect online privacy, by making customers aware of how information about them is collected and used online, and give them a choice to allow it or not.

The two biggest laws regarding user privacy are:

* GDPR (European Union and the UK)
* CCPA (US state of California)

</details>

<details>

<summary><strong>What are Geolocation Rules?</strong></summary>

Geolocation rules are conditions that trigger specific consent forms that meet the legal requirements of the user's location. They are used by Consent Management Platforms to ensure compliance no matter where users are coming from.&#x20;

When setting up a cookie banner capturing consent, you can designate the region where the rule is to be used.

</details>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/consent-management-platforms/faqs.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
