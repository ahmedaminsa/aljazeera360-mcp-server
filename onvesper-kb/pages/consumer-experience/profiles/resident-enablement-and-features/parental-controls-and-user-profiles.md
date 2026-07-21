> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/consumer-experience/profiles/resident-enablement-and-features/parental-controls-and-user-profiles.md).

# Parental Controls & User Profiles

To access this page navigate to;&#x20;

1. Administration&#x20;
2. Parental Controls & User Profiles (If you are unable to see this section then please reach our to you Technical Account Manager).&#x20;

### Parental Controls & User Profiles&#x20;

**Example A: User profile (No kids Profile)**

<figure><img src="/files/kMc2VGOpO1bPkBh91HVv" alt=""><figcaption></figcaption></figure>

*Selecting ‘Manage Avatars’ opens up the component in which additional avatars can be uploaded and the default can be selected*

**Example B: User Profiles & Kids Profiles**&#x20;

<figure><img src="/files/rgTP0TqRyNb7lmBHuUAG" alt=""><figcaption></figcaption></figure>

You will receive the same functionality as shown in *Example A,* but will also have additional options inclusive of:

* Setting ‘Restricted Maturity Ratings’
* Setting Kids Font Size and Color(s)

*Setting Restricted Maturity Ratings:*

* Your VOD catalogue content ratings will automatically appear under ‘Parental Controls’
* From here, you will select which of the ratings are considered ‘Restricted’ - content with ‘Restricted Ratings’ will be hidden from search and view for users within a Kids profile.

<figure><img src="/files/PXWS0t2QTsJkIeQxHaJr" alt=""><figcaption></figcaption></figure>

*Setting Kids Profile Styling*

* Optional Kid Styling & Font Size that will be only applied to Kid Profiles
* Font size is only applicable to Web, as font scale can be managed cleanly from the device
* If no colours are selected, the Realm default will be used

<figure><img src="/files/EqCuNGnZsmiuvM22xknj" alt=""><figcaption></figcaption></figure>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/consumer-experience/profiles/resident-enablement-and-features/parental-controls-and-user-profiles.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
