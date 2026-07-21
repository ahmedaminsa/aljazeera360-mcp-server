> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/dve/video/typed-tags/typed-tags-search.md).

# Typed Tags: Search

## How Typed Tags function today

Historically, Typed Tag selection relies on scrollable dropdowns without search capability. Content managers must manually scan lists to locate the correct typed tag name or ENUM value, increasing time spent tagging, introducing risk of error, and reducing metadata consistency at scale.

<div data-with-frame="true"><figure><img src="/files/6a5cZhVQRClVfQBys5de" alt="Typed Tags Drop-Down Menu" width="386"><figcaption><p>Typed Tags Drop-Down Menu</p></figcaption></figure></div>

## Typed Tags Search - Feature Overview

The Typed Tags Search feature introduces search capability for selecting Typed Tag names and ENUM values across the Vesper VOD User Interface.

The feature enables:

* Search with immediate filtering
* Support for large ENUM value sets without performance degradation
* Consistent behavior across Videos, Playlists, and Collections

This enhancement significantly improves metadata application speed, accuracy, and usability for content managers.

## Search Feature Behavior:

### Searching for Typed Tags

Content Managers will be able to search for (localized) Typed Tag names when applying metadata to an entity (*Video, Playlist, or Collection*).

* Dropdown will filter in real-time as the user types.
* Filtering begins from the first character entered.

### Searching for ENUM values

Content Managers can search for (localized) ENUM values (*within a selected Typed Tag*) when applying metadata to an entity. (*Video, Playlist, Collection*).

* The ENUM value dropdown filters in real-time based on user input.
* Only valid ENUM values are displayed.
* Filtered results are **alphabetically** ordered.&#x20;
* Filtering uses prefix matching only (matches must start at the beginning of the option text).

### Typed Tag Management Search

Content Managers can also search for Typed Tags within the Typed Tag Management page.

* Search is indexed on Typed Tag name only.
* Results filter dynamically as the user types.

## Vesper VOD Search User Interfaces

**Typed Tags Page:**

<div data-with-frame="true"><figure><img src="/files/jxMZN31cLCLUuneRYPAx" alt=""><figcaption><p>Typed Tags Page w/ Search</p></figcaption></figure></div>

**Entity Detail Page (Video, Playlist, and Collections):**

<div data-with-frame="true"><figure><img src="/files/Hk3d91TYKLPHX6Z35o8k" alt=""><figcaption><p>Search/Select Field for Typed Tags Key</p></figcaption></figure></div>

<div data-with-frame="true"><figure><img src="/files/bCObgnTcEEBMcqNnv9kE" alt=""><figcaption><p>Search/Select Field for Tag Value</p></figcaption></figure></div>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/dve/video/typed-tags/typed-tags-search.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
