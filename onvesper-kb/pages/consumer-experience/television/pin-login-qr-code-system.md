> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/consumer-experience/television/pin-login-qr-code-system.md).

# Pin login/QR code system

## Overview

Pin login/QR code allows for a seamless sign up & login experience on **TV applications**. It grants a quicker approach to authenticating user credentials on a TV by sparing users from manually inputting a username and a password via a remote controller: end users can enter a pin code via a browser on a desktop device or scan a QR code to input their login details via a browser on a mobile device instead.

This feature can be used in combination with 'traditional' login mode where users can manually enter their details directly on the TV or it can be used as the sole method of authentication on a TV application.&#x20;

## Authentication availability

Pin login is implemented across any enabled authentication provider within your streaming service:

* Dice ID
* Open ID Connect SSO
* Social login (Facebook, Google, Apple)

## Configuration

Should you choose to enable pin login for your TV applications, your account management team will configure the below settings on your behalf:

* **Duration of the pin code** - Sets the time for which the PIN will be active and available for authentication use
  * Default duration is `5` minutes
  * Can be changed to last `x` minutes or `x` hours
* **Delay** - Sets the duration of the delay in which TV will wait before completing authentication
  * Default delay is `1` second
  * Can be changed to a delay between `1` and `59` seconds, both inclusive
* **Pin Length** - Sets the length of the pin that the end-user will input to complete authentication
  * Default pin length is `6` integers
  * Can be changed to a length between `3` and `15` integers, both inclusive


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/consumer-experience/television/pin-login-qr-code-system.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
