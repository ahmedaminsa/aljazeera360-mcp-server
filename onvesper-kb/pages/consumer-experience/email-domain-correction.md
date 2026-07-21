> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/consumer-experience/email-domain-correction.md).

# Email Domain Correction

The Email Domain Correction feature provides real-time suggestions to users who may have misspelled their email address during sign-up, ensuring they can create a valid account.

<figure><img src="/files/kqCdPW0t0Tjsm6gekDj3" alt="" width="563"><figcaption></figcaption></figure>

## How it Works

When a user is entering their email address during the sign-up process, the platform will automatically detect common typos in the email domain (e.g., gamil.com instead of gmail.com). If a potential misspelling is detected, a helpful correction suggestion will appear, allowing the user to select the correct domain with a single tap.

{% hint style="info" %}
Currently available on TV, web and mobile. Roku is not currently supported.
{% endhint %}

{% hint style="info" %}
To enable, please reach out to your platform account manager.&#x20;
{% endhint %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/consumer-experience/email-domain-correction.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
