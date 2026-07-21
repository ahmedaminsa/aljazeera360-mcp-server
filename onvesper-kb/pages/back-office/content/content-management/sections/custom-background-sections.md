> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/content/content-management/sections/custom-background-sections.md).

# Custom Background Sections​

Vesper Back Office users can now set custom backgrounds for any section page including the service homepage, with the ability to upload background images.

​The backgrounds can be configured to be device-specific across web, TV and mobile apps for maximum flexibility in showcasing your brand.​

## Add a custom background to a section.

### **Step 1: Edit the section.**

Start by clicking the "..." next to your section name in Vesper back office, then click Edit:![](/files/M3Ag7fZoniD323iE2v8E)

### **Step 2: Upload your background image.**

Once you click Edit the side menu will appear, scroll down to Background. Here you can upload your background image. Recommended image size is 1920x1080, less than 1MB in size and the format PNG, JPEG, or JPG:

<figure><img src="/files/22ASZmc8eVE63xb5dkBA" alt="" width="361"><figcaption></figcaption></figure>

### **Step 3: Image Fill Style, Image Opacity, Background Colour and Gradient Overlay.**

Before you can update your section background image you must specify Image Fill Style and Image Opacity.

**Image Fill Style:**

* Fixed (Full Width) - The image will render to the width of the background space and remain static when a user scrolls through content rows.
* Repeated Vertically (Scrolls)\* - The image will repeat as a user scrolls down the page.\
  \* This is best used when the image asset in question is a subtle overlay of shapes/vectors or gradients. It will not work well with branding and strong iconography.

**Image Opacity:** Set the transparency or translucency of an image. 100% opacity = solid image, 0% opacity = completely transparent image.

**Background Colour:** Background colour will add a colour gradient to an image dependent on opacity. If no background image is used, then this would be the section's background colour. To set colour, either enter the Hex code or select from the colour picker.

**Gradient Overlay:** Set a gradient overlay with the option of left, right, top and bottom gradient fill, to go on top of the background image.

<figure><img src="/files/B603azR1vNJHJ7PeTzHh" alt="" width="354"><figcaption></figcaption></figure>

Click **Update** to save changes and publish to the front end.

## Best Practices

We recommend using subtle/partially transparent imagery as a background image. See examples below.

**Background with 100% opacity:**

<figure><img src="/files/IwaYxVEJQ7yze25Laj9P" alt=""><figcaption></figcaption></figure>

**Background with 50% opacity:**

<figure><img src="/files/vDJeEB6sT3gNxs63sDhC" alt=""><figcaption></figcaption></figure>

**Gradient Overlay**

If using the Repeated Vertically (Scrolls) image fill style, it is recommended to use the bottom and top gradient on the image to avoid hard edges.

**Background when all gradient overlays are selected:**

<figure><img src="/files/Xr30Scozk1PmgYGbun4H" alt=""><figcaption></figcaption></figure>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/content/content-management/sections/custom-background-sections.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
