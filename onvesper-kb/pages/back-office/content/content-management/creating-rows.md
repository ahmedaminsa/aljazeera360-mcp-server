> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/content/content-management/creating-rows.md).

# Creating Rows

To start go to Back Office and click ‘Content’ then ‘Add Row’.

### CHOOSING A TEMPLATE <a href="#stage-1-choose-template" id="stage-1-choose-template"></a>

In the Choose template section you can select from the options below;

**Content Carousel: a row made of single videos using standard thumbnails.**

* Single Row: A row of videos&#x20;

![](/files/-MQGmybgyyfFrW-J24o4)

![Single Row](/files/-MQGjaY5zWQOG2kOrFqT)

* Featured Single Row: A row of videos with a background image

![](/files/-MQGn9jd5PjUOzcKEvJU)

![Featured Single Row](/files/-MQGjo1BmQYkDCp7rdwi)

* Double Row: A row of videos that is displayed in a double stacked format

![](/files/-MQGnFGRK4uRh-1cCeqf)

![Double Row](/files/-MQGk0UdAcZytRAZnGKq)

{% hint style="warning" %}
Note: Double rows are not supported on the Vesper TV applications. All double row types will instead be rendered as single rows on TV.
{% endhint %}

* Featured Double Row: A row of videos that is displayed in a double stacked format with a background image

![](/files/-MQGnOghdNRrRxjhqqv5)

![Featured Double Row](/files/-MQGk7A0y6x3-CrURLDH)

* Poster Row: A row of videos that is displayed using poster imagery

![](/files/-MQGnRrmwYK1kkF6byPu)

![Poster Row](/files/-MQGkHBcR1jWyHHtlSv8)

* Featured Poster Row: A row of videos that is displayed using poster imagery with a background image

![](/files/-MQGnXRkd8DroktGkKdD)

![Featured Poster Row](/files/-MQGkOgHZwJkSUgPqd3S)

**Playlist Carousel: a row consisting of a list playlists or shows**

![](/files/-MQGnoHagtJY4moyp8ZZ)

* Basic Playlist Row: A list of Playlists
  * Basic Square Playlist: A list of playlists using the Thumbnail image from the Playlist Metadata in the DVE

![](/files/-MQGnyVOt-oRQg8EV7mf)

![Basic Square Playlist Row](/files/-MQGkdEPBQ8p929GIanG)

* Basic Poster Playlist Row: A list of playlists using the Poster image from the Playlist Metadata in the DVE

![](/files/-MQGo2Kc4Klidu5oQ0B2)

![Basic Poster Playlist Row](/files/-MQGkloTBCSdmNGiriKS)

* Basic Landscape Playlist Row: A list of playlists using the Title image from the Playlist Metadata in the DVE

![](/files/-MQGoAVQqjiDkOU4FBBv)

![Basic Landscape Playlist Row](/files/-MQGkuawUTaLt2pQ3dEJ)

* Featured Playlist Row: A list of Playlists with a background image
* Inline Playlist Row: A list of playlists with metadata focused on the left of screen

![Inline Playlist Row](/files/-MQGltTMgUwUyJ2z4uyj)

**Navigation Carousels a row made of buttons that link to existing** [**sections**](/platform-knowledge-base/back-office/content/content-management/sections.md)

![](/files/-MQGoRe7MoxL1Su7aoh6)

![Navigation Row](/files/-MQGmKVu7_k7tDWTQ9-5)

### CREATING THE ROW <a href="#stage-2-customise-style" id="stage-2-customise-style"></a>

Once you have selected the type of row you wish to create complete the following steps

**Title:** This is the title of the row that will appear on the front end applications that informs the user about the content in the row e.g New, Highlights etc

**Type:** The type of content curation that will power the row

*AUTOMATED*

* New: A row using the most recently uploaded content in the DVE
* Live: A row with Live Events that have been published on your platform
* Upcoming Events: A row with Upcoming Live Events scheduled to appear on your platform
* Continue Watching: A row with a unique list of videos based on the content that user has consumed
* Favorites: Will populate the row with a unique list of videos a user has marked as Favorite within the client applications
* User Recommendations: A list of videos suggested for the user based on correlating tags within videos a user has watched and suggestions for what to watch next

*CURATED*

* Tagged Items: Will populate the row using tags that have been imported from Videos or Playlists within the DVE.
  * Typed tags can also be used here. These are characterised by having the form `{key}|{value}` whereas normal tags do not have the `"|"` character.
* Playlist: Will populate a row with videos in an existing Playlist
* Show: Will populate a row with videos in an existing Playlist

### **Translations**&#x20;

Here, the user can add another language if the platform supports multiple languages.

Users can customize the appearance and functionality of the row at any time by utilizing the modal on the right-hand side of the screen to edit metadata and other settings.

![](/files/-MQGrDWwZ_svwqp3O5rj)


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/content/content-management/creating-rows.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
