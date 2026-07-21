> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/content/content-management/creating-rows/title-rows-mixed-content.md).

# Title Rows (Mixed content)

{% hint style="info" %}
**This feature must be enabled for you to start testing. Reach out to your account manager if you wish to use this capability.**
{% endhint %}

Enabling the display of both Series and Movies side by side in a single row, Title Rows refers to the first time it has been possible on Vesper to curate a row which shows both content types.

We refer to these as "Titles", as the term allows for abstraction out of a catalogue. If you think of your catalogue as set of Box Sets and Movies, each one in the catalogue can be referred to as a Title.

### How Does it Work?

Mixing content into a Title Row is possible only through a tagged row. If you select a Title Row, the Vesper content engine will search for all VODs which match the tags you have provided. Any VODs which have a parent series object (e.g. is an episode of some series), will be automatically converted into a single series object and presented in the row.

If the VOD does not have a parent (e.g. it is a standalone clip or movie), it will be presented as a video.

### Configuring a Title row

{% stepper %}
{% step %}

### Create a new Row

Navigate to content management in back office, click "Create new" button, then "row"
{% endstep %}

{% step %}

### Set up the Row template

1. Choose content carousel
2. Select from the available Row Styles. Poster row formats are recommended for Title rows, but a single row of 16:9 cards is also supported.
3. Name your row and click through to type selection
   {% endstep %}

{% step %}

### Setting the Type

The "Type" of row will be VOD\_VIDEO by default. You need to change this to the curated type shown in the image below (Tagged Titles: Series and standalone videos)

![](/files/YlPc5fdiddluOAkHAGnz)&#x20;

Once set, the Type will show in the dropdown as "TITLES.

You can now add the Tags you want to find (add as many as you need). Remember that the system will load all VODs tagged with the tags you enter and automatically show the Series if one exists. **You do not need to tag the Series or Season assets in Vesper VOD with these tags**. Don't worry if you've only tagged one episode, or many episodes of a series with the tag, either way only one series card entry will show.

<figure><img src="/files/Bh8XYAdX4nNxAXXDHFg3" alt=""><figcaption><p>See that there are 52 VODs for "Breaking_Bad" (and other series), only 8 for the "Poster" tag. Each of the Poster tag items are standalone VODs, so we will expect to see 8 entries in the row there, but only one entry each for Breaking Bad and Mad Men</p></figcaption></figure>

Chose your metadata display mode, whether you want to hide duration on these content items, then set content order as desired, then move on to the next translations.
{% endstep %}

{% step %}

### Translate and publish

Add any translations needed for your row, then publish
{% endstep %}

{% step %}

### Review

On your front end you should now see the results of the mixed content row type.

<figure><img src="/files/Lu761aG3PgRz7qVP4SOD" alt=""><figcaption></figcaption></figure>
{% endstep %}
{% endstepper %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/content/content-management/creating-rows/title-rows-mixed-content.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
