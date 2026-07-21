> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/content/content-management/creating-rows/creating-an-epg-row.md).

# Creating and Editing an EPG Row

## Creating An EPG Row

On the page you wish to create an EPG click Add row in Back Office.

{% hint style="info" %}
If you don't see the Electronic Program Guide (EPG) row, it's likely that this feature isn't enabled for your account. To access it, please get in touch with your Commercial Account Manager or Technical Account Manager.
{% endhint %}

![](/files/-MQCop56UwGojfZbrhZ1)

In the Row Templates section choose Electronic Program Guide.

There are 4 different EPG Options to choose from:

* Basic Grid - Basic EPG Layout
* Feature Grid - Basic EPG Layout with a background image
* Now/Next Cards - EPG layout that indicates Now, Next and Later
* Featured Now/Next Cards - EPG Layout that indicates the above with a background image

Once the template is selected give your EPG a title. This is not displayed anywhere on the front end.&#x20;

Next Add Channel:

There are two Channel Types -

* Curated - Powered by content from the [VLL Channels ](/platform-knowledge-base/vesper-studio/broadcaster.md)created and curated in Vesper Studio.
* Favourite - A channel that is curated automatically if the user has clicked Favorite on a specific Channel in the UI.&#x20;

Category Label:

This will Group your channels in specific themes: Eg Comedy, Action etc.&#x20;

If your Category has already been created you can select it from the dropdown:

![](/files/-MQQuuajrp73VufMLLcg)

This will group the channels on the Front End into distinct categories.&#x20;

**Creating a Category**

If you wish to create a new category. Click "Add New Channel" & Select "NEW"

Entire the title of your new Category in "Category Label\*"

To add a Navigation Icon please upload an Alpha PNG 25px x 25px

This is not compulsory but if it is not added the category will not appear on the left hand side of the Front End Navigation next to your EPG.&#x20;

![](/files/-MSbPJJPPO6rJf2o6oVI)

Next, select the channel you wish to program to the EPG by typing keywords or the channel name into the Select Channel box

![](/files/-MQQvJN6GY_2msFIqmVj)

Click on the channel you wish to include. You can then add additional channels by clicking the add additional channels button to this Category or continue by Saving.&#x20;

Click Next > Publish. This channel will not be saved to your EPG.&#x20;

![](/files/-MQR4PCROq6HqHqF3a4Z)

## Editing Your Existing EPG

Once your EPG row has been created you are able to edit it at any time.&#x20;

Click edit on the burger option within the Bucket on your Content page.&#x20;

![](/files/-MQR0BkaLj8Ce1s3AbCq)

Here you can add more channels to existing rows, change the order of the categories or channels within a category or delete channels from the EPG entirely.&#x20;

**Adding a New Channel**

To add a new channel scroll to the bottom of the customize section and click Add Channel. Complete the process listed above to create a new channel.&#x20;

**Changing the order of a Category**

If you wish to change the order of a category in the EPG display this can be done by clicking on the **BOLD** category title and dragging to your preferred area on the EPG please see the animated example below.

![](/files/-MQR2KZnPcJw0FbsH_XD)

**Deleting a channel**

To delete a channel from your EPG, go to the required channel in your EPG list and select the burger on the right hand side of the channel pod.&#x20;

![](/files/-MQR4sXDpPYaYCS9grBW)

Click delete and this channel will be removed from the EPG.&#x20;

**Deleting a Category**

If you wish to delete an entire category go to Edit EPG in Dice Admin

![](/files/-MSbWT4Pl-ZLnO_GwqgQ)

Select the category you wish to delete:

![](/files/-MSbYknVeiKBz2l3XFNW)

Click Delete

NOTE: This will delete all channels from the EPG on the front end but will not affect any distribution of these channels and they can be added back in by Creating a New Category once again or adding to an existing category.&#x20;


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/content/content-management/creating-rows/creating-an-epg-row.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
