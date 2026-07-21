> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/consumer-experience/related-content.md).

# Related Content

The **Related Content** feature enhances content discovery by displaying a dynamically generated row of relevant video content on the **Content** **Interstitial Page**. This improves user engagement and retention by surfacing related content based on metadata (e.g., genre, tags, descriptions).

<figure><img src="/files/EoOmwWOr7wSECnYouY48" alt=""><figcaption></figcaption></figure>

## Display and User experience

The **Related Content** feature will appear exclusively on the **Content Interstitial Page**, where up to **30 dynamically generated related items** may be displayed per piece of content. The recommendation engine updates **daily**, meaning related content remains static for that period. If no related content is available, the row will be **hidden**. When a user selects a related content item, they will be directed to its respective **Content Interstitial Page**.&#x20;

On **TV devices**, a safeguard prevents infinite back navigation—if a user presses “back” **five times**, they will be returned to the homepage.

## How does it work?

Related Content uses a 'More Like This Query' that runs daily, and finds documents, such as text, that are "like" a given set of documents.&#x20;

The fields used for recommendations are as follows:

* Title - Content title
* Description
* Tags
* Typed Tags.

For these fields, each requires at least the given A% of match. If that match is successful, it is assigned a weighting value: Bx (where x a multiplication weighting value). The final calculated ranks of each potential related content that matches are then used to decide which content is shown, and in order of those calculated ranks.

| Field(s)    | % Match required | x Weighting value |
| ----------- | ---------------- | ----------------- |
| Title       | 10%              | 2x                |
| Typed Tags  | 10%              | 1.5x              |
| Tags        | 10%              | 0x \*             |
| Description | 10%              | 1x                |

So as above, title is the strongest signal of a match provided at least 10% of the title matches. Description is the weakest signal of a match, and also only requires 10% of the entire description to match.

\***Note**: Tags are by default not part of the related content feature as they are often used in Vesper for license management (i.e. tagging content to be shown for free users etc). If you wish tags to be included in your recommended content system please contact your B2B helpdesk.

This is **not a self-service feature**. Should you wish to enable Related Content please speak to your Platform Account Manager

### What's excluded?

The Related Content feature does **not** factor in user behaviour - the recommendations are based purely on **metadata.**

The feature will **not** suggest sibling or ancestor content, meaning episodes from the same season or seasons from the same series will be excluded.

Playlists will **not** recommend items from within the same playlist. For standalone content, recommendations will be limited to other standalone content or a top-level series.

[Trailers](/platform-knowledge-base/dve/video/trailers.md) will not be returned in related content rows. Nor will content which is tagged with the [noindex Tag](/platform-knowledge-base/consumer-experience/search/noindex-tag.md).&#x20;

## Customising the behaviour

### Changing default weighting and match values

If you would like to tweak the approach for content on your realm, you can request these values be adjusted by the Vesper engineering team.

Raise a ticket with your B2B helpdesk using the following template, remove any line items that you do not wish to change.

***

**Subject:**&#x20;

Change to related content configuration

**Text:**

Please change the related content engine for our realm to use these values for weighting and % match required:

Title:

Match required: \<insert>%\
Weighting value: \<insert>x

Description:

Match required: \<insert>%\
Weighting value: \<insert>x

Typed tags:

Match required: \<insert>%\
Weighting value: \<insert>x

***

Replace the above \<insert> options so that the format shows (for example) 10% and 2.5x

### Identifying important typed tags for your content

If you have made an investment in typed tags for your catalogue, and can identify typed tags that are a stronger signal to our related content engine that 2 pieces of content may be related, you can provide that information to our team.

Raise a ticket with your B2B helpdesk using the following template, removing the "buckets" of weighting as neccessary.

***

**Subject:**&#x20;

Related content: specific typed tag weighting configuration

**Text:**

Please change the related content engine for our realm to use custom weighting values for these typed tags:

3x Weighting:

* \[Typed tag key]
* \[Typed tag key]

2x Weighting:

* \[Typed tag key]
* \[Typed tag key]

1x Weighting:

* \[Typed tag key]
* \[Typed tag key]

***

This instruction will be passed to our engineering team. Note that you are defining the list of tags to be "3x" or "2x" weighting. All other typed tags will be 1.5x under the normal system design.You can also use this request to remove or lower the weighting of certain tags be asking for 1x or 0x weighting.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/consumer-experience/related-content.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
