> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/content/content-management/creating-hero-images.md).

# Creating Hero Slides

A Hero Image can be created in 3 simple stages. To begin, navigate to the Back Office, and under the Content tab, select 'Content Management', then 'Create New' -> 'Hero'.

<figure><img src="/files/q0hsvTgxxu4x9xSwk06N" alt=""><figcaption></figcaption></figure>

### STAGE 1  – CREATING A HERO <a href="#stage-1-customise-hero" id="stage-1-customise-hero"></a>

<figure><img src="/files/6juwQ2fkUUOKcocvMOWN" alt=""><figcaption></figcaption></figure>

Here you’ll need to ‘add’ your hero image. If there was already a hero image on this platform it would appear here, otherwise, it will always state ‘No Heroes’. All hero images must be **1920 x 1080 .jpeg** and under **1mb** in size. If needed, you can reduce the image using a compressing tool such as [TinyJPG](https://tinyjpg.com/) or [Squoosh](https://squoosh.app/) or exporting for optimized quality using your photo editing software (Adobe PS or Sketch).

In addition to the **required landscape-format** background image, Vesper now allows for the addition of an **optional portrait** background for use on mobile web and apps (starting from version 4.21.2). We recommend using a 640x960 PNG file with a transparent background for this portrait image. Although optional, it is advised to use a dedicated hero segment to better target mobile devices. For further recommendations, please refer to [Heroes: Best Practices](/platform-knowledge-base/back-office/content/content-management/creating-hero-images/heroes-best-practices.md).

Adding Info To Your Hero:

* **Background:** This is the image uploader.
* **Title:** This function is the main title of the hero
* **Description:** Provide further information for the hero
* **Optional Additional Information:** This allows the user to input Tagline, Channel Logo & Title Image
  * Tagline: Extra Information about the hero image
  * Channel Logo: Small Logo
  * Title Image: Image describing the content See Display below (If a title image is uploaded this will overwrite the Title text of the hero input previously)
* **Primary CTA Button:** Allows you to link an asset corresponding with the Hero message
* **Text:** the Call To Action (CTA) on the button e.g. Watch Now, Watch Here, Click Here
* **CTA Content Type:**&#x20;
  * Live: Links to a Live event on the platform
  * VOD: Links to a single VOD asset on the platform
  * Playlist: Links to a playlist or list of videos on the platform
  * Shows: Links to a playlist that is grouped in a selection
  * External: Links to an external site or link
  * Auto: Links to the first Live event, or the most recently added VOD if there is no Live event
* **Entity ID:** is the video, playlist or live event ID. This will only be available for selection when Live, VOD or Playlist entity types are selected for the CTA Content Type.
* **Link:** Is the url or address of the external link you wish the CTA to action when you select External for the CTA Content Type

{% hint style="info" %}
Important note: if the linked piece of content is not available for purchase on the device targeted in the hero, the hero will not be displayed at all to avoid user bad experience. i.e.: to prevent this when the hero is focused on marketing PPV events, its CTA should be hidden or should link to a section
{% endhint %}

* **Secondary Button:** Is the option to have more than one CTA on the hero image

As you fill the information above on the left-hand side, a preview of how your Hero will appear will show on the right-hand side.

![](/files/-MQCc34kCps41lQ7kLBf)

You have four alignment sections to help make the text stand out;

* **Horizontal Alignment:** Changes the positioning of the Hero text and CTA info to Left, Middle or Right of the screen
* **Vertical Alignment:** Changes the positioning of the Hero information to Top, Middle or Bottom
* **Text Alignment:** Changes the text alignment from Left to Right, Right to Left or Centred
* **Gradients Overlay:** To add gradients to your uploaded picture, select the Area of the picture you want to add a gradient to in from the options presented. The gradient will provide a subtle blend from black, we’d definitely recommend leveraging this.

### STAGE 2 – ADDING MORE SLIDES (HEROES) <a href="#stage-2-translate" id="stage-2-translate"></a>

To add more than one hero at one time click the '**+ Add**' slide button in the top right of the modal and complete the above process.

<figure><img src="/files/FcDOKhMte8gSaoVKYwDx" alt=""><figcaption></figcaption></figure>

### STAGE 3 – TRANSLATE <a href="#stage-2-translate" id="stage-2-translate"></a>

In the next step, you can translate the text that appears alongside your hero. The default language of your realm is set at the start of your Vesper Realm. If you wish to add another translation for your hero, you can do so by selecting the three dots on the Translate step.

<figure><img src="/files/DbVaqO9ZpWFnUMLv4ljF" alt=""><figcaption><p>Adding another translation for your hero</p></figcaption></figure>

### STAGE 4 – PUBLISH <a href="#stage-3-publish" id="stage-3-publish"></a>

Click Publish and your hero image will appear across the top of the home page, you can add in up to 8 hero images on your platform. This will create a slideshow of hero images across the top of the platform.

Front End Display example:

![](/files/-MQCcpolHrNALDnbp64J)


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/content/content-management/creating-hero-images.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
