> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/dve/video/typed-tags/typed-tags-best-practices.md).

# Typed Tags: Best practices

[Typed tags](/platform-knowledge-base/dve/video/typed-tags.md) allow the association of structured text metadata with VOD assets. We recommend reading [Typed Tags](/platform-knowledge-base/dve/video/typed-tags.md) before this page!

Below are some best practices to adhere to when planning how to send metadata to Vesper.

### Enum or Text?

Enum types are useful when you have a very strict set of possible values that you expect to never change. If you have colleagues updating VOD metadata and it is essential they never input unexpected values (for example if you are building an integration with Vesper that relies on certain values in a specific tag), then an enum is a powerful input validation mechanism.

For all other use cases, the flexibility of a Text typed tag is generally recommended. It will allow you to define new values without becoming blocked and requesting support from the Endeavor Streaming team. We generally recommend that most Typed Tags are Text.

### Preparing data for display on an interstitial page

An [interstitial page](/platform-knowledge-base/consumer-experience/interstitial-pages.md) allows for displaying of typed tags to expand on the VOD metadata to show more information about the content.&#x20;

<figure><img src="/files/gmOpP1W6S0VoH0TNCxMX" alt=""><figcaption><p>Example of video metadata plus typed tags</p></figcaption></figure>

The output above demonstrates the two different ways a "text" tag could be shown. The actors/cast are output as values only (e.g. "Kate Winslet", "Jack Black"), whereas the director tag has had an English language label added to the template ("Director: ").

{% hint style="info" %}
At time of publication, Typed Tag metadata is not multi-lingual. If your service is offered in a single language then the tag values and a label can be applied. This feature is not currently suitable for multi-lingual services.
{% endhint %}

As an example, the tag input for the above screenshot would be:

| Type          | Value        | Visibility  |
| ------------- | ------------ | ----------- |
| Genre         | Drama        | User Hidden |
| Year Released | 2006         | User Hidden |
| Director      | Nancy Meyers | User Hidden |
| Cast          | Cameron Diaz | User Hidden |
| Cast          | Kate Winslet | User Hidden |
| Cast          | Jude Law     | User Hidden |
| Cast          | Jack Black   | User Hidden |

Each value for "Cast" is output on the interstitial page between a • character.

If you wished to add a "Cast" label, with separated values above Vesper would output:

```
Cast: Cameron Diaz • Cast: Kate Winslet • Cast: Jude Law • Cast: Jack Black
```

If you wished to instead output the entire Cast in a list rather than separated values, the input would need to be:

| Type          | Value                                            | Visibility  |
| ------------- | ------------------------------------------------ | ----------- |
| Genre         | Drama                                            | User Hidden |
| Year Released | 2006                                             | User Hidden |
| Director      | Nancy Meyers                                     | User Hidden |
| Cast          | Cameron Diaz, Kate Winslet, Jude Law, Jack Black | User Hidden |

Using the above structure allows Vesper to output&#x20;

```
Cast: Cameron Diaz, Kate Winslet, Jude Law, Jack Black
```

With a single text block label for "Cast".

### Typed tags for search and filtering

Providing data as a list with commas is only recommended for the purpose of displaying on the interstitial page. If you do provide the list option you are encouraged to provide **both** the individual items **and** a list under a different tag name.

| Type   | Value                  | Visibility  |
| ------ | ---------------------- | ----------- |
| Genre  | Drama                  | User Hidden |
| Genre  | Comedy                 | User Hidden |
| Genre  | Romance                | User Hidden |
| Genres | Drama, Comedy, Romance | User Hidden |

By presenting the data this way, Vesper will still be able to use Typed Tags in our future search and [grid](/platform-knowledge-base/consumer-experience/grid-view.md) pages as shown below.

<figure><img src="/files/5MW6zce6TBI1TSARhnGY" alt=""><figcaption><p>Genre filtering</p></figcaption></figure>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/dve/video/typed-tags/typed-tags-best-practices.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
