> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/content/content-management/creating-rows/live-event-rows-and-tournament-filter.md).

# Live Event Rows and Tournament Filter

Within Back Office Content managers have the ability to use "Live (events only)" content type to create rows which will display Live events while excluding Live linear channels.&#x20;

This includes two Live content type options which is displayed below.

<figure><img src="/files/OJ4BkOPQZWEIUHv3UrE2" alt=""><figcaption></figcaption></figure>

**Live (events + channels)**&#x20;

The first option highlighted above "Live (events + channels)" provides the capability to create rows which will display both live events and live linear channels.

**Live (events only)**&#x20;

The second option highlighted above displays the content type option which provides the capability to create rows which will only display live events.

**Tournament Filter**&#x20;

Content managers have the ability to use the Tournament filter which can be found when selecting the "Live (events only)" option as displayed below.

<figure><img src="/files/OLHp3HfE4e0PdsnaKyaJ" alt=""><figcaption></figcaption></figure>

Choosing a tournament will create a row that shows only events from that tournament. For example, it can be used to have a section page for a specific tournament, showing only upcoming and/or live events for that tournament.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/content/content-management/creating-rows/live-event-rows-and-tournament-filter.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
