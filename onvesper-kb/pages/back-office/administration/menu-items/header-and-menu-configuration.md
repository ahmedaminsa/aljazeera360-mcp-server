> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/administration/menu-items/header-and-menu-configuration.md).

# Header and Menu Configuration

A new upgrade to the [Menu items](/platform-knowledge-base/back-office/administration/menu-items.md), mobile apps now support custom header & menu configuration

Just like that original system, all iconography is customisable to bring your own branding into the experience.

<figure><img src="/files/O1LP8VsT5pyTIrXpqkFK" alt=""><figcaption></figcaption></figure>

### Header Configuration <a href="#id-1.-header-configuration" id="id-1.-header-configuration"></a>

The header is the iconography which is shown on top of the home page/home section for the apps by default. This historically included "live now", "cast" and menu options, but this is now customisable for your individual preferences.

Only one option can be configured for the **top left**:

* **Profile** → Shows the profile icon.
* **Menu** → Shows the hamburger menu.

For **top right** configuration:

* Up to **three items** can be configured.
* Items can include defaults (**Search, Casting, Live Now**) or any custom item.

### Menu Configuration <a href="#id-2.-menu-configuration" id="id-2.-menu-configuration"></a>

This section configures both the **Profile** and **Menu** items chosen in the header.

If [**Profiles**](/platform-knowledge-base/consumer-experience/profiles.md) are enabled and user profiles are turned on, the menu allows profile switching ***plus*** configured menu items\
![](/files/Otb37FGFjIYvLAIIey7h)

If [**Profiles**](/platform-knowledge-base/consumer-experience/profiles.md) are **not** enabled or user profiles are **not** turned on, the menu will show configured menu items\
![](/files/fEBKFEAIJFXhfrm4fW2H)

Any item type can be added to the menu, including:

* [**Sections**](/platform-knowledge-base/back-office/content/content-management/sections.md)
* **Views**
* **Outbound Links**
* [**Plugins**](/platform-knowledge-base/back-office/content/plugins.md)

<br>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/administration/menu-items/header-and-menu-configuration.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
