> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/licences/gifting.md).

# Gifting

## Overview <a href="#overview" id="overview"></a>

{% hint style="warning" %}
Gifts can be purchased by guest users and registered users. Registered users, however, **will not be able to redeem a gift for a** [**license within a family**](/platform-knowledge-base/back-office/licences/licence/licence-family-architecture-and-upgrades-downgrades.md) **they already have a purchased license on.**&#x20;
{% endhint %}

## Configuration&#x20;

#### 1. Background Image

Provide a background image to your Account Management team that gifters will see when selecting a license to gift. &#x20;

Suggested size: 1920x1080 jpg

<figure><img src="/files/qmn5W2yg2d06vsBSNUSC" alt=""><figcaption><p>Example background image</p></figcaption></figure>

#### 2. Configure Purchasable/Paid Licenses&#x20;

[Create](/platform-knowledge-base/back-office/licences/licence/creating-a-licence.md) a paid subscription license in Vesper Backoffice.&#x20;

Note: all purchasable licenses will pull through to the gifting checkout screen.&#x20;

#### 3. \[Optional] Update Gifting labels &#x20;

Vesper supports additional labels to customize the gifting experience. Below are the labels Endeavor can customize to reflect the voice of your brand.&#x20;

| Gifting Label                          | Default text                                                                                     |
| -------------------------------------- | ------------------------------------------------------------------------------------------------ |
| **giftPickerDescription**              | *Simply select a licence, choose the duration, tell us who you want to send it to and checkout.* |
| **giftPageTitle**                      | *Gift a license today!*                                                                          |
| **selectCountryGift**                  | *Recipient Country*                                                                              |
| **selectGiftDuration**                 | *Select Duration*                                                                                |
| **noteOptional**                       | *Note (Optional)*                                                                                |
| **recipientEmai**l                     | *Recipient email*                                                                                |
| **alternativeAuthenticationSeparator** | *or (for continuing as a guest or login option)*                                                 |
| **alreadyHaveAnAccountSignIn**         | *Already have an account? Sign in*                                                               |
| **CONTINUEASGUEST**                    | CONTINUE AS GUEST                                                                                |

#### 4. \[Optional] Add a "Gift" menu item via Dynamic Menu System

Once Gifting is enabled, the gifting URL is hidden until it is displayed as a menu item. Create a menu item via the [dynamic menu system ](/platform-knowledge-base/back-office/administration/menu-items.md)so end users can easily navigate to the gifting page.

<figure><img src="/files/yWWY8nc7jh39ZT4WVG3I" alt=""><figcaption><p>Example of a Gift section added as a menu item</p></figcaption></figure>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/licences/gifting.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
