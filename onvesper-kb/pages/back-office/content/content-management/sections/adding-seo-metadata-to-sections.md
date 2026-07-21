> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/content/content-management/sections/adding-seo-metadata-to-sections.md).

# Adding SEO metadata to sections

If you are structuring your service to use multiple sections to house different parts of your content library, Vesper now supports defining the metadata you want to expose to web services about that section.&#x20;

Even if you don't use sections on your site, it's a good idea to set up your "home" section's metadata to make sure you're offering useful information to search engines regarding your home page. Please note that if you're using a custom welcome page to take full control over your SEO metadata, search engines are expected be directed to that welcome page and will index it as the preferred result for your site.

### Edit the section

Start by clicking the "..." next to your section name in Vesper back office, then click edit:

<figure><img src="/files/t1NFRCnZmxtUbF9t9PR4" alt=""><figcaption><p>Editing the "Drama" section</p></figcaption></figure>

You will see a dedicated part of the editor for "SEO"

<figure><img src="/files/Z2cH4fUeNPwEyGsUfpb0" alt=""><figcaption></figcaption></figure>

When editing a section, you can provide an image, title and description to be shown to web crawlers and social networks when links to your service are shared. You are also able to provide localised descriptions and titles if your service supports multiple languages.

<figure><img src="/files/06diATKRA8lkMizdccWa" alt=""><figcaption><p>A completed en_GB section</p></figcaption></figure>

### Test!

To test your config, you can simply paste a link to \<yourservicedomain>/section/\<yourSection> into most messaging services (WhatsApp, Slack, etc) and confirm that when sent, you see the preview you set up. Here's an example using Slack:

<figure><img src="/files/Yww5dNmwbTrUJKFYY6eM" alt=""><figcaption><p>Preview of the section shown in Slack</p></figcaption></figure>

You can also try using [Facebook's sharing debugger](https://developers.facebook.com/tools/debug/) to see more details.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/content/content-management/sections/adding-seo-metadata-to-sections.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
