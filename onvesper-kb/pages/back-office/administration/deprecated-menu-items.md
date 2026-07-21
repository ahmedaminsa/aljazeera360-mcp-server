> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/administration/deprecated-menu-items.md).

# DEPRECATED Menu items

{% hint style="info" %}
DERECATED page, see: [Menu items](/platform-knowledge-base/back-office/administration/menu-items.md)
{% endhint %}

## Introduction

This feature allows you to flexibly create and edit menu items within the self-service capabilities of Vesper Admin so the menus can be easily customised to meet your specific needs.&#x20;

Having customised menu items will distance your product from other clients within Vesper Admin, allowing you to fortify the unique characteristics of your brand amongst your present and future fanbase. Customised menu items will also empower you to feature specific content more prominently and adorn your product with seasonal items.

{% hint style="info" %}
This feature is available for Web, TV and Mobile; any changes published will be immediately updated in production.
{% endhint %}

## Implementation

1. Navigate to Vesper Admin -> Administration -> Menus
2. Select 'Edit' on web
3. **Layout** - Select which layout you'd like to have and click 'Next' (preview is still to be finalised, but you can get an idea of how each layout works thanks to a thumbnail in the navigation menu

<figure><img src="/files/GyNEPW7fKacdFwGrXrqq" alt=""><figcaption><p>The navigation menu on the left highlights the available layouts to choose from</p></figcaption></figure>

4. **Items** - items are divided between:
   * Primary items: these are usually Home/Browse/Schedule and they appear in the primary position (depending on the layout). Within the primary items, there are two sub-categories:

     1. Featured Items: these are usually Favorites/Account/History and are located under a 'More' section of a top menu. In a hamburger menu, they appear on the left and are marked in bold.&#x20;
     2. Non Featured Items: these are usually FAQs/Privacy Policy/Cookie Policy. They appear on the right.

     <figure><img src="/files/CZOtc17wICFoq7JRQ437" alt=""><figcaption><p>Primary items via a Hamburger menu</p></figcaption></figure>
   * Utilities shortcuts: these are usually Search/Live Now/Account and are located on the top right of the Home page.&#x20;
5. **Editing items** - right click on the three dots on the right side of the item to edit them or hide them. Items can be edited to:
   * Change the name
   * Change their location (Main/Featured/Non Featured)
   * Redirection to a specific Section, View or Outbound link&#x20;
   * Navigation icon (recommended SVG 128px x 128px) - navigation icons are only available when using the sidebar layout and/or for utilities shortcuts appearing on the top right.

{% hint style="info" %}
Some items have been pre-populated and sections cannot be edited. However, **all items can be hidden from the UI.**&#x20;
{% endhint %}

6. **Creating a new Menu Item** - adding a new menu item will allow you to add a customised menu item to the Main/Featured/Non Featured location.&#x20;
7. **Translation** - You can translate the menu items in all available languages for the realm.&#x20;
8. **Publish** - time to publish your changes and see your new menu items come to life in production!


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/administration/deprecated-menu-items.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
