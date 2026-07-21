> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/content/plugins/iframe-specifications.md).

# iFrame Specifications

**Build Specification**

Since you, or a third-party, can build the experience you wish to add to your product via an iFrame Plugin, there are certain configurations that we would recommend in order to get the best experience

**CORS (Cross-origin resource sharing)**

It is not possible to simply use any website as an iFrame. Only pages with the below considered will be possible to use within an iFrame Plugin:

* The server serving the URL of the iframe should allow the URL to be served as an iframe on the app domain, for example, through the [Content-Security-Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy) or [X-Frame-Options](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options) headers
* No “[iframe busting](https://en.wikipedia.org/wiki/Framekiller)” mechanism in the iframe, or whitelist the app domain explicitly

**Styling**

* We respect the background colour of the iFrame view - so it is worth ensuring that the page built matches the Background Colour of the application (typically black, but not always).
* On **Mobile**, the Sidebar takes up roughly 40% of the screen when opened. This will mean the available space varies by application (Larger devices will naturally have a larger viewspace).

&#x20;

As an ***indicative*** guide in terms of pixels this would result in the following initial view spaces:

* **Landscape:**

  * iPhone 12: 400x325px (the vertical area is scrollable)
  * iPhone 8: 315x340px (the vertical area is scrollable)

  <figure><img src="/files/xi6niwCdRAbER0z9omQd" alt=""><figcaption><p>Landscape Viewspace Example</p></figcaption></figure>

* **Portrait:**

  * iPhone 12: 390x470px (the vertical area is scrollable)
  * iPhone 8: 375x370px (the vertical area is scrollable)

  <div data-full-width="false"><figure><img src="/files/uy2o61QG8twHEXohxwa6" alt="" width="375"><figcaption><p>Portrait Viewspace example</p></figcaption></figure></div>

* For **Web** Applications:

  * Landscape (only): 800x1000px \*note this will depend on the users browser window size.

  <figure><img src="/files/SMG3JhlUsAM1kZNpHD3c" alt=""><figcaption><p>Web Viewspace Example</p></figcaption></figure>

{% hint style="info" %}
Note: The above pixel values are an indication of the sizes available - you should ensure that the plugins you use/design are responsive to accommodate a variety of device sizes.
{% endhint %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/content/plugins/iframe-specifications.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
