> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/content/content-management/creating-rows/curating-grouped-content/series-carousel.md).

# Series Carousel

After navigating to your desired section on BackOffice, create a new row:

<figure><img src="/files/3fARu6db5YG21zIoQQ5w" alt=""><figcaption></figcaption></figure>

Select your grouped content type:\
\- For a collection of Playlists/Seasons select [Playlists/Seasons Carousels](/platform-knowledge-base/back-office/content/content-management/creating-rows/curating-grouped-content/playlists-seasons-carousels.md)\
\- For a collection of Series select "Series Carousel"

<figure><img src="/files/UmtwIO9H8FZSQlzDPHLn" alt=""><figcaption></figcaption></figure>

### Playlist Carousels

1. Select your desired appearance layout inclusive of creative and metadata

<figure><img src="/files/IR9rJJWYk8slG1MItJee" alt=""><figcaption></figcaption></figure>

2. Next select your desired appearance specific to the layout of the creative (options are the same regardless of your desired template in the previous step

<figure><img src="/files/xtvGD0mGPX7NCvREu1vK" alt=""><figcaption></figcaption></figure>

3. Give your collection a title

<figure><img src="/files/jXQS9BTUGSM9crBKHtTR" alt=""><figcaption></figcaption></figure>

4. Select the tags/series names that should be shown in this collection, note multiple series' that contain multiple seasons can be defined from the dropdown menu

<figure><img src="/files/q4hqNubbxOcankWUzaew" alt=""><figcaption></figcaption></figure>

6. Add any translations for additional languages as required

<figure><img src="/files/1tw9vtJQGkUD8iNXz4BZ" alt=""><figcaption></figcaption></figure>

Once your row is created you can observe it's appearance on the front end:

<figure><img src="/files/rEa85AlCUFLUjVsOWGuw" alt=""><figcaption></figcaption></figure>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/content/content-management/creating-rows/curating-grouped-content/series-carousel.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
