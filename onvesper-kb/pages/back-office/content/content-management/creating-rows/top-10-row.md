> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/content/content-management/creating-rows/top-10-row.md).

# Top 10 Row

The top 10 row allows you to curate a row of videos that can be showcased along side a numbered icon, highlighting the top 10 pieces of content on your service today.&#x20;

<figure><img src="/files/ns5s9UnMkMI00581dRyT" alt=""><figcaption></figcaption></figure>

The row is set up like any other row in back office, but does include x2 additional steps highlighted below;&#x20;

1. Set up of the icon store&#x20;
2. Selecting "Is a postion row"&#x20;

### Set-up Instructions <a href="#ud83d-udcd8-instructions" id="ud83d-udcd8-instructions"></a>

{% stepper %}
{% step %}

#### Navigation

Navigate to Vesper Backoffice > Content Management
{% endstep %}

{% step %}

#### Create a Row

1. Select **Create new > Row**.
2. Chose **Content Carousels** row template
3. Create either a **Single Row** or **Poster Row**.
   {% endstep %}

{% step %}

#### Select Row Type

Set the **row type** to **vod\_playlist**.
{% endstep %}

{% step %}

#### Select Playlist

Choose the pre-created playlist from **VOD on Vesper** that contains the content you want to feature.
{% endstep %}

{% step %}

### Enable position row

Tick the box labelled **“Is a Position Row”**.
{% endstep %}

{% step %}

### Save & Publish

1. Save the row configuration.
2. The row will display as a numbered **Top 10 Row** on the front end
   {% endstep %}
   {% endstepper %}

### Numbered Icons <a href="#known-behaviour-and-constraints" id="known-behaviour-and-constraints"></a>

The numbers used along side this row are generated from the Icon Store (see [Iconography](/platform-knowledge-base/consumer-experience/theming-and-customisation/iconography.md) for more information).  If you would like to change the icons used, please reach out to your account manager.

Below are some high level specs of what should be used when creating your own icons.&#x20;

<details>

<summary>Icon Imagery specifications</summary>

Landscape: 104px X 198px\
Poster: 159px X 360px

Note, the sizes provided indicates the space in which these icons will be placed according to the size of the video cards. The positioning and size of the number is up to your discretion - See some examples below;&#x20;

<figure><img src="/files/UA2McetV4LW0o25ea6KK" alt="" width="42"><figcaption></figcaption></figure>

<figure><img src="/files/QyIbu0q92sh0RstiT7wR" alt="" width="42"><figcaption></figcaption></figure>

<figure><img src="/files/KmrnvKsgeFpwRF4R1mpg" alt="" width="42"><figcaption></figcaption></figure>

</details>

### Known Behaviour & Constraints <a href="#known-behaviour-and-constraints" id="known-behaviour-and-constraints"></a>

* Only VOD assets and movies are available for this row&#x20;
* The VOD playlist has to be pre-created in Vesper VOD back office&#x20;


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/content/content-management/creating-rows/top-10-row.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
