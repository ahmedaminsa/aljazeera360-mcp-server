> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/consumer-experience/mobile.md).

# Mobile

- [Push Notifications (Firebase)](https://docs.onvesper.com/platform-knowledge-base/consumer-experience/mobile/push-notifications-firebase.md): How to create push notifications through Firebase and test before sending
- [Linking directly to content in mobile apps](https://docs.onvesper.com/platform-knowledge-base/consumer-experience/mobile/linking-directly-to-content-in-mobile-apps.md)
- [Universal Links](https://docs.onvesper.com/platform-knowledge-base/consumer-experience/mobile/linking-directly-to-content-in-mobile-apps/universal-links.md): Open content directly in your app if installed on the user's device
- [Push Notification deeplinks & Custom protocols](https://docs.onvesper.com/platform-knowledge-base/consumer-experience/mobile/linking-directly-to-content-in-mobile-apps/push-notification-deeplinks-and-custom-protocols.md): How to use Firebase to send Deeplinks
- [Creating Dynamic Links](https://docs.onvesper.com/platform-knowledge-base/consumer-experience/mobile/linking-directly-to-content-in-mobile-apps/creating-dynamic-links.md): Firebase links for marketing & social media
- [Smart Banners](https://docs.onvesper.com/platform-knowledge-base/consumer-experience/mobile/linking-directly-to-content-in-mobile-apps/smart-banners.md): Advertising the native applications from mobile web
- [Mobile Apps Ratings](https://docs.onvesper.com/platform-knowledge-base/consumer-experience/mobile/mobile-apps-ratings.md): Encourage users to feedback on positive experiences
- [Data Saver](https://docs.onvesper.com/platform-knowledge-base/consumer-experience/mobile/data-saver.md)
- [RSS Feed](https://docs.onvesper.com/platform-knowledge-base/consumer-experience/mobile/rss-feed.md)
- [Link to Licences](https://docs.onvesper.com/platform-knowledge-base/consumer-experience/mobile/link-to-licences.md): How to create links for mobile applications that direct users to purchase a licence
- [Default Video Orientation](https://docs.onvesper.com/platform-knowledge-base/consumer-experience/mobile/default-video-orientation.md): Expanded control over your playback experience.
- [Section page card sizes](https://docs.onvesper.com/platform-knowledge-base/consumer-experience/mobile/section-page-card-sizes.md): Smaller cards on the Vesper mobile applications


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/consumer-experience/mobile.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
