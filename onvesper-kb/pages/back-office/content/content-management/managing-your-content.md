> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/content/content-management/managing-your-content.md).

# Managing your content

Once you’ve created your Hero and Rows you can edit fields and change the order that they appear to help your content stand out.

### EDIT AN EXISTING HERO/ROW <a href="#edit-an-existing-hero-row" id="edit-an-existing-hero-row"></a>

Go to the ‘Content’ page and select the three dots on the top right hand corner of the hero/row you wish to edit. NB: While you can't change a row's type—for example, from a Featured List of Playlists to a Basic Row of Videos—you can:

[‘Customise the Row Style’ ](https://docs.onvesper.com/platform-knowledge-base/back-office/content/content-management/pages/-LvKoeFfVsdV-s_Rbf8Y#stage-2 -–-customise-style)– to change the Title, Description, Background or add in a Call to Action button.

[‘Edit Translations’](/platform-knowledge-base/back-office/content/content-management/creating-rows.md#translations)  – to add / delete a language or edit the text.

[‘Publish the Row’](https://docs.onvesper.com/platform-knowledge-base/back-office/content/content-management/pages/-LvKoeFfVsdV-s_Rbf8Y#stage-5 -–-publish) – Don’t forget to hit publish once you’ve finished your edits. You’ll then see a small notification pop up on your screen confirming the change.

### CHANGE ROW ORDER <a href="#change-row-order" id="change-row-order"></a>

To move a row to a higher or lower position on the page, simply click on the row and drag it up or down. After completing your changes, click ‘Save’ on the bottom right. You will receive a notification confirming that your changes have been successfully saved.

### CHANGE CONTENT ORDER / PIN CONTENT

<figure><img src="/files/QIfyaquIBaQKmhR1Gzz0" alt=""><figcaption><p>Select the ... menu and chose "Order Content"</p></figcaption></figure>

To pin a video assets or playlist in the row so it appears first, find the row and select ‘Order Content’ from three dots drop down menu.

In the window which appears, you can chose to pin any content to be first in the row by chosing "PIN" in the ... menu. To unpin or re-order, simply chose "unpin" for content that is already pinned in a row.

<figure><img src="/files/XpgV63BEmudWdQ73ErY9" alt=""><figcaption><p>Pinning content</p></figcaption></figure>

<figure><img src="/files/SW4yb3OnttTUqzhadMt2" alt=""><figcaption><p>Unpinning content</p></figcaption></figure>

### DELETE A ROW

If you wish to change the row type or no longer want it to appear on the homepage,  find the row and select ‘Delete’ from three dots drop down menu.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/content/content-management/managing-your-content.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
