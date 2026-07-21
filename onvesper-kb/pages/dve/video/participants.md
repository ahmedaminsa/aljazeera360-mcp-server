> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/dve/video/participants.md).

# Participants

The ***Participants*** feature provides end users with quick access to information about individuals involved in the content they watch, such as actors, hosts, and directors. They are displayed within the interstitial page and may also be searchable.

<figure><img src="/files/t8F6KYN4WPiEVplh8Fkz" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}

Please note that this feature is part of the new VOD platform UI. You can access the new UI on any individual VOD page by pressing the below "Try The New UI" button.\ <img src="/files/xqNbWToqvqb0DrTTG4fN" alt="" data-size="original">

If you cannot see this button on VOD pages, please reach out to your Platform Account Manager for enablement.
{% endhint %}

## Adding a Participant

<figure><img src="/files/w5Jp7VdcwB6lTscGq2cf" alt=""><figcaption></figcaption></figure>

* Navigate to the Participants section in the Video Detail UI.
* Click the Edit button to open the Participants modal.
* Use the modal to manage participant metadata.

<figure><img src="/files/pndAjgJm3X7n1WUfxqJf" alt=""><figcaption></figcaption></figure>

The modal is divided into two sections:

* Participant Groups
* Participants

### Participant Groups

The Participant Groups section allows content managers to categorise participants *(e.g., actors, directors, writers)* into named groups. This grouping informs how participants are displayed on the interstitial page - either by category or in a defined sequence.

{% hint style="warning" %}
Note: Creating participant groups is optional. None of the fields in this section is mandatory. Worth highlighting that groups must contain at least 1 configured participant to be successfully stored as a group.
{% endhint %}

<figure><img src="/files/62crQ7bjlABJF8mVW8UO" alt=""><figcaption></figcaption></figure>

* Order: Numerical value that determines the display order of groups. Values can be adjusted manually or by drag-and-drop.
* Group Name: A unique key identifying the group *(used for localisation)*.
* Group Value: The localised label shown on the interstitial page for the selected language *(e.g., ممثل for "Actor" in Arabic).*

Use the + / - buttons to add or remove group rows.

### Participants

The Participants section is used to define metadata for each individual participant.

<figure><img src="/files/pVPopn4K7VAVZH57BR2A" alt=""><figcaption></figcaption></figure>

Metadata fields include:

* Order: Numerical value indicating the display order of participants. Can be changed manually or by drag-and-drop.
* Name ***(required)***: Localised name of the participant.
* Role: Localised role of the participant (e.g., character name like *Batman*).
* Description *(optional)*: Additional metadata displayed on the interstitial page. If used, ensure consistent application - this can be used for example to include the date of birth of participants/website or handles for socials.
* Group: Associates the participant with an existing participant group, if defined.
* Image: Profile image of the participant.

{% hint style="info" %}
Where a participant image is not provided, a default headshot image is used. This can be configured by reaching out to your Platform Account Manager with the desired creative.
{% endhint %}

Use the + / - buttons to manage participant entries.

### Localisation

All participant metadata supports localisation. To localise participant data:

1. Select the required language(s) from the language menu.
2. Enter participant metadata for each selected locale.\
   ![](/files/FSPqlfWtJNKCyEQxShta)

In the Participant Groups section:

* The Group Name remains constant as a unique key.
* The Group Value must be translated for each configured language (e.g., *Actor* → *ممثل* for Arabic).

<div><figure><img src="/files/UhUsBwuhTs9Oq5psM3zr" alt=""><figcaption></figcaption></figure> <figure><img src="/files/9gUdkI6rM2UuWim2FG0b" alt=""><figcaption></figcaption></figure></div>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/dve/video/participants.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
