> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/consent-management-platforms/onetrust/configure-onetrust.md).

# Configure OneTrust

{% hint style="info" %}
This guide is intended to assist you with the initial setup of OneTrust Cookie Banner, a product not owned or operated by Endeavor Streaming. While we strive to ensure the accuracy and relevance of the information provided based on our experience with the product, you should consult the official documentation provided by OneTrust or contact their customer support for detailed instructions, updates and additional support.
{% endhint %}

## Scan the domain

Before implementing your cookie consent, OneTrust must scan the domain used for your OTT to identify which cookies are being dropped.

Follow the below steps within the OneTrust dashboard or watch this tutorial from OneTrust [here](https://my.onetrust.com/s/article/UUID-89c7e418-8921-9338-99d1-f232726661e6?topicId=0TO1Q000000sseOWAQ):

| Action                                                                                                                                                                        | Visual                                                              |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| <ol><li>On the left-side menu, go to Digital Properties -> Websites and click 'Add Website'</li></ol>                                                                         | <img src="/files/Qnv3eQiTJcSkJY2vSG9E" alt="" data-size="original"> |
| <ol start="2"><li>Include the website URL, the name of your organisation and the main location where consent will be requested. Click 'Scan Only' when you're done.</li></ol> | <img src="/files/cxuAPbj6Ic5rK88a6DKs" alt="" data-size="original"> |

Please note:

* Use the top level url of the website you want to scan, e.g `example.com`, not `www.example.com`&#x20;
* Scans can take several hours or days depending on the size of the website.
* If you select 'Scan & Configure' rather than 'Scan Only', you'll be prompted to the Experience Kit, a container encapsulating a geolocation rule and each of the templates assigned to the rules within the rule group. If you're a OneTrust power user, this will expedite the configuration process.&#x20;

{% hint style="info" %}
For more information regarding scanning the OTT domain, visit OneTrust's Knowledge Base [here](https://my.onetrust.com/s/article/UUID-49bd8301-a150-6107-7409-de3297816efa?language=en_US).
{% endhint %}

## Categorise the cookies

After your domain scan is over, you'll see all the cookies and tracking technologies present on your website and will be able to categorise them based on function. These categories will allow your visitors to consent to cookies by category in your Preference Center.&#x20;

Follow the below steps within the OneTrust dashboard or watch this tutorial from OneTrust [here](https://my.onetrust.com/s/article/UUID-309d4544-c927-fe00-da50-60ed7668c6b5?topicId=0TO1Q000000sseOWAQ):

| Action                                                                                                                                                                                                                          | Visual                                                              |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| <ol><li>On the left-side menu, and after your scan is completed, go to Digital Properties -> Websites and click on your domain to see the scan results</li></ol>                                                                | <img src="/files/GPHF3eieMiN2m11UvW7q" alt="" data-size="original"> |
| <ol start="2"><li>Navigate to Setup -> Categorisations. Many of your cookies will be automatically categorised by OneTrust. If there are cookies of category unknown, click on them and assign them a categorisation.</li></ol> | <img src="/files/cWPBbec8xlaeiIDTwoie" alt="" data-size="original"> |
| <ol start="3"><li>If you want to edit the existing cookie categories or create a new category, navigate to the 'Categories' tab. </li></ol>                                                                                     | <img src="/files/cYcI9X5GCErM4YYjH3fO" alt="" data-size="original"> |

## Configure templates

Templates control the look and feel of your Cookie Banner, Preference Center, and Cookie List to seamlessly match the style of your website and comply with applicable consent frameworks.

Follow the below steps within the OneTrust dashboard or watch this tutorial from OneTrust [here](https://my.onetrust.com/s/article/UUID-b85c6e9d-6120-2b50-ce5b-fbcb21480f82?topicId=0TO1Q000000sseOWAQ):&#x20;

| Action                                                                                                                                                                                                                                                                                    | Visual                                                              |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| <ol><li>On the left-side menu, go to Setup -> Templates and select 'Create New Template'. OneTrust offers pre-seeded templates for frameworks to be selected upon creating your template.</li></ol>                                                                                       | <img src="/files/teJd1mdhswA2vUoP37Ht" alt="" data-size="original"> |
| <ol start="2"><li>Give the template a name, assign to an organisation and select your default language.</li></ol>                                                                                                                                                                         | <img src="/files/2xDXNGCKlZmOxNiRa7Kj" alt="" data-size="original"> |
| <ol start="3"><li>Customise your cookie banner. The layout, styling, content and behavior can be configured for the cookie banner and preference center. Styling and content can be configured for the cookie list. You'll see a preview of your banner right on the dashboard.</li></ol> | <img src="/files/tvryipkRtcs6JhXxIhGA" alt="" data-size="original"> |
| <ol start="4"><li>Save the template when you're done. </li></ol>                                                                                                                                                                                                                          | <img src="/files/h8ynOMjCiCY5w71Q3he0" alt="" data-size="original"> |

Please note you should create one template for every framework that your website must comply with.

## Set up consent settings and Geolocation Rules

Consent settings allow you to collect data on consent responses; geolocation rules ensure that your website is compliant with regional privacy laws.

A Global Rule is present and used when no specific Geolocation Rule applies to the website visitor. You can add as many rules as needed to comply with regional privacy laws.

Adding a rule allows you to designate the region where the rule is to be used and assign a Template configured for the laws of that region. You can also edit the consent model and the behavior of the banner. Finally, you can enable consent logging to track when site visitors are giving consent.

Follow the below steps within the OneTrust dashboard or watch this tutorial from OneTrust [here](https://my.onetrust.com/s/article/UUID-56ae6d0d-2c92-982a-ee5b-a7650bc4c72c?topicId=0TO1Q000000sseOWAQ):&#x20;

| Action                                                                                                                                                                             | Visual                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| <ol><li>One the left-side menu, go to Setup -> Geolocation Rules and create a new Geolocation Rule Group</li></ol>                                                                 | <img src="/files/yIWHWIY0t38hmva3V6Xq" alt="" data-size="original"> |
| <ol start="2"><li>Within the Geolocation Rule Group, click 'Add Rule'. </li></ol>                                                                                                  | <img src="/files/g23TYY5hyixUQRuda6po" alt="" data-size="original"> |
| <ol start="3"><li>Add the name of the rule, select the region where this policy will be assigned, apply one of your previously created Templates to it and click 'Save'.</li></ol> | <img src="/files/GXZG3ipmdLoWFQTxF7RO" alt="" data-size="original"> |
| <ol start="4"><li>Navigate to 'Assigned Domains' to select the domain you'd like to assign this geolocation rule to.</li></ol>                                                     | <img src="/files/8eYh2SoLNRGkFZHqAIqO" alt="" data-size="original"> |


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/consent-management-platforms/onetrust/configure-onetrust.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
