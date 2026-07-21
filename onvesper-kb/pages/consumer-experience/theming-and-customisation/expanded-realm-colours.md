> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/consumer-experience/theming-and-customisation/expanded-realm-colours.md).

# Expanded Realm Colours

The Expanded **Realm Colours** feature allows realms to override the default platform colour scheme for CTAs and menus. Admins can configure device-specific colours for primary and secondary CTAs, as well as menu text states, to align the platform experience with realm branding.

Updating these new colours can be performed by your Account Management team, or by raising a ticket into the B2B helpdesk.

If you wish to update a colour, please quote the name shown in the table below, and provide your new preferred colour(s) in hex code format (e.g. #ffffff for white)

{% hint style="warning" %}
At time of publishing, changes to these colours may not immediately appear on Mobile & TV apps, and require a future update or rebuild to be visible.
{% endhint %}

| Colour Name                | Web                                                                  | Mobile                                                               | TV                                                  |
| -------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | --------------------------------------------------- |
| Primary CTA Default        | <ul><li>Hero</li><li>Interstitial</li><li>Featured Row CTA</li></ul> | <ul><li>Hero</li><li>Interstitial</li><li>Featured Row CTA</li></ul> | <ul><li>Hero</li><li>Interstitial</li></ul>         |
| Primary CTA Default Text   | <ul><li>Hero</li><li>Interstitial</li><li>Featured Row CTA</li></ul> | <ul><li>Hero</li><li>Interstitial</li><li>Featured Row CTA</li></ul> | <ul><li>Hero</li><li>Interstitial</li></ul>         |
| Primary CTA Hover          | <ul><li>Hero</li><li>Interstitial</li><li>Featured Row CTA</li></ul> | N/A                                                                  | N/A                                                 |
| Primary CTA Focus          | <ul><li>Hero</li><li>Interstitial</li><li>Featured Row CTA</li></ul> | N/A                                                                  | <ul><li>Hero</li><li>Interstitial</li></ul>         |
| Primary CTA Hover Text     | <ul><li>Hero</li><li>Interstitial</li><li>Featured Row CTA</li></ul> | N/A                                                                  | N/A                                                 |
| Primary CTA Focus Text     | N/A                                                                  | N/A                                                                  | <ul><li>Hero</li><li>Interstitial</li></ul>         |
| Secondary CTA Default      | <ul><li>Hero</li><li>Interstitial</li></ul>                          | <ul><li>Hero</li><li>Interstitial</li></ul>                          | <ul><li>Hero</li><li>Interstitial</li></ul>         |
| Secondary CTA Default Text | <ul><li>Hero</li><li>Interstitial</li></ul>                          | <ul><li>Hero</li><li>Interstitial</li></ul>                          | <ul><li>Hero</li><li>Interstitial</li></ul>         |
| Secondary CTA Hover        | <ul><li>Hero</li><li>Interstitial</li></ul>                          | N/A                                                                  | N/A                                                 |
| Secondary CTA Hover Text   | <ul><li>Hero</li><li>Interstitial</li></ul>                          | N/A                                                                  | N/A                                                 |
| Secondary CTA Focus        | N/A                                                                  | N/A                                                                  | <ul><li>Hero</li><li>Interstitial</li></ul>         |
| Secondary CTA Focus Text   | N/A                                                                  | N/A                                                                  | <ul><li>Hero</li><li>Interstitial</li></ul>         |
| Menu Text                  | <ul><li>Primary menu</li></ul>                                       | <ul><li>Primary menu</li></ul>                                       | <ul><li>Primary menu</li><li>Account menu</li></ul> |
| Menu Hover Text            | <ul><li>Primary menu</li></ul>                                       | N/A                                                                  | N/A                                                 |
| Menu Focus Text            | N/A                                                                  | N/A                                                                  | <ul><li>Primary menu</li><li>Account menu</li></ul> |
| Menu Selected              | <ul><li>Primary menu</li></ul>                                       | <ul><li>Primary menu</li></ul>                                       | <ul><li>Coloured line under menu icon</li></ul>     |
| Alert Colour               | <ul><li>Text colour for download 2 go expiry</li></ul>               | N/A (as of publishing)                                               | N/A (as of publishing)                              |

## Detailed behaviour & Known constraints <a href="#known-behaviour-and-constraints" id="known-behaviour-and-constraints"></a>

* Realm colours only apply if explicitly configured; otherwise, default platform colours remain unchanged.
* Colours may be set differently per device (Web, Mobile, TV), allowing device-specific branding.
* Hover states apply **only on Web**.
* Focus states apply **only on TV**.
* Changes apply globally across the realm once saved.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/consumer-experience/theming-and-customisation/expanded-realm-colours.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
