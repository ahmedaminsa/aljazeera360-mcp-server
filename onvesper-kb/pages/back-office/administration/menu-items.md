> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/administration/menu-items.md).

# Menu items

The Dynamic Menu System allows Vesper Admin users to spin up menu items for Vesper Mobile apps that link out to sections within Vesper Admin, or even third party web experiences.

For example, the system can be used as an e-commerce functionality so consumers can shop for tickets and merchandise without having to leave the Vesper mobile app.&#x20;

The dynamic menu system can also be utilized for tentpole events by creating plugin menu items for stats in near real time so fans can get score updates on the fly.&#x20;

*You can freely control the menu items without requesting a new app build.*&#x20;

{% hint style="info" %}
This system has been upgraded for Mobile!

The below refers to Mobile's **bottom menu configuration**, see [Header and Menu Configuration](/platform-knowledge-base/back-office/administration/menu-items/header-and-menu-configuration.md), as well as [Account Menu](/platform-knowledge-base/back-office/administration/menu-items/account-menu.md) for new capabilities!
{% endhint %}

## Platforms

You may add and customize your menu configurations on the following platforms:

<figure><img src="/files/Oehd4sKa7Q0V9hvdJJkW" alt=""><figcaption><p>All required menu configurations (when utilizing all Vesper front-end applications)</p></figcaption></figure>

* **Web** - Top, Top-Left, Hamburger, or Sidebar menu&#x20;
* **Mobile** - Bottom nav bar and Hamburger menu&#x20;
* **Mobile-web** - Browser view on mobile device\*
  * Bottom nav bar or Hamburger menu&#x20;
* **TV** - Sidebar menu&#x20;
* **Roku** - Sidebar menu&#x20;

\*mobile-web is optional, if not configured the "web" menu will be used for all devices that visit the webapp

## How to set up or edit a menu

This guide example will use the mobile app, but other platforms are very similar.

Head into Back Office -> Administration -> Menus -> Edit/Mobile -> Select [Navigation Template](#navigation-templates) -> Click on Add Item.&#x20;

Once you're in the "Add Item" menu,  type the title of the menu. End users will see the title of the menu you add here. To avoid texts truncating, try using shorter words like "Tickets" ,"Shop", or "Scores."&#x20;

<div data-full-width="true"><figure><img src="/files/8cHYgc3d7E9Uts2pUXj8" alt=""><figcaption><p>Creating a new menu item</p></figcaption></figure></div>

{% stepper %}
{% step %}

### Select where you want your menu item to be located:

* **Main Menu -** The primary items nav bar&#x20;
* **Featured Folder Menu -** The hamburger menu&#x20;
* **Non Featured Folder Menu**&#x20;

<figure><img src="/files/tWmorOGOOfJOx2ebOICU" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### Select where you want the new menu item to redirect:

* [**Section**](/platform-knowledge-base/back-office/content/content-management/sections.md)
* **View -** */Account, /Schedule, /Browse*&#x20;
* [**Outbound Link**](#outbound-link-options) - *third party URL  (\*Note that some devices only support HTTPS links)*
* [**Plugin**](/platform-knowledge-base/back-office/content/plugins.md) **-** *Plugin Instance ID*&#x20;

<figure><img src="/files/AqbS8bO4GaGIjtF1mk9p" alt=""><figcaption><p>Example of an outbound link section - only shown to logged in users</p></figcaption></figure>
{% endstep %}

{% step %}

### Selected menu item for

Define which type of users should have this as their default menu item (i.e. their homepage)

* Logged in users
* Guest users
* All users&#x20;
* No users

Using this system you can have a different homepage for guest users and logged in users
{% endstep %}

{% step %}

### Hide menu item for

This allows you to completely hide the menu item for a class of users shown below

* Guest users
* Logged in users
* All users&#x20;
* No users
  {% endstep %}

{% step %}

### Add a Navigation Icon

This is the icon when it is *unselected* by the end user.

<figure><img src="/files/Tawxy7n1noPJEGHyxl3Z" alt=""><figcaption></figcaption></figure>

Recommended format and sizing:&#x20;

* **For Mobile - PNG -** Required size: 72x72px
* **For Web/TV** - **SVG** - Required size: 128x128px
* **For** **Roku** - **PNG** - Required size: 64x64px

{% hint style="warning" %}
We do not support `<style>` tags in SVG files for TV. \
Please ensure all your SVG styling is handled independently of these tags.
{% endhint %}
{% endstep %}

{% step %}

### Active Navigation Icon

This is the icon when it is in the "active" mode where a user has *selected* the menu item. &#x20;

<figure><img src="/files/EuJabOownye2fgShk9GJ" alt=""><figcaption></figcaption></figure>

Recommended format and sizing:&#x20;

* **For Mobile - PNG -** Required size: 72x72px
* **For Web/TV** - **SVG** - Required size: 128x128px
* **For** **Roku** - **PNG** - Required size: 64x64px

{% hint style="warning" %}
We do not support `<style>` tags in SVG files for TV. \
Please ensure all your SVG styling is handled independently of these tags.
{% endhint %}
{% endstep %}
{% endstepper %}

### Navigation Templates

#### **Web:**

On this platform, you are chosing **which** menu type you want to display. Each style is different and you can select one of the 4 options available to you.

<figure><img src="/files/zlRFBsOWjqqjsrGMwgdm" alt=""><figcaption></figcaption></figure>

#### Mobile

Mobile "Navigation templates" refers to the 3 different mobile menus which are available in the vesper app. All 3 are always in use, so you may want to make edits to all 3 of them.

<figure><img src="/files/RVb9448dzlyb8oSUu37G" alt=""><figcaption></figcaption></figure>

#### TV/Roku

Vesper UTV and Roku enforces use of the "Sidebar" menu style. You will only be able to select this navigation template and begin editing it. Note that the TV menu is split into two sections in a different way to the web:

* Primary items: Shown in the side menu's primary display area
* Utilities shortcuts: Shown at the bottom of the side menu
* Account items: Will be shown on a dedicated side menu in the account page

### Outbound link options

When editing links in the mobile menu system for either the "Menu" or "Bottom" configuration, you have options as to how these links will behave in app.

{% hint style="info" %}
Note! These options are for mobile apps only, they require Vesper mobile version 11.0 to function. If you set these values before mobile version 11.0 is available, they will continue to operate as in-app web links
{% endhint %}

<figure><img src="/files/GeeziNtNwdd7Sv4cKquY" alt=""><figcaption></figcaption></figure>

* **In-App Browser (Incognito)**\
  This is the default behaviour and is how Vesper mobile historically operated. The link will open in an in-app browser. This works great for maintaining the in-app experience, but it has the downside of not having context about the user. Any sign in information that is in the user's mobile app browser will not be available. It will be as if they are browsing incognito
* **In-App Browser (Shared Session)**\
  The presentation of this system will be similar to if you were directed to an external SSO service to sign in on the app. The user may be presented with an operating system prompt that the app wants to open another website, and that there are some security considerations. However this will also allow the user to stay largely in-app whilst completing some task in the browser, maintaining all their cookies and sign in information. *If you're trying to link a user to your SSO site to manage their preferences or account settings, this is the best approach.*
* **External Browser**\
  The user will leave the app completely and be launched into their default web browser to view the website.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/administration/menu-items.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
