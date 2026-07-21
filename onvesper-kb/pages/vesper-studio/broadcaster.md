> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/vesper-studio/broadcaster.md).

# Broadcaster

The Vesper Studio Broadcaster tool allows users to create Virtual Live Linear (VLL) channels powered by existing VOD assets in their DVE catalogue.

To create a new Virtual Live Linear Channel please contact your Technical Account Manager with the following information:

* Channel Name
* Channel Logo&#x20;
* Channel Start Time

Once the channel is create it will populate in your timeline.&#x20;

*Live Now* = Channels that are currently live.&#x20;

*Upcoming* = Channels that will begin at a future date.

![](/files/-MQBoWaY_qP0x7doEjk9)

## Adding Content To A VLL Channel

Once the channel is created it will be available for you to add content. Click on your preferred channel and start adding content.&#x20;

When you click into your content you will see the current timeline and navigational bar that shows what video assets are queued next:

![](/files/-MQBpQlE7Rz4Lmnt92ea)

All content is editable apart from the currently live VOD asset in slot 1. If a content pod is not editable a lock icon will appear at the bottom of the pod.&#x20;

To add new videos to the timeline click the ADD CONTENT button in the top right of the page:

![](/files/-MQBprYqgj_J20xE5fF8)

You can select content to add from the list or by using the search bar.&#x20;

* Searching requires exact match to the title that is within the [DVE](/platform-knowledge-base/dve/overview.md) - titles will not appear if missing accents, exclamation marks etc
* Some episode titles are names, others numbers. Search will only display what is in the asset title.&#x20;

When you have selected the asset you wish to add to the timeline you will be presented with the following information:

![](/files/-MQQcBevxWYjoSIAMtK1)

Listed will be the content information for what you are adding. None of this information is editable within this screen.&#x20;

To add this asset to your timeline click the pod itself and the video will then be added to the end of the timeline.

![](/files/-MQQcdbfX_YPeZNXfwDC)

As illustrated above the asset is now added to your timeline. It is not saved however. In order to complete this step you MUST click Publish. Once published the timeline will be saved. You can add multiple pods of content before saving. Or one at a time, this is up to user preference.&#x20;

To move the order of pods you can use:

* Navigation Arrows in the top left of the pod
* Physical Drag and Drop of the pod itself
* Editing the number in the top left of the pod. By changing this number the pod will move to that exact place in the timeline.

Any changes to the timeline must be Published if you wish to save. If not you can discard the change.&#x20;

To scroll through the timeline itself there are multiple options:

* Use your mouse to scroll left or right
* Click the **`>> button`** at the bottom of the page to go left or right.&#x20;
* **`|<< LIVE`** will bring you back to the currently live pod in the timeline.&#x20;
* **`END >>|`** will bring you to the very end of the scheduled timeline

See Below: Step by step example for adding content to your VLL Timeline

![](/files/-MQRKU-2d-rKnDsc_kZ8)

***Copy and Pasting content in your timeline***

To duplicate content in your timeline click the copy & paste button in the top right of the screen:

![](/files/-MR5eF470uUDTcIIQ8AF)

Once this is clicked your timeline will appear as illustrated below -&#x20;

![](/files/-MR5e_NHErjc_MJWziMK)

You can click your required videos that you wish to copy&#x20;

Once you have selected which content you wish to paste clip Paste To End and this content will now appear at the end of your timeline.&#x20;

Once this is clicked make sure to click Publish or your changes will not be saved.&#x20;

To copy and paste content to another location on the timeline:

Complete the steps above but instead of clicking "Paste to End", navigate to any location between a content pod and click the burger option:

![](/files/-MRUL7-ibDJaSAIpXbdc)

This will offer the option to paste selection here. The selected content will then be pasted to this exact location.&#x20;

**To copy and paste multiple times.**&#x20;

* Click the Copy and Paste Button at the top of the page
* Choose your selection
* Click Paste To End
* If you wish to select more content simply click on more content pods.
* One you are finished - Click Done
* This will collate all the Copy and Paste changes
* To implement on the timeline click Publish

[Linking your VLL channel to your Front End](/platform-knowledge-base/back-office/content/content-management/creating-rows/creating-an-epg-row.md)


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/vesper-studio/broadcaster.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
