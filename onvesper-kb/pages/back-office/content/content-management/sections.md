> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/content/content-management/sections.md).

# Sections

Sections’ are essentially a flat page or area where you can display specific content.

Each Section is a blank canvas for content curation, into which you can add hero images and content rows.

A platform manager can create a new section and curate that page in exactly the same way they do on Home & Browse, allowing for deeper content nesting and subcategorisation of content libraries.

### ADDING A NEW SECTION <a href="#adding-a-new-section" id="adding-a-new-section"></a>

In order to add a new ‘Section’ in, you need to go to ‘Content’ then ‘Section’. Next to the ‘Sections’ title you will see three dots, when you click on them the option to ‘Add Section’.

![](/files/-M-AwLAEXnQKuTe138K0)

When you click on ‘Add Section’, you will be taken to a new page where you can enter the title for the new section.

Once you have added in your new section, you will now see this appear in the list on the right hand side of the ‘Content’ page.

### POPULATING THE SECTION

After creating the new section, you can now populate this section with [hero images](/platform-knowledge-base/back-office/content/content-management/creating-hero-images.md)/[rows](/platform-knowledge-base/back-office/content/content-management/creating-rows.md) just as you would with the Home and Browse sections in Back Office.

You will need to access the newly created section from the “Sections” area on the right side of the “Content” page. Once you are in your new section you will notice that the page is blank as no content has been loaded onto this page yet.&#x20;

![](/files/-M-Awjd-0AVAfjX1ByRR)

If you select the 'Add Row' button on the right hand side, you will be taken through to the 'Choose Template' area.&#x20;

#### CHOOSING TEMPLATE

In the Choose Template section you can select from the three options below;

* Content Carousel: a row made of single videos using standard thumbnails.
* Playlist Carousel: a row made from playlist collections using vertical playlist cards, (mainly used for highlights).
* Navigation Carousels: a row made by linking to existing sections.

If you select either Content or Playlist Carousel then you can follow the steps as per [Creating Rows](/platform-knowledge-base/back-office/content/content-management/creating-rows.md).

We would recommend selecting 'Navigation Carousels' then select either “Basic Navigation” or “Featured Navigation”.

![](/files/-M-AwvYIJDDEuZE6L9ls)

#### CUSTOMISE STYLE

In the Customise Style section with 'Basic Navigation' you will just need to enter in a title only and with 'Featured Navigation' you will need to fill out the following;

* **Background Image**: This is the image that will in sit in the background of the Featured Navigation. Its recommended size for this is 1920×601. (***NB: choosing an image approx. 50-100 pixels above the recommended size tends to ‘look better’***)
* **Title**: Title of the row that will sit above the row
* **Description**: Information about the row, which will sit below the title
* **CTA**: The Call to Action button

#### CUSTOMISE CONTENT

In the Customise Content section&#x20;

* **Section Title:** Title for each of the sections
* **Section:** Each section will need to be linked to 'Sections' that have already been created in 'Content'&#x20;
* **Background:** Add a video and an image to your Section to help the content stand out.&#x20;
  * ***Selection Image:***  This image will be the cover image for the section and it will need to be 500x500
  * ***Video On Hover:*** This video will play when the user hovers over the thumbnail. The video will need to be a short muted MP4 Video and 300x300

When a customer hovers over a Section either a video will play, otherwise the image will just be displayed.

![](/files/-M-Ax2L1Yh1Qm-iS7U3H)

Once you have filled in the above details, click on 'Save'.&#x20;

If you need to add more sections to the row then you will  need to select 'Add Section' button, underneath the newly created section and follow what you have done previously.

![](/files/-M-AxEK2V0ShtGbyp84D)


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/content/content-management/sections.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
