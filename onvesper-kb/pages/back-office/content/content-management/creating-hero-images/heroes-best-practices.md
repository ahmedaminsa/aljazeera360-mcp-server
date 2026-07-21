> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/content/content-management/creating-hero-images/heroes-best-practices.md).

# Heroes: Best Practices

Heroes are the one of the first pieces of content that a user will consume and are a key promotional tool/incentive for end users into further content consumption on the platform. As such, it is extremely important that the hero is cleanly constructed and displays appropriately across your application suite. The very simplest approach to deploying heroes is to simply have a single image that fits across all platforms, ideally with the focal point of your image being centralised in the image so that it scales well on small and big screens.

However, to maximise the impact of your assets, you can use Vesper's segmentation system to define 2 hero segments, 1st for Web/TV devices and a 2nd for mobile devices.&#x20;

Vesper allows the upload of both landscape and portrait orientation hero assets for every hero slide. If you would like further control of the hero (for example to change the length of description shown on mobile apps), our recommendations are as follows (please refer to [Hero Segmentation](/platform-knowledge-base/back-office/content/content-management/segmentation.md) for further information on segmenting for device restrictions i.e. Browser/TV/Mobile segments):

* Hero creative should have an image size of <mark style="background-color:orange;">**1920x1080**</mark>
* When designing hero creative:

  * Since text, CTA's and overlay gradients are configured on the platform, always consider a neutral spaces/areas in your creative where the text, CTA's and gradients will overlay
  * Browser/TV segments and landscape images: the image subjects should populate the <mark style="background-color:blue;">**left hand area**</mark> of the image, with a neutral background on the <mark style="background-color:blue;">**right and bottom areas**</mark> to allow for configured gradients and text to overlay

  <figure><img src="/files/jOXLnnGYptotJ8skivrU" alt=""><figcaption></figcaption></figure>

  * Mobile segments and portrait images: the image subjects should populate the <mark style="background-color:green;">**center area**</mark> of the image, with a neutral background on the <mark style="background-color:green;">**left, right and bottom area**</mark> to allow for device with restrictions alongside configured gradients and text to overlay

  <figure><img src="/files/7mnmd8jDQl2YfBbS9jK6" alt=""><figcaption></figcaption></figure>
* Following the above creative guidance, the best practice for text placement and gradient overlays is as follows

  * Browser/TV segments:
    1. Horizontal alignment: <mark style="background-color:blue;">**Right**</mark>
    2. Vertical alignment: <mark style="background-color:blue;">**Center**</mark>
    3. Gradient Overlay: <mark style="background-color:blue;">**Right and Bottom**</mark>
    4. Text alignment: <mark style="background-color:blue;">**Right**</mark>

  <figure><img src="/files/I4xE38n4EXgRn876vYSJ" alt=""><figcaption></figcaption></figure>
* Mobile segments:

  1. Horizontal alignment: <mark style="background-color:green;">**Center**</mark>
  2. Vertical alignment: <mark style="background-color:green;">**Middle**</mark>
  3. Gradient Overlay: <mark style="background-color:green;">**Bottom**</mark>
  4. Text alignment: <mark style="background-color:green;">**Center**</mark>

  <figure><img src="/files/2vXV2qv0yvVK3Zu8PxXU" alt=""><figcaption></figcaption></figure>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/content/content-management/creating-hero-images/heroes-best-practices.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
