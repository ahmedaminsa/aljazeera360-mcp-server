> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/consumer-experience/mobile/section-page-card-sizes.md).

# Section page card sizes

Starting with Vesper App version 6.0.0, Vesper mobile can now be configured to show all cards on a section page in a smaller size than our defaults.

This redesign gives a more modern look to the applications, and allows showcasing more content on a single screen. The horizontal width of all cards will be reduced so each rail shows more content, the vertical height of all rows is also reduced (the amount depends on the rail type being used), which will allow slightly more content to be shown per vertical page

{% tabs %}
{% tab title="Smaller Cards" %}

<div><figure><img src="/files/KF9LspTuNSVcKhzOc4uJ" alt=""><figcaption></figcaption></figure> <figure><img src="/files/aUsCleJRtMwdZy9VH1t2" alt=""><figcaption></figcaption></figure> <figure><img src="/files/Tcxof1Vavm2LFSt3TO4F" alt=""><figcaption></figcaption></figure></div>
{% endtab %}

{% tab title="Default Card size" %}

<div><figure><img src="/files/Uau0DK8RyLPQctzPOB4d" alt=""><figcaption></figcaption></figure> <figure><img src="/files/eTLLjJc8p1livAWReENj" alt=""><figcaption></figcaption></figure> <figure><img src="/files/xXAttvLwNPLK5zlhbUvH" alt=""><figcaption></figcaption></figure></div>
{% endtab %}
{% endtabs %}

\*Note both **smaller** and **default** screenshots above were captured on an Android device set to the smallest possible font size and maximum screen real estate. Card and font sizes in Vesper apps will change according to the device or user's screen display scaling options set in their iOS or Android device settings.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/consumer-experience/mobile/section-page-card-sizes.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
