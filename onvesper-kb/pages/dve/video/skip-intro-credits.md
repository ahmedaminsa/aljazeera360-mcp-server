> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/dve/video/skip-intro-credits.md).

# Skip Intro/Credits

The **Skip Intro/Credits** feature enhance the user experience by allowing viewers to conveniently skip the intro or credits of video content.&#x20;

This page provides detailed instructions on how to manually add and manage skip markers within your content on the [Vesper VOD Platform](https://vod.onvesper.com).

{% hint style="info" %}
For those interested in streamlining this process, we also offer an AI-powered solution that automatically identifies and applies skip markers to content, greatly reducing your manual overhead.\
To explore this option, please reach out to your account management team for further information and pricing options.
{% endhint %}

## Adding Skip Markers manually

**Select your video:**

On the Vesper VOD platform, navigate to and select the video you'd like to add skip markers to.

**Enter Annotate mode:**

Click on the **Annotate Video** button to start editing markers.

<figure><img src="/files/tkJJpQKQxw4HCPhrZLRI" alt=""><figcaption></figcaption></figure>

**Create a marker:**

Click **Create skip intro marker** or **Create Skip Credits marker** to add a marker for the intro or credits respectively.

<figure><img src="/files/QIYQKycrMxAObI4KaC4o" alt=""><figcaption></figcaption></figure>

**Set the Skip marker's parameters:**

Specify the start and end times for the video clip that should be skipped. Use the previews on side to help visualize where in the content the clip will begin and end.

<figure><img src="/files/jZhxNJSB3dGRb00AVFJ9" alt=""><figcaption><p>Set the Skip marker Start/End time</p></figcaption></figure>

**View and Edit markers:**

After saving, the Skip marker will appear as a white bubble on the timeline and in the right sidebar. Clicking on either allows you to edit or delete the skip marker.

<figure><img src="/files/xzX2RFaXJlqhOXeZVyfo" alt=""><figcaption></figcaption></figure>

**Publish your markers:**

Once you're satisfied with the markers, click **Publish** to apply them. The markers will then be displayed during the video playback.

<figure><img src="/files/FUQzaHkZXaoY3HVQ9ELH" alt=""><figcaption></figcaption></figure>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/dve/video/skip-intro-credits.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
