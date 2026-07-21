> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/content/content-management/geo-templates-and-geo-policies-on-vesper-back-office.md).

# Geo-templates and geo-policies on Vesper Back Office

## Introduction

Content managers can set the following parameters against a hero when creating it:

* Allow rules (geo-template): You can select a template containing a list of regions where your hero should be displayed.&#x20;
* Time and date rules (geo-policy): You can select a policy whereby your hero will be displayed in a list of predefined regions at a determined time and date.

These segmentation features enhance the speed and efficiency with which content managers can prepare to publish hero carousels ahead of time.

## Geo-templates

If one or more of your heroes should be accessible only in some regions, you can select each region manually each time you create a hero or you can make a template. This allows you to reutilise the list of regions as a template should you need it in the future, without having to manually input all the regions again.

To create geo-templates for your Hero creatives, follow these steps:

1. Go to Vesper Back Office
2. Navigate to Administration -> Publication Rules
3. Select 'Create New Template'
4. Give the template a name, eg. Summer League
5. Select all regions that should be **allowed** to see the Hero
6. Click 'Create'

   <figure><img src="/files/cDFpsldFKWXBiOQlInIp" alt=""><figcaption><p>Select the regions allowed to see the Hero to create a geo-template</p></figcaption></figure>

Your new template will appear on the 'Template' dashboard, where you can edit or delete it as your needs evolve.

To implement the geo-template on your Hero creatives, follow these steps:

1. Go to Vesper Back Office
2. Navigate to Content -> Content Management
3. In 'Home', press the **+** button on the right side to create a new Hero.
4. Give the segment a name eg. Summer League.
5. Select Segmentation Format -> Geo-Template

<figure><img src="/files/ouNEDpWQ9jWFPvLj6M5s" alt=""><figcaption><p>Select geo-template when creating your hero</p></figcaption></figure>

6. Select 'Configure' on the Geo-Template section
7. Start writing the name of your template and it will appear in a dropdown menu

<figure><img src="/files/i1fqe2qMxRuwpYRIOBrv" alt=""><figcaption><p>Available geo-templates will appear in a dropdown menu</p></figcaption></figure>

8. Select 'Confirm'
9. Customise the Hero as per usual

This hero will be shown only in the regions specified in the geo-template. Should you need to append or remove the list of regions, you should edit the template in the Publication Rules dashboard rather than on the Hero.

{% hint style="info" %}
The geo-templates apply to all the slides within the hero. If you are showcasing multiple slides with different geo-restrictions, a template is not the best solve: you should copy the hero and tailor it to different regions instead.
{% endhint %}

## Geo-policies

Geo-policies allow you to specify when you want your geo-templates implemented. This allows content managers to schedule their hero carousels ahead of time and update the geo-restrictions in bulk at a specific time.

One common use case for the use of geo-policies is **content embargo**. Geo-policies ensure that you remain compliant with the existing broadcast deals in the region(s) and hero carousels are only displayed to the pertinent regions after the embargo has been lifted.

To create geo-policies for your Hero creatives, follow these steps:

1. Go to Vesper Back Office
2. Navigate to Administration -> Publication Rules
3. Select 'Create New Policy'
4. Give the policy a name, eg. Summer League Embargo
5. Start writing the name of the geo-template to use and it will appear in a dropdown menu
6. Select when should the policy should start after the Hero is created eg. 2 days, meaning that the Hero will be made available to the regions in the geo-template 2 days after the Hero is published
7. Click 'Add'
8. Click 'Create'

<figure><img src="/files/SPKsO0bchnhQ07odtRPe" alt=""><figcaption></figcaption></figure>

Your new geo-policy will appear on the 'Policies' dashboard, where you can edit or delete it as your needs evolve.

To implement the geo-policy on your Hero creatives, follow these steps:

1. Go to Vesper Back Office
2. Navigate to Content -> Content Management
3. In 'Home', press the **+** button on the right side to create a new Hero.
4. Give the segment a name, eg. Summer League.
5. Select Segmentation Format -> Geo-Policy
6. Set up a schedule, this is the time when you want your Hero to be published
7. Start writing the name of the geo-policy to use and it will appear in a dropdown menu

   1. The geo-policy template will indicate at what time the policy will go live depending on the offset set up. For example, if your hero is scheduled to go live on the 4th and your policy has an offset of 2 days, the policy will go live on the 6th.

   <figure><img src="/files/SZRFyv7GNLihcKD7ldLn" alt=""><figcaption></figcaption></figure>
8. Select 'Confirm'
9. Customise the Hero as usual

If you would like to have these features enabled, please reach out to your Account Management team.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/content/content-management/geo-templates-and-geo-policies-on-vesper-back-office.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
