> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/content/content-management/creating-rows/row-segmentation.md).

# Row Segmentation

## Introduction&#x20;

Row Segmentation allows you to create dedicated rows specific to a geographic regions, entitlements, partitions, devices or user authentication status. This enhances the user experience by creating bespoke and personalised content rows for specific subsets of users.&#x20;

Combining multiple segmentations will enrich the content offering provided to your user base. If you wish to provide multiple segments and complex targeting, then familiarity with the segmentation priority rules applied on Vesper is recommended. Read more at [Content Segmentation Priority and rules](/platform-knowledge-base/back-office/content/content-management/content-segmentation-priority-and-rules.md).

## Back Office configuration

{% stepper %}
{% step %}

### Create a generic row&#x20;

* On Vesper Back Office, go to Content -> Content Management ->  Home (or any new or existing section).
* Select **+** on the top right side of the page&#x20;
* Select "Row"
* Follow the steps outlined in the document here ([Link](https://docs.onvesper.com/platform-knowledge-base/back-office/content/content-management/creating-rows/step-by-step-row-creation-guide)).
  {% endstep %}

{% step %}

### Segment your row

* Navigate to your generic row
* Select + on the right hand side&#x20;
* Select "Add Segment"&#x20;

<figure><img src="/files/cCuZVDiaYY12PGvYIW5d" alt=""><figcaption></figcaption></figure>

* Select the Segmentation Format. By default, it will be 'Custom'. For guidance on how to use a Geo-Template or a Geo-Policy instead, please read [this](https://docs.onvesper.com/platform-knowledge-base/back-office/content/content-management/geo-templates-and-geo-policies-on-vesper-back-office).&#x20;
* By default, you can segment by all the available options on Vesper. For more information on each segment see document [here](https://docs.onvesper.com/platform-knowledge-base/back-office/content/content-management/segmentation).&#x20;
* Once a segment has been chosen follow the usual steps for creating a row ([Link](https://docs.onvesper.com/platform-knowledge-base/back-office/content/content-management/creating-rows/step-by-step-row-creation-guide)).
  {% endstep %}
  {% endstepper %}

Once you have followed the steps above you will end up with a series of tabs at the top of your row e.g "Generic" & "England".&#x20;

<figure><img src="/files/JcvzH3QBzgac0etBRMGc" alt=""><figcaption></figcaption></figure>

## What does this mean?

In the example above, we have two rows - "Generic" and "England" row. The "Generic" row is a row that is visible to all default users whereas an "England" row is a row that is only displayed to users who have chosen "England" as their favourite team (we have segmented by "partitions" in this scenario). For example;&#x20;

1. User signs up for the service&#x20;
2. User chooses "England" as their favourite team on sign up&#x20;
3. User navigates through sign up and lands on home&#x20;
4. The user is presented with JUST the "England" only row&#x20;

{% hint style="info" %}
NOTE: when creating a generic and segmented row - The segmented row will always override the generic row if users fall into that criteria. Users will never be shown both rows.&#x20;
{% endhint %}

Alternatively&#x20;

1. User signs up for the service&#x20;
2. User chooses "Italy" as their favourite team on sign up&#x20;
3. User navigated through sign up and lands on home&#x20;
4. The users is presented with JUST the "Generic" row

## Removing the Generic Row&#x20;

As mentioned above you have to create a "Generic" row before you can create segmented rows. However, there will likely be a scenario whereby you don't want the "Generic" row to display anywhere&#x20;

For example - In the use case above;&#x20;

* User signs up for the service&#x20;
* User chooses "Italy" as their favourite team on sign up&#x20;
* User navigated through sign up and lands on home&#x20;
* The users is NOT presented the "Generic" row&#x20;

To achieve this you still have to create a "Generic" row but you create an EMPTY "Generic" row. This generic row should be created with 0 videos so that the row is not shown anywhere. To do this;&#x20;

* Add a generic tag to any published video e.g "empty"&#x20;
* Create the row using the "empty" tag
* Once the row is created remove the tag "empty" from the video&#x20;

This will allow you to achieve the use case above - i.e create segmented rows without the generic row being displayed anywhere on the service.&#x20;

This will work with any segment.&#x20;

For more information on Partitions see link [here](https://docs.onvesper.com/platform-knowledge-base/~/revisions/CKD2efIyERQojqKoYhxR/back-office/content/content-management/optional-partitions).&#x20;


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/content/content-management/creating-rows/row-segmentation.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
