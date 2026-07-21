> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/content/content-management/optional-partitions.md).

# Optional Partitions

## What is a Partition?

The optional partition experience refers to the ability to pick "Your Favourite team" on sign up. Each team refers to a separate "Partition", meaning that you can create bespoke and personalised experience based on which partition the user is associated with.&#x20;

## Setting up Partitions:&#x20;

To set up partitions you will need to speak with your Account Manager. However, you must have the following information before you do so;&#x20;

* List of Teams / Players that you want to display&#x20;
* Abbreviation of these teams / players (e.g Atlanta = ATL)
* Logos / Pictures for these teams and players&#x20;
  * 1:1 ratio
  * The higher resolution, the better.&#x20;
  * JPG/PNG format
  * Min 1024x1024 pixels
    * If the logo gets cut off, 347x347 is recommended

Once this information is available, then you can request set up with your Account Manager.&#x20;

## Choosing your Favourite Team

Setting up optional partitions will allow the user to be presented with a "Choose your favourite team" on sign up. See example below;&#x20;

Example

<figure><img src="/files/NffWxYzIZsR5U8WfYDhp" alt=""><figcaption></figcaption></figure>

Users also have the ability to switch teams. They can do this by;&#x20;

1. Navigating to their account page&#x20;
2. Choosing the account menu "Favourite teams"&#x20;
3. Then switching / choose their favourite team here

Example

<figure><img src="/files/0sYagJV6WDp7YCUM5OLG" alt=""><figcaption></figcaption></figure>

### Segment content based on partitions

Setting up optional partitions is most valuable when you can begin to create bespoke and personalised front end experiences based on what team the user has chosen. You do this by "Segmenting by Partitions". For more information on how to do this see the following links below;&#x20;

1. Segment your Hero by Partition - [Link](https://docs.onvesper.com/platform-knowledge-base/~/revisions/SZJs5bLGsYWhPfAqKYZq/back-office/content/content-management/segmentation)
2. Segment a Row by Partition - [Link](https://docs.onvesper.com/platform-knowledge-base/~/revisions/SZJs5bLGsYWhPfAqKYZq/back-office/content/content-management/creating-rows/segment-by-row)

<figure><img src="/files/dGnBJIMNd9QjXXsoKwWJ" alt=""><figcaption></figcaption></figure>

## End User Experience

Setting up the above will allow you to achieve the following use case;&#x20;

"As a content manager I would like to show a hero image of the England Flag and a dedicated row for England content to all user who pick "England" as their Favourite team".&#x20;

<figure><img src="/files/sXhGCgyYLImnx79oMExd" alt=""><figcaption></figcaption></figure>

Whereas if you had chosen "Italy" as your favourite team you will be shown a different hero and will not be presented with the England row.&#x20;

## Reporting & Analytics&#x20;

We have the ability to track and manage data for optional partitions on a per user basis allowing you to input this into a CRM or marketing tool. This allows you to determine which teams might be the most popular, giving you valuable insight to drive your content strategy.&#x20;

This data can be found in;&#x20;

1. **Vesper Insights** - The data point is "Partitions club" and can be found within the customer insights section of vesper insights - <https://docs.onvesper.com/platform-knowledge-base/back-office/vesper-insights/analytics-dashboards/dashboard-deep-dive/customer-insights>
2. **Data Export Syncs** - To set this up please speak to your Account Manager

To access or gain a deeper understanding on this data please speak to your Account Manager.&#x20;


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/content/content-management/optional-partitions.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
