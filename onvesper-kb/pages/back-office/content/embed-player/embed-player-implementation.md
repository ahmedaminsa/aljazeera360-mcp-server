> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/content/embed-player/embed-player-implementation.md).

# Embed Player Implementation

Once config has been completed as described in [Embed Player Config](/platform-knowledge-base/back-office/content/embed-player/embed-player-config.md) then you can proceed to implement the embed player code into your respective web page(s).

Firstly, select the required asset you want to embed. This can be VOD or Live (of note, upcoming events can also be embedded and a countdown will be presented).

<figure><img src="/files/bcIZOdGG9IzbC4rcIOds" alt=""><figcaption></figcaption></figure>

**VOD Selection**

<figure><img src="/files/P6SKdnVQvhpqOjVViyot" alt=""><figcaption></figcaption></figure>

**Live Selection - Upcoming Event**

<figure><img src="/files/bWWEEs1HFOiBoRmC022D" alt=""><figcaption></figcaption></figure>

**Live selection - Currently Live Event**

<figure><img src="/files/wbSBEIXkNEE0Jz9sRcIM" alt=""><figcaption></figcaption></figure>

Once you have selected your content, please ensure you have selected the correct embed config as related to your particular implementation (you can have several configs, for example on per team basis with varying logos/branding).

<figure><img src="/files/409SiLzdVdCXRlO1Xgg3" alt=""><figcaption></figcaption></figure>

The code is now ready for insertion into your web page(s) upstream of the ES web application! **Here is a sample test HTML page made with the player embedded**&#x20;

{% file src="/files/zPdBbD7v0BBiGWxLWzzM" %}

<figure><img src="/files/QCGnyben8zUg0oadQxE4" alt=""><figcaption></figcaption></figure>

Styling/placement/resizing can be achieved with HTML styling and must be done by the website owner.\
For example, you can horizontally fit to page with the below modification of the HTML code:

**Before editing:**

```
<iframe src="VIDEO_URL_HERE" title="Embed player" width="560" height="315" frameborder="0" allow="autoplay; encrypted-media; picture-in-picture;" allowfullscreen></iframe>
```

**After editing:**

```
<div style="padding:56.25% 0 0 0;position:relative;"><iframe src="VIDEO_URL_HERE" title="Embed player" style="position:absolute;top:0;left:0;width:100%;height:100%;" frameborder="0" allow="autoplay; encrypted-media; picture-in-picture;" allowfullscreen></iframe></div>
```

This modified implementation appears as below on our sample test page:

<figure><img src="/files/3bmgIbkNRXhdqbBXyRpr" alt=""><figcaption></figcaption></figure>

**Sample HTML of a fit-to-page amendment can be found below:**

{% file src="/files/cu3LBS0MeSMMt215mhzR" %}

While this should be straightforward for a web developer to accomplish, further reading can be found here for styling options of the HTML iframe here: <https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe>

{% hint style="warning" %}
If Sticky Player is desired, additional code will need to be inserted before the embed player code to implement the Sticky Player SDK

`<script defer`\
&#x20;  `src="`[`https://doris-embed.diceplatform.com/sticky-player/1/sticky.min.js`](https://doris-embed.diceplatform.com/sticky-player/1/sticky.min.js)`">`\
`</script>`
{% endhint %}

**Sample HTML example, including Sticky Player SDK implementation**

{% file src="/files/Z5wiRBXD9xvSp7qtbG0w" %}

### "Start at" time parameter

If you wish to start a VOD at a specific time, see [Link to a moment within a video](/platform-knowledge-base/consumer-experience/web/link-to-a-moment-within-a-video.md#link-to-a-moment-of-a-vod-with-embed-player) for how to add the `s=` parameter to your embed code.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/content/embed-player/embed-player-implementation.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
