> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/content/content-management/creating-rows/step-by-step-row-creation-guide.md).

# Step By Step Row Creation Guide

**Example:** Creating a Landscape Season Row

![1. Click Add Row](/files/-MQGri8UmZmSdO1fubM-)

![2. Choose Playlist Carousel ](/files/-MQGrvdQXNXS7Y8mlGE4)

![3. Choose which type of Row Style you wish to use ](/files/-MQGuyxwnpNbbHYNx-Vr)

![4. Choose which type of Row Display Style you wish to use ](/files/-MQGvH9LvjDPdkwbNbde)

![5. Enter your title and toggle the Hide Metadata button if you wish to hide the build in platform metadata overlay](/files/-MQGvaoyzjubkK00Yq1D)

![5.2 This will remove the "Video Title" from the bottom of the card](/files/-MQGvnfSz7Jhuj3ZdtUT)

![6. Select List of Seasons from the Type Dropdown](/files/-MQGw6wlavqC4hawe-lU)

**Tags:** This is what will power your row. The tag that you choose must already exist within the [DVE](/platform-knowledge-base/dve/overview.md) on a subset of Playlists relevant to the content row that you are creating.&#x20;

#### **To add a navigation anchor to your row**

To add an Anchor Menu Icon, please upload an Alpha PNG 25px x 25px

![](/files/-MSbSHGa-qK7W1QUXoLE)

This is not compulsory but if it is not added the category will not appear as anchor on the left hand side of the Front End Navigation next to your VOD Library.&#x20;

![](/files/-MSbQGrXWe-M9LABZyOR)

Within the DVE use a consistent tag for all playlists that you wish to populate in this row. eg NUEVOROW

<br>

![](/files/-MQGys_eJuNJqsQnuAx7)

![The dropdown will populate with all existing tags available](/files/-MQGz3pJaDpMAuAbUnKQ)

The order can be chosen based on the way you wish to display the row.&#x20;

![7. If you wish to add another language you can do this by clicking the burger on the left hand-side](/files/-MQGzNBWhD3IXOvvGQhb)

Once all is complete click Publish in the top left

The row will populate at the bottom of you Content Section on Dice Admin&#x20;

![](/files/-MQH-FIm4f2TqVRzFXoQ)

You can move the order of where this row is placed by pressing the navigation arrows or dragging and dropping to another order in your content list.&#x20;

Between 1 and 5 minutes later your new content row will populate on your platform.&#x20;

![](/files/-MQH0qeEt6gDsS5e1nd5)

#### Metadata display modes

The default settings are for Video Metadata and Duration info to be displayed see image below:

![](/files/-MSbShdTZ5nyQ9xjnxhw)

If you wish to not display this information, or wish to display it below content cards, Go back to this Row in Dice Admin.

<figure><img src="/files/ASSSeTiXidCucIBEe1TP" alt=""><figcaption></figcaption></figure>

Click the boxes you wish to hide on the Front End. You will have the options to display metadata in a new order on the card thumbnails.

1. Overlay show metadata = default metadata style with metadata on the card\
   ![](/files/WQYnqzG8CqLbpF0myz5X)
2. Overlay hide metadata = hides some metadata on the overlay card style\
   ![](/files/pszT70s0bg9k1Uh10YPI)
3. Stacked metadata = All metadata is shown below the card (description is still shown on the thumbnail on hover on web)\
   ![](/files/ZxUTtDmLZqZE9vmI2wRs)
4. Hide Duration flag will allow you to hide or display the duration of single VOD's on the thumbnail

Click "Next" & "Publish" to implement this on the Front End. The changes may take up to 5 minutes to be displayed on the FE.&#x20;

![](/files/-MSbVidUZmC4UJ411sOc)


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/content/content-management/creating-rows/step-by-step-row-creation-guide.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
