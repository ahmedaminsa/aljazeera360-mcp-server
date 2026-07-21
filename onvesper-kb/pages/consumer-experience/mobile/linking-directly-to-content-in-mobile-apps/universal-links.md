> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/consumer-experience/mobile/linking-directly-to-content-in-mobile-apps/universal-links.md).

# Universal Links

Universal Links (as defined by [Apple](https://developer.apple.com/ios/universal-links/)) allow Vesper to seamlessly link to content either on a website, or within the mobile app if the user has it installed.

They work by hosting a small file on the website route domain, that iOS/Android will automatically retrieve, instructing the operating system that your verified mobile application (with a signature) is authorised to open certain website links. If the operating system detects the app is installed, it will offer the end user to open the link using the given app.

On Android, these links are called [Android App Links](https://developer.android.com/training/app-links). As they serve an identical purpose, we refer to both as "Universal Links" throughout Vesper documentation.

One-time setup is required in order to enable universal links. Please contact the B2B helpdesk to start this process if you would like Universal Links enabled for your Vesper instance.

Once they are enabled, any of the supported website addresses will open in the mobile app if a user visits them with their mobile devices' web browser (e.g. Chrome or Safari). Note that "app.exampledomain.com" is just an example, it will be replaced with the address where you host your Vesper web app:

| Address                                    | App location                                                  |
| ------------------------------------------ | ------------------------------------------------------------- |
| app.exampledomain.co&#x6D;**/browse**      | "Browse" section                                              |
| app.exampledomain.co&#x6D;**/epg**         | "EPG" section if configured                                   |
| app.exampledomain.co&#x6D;**/favourites**  | User Favourites                                               |
| app.exampledomain.co&#x6D;**/history**     | User History                                                  |
| app.exampledomain.co&#x6D;**/home**        | The home section of the site                                  |
| app.exampledomain.co&#x6D;**/live/\***     | A given live event, where \* is the live event ID. e.g. 12345 |
| app.exampledomain.co&#x6D;**/news/\*/\***  | A news article, if you are utilising Vesper's RSS news reader |
| app.exampledomain.co&#x6D;**/playlist/\*** | A given playlist, where \* is the playlist ID. e.g. 12345     |
| app.exampledomain.co&#x6D;**/schedule**    | The upcoming events schedule                                  |
| app.exampledomain.co&#x6D;**/search**      | Vesper's search                                               |
| app.exampledomain.co&#x6D;**/season/\***   | A season interstitial page, where \* is the season ID         |
| app.exampledomain.co&#x6D;**/section/\***  | Any content section, where \* is the section name             |
| app.exampledomain.co&#x6D;**/video/\***    | A given VOD asset, where \* is the VOD ID e.g. 12345          |


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/consumer-experience/mobile/linking-directly-to-content-in-mobile-apps/universal-links.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
