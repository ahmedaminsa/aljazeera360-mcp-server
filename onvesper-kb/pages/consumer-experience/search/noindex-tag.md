> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/consumer-experience/search/noindex-tag.md).

# noindex Tag

The `noindex` tag ensures that videos or playlists are excluded from Vesper search results and cannot be referenced within the Vesper Back Office. However, they will still be accessible via direct URL on the front end of your platform.

## Adding a no-index tag

Simply add `noindex` as a tag to your VOD / Playlist / Series of your choice when [adding the metadata](/platform-knowledge-base/dve/video/metadata.md).

<figure><img src="/files/uTV9mtKboPeyPlqvl8Rt" alt=""><figcaption></figcaption></figure>

## Result of using noindex

Using the `noindex` tag will result in the following behaviour:

* VODs, Playlists, Series and Seasons will not appear in Vesper search results on the front end of your platform.
* VODs, Playlists, Series and Seasons with the tag cannot be referenced in Vesper Back Office. e.g. you will not be able to add that asset to a hero carousel.
* The asset can still be available for sharing on the front via the URL.

#### Of Note

* If the `noindex` tag is applied retrospectively, the asset may still appear in an existing tag-driven content row. To ensure it is fully excluded from that content row on the front end, any associated tags must be removed from the asset.<br>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/consumer-experience/search/noindex-tag.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
