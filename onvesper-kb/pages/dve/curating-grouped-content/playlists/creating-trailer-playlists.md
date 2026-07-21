> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/dve/curating-grouped-content/playlists/creating-trailer-playlists.md).

# Creating trailer playlists

With trailer playlists, content managers can arrange a **free** asset before a paid/sign-up-to-watch VOD so guest users can get a glimpse of the content before they commit to purchasing or registering to the platform to consume a related premium asset.

### Configuration steps

1. Design a specific tag for your free assets (such as FREEFORGUESTS), which will sit at the top of your playlists.
2. Integrate the tag into Vesper VOD when uploading and publishing your free VOD content.

<figure><img src="/files/znnhE1JuYCutvtooZOnQ" alt=""><figcaption><p>Design a specific tag for free assets and include it as metadata when publishing your VOD</p></figcaption></figure>

1. Place the free asset first: when curating content for the playlist, ensure the asset with the free tag is the first on the list.&#x20;
2. Follow up with Premium content: the next asset in the playlist should be premium content, which will be locked behind a sign-up or purchase prompt for guests.&#x20;
3. Go to Vesper Admin -> Licences -> Package Licences and modify your Guest licence to restrict VOD content with the specific tag for your free assets.

<figure><img src="/files/AqtU4dU287iyR0ORdRnR" alt=""><figcaption><p>Use the specific add targeting your free events and include it in your Guest licence</p></figcaption></figure>

4. Confirm the changes and save the new licence configuration.
5. Visit your playlist as a guest user on the front end and you'll see the first event being made available for free (no padlock) whilst the second one will be padlocked.

   <figure><img src="/files/6lAltL6an9WJfO8EH7PK" alt=""><figcaption><p>The first event of the playlist is offered for free</p></figcaption></figure>
6. The guest user will be able to consume the trailer and once the second premium asset is loaded, the user will be prompted to sign up/purchase.&#x20;
7. After the sign up/purchase flow is completed, the user will be able to playback the premium asset.

&#x20;


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/dve/curating-grouped-content/playlists/creating-trailer-playlists.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
