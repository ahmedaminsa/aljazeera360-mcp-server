> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/dve/video/typed-tags.md).

# Typed Tags

Typed Tags allow our residents/content managers to define metadata using key-value pairs, which can then be associated with content, enhancing discoverability and personalisation across supported languages.

Typed Tags can be locailsed to different languages and applied at all levels of the content hierarchy: Videos, Playlists (including Seasons) and Collections (including Series). Typed Tags can be managed through the Vesper VOD UI or the Onboarder API.

This document focuses on managing localised typed tags using the Vesper VOD UI.

## Feature Configuration

Before a Typed Tag can be applied to content, it must be defined at the customer level. There are two steps to applying a typed tag to content:

* Typed Tag Definition: creating the tag and its configuration.
* Typed Tag Application: applying the defined tag to Videos, Playlists, or Collections.

### Typed Tag Definition <a href="#typed-tag-definition" id="typed-tag-definition"></a>

<figure><img src="/files/flY4cfL8fHUsk3Vs6nTG" alt=""><figcaption><p>Typed Tag Manager Page in Vesper VOD​​</p></figcaption></figure>

Typed Tag Definition is managed through the Typed Tag Manager Page (**Admin** > **Typed Tag Manager**). Here, content managers can create new typed tags and edit or delete existing typed tags.

To create a new typed tag, the content manager must specify the following:

* **Typed tag attributes:**
  * Visibility (normal or row displayable)
  * Select Tag Type (enum or text)
* **Typed tag info:**
  * Typed Tag Name
  * Typed Tag Description
  * Typed Tags are initially created in the default customer language. Other languages can then be added using the language selector in the UI. "**Add language**"
  * Localised Typed Tag Name, here the content manager can specify language tarnslations within the selected language, e.g. (English UK) "Genre", (German) "das Genre".
  * Locailised Typed Tag Value e.g. "Action" / "Aktion"

<p align="center">                    ​​</p>

<figure><img src="/files/2azOA5sFOkSwCm9sRNLE" alt="" width="439"><figcaption></figcaption></figure>

Enum-typed tags require localised values for all keys in each added language. For example, if the tag is “Genre” and supports English, French, and Spanish, each genre (key) must have a label in all three languages.

<figure><img src="/files/wIUk50QnucL03E6zNwIa" alt="" width="375"><figcaption></figcaption></figure>

### Typed Tag Application <a href="#typed-tag-application" id="typed-tag-application"></a>

Once a Typed Tag has been defined, it can be applied to any of the following content types: Videos, Playlists and Collections.

#### **To apply a localised typed tag:**

1. Navigate to the typed tag section of the content item's detail page.
2. Click Edit.

<figure><img src="/files/ekqKOcQgLrogdoWdVjjj" alt="" width="563"><figcaption><p>Empty Typed Tags Metadata</p></figcaption></figure>

The content manager may type the Typed Tag to insert it or simply click on *Add.* The drop-down menu will display all the available Typed Tags.&#x20;

#### **Configuration**:

* If the desired Typed Tag allows a custom value (TEXT), the content manager can set any text:

<figure><img src="/files/900veu3CQaISFMjWM1Q8" alt="" width="563"><figcaption><p>Typed Tag of TEXT kind (any value is valid)</p></figcaption></figure>

* If the chosen Typed Tag already has a set of predefined values (ENUM), the content manager may only pick one of the values in the list:

<figure><img src="/files/DEgC5wW838jq08T0GKk8" alt="" width="563"><figcaption><p>Typed Tag of ENUM kind (predefined values)</p></figcaption></figure>

* VOD assets can have up to 150 Typed Tags, and the Type can be used more than once:

<figure><img src="/files/7Gdd1Lj96T2QVcUVc7bo" alt="" width="563"><figcaption><p>Example of different Typed Tags</p></figcaption></figure>

**Note:**

Once an Enum value is applied to an entity, it will no longer appear in the dropdown for that same typed tag on the same entity.

Example: If "English" is selected for a "Supported Audio Language" typed tag with English, French and Spanish as localised values, only "French" and "Spanish" will be available the next time the same typed tag is added.

If a language is selected which doesn’t have localised values, the default language values will be presented.

Untranslated values are visually flagged in the UI with a distinct colour, indicating that localised versions weren’t defined.<br>

<figure><img src="/files/3w19ErKM3z23j0VhAjhW" alt="" width="563"><figcaption></figcaption></figure>

If localised values are required in the desired language, the content manager can update/edit the typed tag definition from the typed tag manager page.

See [Typed Tags: Best practices](/platform-knowledge-base/dve/video/typed-tags/typed-tags-best-practices.md) for more guidance and considerations.

### Visibility

Vesper's defined "Visibility" of tags are defined below:

#### Row Displayable:

{% hint style="info" %}
There is a limit of 10 of these typed tags on any given video. You may define as many typed tag definitions as you wish but you can only add up to 10 on a single video
{% endhint %}

This typed tag will be available on the VOD asset when it is returned as part of a **content bucket** API call. For example, on the home page, section page or other playlist page.

Third parties building custom User Interfaces will be able to use these tags to change the user interface of the video "card" or "tile" when listing content.&#x20;

<figure><img src="/files/dNbAJn1VNW6yUiTf9vhL" alt=""><figcaption><p>User Visible tags would be surfaced for third parties when listing videos on rails such as this one</p></figcaption></figure>

As of publishing; Row Displayable tags do not have a function on the Vesper user interfaces. Future roadmap changes may include providing such optionality.

#### Normal:

All other typed tags. These tags are available on [Interstitial Pages](/platform-knowledge-base/consumer-experience/interstitial-pages.md) and can also be used with advertising macros. There are no defined limits for the number of Normal tags that can be associated with a single video, although we would expect performance implications if one video was tagged with more than \~500 tags.

{% hint style="info" %}
Typed tags are not recommended for use with [Licences & Promotions](/platform-knowledge-base/back-office/licences.md), however if you have a specific use case for licensing based on typed tag definitions, please use "Normal" and then contact your Platform Account Manager for more information.
{% endhint %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/dve/video/typed-tags.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
