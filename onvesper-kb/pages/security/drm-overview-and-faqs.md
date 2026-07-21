> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/security/drm-overview-and-faqs.md).

# DRM: Overview and FAQs

Endeavor Streaming’s Shield product includes multiple content protection methodologies. The most commonly deployed is Digital Rights Management (DRM)

### **What is DRM?**

DRM is a method of securing digital content to prevent unauthorised use and piracy. It ensures that video content is stored and streamed in an encrypted form. Whatever video player then tries to open and play the video, must have the decryption keys in order to render the video content.&#x20;

### **Do I need DRM?**

DRM is typically used for high value content such as premium sports events and studio level productions. If you are utilising download-to-go and need to ensure that the downloaded video content is encrypted on the user’s device, it is highly recommended. For most other scenarios, it is required only when you have a contractual obligation with the content owner.

### **Does this mean without DRM my content is unprotected?**

No. Endeavor Streaming’s video services transmit data using HTTPS encryption as standard. We also do not list the addresses of videos files or streaming manifest when using the website. Retrieving video content from our system requires being integrated with our APIs, creating an access token using a secret key (unique to each customer), and providing that access token immediately after creation. Access tokens expire within seconds ensuring that they cannot be captured and re-used.

### **Will DRM stop my live content being re-broadcast?**

DRM is not a one stop shop for piracy prevention and should be used in conjunction with other piracy prevention methods such as EXID injection. With DRM, the video content is protected and only authorised video players may access it, but, once the video is being openly played on a computer system, it can be re-captured through a variety of methods. EXID injection is our recommended approach to combat this behaviour.

### **What is the downside of DRM’d content?**

* You cannot clip the DRM protected version of a VOD asset.
* Other features of Digital Video Exchange that rely on viewing video content (such as setting a thumbnail from the video preview) cannot function with DRM encryption.
* Adding DRM protection to any content introduces *significant* complications for Server-Side Advertising, preventing several configurations. We advise against using DRM content if you intend to monetise your content through advertising.
* DRM is not supported today on some Vesper applications (PS4 & PS5).
* Enabling DRM requires additional processing and storage solutions, which will incur additional cost.
* A few platforms cannot support DRM playback, see below.

### **DRM Costs**

Our standard cost structure includes a setup fee as well as an ongoing variable cost at a per event/subscription level.

### List of known players that do not support DRM

* \[Android] Chrome browser, when in an incognito tab. See Google's blog post here: <https://developer.chrome.com/blog/media-updates-in-chrome-62/> for more information and the quote: "Note: Widevine support is disabled in \[Incognito mode] in Android. That way users do not inadvertently lose paid licenses when closing Incognito tabs."


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/security/drm-overview-and-faqs.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
