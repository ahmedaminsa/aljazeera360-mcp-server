> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/vesper-insights/data-sync/faq.md).

# FAQ

The data in the view\_session view and DVE/DGE Analytics originates from two different sources. The view\_session data is derived from viewership start and end events produced by the ES platform. On the other hand, DVE/DGE Analytics data is sourced from log records within the CDN which are nothing more than access logs.

Note: We do not recommend comparing view\_session view data with DVE/DGE Analytics, as the latter is not reliable, lacks real-time accuracy, and will not be supported in the future

**If a user watches content, presses pause, then return back to the content does this count as one session or two?**&#x20;

This depends on the how long the user paused their session. If a user pauses then resumes watching the content within 360 seconds, it will be considered as a single session. However, if the user resumes after 360 seconds, it will be recorded as two different view session records with the same session id.

There are no triggers or events saying a video was paused, it is only assumed it was paused or went to ad if the session ended but then resumed within 360 seconds. After 360 second, it is assumed the user stopped and restarted.

Note: In the scenario where a user resumes after 360 seconds, both sessions will still share the same session\_id. However, they will be differentiated by the session\_seq value. The phase before a pause will have session\_seq = 1, and the phase after the pause will have session\_seq = 2. Consequently, although they share the same session\_id, they will account for 2 rows in the view\_session feed, resulting in two separate viewership records being counted towards the total number of views metric.

**How do I compute MAU (Monthly Active Users)?**&#x20;

Experience has told us that different clients have asked to compute MAU different ways. But it always one of 3 methods, each one listed below. You should work with your TAM to determine the best one for you based on the resident’s business model and how you want to measure MAU. In other words, we are quite flexible.

Ex: if you want to know “X number of monthly users that have watched content each month” – then use bullet 3 below

Ex: if you want to know “X visitors each month to the service/site”– then use bullet 1

Ex: if you want to know “X number of active subscriptions” – then use bullet 2

There are 3 ways to determine MAU depending on the resident business model….

1-. For residents with free access to content, no subscription nor registration required – then the MAU would have to be based on users accessing the service (including watching content, and really means visiting the site) which is either done by a guest user granted a token to access or registered user successfully logged in. This is the “Customer Insight” dashboard using the “User Access History” sheet. Or you can use the User Access History feed&#x20;

2-. For residents that provide a subscription based model to watch content – then the MAU can be bullet 1 above if they choose to. OR, they can count the number of Users with an Active Subscription each month. This is the “Subscriber Management” Dashboard. Or you can use the Customer Licence feed

3-. For resident that only want to track MAU based on what users watched content  – they can count the number of Unique Users that watched a single piece of content each month. This is the “All Watch Data” dashboard. Or you can use the View Session feed.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/vesper-insights/data-sync/faq.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
