> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/security/drm-overview-and-faqs/multi-key-drm-support-for-live.md).

# Multi Key DRM Support for LIVE

Multi key DRM allows you to encrypt different tracks in a stream with different keys, providing enhanced security. Multi key DRM is available on live content only. It can be applied at an event, tournament or realm level.

The presence of hardware DRM support will vary based on device manufacturers, device age and installed drivers/firmware. The table below assumes that the device itself is capable of Hardware DRM decryption, and outlines only potential software limitations. Note that lack of hardware support is most likely to be an issue on older, or misconfigured, Windows & Android devices

If the playback device does not meet the requirements for most secure DRM playback customers on those devices will see the streams in 504p (SD)

[Browser](#browser-web-mobile)\
\
[Native Apps](#apps)

#### **BROWSER (WEB/MOBILE)**

| **MacOs**   | **Max Support** | **Notes**                                                                                              |
| ----------- | --------------- | ------------------------------------------------------------------------------------------------------ |
| Safari      | 1080p           | <p><br></p>                                                                                            |
| Chrome      | 504p            | <p><br></p>                                                                                            |
| Firefox     | 504p            | <p><br></p>                                                                                            |
| **Windows** | <p><br></p>     | <p><br></p>                                                                                            |
| Chrome      | 504p            | <p><br></p>                                                                                            |
| Firefox     | 504p            | <p><br></p>                                                                                            |
| Edge        | 1080p\*         | <p><br>Requires back end infrastructure updates, please confirm with your TAM/Ops team for support</p> |
| **iOS**     | <p><br></p>     | <p><br></p>                                                                                            |
| Safari      | 1080p           | <p><br></p>                                                                                            |
| Chrome      | 1080p           | <p><br>Chrome on iOS is a reskinning of the Safari browser engine, so retains equal support</p>        |
| **Android** | <p><br></p>     | <p><br></p>                                                                                            |
| Chrome      | 504p            | <p><br></p>                                                                                            |
| **Airplay** | <p><br></p>     | <p><br></p>                                                                                            |
| Apple TV    | 1080p           | 6.6Mbps                                                                                                |
| MacBook     | 1080p           | 6.6Mbps                                                                                                |
| Roku        | 1080p           | 6.6Mbps                                                                                                |

<br>

#### **NATIVE APPS** <a href="#apps" id="apps"></a>

| iOS                | <p><br></p> | <p><br></p>    |
| ------------------ | ----------- | -------------- |
| Android            | 1080p       | <p><br></p>    |
| Fire TV            | 1080p       | <p><br></p>    |
| Android TV         | 1080p       | <p><br></p>    |
| Apple TV           | 1080p       | <p><br></p>    |
| Samsung (Tizen) TV | 1080p       | <p><br></p>    |
| LG TV              | 1080p       | <p><br></p>    |
| Panasonic          | 504p        | <p><br></p>    |
| Hisense            | 1080p       | <p><br></p>    |
| Chromecast         | 1080p       | Gen 1 - 504p   |
| Roku               | -           | <p><br></p>    |
| Xbox               | -           | No DRM Support |
| PS4                | -           | <p><br></p>    |
| PS5                | -           | <p><br></p>    |


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/security/drm-overview-and-faqs/multi-key-drm-support-for-live.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
