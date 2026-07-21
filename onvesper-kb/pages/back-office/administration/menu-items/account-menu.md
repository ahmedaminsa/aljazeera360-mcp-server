> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/administration/menu-items/account-menu.md).

# Account Menu

The [Dynamic menu system](/platform-knowledge-base/back-office/administration/menu-items.md) has now been expanded to the account menu. If you wish to assume direct control of the options available to your end-customers in the account menu, Vesper will now support you.

Available on all front ends (Web, Mobile, TV and Roku), the account menu options will appear under the same Vesper back office menu used for other menu items - simply navigate to the "Administration" -> "Menus" option, where you will see all account menu options:

<figure><img src="/files/JXpBuQgwqyv7dv27LBls" alt=""><figcaption><p>Example Account Items options for the Vesper web experience</p></figcaption></figure>

Here, you can hide or re-name pre-populated items, or add additional links.

For example, if your service is Free, you may want to hide the "Subscriptions" item and "Payment Details" item.

Another popular use case, you may want to add an external link into the account menu which will link out to your help pages or open an e-mail client to contact support.

Iconography that is set on the account menu will only apply to TV platforms, as icons are not shown on the Vesper web or Mobile designs.

#### Enabling

Note that to ensure there are no unexpected changes as a result of the rollout of this feature, it will not be applied to your configuration by default. If you are interested in using this feature, we recommend that you first set up the menu items you expect for **all apps**, then contact your Account Manager to request that they switch your realm to utilise the menu API for the account page menu items.

<figure><img src="/files/TwlDkUxQzyx9orSqdBoT" alt=""><figcaption><p>An example of the account menu with "Need Help?" linking to a support page</p></figcaption></figure>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/administration/menu-items/account-menu.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
