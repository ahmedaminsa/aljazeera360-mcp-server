> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/consumer-experience/profiles/resident-enablement-and-features/user-preferences.md).

# User Preferences

To access this section navigate to;&#x20;

1. Administration&#x20;
2. User Preferences (If this option isn't available, please reach out to you Technical Account Manager).&#x20;

**Subtitle and Audio Language Preferences**&#x20;

As part of this capability, we’ve also built the ability for end-users to select their Audio and Subtitle Language preferences on their profile.

Residents can select which language options they wish to appear for end-user selection.

#### Resident Enablement <a href="#resident-enablement" id="resident-enablement"></a>

Once exposed at the Realm level (please ask your TAM), the Resident can turn on and set which Audio and/or Subtitle Languages they wish to appear for end-user selection.

If disabled, the preferences available for selection by the end-user will default to the languages set up within the Realm. It is highly recommended that Resident’s utilize this feature when enabling User Profiles to ensure all priority subtitle and audio languages are made available under user preferences.

<figure><img src="/files/98UGsjK406vkBsf15Ong" alt=""><figcaption></figcaption></figure>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/consumer-experience/profiles/resident-enablement-and-features/user-preferences.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
