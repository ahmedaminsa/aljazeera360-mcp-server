> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/dve/video/trailers.md).

# Trailers

Trailers are a vital component for end users to learn more about a content prior to committing to watching the entire asset and give viewers an idea of what they can expect. Trailers are a great way to give a preview of an upcoming release, episode, event, or movie.&#x20;

On Vesper, trailers can be used in combination with [Scheduling Releases](/platform-knowledge-base/dve/video/scheduling-releases.md) to provide a preview of an upcoming episode or featured release. Trailers are also a great way to show a preview of gated content to all users, encouraging sign up or purchase to access the full release.

## How to Configure

#### 1:  Create the trailer in the VOD platform

A trailer is created from the VOD page by clicking on the `+` icon and selecting trailer.&#x20;

The creation flow is similar to [creating a VOD asset](/platform-knowledge-base/dve/video/metadata.md) as they have similar sets of metadata you can add.&#x20;

<figure><img src="/files/FyvEQyGqXM9nMTrNQFLD" alt=""><figcaption></figcaption></figure>

Once saved, your trailer will appear in your platform’s content list, marked by a Trailer icon.

<figure><img src="/files/XqgNCZwzFmPofZDppew6" alt=""><figcaption><p>Example of a trailer listed in Vesper VOD</p></figcaption></figure>

{% hint style="warning" %}
Be sure to publish the trailer so it is accessible to your users.

Published trailers **will not appear** in the *"Recently Added"* or *"Continue Watching"* rows of your platform.\
\ <img src="/files/XyNSu7dHxRrV8K8UblkY" alt="" data-size="original">
{% endhint %}

#### 2: Link your trailer to an entity&#x20;

A trailer can be associated with additional entities such as *VODs, Seasons, or Series* and this association/linking, can be done either in the creation flow from the trailer detail page, or from the entity page (VOD, Season, Series detail page in Vesper VOD).

<figure><img src="/files/cr7nkICxmuORshIh2iO7" alt=""><figcaption><p>Trailer Creation Flow</p></figcaption></figure>

<figure><img src="/files/MG0ERsmIObbK9ze6xHBz" alt=""><figcaption><p>Trailer detail page indicating what entities a trailer is associated with</p></figcaption></figure>

#### 3: \[Optional] Process trailers at a different preset&#x20;

A trailer can be processed at a different encoding preset to that used for a standard VOD.  This can be configured at a customer/Resident level

* A Customer (Resident) can define the trailer encoder preset&#x20;
* Where a trailer preset isn’t set, the VOD preset is used to process trailers.

<figure><img src="/files/OvemUKStfxsMhyJsnzoQ" alt=""><figcaption></figcaption></figure>

## Results

Once the trailer is linked and published, users will see a **Trailer** button on the associated content/playlist/collection’s interstitial page, allowing them to view the Trailer before watching the full video.

<figure><img src="/files/GSoheudIspzHXAGCdpIs" alt=""><figcaption><p>Trailer button on a content's<a href="/pages/Jn04gNFCLgsB7DMrlWCR"> interstitial page</a> (Subject to change)</p></figcaption></figure>

<figure><img src="/files/UurkpJEHhJgm2AJEYPLU" alt=""><figcaption><p>Trailer associated to a <a href="/pages/ClisopC6UsYnweQ7EeVk">Scheduled Release</a> (Subject to change)</p></figcaption></figure>

### Trailer-specific tag and Licencing <a href="#trailer-specific-tag-and-licencing" id="trailer-specific-tag-and-licencing"></a>

All trailers are automatically tagged with **type:trailer**, which can be used to allow non-subscribed users or guests to have access to trailer, even if they don’t have permission to watch the full content.

To configure trailer-specific access:

On [Vesper Back Office](https://backoffice.onvesper.com/), \
Go to *Licences* → *Package Licences* → Look for the relevant licence → *Edit* → Go to the “*Add Content to Licence*” section → Add the *"type:trailer"* tag for VODs (see example below)

<figure><img src="/files/pjyvmb5OIMQ3IAfQk0fo" alt=""><figcaption><p>Adding the type:trailer tag to a licence</p></figcaption></figure>

This configuration can be useful for giving potential viewers a taste of your content, encouraging them to subscribe/purchase while restricting access to the main content to paying customers.

### FAQs

* **Where does the trailer appear?**&#x20;
  * From the video details page
* **Are trailers supported on Interstitial pages?**
  * Yes, support is planned on [interstitial pages ](/platform-knowledge-base/consumer-experience/interstitial-pages.md)(Season/Playlist/VOD) soon
    * Series-level trailer is not planned for support at this time&#x20;
* **Are trailers considered an individual asset?**&#x20;
  * No, they will not appear as an individual asset, therefore they cannot be searched on the frontend&#x20;
  * Residents can search trailers based on "title" in the VOD platform&#x20;
* **Will trailers appear in the "recently added" row in the CMS?**
  * Trailers will not be included in the recently added row. They are not returned as individual VOD assets in content rows&#x20;
* **If the content is geo-restricted, can end users see the trailer?**
  * No, if content is geo-restricted, the end user will not be able to view the trailer. This is also applicable if the content has a content rating that is restricted ([e.g. child profiles](/platform-knowledge-base/consumer-experience/profiles.md))&#x20;
* **Can I pull a report on trailers?**
  * Viewing analytics for trailers are similar to VOD analytics&#x20;
  * Vesper does not track watch progress for trailers and allow users to pick up where they left off&#x20;
* **Can I use onboarder API or** [**batch tooling**](/platform-knowledge-base/dve/batch-video-upload-via-ui.md) **to upload trailers?**
  * Onboarder APi is supported, batch tooling to be supported by year-end 2025.
* **Can I convert an existing regular VOD into a&#x20;*****trailer*****?**
  * Regular VOD cannot be converted into *trailers.* Residents will need to create new *trailers* as a separate video type and delete the original VOD assets


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/dve/video/trailers.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
