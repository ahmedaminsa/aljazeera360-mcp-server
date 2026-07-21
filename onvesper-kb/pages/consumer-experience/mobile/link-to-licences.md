> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/consumer-experience/mobile/link-to-licences.md).

# Link to Licences

Note: This feature should be discussed with your technical account manager for assistance in enablement and initial configuration

The deep-linking feature provides three distinct options to streamline customer interaction with licenses.

**Direct License Link**: Link to a single licence directly (e.g., `dicemobile://licence?licenceId=[37]`), simplifying navigation.\
**Deep-linking option no.1 only allows one licence to be displayed at a time.**

<div align="left"><figure><img src="/files/Wr3QwQ8spV4UzQrTU5pe" alt="" width="188"><figcaption></figcaption></figure></div>

\
**Direct Purchase Trigger**: Enables the purchase flow for a single license immediately (e.g., `dicemobile://licence/buy?licenceId=[24]`), bypassing intermediate steps. Adding `buy?` parameter to the url will immediately trigger the purchase overlay on both iOS and Android devices.\
**This only allows one licence to be displayed at a time.**

<div align="left"><figure><img src="/files/kGrkjSuAbs2TKHYH8PRJ" alt="" width="188"><figcaption></figcaption></figure></div>

**License Group Link**: Supports linking to multiple licenses (e.g., `dicemobile://licence?licenceId=[2020,967,862]`), displaying several licenses at once.\
**This allows more than 1 licence to be displayed at a time, but it does not support** `?buy` **parameter.**

<div align="left"><figure><img src="/files/2IeW38lzO4aWvQXEWP8u" alt="" width="188"><figcaption></figcaption></figure></div>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/consumer-experience/mobile/link-to-licences.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
