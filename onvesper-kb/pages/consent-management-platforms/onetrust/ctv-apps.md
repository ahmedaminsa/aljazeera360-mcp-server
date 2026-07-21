> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/consent-management-platforms/onetrust/ctv-apps.md).

# CTV Apps

{% hint style="info" %}
This guide is intended to assist you with the initial setup of OneTrust Cookie Banner, a product not owned or operated by Endeavor Streaming. While we strive to ensure the accuracy and relevance of the information provided based on our experience with the product, you should consult the official documentation provided by OneTrust or contact their customer support for detailed instructions, updates and additional support.
{% endhint %}

## Add CTV Apps

Once cookie categorizations, consent settings, geolocation rules, and templates have been configured to your organization’s policies, you will add in your CTV apps.

Follow the below steps within the OneTrust dashboard.

| Action                                                                                                                                                                                                       | Visual                                                              |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------- |
| <ol><li><p>Navigate back to the OneTrust home screen and select CTV Apps under “Digital Properties” to add your individual CTV apps.</p><ul><li>Menu → OTT & CTV Consent → Add CTV Apps</li></ul></li></ol>  | <img src="/files/f5wbQYidYDfO4Iu6BZLV" alt="" data-size="original"> |
| <ol start="2"><li><p>Enter details CTV App Name (ie Endeavor Streaming Roku), Platform (Roku, FireTV, etc), Organization.</p><ul><li>Note: Scanning is not supported for all CTV devices</li></ul></li></ol> | <img src="/files/b7qQcKeAMllgWlUttqaL" alt="" data-size="original"> |
| <ol start="3"><li>The newly created CTV configuration will be available under “CTV Apps”</li></ol>                                                                                                           | <img src="/files/jBgE62naVX9LYfs0qlGq" alt="" data-size="original"> |

## Publish SDK

After you have entered in the configurations for all of your required CTV devices, you will publish the devices' SDKs and pass pertinent information to Endeavor Streaming to complete the OneTrust integration.

| Action                                                                                                                                                                                                                                                                                                                           | Visual                                                              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| <ol><li><p>Navigate back to the OneTrust home screen and select SDKs under “Integration”</p><ul><li>Menu → Integrations → SDKs</li></ul></li></ol>                                                                                                                                                                               | <img src="/files/dg6mAjh3iaWyD4WQD6L1" alt="" data-size="original"> |
| <ol start="2"><li><p>Click on the Name of the Device and click “Publish” to begin the process.</p><ul><li>Select API Version (Please contact your Endeavor Streaming Project Manager or Platform Account Manager for which version to use)</li><li>Note: OneTrust will remove versions older than 12 months.</li></ul></li></ol> | <img src="/files/K3EgOPwtRXAnqxkOyJs4" alt="" data-size="original"> |
| <ol start="3"><li>Toggle additional parameters (ie, Publish individual languages, enabling re-consent toggles, etc) if necessary, based on your organization’s requirements.</li></ol>                                                                                                                                           | <img src="/files/3HwHIa0jJI5vU05QqDfd" alt="" data-size="original"> |

4. Select Publish Production SDK

## **Hand-off to Endeavor Streaming PAM for additional configuration** <a href="#id-7.-hand-off-to-endeavor-streaming-pam-for-additional-configuration" id="id-7.-hand-off-to-endeavor-streaming-pam-for-additional-configuration"></a>

The following information will need to be provided to your Deltatre representative to complete integration:

1. **Device** (ie, Roku, LG, Android TV, etc)
2. **App ID**
   1. Provide the Test and Published SDK for the device, ie
      1. ***Test CTV App ID:** 01926bf4-84bf-7a90-972d-866c52b706b1-test*
      2. ***CTV App ID:** 01926bf4-84bf-7a90-972d-866c52b706b1*
3. **CDN/Source URL**, ie **CDN Location:** [cdn.cookielaw.org](http://cdn.cookielaw.org/)
4. **Consent ID**; corresponds to the Cookie categorization selected earlier in the process:
   1. Strictly Necessary Cookies (C0001)
   2. Performance Cookies (C0002)
   3. Functional Cookies (C0003)
   4. Targeting Cookies (C0004)
   5. Social Media Cookies (C0005)
5. **SDK Version**: the software version selected during the Publishing step, ie 202407.2.0

<figure><img src="/files/BwqJXlOy3pswaieLVinu" alt=""><figcaption></figcaption></figure>

<br>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/consent-management-platforms/onetrust/ctv-apps.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
