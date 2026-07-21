> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/consumer-experience/mobile/mobile-apps-ratings.md).

# Mobile Apps Ratings

Mobile apps include a method to let users to rate the app experience and performance. The prompt is intended to gather positive feedback and increase your ranking in the relevant app stores.

We include two different prompts, the positive reaction forwards the user to the App Store (iOS)/Google Play App Store (Android) to rate the app there. This is how those popups work:

1. ***“Do you like the app”*** popup:
   * Implemented by Endeavor. We can call it *"Feedback"* popup
   * This popup is displayed after the user collects 100 “interaction points”
     * 1 point is rewarded for each screen view, interaction, etc
     * User can only collect 50 points a day
   * Feedback: user can give a *thumbs up* or a *thumbs down*
   * A *Thumbs up* will send the user to the Review Popup
2. ***“Review"*** popup:

   * This is the *native* App Store (iOS)/Google Play App Store (Android) rating review
   * User is redirected to the store when he reaches 100 points and the *"Feedback"* popup is displayed AND the user gives a *thumbs UP*
   * Feedback: user can give *up to 5 starts* and add a *comment*

   <figure><img src="/files/k8oeXQevdDoEyCgtoRgk" alt=""><figcaption><p>Review popup for iOS Store</p></figcaption></figure>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/consumer-experience/mobile/mobile-apps-ratings.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
