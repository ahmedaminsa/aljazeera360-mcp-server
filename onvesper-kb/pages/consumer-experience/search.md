> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/consumer-experience/search.md).

# Search

Vesper Search, now in general availability to customers using Vesper applications, replaces the legacy search system previously in use on the platform.

For the first time, Search results can be fully aware of the context of a user and the content they are able to see. That means that content which is not available to a user because of their current license, or geolocation, will be excluded from search results providing a consistent content experience across the platform.

Vesper search's UI is built on the platform's templated views, utilising [Grid View](/platform-knowledge-base/consumer-experience/grid-view.md) as a base. By leveraging templates, there are more customisations available to our residents to personalise their search experience.

## Display and User Experience&#x20;

Navigate to the home page of your service and click the "search" icon, typically displayed in the top right hand corner. This will take you to the search landing page.&#x20;

By default, users will see all content that is available on your service, ordered by publish date so that newest content is shown first.

<figure><img src="/files/ZT74OCUyov1ygx8zPjXL" alt=""><figcaption></figcaption></figure>

Searching in the panel will then display the relevant search results&#x20;

<figure><img src="/files/kLUe1Yoig80BJdGKOs8X" alt=""><figcaption></figcaption></figure>

#### Filters

Out of the box, Vesper search will show a content filter to end users, allowing them to filter their results if they are looking only for a particular Show/Series, or for a specific live stream.

<figure><img src="/files/cRJWxXD4mA2Wl7lRxjJ2" alt=""><figcaption></figcaption></figure>

#### Sort

The "relevance" sort is applied by default, which shows content which scores the highest with a given search term first. If two content items score identically, the results are then sorted by recency to show newer content first.

<figure><img src="/files/m9sKkb3m3484bUcK05vu" alt=""><figcaption></figcaption></figure>

Customers can instead chose to see all results in an alphabetical order, should that be preferable for finding specific content.

## How does it work?

Vesper will search across the metadata fields shown in the table below. If a match is found in a metadata field, it will be scored and added to the total score for that content asset. The final scores of each asset are then used to decide which asset is most relevant for the given search term.

<table><thead><tr><th width="196.3984375">Field</th><th width="120.3671875">Score</th><th>Notes</th></tr></thead><tbody><tr><td>Title</td><td>1.0</td><td></td></tr><tr><td>Description</td><td>0.05</td><td></td></tr><tr><td>Long Description</td><td>0.05</td><td></td></tr><tr><td><a href="/pages/9RQEU8Z6BqzpWwCb57rh">Typed Tags</a></td><td>0.8</td><td></td></tr><tr><td><a href="/pages/KC36eg6hsLD6BHFzs3TH">Participants</a></td><td>0.8</td><td>Matches on name of a participant</td></tr><tr><td><em>VOD only</em>: Series Title </td><td>0.0</td><td>Optional, off by default; Can be used to include a VOD's series title in the metadata.</td></tr></tbody></table>

For example, if your user searches the term "Last", and you have a series on the service called "The Last of Us", with a description "The events of last night catch up to Ellie", and a typed tag "Last chance",  the score will be 1.0 + 0.05 + 0.8 = 1.85.&#x20;

There is no maximum score an asset can be given by the search system.

#### Content type weighting

By default, this is off for all of Vesper Search. However if you wish to boost a specific content type (e.g. Series is more relevant to your searches than individual VODs) then a score is allocated to that type and added. For example a Series content type boost of 2.5 would heavily favour relevant series assets.

#### Can I boost a particular content asset in search?

Yes! If you want to match the content to a specific term, simply add the term you want the asset to match for as a typed tag, or even multiple typed tags. Each match will add the typed tag match value (0.8) to the final score - boosting that result for the given query.

If you want to simply boost a given asset so that if it is ever relevant to a particular query in any way it will be boosted, add a *regular* tag (**not** typed tag) to the asset following this format:

`searchBooster2`

Where 2 can be replaced with any number. The search system will multiply that asset's score by the given number (e.g. 2x).

#### How do I hide an asset from search?

As Vesper search is now fully user context aware, assets that are georestricted everywhere (and therefore only available to "universal" users on your system) will be hidden from search for your regular customers.

However if you want to ensure an asset can never be found in search, add the [noindex Tag](/platform-knowledge-base/consumer-experience/search/noindex-tag.md).

## What customisation options are available?

To refine the experience you provide to your end-customers, you have the following options.

#### Initial results

You can provide a default search query to filter the initial results shown to an end user. This can be any term. It will not be shown to the end user (who will continue to see your search placeholder text).

If you wish to have some editorial control over your search results; one option would be to set the default query to a term such as "INITIAL\_SEARCH\_RESULT". You can then add this value to a typed tag in Vesper VOD so that only VODs which are tagged with `INITIAL_SEARCH_RESULT` would be shown to users that land on this page.

To make this request, contact helpdesk with the query you would like to set as the default query.

#### Custom filters

Any typed tag can become a content filter. As an example, if you have added typed tags to you content to indicate "Genre" of the content, you can request that Genre becomes a filter for the search system.

<figure><img src="/files/YsWgMYEsjGYJgHTbnAxv" alt=""><figcaption></figcaption></figure>

To make this request, contact helpdesk confirming the typed tag name you would like to use. You may also be asked to provide the display name of the filter (and any translations) to be shown in the UI.

#### Displayed metadata

The metadata shown to the end user can be customised. For example the format of the title, including whether or not to include Series or Episode number information can be adjusted. The iconography in use to indicate series, seasons, playlists and episodes is also optional - as is the display of the number or episodes or the duration of a video asset.

<figure><img src="/files/gr04sE7GHBFQtwOxlWN0" alt=""><figcaption></figcaption></figure>

To customise this display, you are advised to contact your Platform Account Manager.

#### Search Ranking Scores

Two values specified in [#how-does-it-work](#how-does-it-work "mention") can be customised for your experience; Series Title (for VOD) and Content type boosters.&#x20;

For example, if you want to include series title for your VODs (so that a search for "Into the Badlands" would return individual VODs where relevant), you can request that value be set. Endeavor recommends 0.9 so that the series remains more relevant.

To change the rankings applied to your search results, contact the helpdesk using the template below:

***

**Subject:** Custom search ranking scores for \<service name>

**Detail:**

Please update the Vesper search ranking scores to be as follows

Series Title (for VOD): 1.5

Content type Series: 2.5\
Content type Live: 1.0

***

(Remove or add Content Type fields and scores as required)


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/consumer-experience/search.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
