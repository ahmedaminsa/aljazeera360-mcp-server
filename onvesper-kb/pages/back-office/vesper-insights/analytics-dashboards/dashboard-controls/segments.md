> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/vesper-insights/analytics-dashboards/dashboard-controls/segments.md).

# Segments

<figure><img src="/files/YcFXz6fyjqaLjh72wThL" alt=""><figcaption></figcaption></figure>

Segments are groupings of filters that allow you to monitor the state/count of users that fall into that particular set of filters at a given time. Segments can be saved and re-applied at any time. Segments can be made public so the rest of your team can load the same set of filters or kept private so they are only viewable/editable by you.

Segments of users can be sent out to a Target for marketing purposes, for example:

* Create segment of all users with more than 30 minutes of view time in the past 7 days
* This segment of users can be pushed out directly to 3rd party marketing tooling such as Google, Meta, Cheetah (on demand or scheduled)
* As users fall into or out of this segment, this can be sent out to the selected 3rd party marketing tooling for comms/targeting specific to these users e.g. sending users who fall into this "high engagement" segment promotional offers for physical merchandise/live ticketing/etc


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/vesper-insights/analytics-dashboards/dashboard-controls/segments.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
