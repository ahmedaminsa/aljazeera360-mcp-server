> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/consumer-experience/theming-and-customisation/checkout-and-account-page-customisation.md).

# Checkout & Account page Customisation

{% hint style="info" %}
Customisation options only apply to the web app  (Checkout & Sign up & Account screens)
{% endhint %}

Like individual [Licence Card Configuration](/platform-knowledge-base/back-office/licences/licence/licence-card-configuration.md), you are able to customise the background that will be shown during your checkout and account page experience.

## Key Capabilities

* Consistent Brand Experience: The background of the entire web checkout and sign-up flow seamlessly matches your brand's identity.&#x20;
* Optimal Readability: The configurable *Image Opacity* ensures that any background images do not interfere with text, labels or form fields making the process more accessible.&#x20;
* Enhanced Loading Reliability: By providing a *background colour* as a fallback layer, the customer never encounters a blank or broken background, even if the primary image fails to load quickly.&#x20;
* Visually Engaging Design: Customers benefit from background options like repeating image tiles, static background images (fixed scrolling) and subtle *Gradient overlays* that make the sign up steps feel more modern and engaging.&#x20;

<figure><img src="/files/edpBDvcDSAzxySI6q1za" alt=""><figcaption><p>A simple dark colour, and dark scheme applied to the account page, with licence cards still showing in white (this can be edited in licence card configuration)</p></figcaption></figure>

## Checkout/Purchase Page

This is the content shown to users at the webapp's /signup or /purchase page.

### Design Options & Making changes

To customise your checkout flow background, provide any of the following options to your Account Manager:

| Option                | Description                                                                        | Values / Behaviour                                            |
| --------------------- | ---------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| **Background Colour** | Hex/RGB colour applied as background or fallback                                   | Any valid colour code                                         |
| **Background Image**  | Image uploaded or linked via realm settings                                        | JPG, PNG, WEBP formats supported                              |
| **Image Fill Style**  | Defines how the image is applied within the background                             | Fixed (content scrolls over) / Repeat (image tiles down page) |
| **Image Opacity**     | Controls transparency of background image relative to colour                       | Range: 0% (transparent) – 100% (fully visible)                |
| **Gradient Overlay**  | Optional gradient overlay that sits between background colour and background image | Configurable start/end colour + direction                     |

### Known Behaviour & Constraints <a href="#known-behaviour-and-constraints" id="known-behaviour-and-constraints"></a>

* Background image and colour configuration applies only to **checkout and sign-up flow backgrounds**, not to buttons or form elements.
* If both colour and image are configured:
  * The colour serves as the fallback layer.
  * The image overlays the colour with configurable opacity.
* Gradient overlays apply consistently across the flow.
* Text or UI element theming is not part of this configuration and must be handled separately.

## Account Page

This is the content shown to users at the webapp's /account page. Customisations made here will apply to all sections of the account page (e.g. "subscriptions", "account details" "preferences" etc)

Want to further customise the account page? use the dynamic menu system [Account Menu](/platform-knowledge-base/back-office/administration/menu-items/account-menu.md) to configure the options which are shown in the menu.

### Design Options & Making changes

To customise your account page background, provide any of the following options to your Account Manager:

| Option                              | Description                                                                        | Values / Behaviour                                                |
| ----------------------------------- | ---------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| **Background Color**                | Hex/RGB colour applied as background or fallback                                   | Any valid colour code                                             |
| **Background Image**                | Image uploaded or linked via realm settings                                        | JPG, PNG, WEBP formats supported                                  |
| **Image Fill Style**                | Defines how the image is applied within the background                             | *Fixed* (content scrolls over) / *Repeat* (image tiles down page) |
| **Image Opacity**                   | Controls transparency of background image relative to colour                       | Range: 0% (transparent) – 100% (fully visible)                    |
| **Account Page Text Colour Scheme** | Determines text contrast for readability                                           | Light scheme (black text) / Dark scheme (white text)              |
| **Gradient Overlay**                | Optional gradient overlay that sits between background colour and background image | Configurable start/end color + direction                          |
| **Sub-section Backgrounds**         | All account page subsections share the same background                             | Always inherits configured background                             |
| **Header Styling**                  | Header remains fixed with realm background colour                                  | Not configurable beyond realm colour                              |

### Known Behaviour & Constraints <a href="#known-behaviour-and-constraints" id="known-behaviour-and-constraints"></a>

* Background image **does not extend to side menu**; only background colour applies there.
* The **header** always uses the **realm background colour** and cannot be overridden with an image.
* If both colour and image are configured:
  * The colour serves as the fallback layer.
  * The image overlays the colour with configurable opacity.
* Text mode (light/dark) applies **globally** across all account page sections.
* Background configuration applies consistently across **all account page sub-sections** (e.g., account settings, payment details).


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/consumer-experience/theming-and-customisation/checkout-and-account-page-customisation.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
