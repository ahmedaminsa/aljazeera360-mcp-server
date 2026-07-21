> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/consumer-experience/payments-and-subscription-management/apple-and-google-pay-wallets.md).

# Apple and Google Pay (wallets)

Enabled Google and Apple pay options will appear in the checkout flow, allowing your customers to make quick payments.

**Google Pay** allows payments via the webapp using any credit or debit card saved in the user's Google account via the Chrome browser

![](/files/kMM3BbVG3fZ9tfNL24Bc)

**Apple Pay** allows payments via saved credit or debit card in Safari browser (starting with iOS 10 or macOS Sierra)&#x20;

![](/files/a9tsdO090yUvzvG3y3KR)

This feature is available to all residents please get in touch with your Technical Account Manager for more information.

**How to Test:**

**Google Pay:**&#x20;

*Please note that this feature will only appear to the end user when they have enabled payment via their Chrome browser, and have stored payment details in their Google Pay account (also applies to mobile browsers)*

* Using Google Chrome - [<img src="https://support.google.com/favicon.ico" alt="" data-size="line">Fill out forms automatically - Computer - Google Pay Help](https://support.google.com/googlepay/answer/142893?hl=en\&co=GENIE.Platform%3DDesktop)
* Signed in to a Google account in Chrome
* Have saved cards available in that Google account
* Desktop or Mobile web

**Apple Pay:**

*Please note that this feature will only appear to the end user when they have enabled payment via their Safari browser, and have stored payment cards in their Apple Pay account, activated for their current device (also applies to mobile browsers)*

* Using Apple Safari Using Apple Safari - [<img src="https://support.apple.com/favicon.ico" alt="" data-size="line">Pay with Apple Pay in Safari on Mac](https://support.apple.com/en-gb/guide/safari/ibrw8e207504/mac)
* Have Apple Pay/Wallet configured on the device for your account
* Safari Privacy settings set to enable Apple Wallet/Apple Pay
* A biometric device is available and active (Face ID / Touch ID) - A closed Macbook Pro will not have a fingerprint reader active!
* Desktop or Mobile web

<img src="/files/Zkoygtc9AALxc5kHGwEV" alt="" data-size="line"> In addition:

Apple Wallet (or Apple Pay) will only show if your laptop is open.

If your laptop is closed and docked then the finger print reader is disabled. Therefore there’s no biometric authentication available and your Mac responds to websites saying “Nope, there’s no secure payment I can give you in the wallet, Apple pay is not available!”


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/consumer-experience/payments-and-subscription-management/apple-and-google-pay-wallets.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
