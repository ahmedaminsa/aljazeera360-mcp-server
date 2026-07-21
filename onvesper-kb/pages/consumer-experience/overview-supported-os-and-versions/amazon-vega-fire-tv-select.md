> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/consumer-experience/overview-supported-os-and-versions/amazon-vega-fire-tv-select.md).

# Amazon Vega / Fire TV Select

In Q4 2025, Amazon started releasing devices running "Vega OS", a new Fire TV operating system. Those devices are often branded as "Select" Fire TV, for example "Fire TV Select 4k". This is the beginning of their transition away from Android as their operating system of choice for TV devices.

Amazon took the decision to automatically enroll many Vesper apps in their cloud app streaming program, where the Android Fire TV application is run on cloud infrastructure, then streamed back to the Fire TV Select device.

The Vesper team is unable to conduct testing on this device using this program. Our support teams received several reports of issues on the device after Amazon made this unilateral decision.&#x20;

The Vesper platform is designed to be used by real customer (edge) devices, we have tools in place that will block suspicious traffic from servers accessing our platforms. The level of protections depends on your specific content protections for your content on Vesper, but the entire platform will protect itself in the event of access patterns that look suspicious.

Vesper is therefore unable to support the cloud app streaming program, so we have taken the action to opt all residents out of the program.

This decision ensures that (1) we’re operating on hardware we can test and support (2) we do not put our residents in a position that will incur additional cost: Amazon have indicated that at some point in the future they will charge for remaining on this cloud app streaming program.

Deltatre are building support for VEGA OS / Fire TV Select devices. At the time of publication we expect the MVP of that application to be available in Q4 2026.

When VEGA OS support is ready, contact your account management team to discuss releasing on this new operating system.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/consumer-experience/overview-supported-os-and-versions/amazon-vega-fire-tv-select.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
