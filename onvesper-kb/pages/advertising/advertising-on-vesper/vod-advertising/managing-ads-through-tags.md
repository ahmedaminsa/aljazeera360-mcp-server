> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/advertising/advertising-on-vesper/vod-advertising/managing-ads-through-tags.md).

# Managing ads through tags

If you have followed the guide in [Advanced targeting](/platform-knowledge-base/advertising/advertising-on-vesper/targeting/advanced-targeting.md), you will have added a Key-Value pair into your SSP with the key "tags".

This custom key will return a list of all the tags defined in your video in Video Exchange [Video Exchange (DVE)](/platform-knowledge-base/dve/overview.md). You can then introduce advertising logic on your SSP that only shows adverts to videos with a certain tag.

Example 1:

You have created advert inventory on your SSP for a football boot advertising parter who is sponsoring your content. You set up the advert inventory to be returned whenever the tag "football" or "abbibas" is sent by Vesper.

Example 2:

You create an advert rule on your SSP which blocks any adverts from being returned when the VOD tag "noads" is sent by Vesper.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/advertising/advertising-on-vesper/vod-advertising/managing-ads-through-tags.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
