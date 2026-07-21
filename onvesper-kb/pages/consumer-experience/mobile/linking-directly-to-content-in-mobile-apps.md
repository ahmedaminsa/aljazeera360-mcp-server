> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/consumer-experience/mobile/linking-directly-to-content-in-mobile-apps.md).

# Linking directly to content in mobile apps

There are three systems that can be used to link directly to content in Vesper mobile applications.

1. [Universal Links](/platform-knowledge-base/consumer-experience/mobile/linking-directly-to-content-in-mobile-apps/universal-links.md) (preferred & recommended)
2. [Custom protocol](/platform-knowledge-base/consumer-experience/mobile/linking-directly-to-content-in-mobile-apps/push-notification-deeplinks-and-custom-protocols.md#app-deep-link-options) links (used in [Push notifications](/platform-knowledge-base/consumer-experience/mobile/push-notifications-firebase.md))
3. Firebase [Dynamic links](/platform-knowledge-base/consumer-experience/mobile/linking-directly-to-content-in-mobile-apps/creating-dynamic-links.md) (deprecated by Google in 2025)

We recommend reading our documentation on each link above, but we will highlight when you might want to use each link type below:

### Universal Links

The preferred approach by the majority of the app development industry. Use them if you want to allow customers to use your native mobile app whenever they come across a link to your service on the open web. Universal links work great with social sharing, where a customer sends a message to a friend with a link to your service, the recipient can open the link directly in their app if installed.

### Custom protocol Links

Should only be used for push notifications. It is possible to use them with other mobile applications, however this requires development effort from the other [application developers](/platform-knowledge-base/consumer-experience/mobile/linking-directly-to-content-in-mobile-apps/push-notification-deeplinks-and-custom-protocols.md#using-custom-protocol-links-from-other-apps). They are not suitable for use on the open web.

### Firebase Dynamic Links

These are mostly replaced now by Universal Links across the industry. Which has led to Google chosing to deprecate them in 2025.

Their primary purpose was to drive app installs. The service allowed the use of a single web link that could detect if the user had the app installed, and then on a per-link basis, decide whether to send them to the relevant App Store or the website if the app wasn't installed. Firebase Dynamic links could also attribute app installs (with limited success) to those clicks, making them a useful marketing tool for measuring conversion.

#### **Why are Google deprecating this feature?**

Our best insight would suggest this is primarily because Apple have made it much more difficult to attribute app installs to web links and traffic. Coupled with the cost of maintaining this service that was offered for free.

If you're interested in Endeavor Streaming building a replacement service, please submit a Feature Recommendation or discuss with your Account Manager.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/consumer-experience/mobile/linking-directly-to-content-in-mobile-apps.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
