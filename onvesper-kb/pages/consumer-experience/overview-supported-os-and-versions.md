> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/consumer-experience/overview-supported-os-and-versions.md).

# Overview, Supported OS & Versions

This section of documentation will cover specific features or capabilities of the Vesper consumer applications.

Vesper applications can be developed and deployed on the devices and operating systems listed below.

### Mobile

<table><thead><tr><th width="358">Platform</th><th>Minimum Supported OS / device version</th></tr></thead><tbody><tr><td>iOS</td><td>13.0</td></tr><tr><td>Android</td><td>8.0</td></tr><tr><td>Amazon Fire OS</td><td>7.0 (2018+)</td></tr></tbody></table>

### Connected & Smart TVs

<table><thead><tr><th width="358">Platform</th><th>Minimum Supported OS / device version</th></tr></thead><tbody><tr><td>tvOS</td><td>11.2</td></tr><tr><td>Android TV*</td><td>8.0</td></tr><tr><td>Amazon Fire TV</td><td>7.0</td></tr><tr><td>Samsung Tizen</td><td>5.5 (2020)</td></tr><tr><td>LG WebOS</td><td>5.0 (2020)</td></tr><tr><td>Roku</td><td>11</td></tr><tr><td>Hisense VIDAA</td><td>3 (2019)</td></tr><tr><td>VIZIO</td><td>2019 +</td></tr><tr><td>Comcast </td><td>Xfinity Flex, Xumo, Xumo TV, X1</td></tr></tbody></table>

\*Android TV refers to Google certified Android TV devices. If you need to clarify whether a device is a Google certified Android TV, there’s an official list of “Global TV partners” at the bottom of this official page: [Android TV](https://www.android.com/tv/) . Alternatively, you can use this third party site: [Android TV Guide](https://www.androidtv-guide.com/)

### Games Consoles

<table><thead><tr><th width="358">Platform</th><th>Minimum Supported OS / device version</th></tr></thead><tbody><tr><td>Xbox</td><td>Xbox One, Xbox Series (S &#x26; X)</td></tr><tr><td>PlayStation </td><td>PlayStation 5</td></tr></tbody></table>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/consumer-experience/overview-supported-os-and-versions.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
