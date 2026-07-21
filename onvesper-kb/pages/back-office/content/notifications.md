> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/content/notifications.md).

# Promo Notifications

{% hint style="success" %}
The ***Promo Notifications*** feature has been updated, allowing residents to target their in-app messages to specific license holders, countries, or devices.
{% endhint %}

This functionality brings the additional capability for our Residents on the top of [Firebase Notifications ](/platform-knowledge-base/consumer-experience/mobile/linking-directly-to-content-in-mobile-apps/push-notification-deeplinks-and-custom-protocols.md)to reach and engage the audience.&#x20;

Accessible through Back Office under *Content -> Promo Notifications*, this messaging capability enables the display of promotional messages on any devices for *logged-in* users.

<figure><img src="/files/0fsrm7tS1sMhol3EQD3j" alt=""><figcaption></figcaption></figure>

After selecting "Create new message", you can start editing. Similar to the available options for targeting heroes, you can now target *audiences & cohorts*, and allow or block *regions*, *devices*, and specific *licenses:*&#x20;

<figure><img src="/files/IRqLFclNk2DqwOG1hBgo" alt=""><figcaption></figcaption></figure>

Here's an example of a use case that will send a promo message to mobile users in the USA:

<figure><img src="/files/h5FkZ8Xom9QgXGprqfdV" alt=""><figcaption></figcaption></figure>

Once the first page is configured and you click "Next," you will be prompted to set up the message:

<figure><img src="/files/LbAB1Zjz4T0zr3edbq7g" alt=""><figcaption></figcaption></figure>

* **Title:** This function is the main title of the promo message (**Note**: required character limit between 2-64 characters)
* **Description:** Provide further information about the promo message
* **CTA:** The Call To Action is the text on the button that will be included in the promo message (e.g. Click here)
* **Link Through Type:** There are four different types of CTA’s you can use:
  * VOD: Links to a single VOD asset on the platform
  * LIVE: Links to the upcoming live event on the platform
  * PLAYLIST: Links to a playlist or list of videos on the platform
  * EXTERNAL: Links to an external site or link

{% hint style="warning" %}
When "Link Through Type" is set to "EXTERNAL," promo notifications won't display on TV platforms, as they don't support external links.
{% endhint %}

When selecting VOD, LIVE or PLAYLIST in Link Through Type section you will be requested to provide the *Content ID***.**

![](/files/DsJJ6N8VgNsXP19sS7G8)

The *Content ID* is a numeric identifier which can be located at the end of your content's URL. For example, if your content's URL is "[https://myvideoservice/video/289513](<&#xA;https://myvideoservice/video/289513>)", then the Content ID would be *289513* e.g Live stream below&#x20;

![](/files/eBmMSOQO3fxjEuFMQ4qi)

For the External Link Through option, you will be asked to provide an external "URL" value, e.g., a link where end-users can purchase tickets.

* **Active Date Range:** This is the start and end date of the promo message
* **Upload Image:** This is the thumbnail that will appear alongside the promo message sent to customers. It must be 660 x 330 px.
  * To avoid cropping across devices, it is recommended to add 30px clean space around the image (included in the 660 x 330 px)
* **Status:**
  * ACTIVE: Indicates the promo message is live
  * INACTIVE: Indicates the promo message is not live

In the example below, you can see the Promo Notification in the bottom right corner of the website. Enjoy your messages!

![](/files/rOi1NFzKDi91wg1hFRhT)

Please note that you can also clone and edit your existing notifications.

We highly recommend saving the promo notification as *inactive* first, then clicking on "Edit" to review the entire configuration to ensure you are targeting the correct users and devices before setting it as *active*.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/content/notifications.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
