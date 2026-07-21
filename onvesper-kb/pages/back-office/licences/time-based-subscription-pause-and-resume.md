> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/licences/time-based-subscription-pause-and-resume.md).

# Time Based Subscription Pause & Resume

## Introduction

Time-based subscription pause and resume is a feature that allows customers to pause their subscription for a configurable amount of time. This is a powerful tool that will allow you to reduce voluntary churn.

Once enabled, the subscription will be paused at the start of the next billing cycle and will  automatically resume after the pre-determined period. The customer, however, can reactive the subscription at any time. If the customer manually resumes before the time-based pause expires, the customer's renewal date will change to the date the customer manually reactivated.&#x20;

As a resident, you can control where users are presented with this option and for how long thanks to the self-service tools provided in Vesper Back Office.&#x20;

## Configuration

### Configure the pause periods offered

1. Pause periods offered are controlled at a licence level. To enable them, navigate to the licence that should offer the pause periods via Vesper Back Office -> Licences -> Package Licences&#x20;
2. Edit the section “Define Type of Licence“, toggle to “Yes“ on the setting “Enable subscription pause & resume (Web only)”.
3. Once enabled, click the plus icon to add a pause period. The unit must be 'Month'.
4. Confirm and Save.

<figure><img src="/files/lv7ssgUt1kpivWTkz4vm" alt=""><figcaption><p>Enable Subscription Pause &#x26; Resume on Vesper Back Office</p></figcaption></figure>

{% hint style="info" %}
The recommend max number of pause periods offered is 4.
{% endhint %}

### Determine where the pause Call To Action is presented

There are three options for how to offer the pause Call To Action:

| <p>A) On the account page, on the licence card itself next to cancel.</p><p></p> | <img src="/files/vPZA5wYbvSlJGmOxySeR" alt="" data-size="original"> |
| -------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| B) Only after the user has attempted to cancel                                   | <img src="/files/jLT5zkgjAZFCz3SAhXJX" alt="" data-size="original"> |
| C) **Both** A and B                                                              |                                                                     |

Once you've decided which CTA option aligns best with your objective, reach out to your Technical Account Manager and they will enable it for you.

<br>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/licences/time-based-subscription-pause-and-resume.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
