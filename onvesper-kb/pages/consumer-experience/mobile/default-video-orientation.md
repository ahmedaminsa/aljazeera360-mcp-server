> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/consumer-experience/mobile/default-video-orientation.md).

# Default Video Orientation

We've introduced a  feature that gives you more control over the mobile playback experience for your users. You can  choose whether your videos default to either Portrait or Landscape orientation. Currently, your apps play videos in Portrait mode, but with this  setting, you can ensure your content automatically plays full-screen in landscape on mobile devices.

## How it Works

When a user taps on a video, it will automatically open in the orientation you've selected, providing a seamless and immediate viewing experience.

* If a user plays a video from a hero banner, the video will go straight to full-screen playback. When the user hits the "Back" button, it will take them to the interstitial screen. From there, they will hit "Back" again to return to the home screen.
* If a user plays a video from a row, the player will open in the selected orientation. Hitting the "Back" button will then return them directly to the home screen, since there is no interstitial screen in that specific flow.

{% hint style="info" %}
To enable this change, please reach out to your platform account manager.&#x20;
{% endhint %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/consumer-experience/mobile/default-video-orientation.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
