> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/dve/geo-blocking.md).

# Geo-Blocking

## Geo-blocking rules on individual VOD assets

A VOD’s geo-restriction can be updated from the VOD detail page. From the VOD detail view indicated below, a user can:

* link a geo-template *(up to 5 templates can be associated with a VOD)*
* apply a geo-policy
* create a single-VOD restriction *(note, clicking on the restriction type changes the option from Block to Allow and vice versa)*

<figure><img src="/files/IyvigsxUmrbaC1PTJf7V" alt=""><figcaption><p>The geo blocking section on VOD metadata screen</p></figcaption></figure>

<figure><img src="/files/gPClxvH1amoxrPZ8BtM3" alt=""><figcaption><p>The full screen shown when "edit" button is pressed</p></figcaption></figure>

For Custom restrictions, you can either manually select the countries, or enter up to 50 US Zip codes for the restriction. If you need to enter more than 50 zip codes, please create a CSV file with a single column (no header/title), and upload the CSV.

<figure><img src="/files/m3PKpVd1qYXa4EPVyHJd" alt=""><figcaption></figcaption></figure>

## Creating Templates and Policies

If you want to create templates or policies that you can re-use across all future VODs, visit the "*Geo-blocking*" section.

The '*Geo-Blocking*' section is where you can set any Geo-blocking templates (Blacklisted or Whitelisted) or policies along with being able to organise time based publishing for all videos on the Video Excchange platform.&#x20;

When you select the 'Geo-Blocking' section you will see an option to select between **Policies** or **Templates.**

<figure><img src="/files/JSfMiZTPhGNiJomDmne8" alt=""><figcaption></figcaption></figure>

### Templates

Selecting **Templates** from the dropdown will take you to the Templates section, where you can create geo-blocking rules for your content.

![](/files/-M4xx6sN6jHTcJ-XWRPL)

To create the Geo-blocking rule, you need to select the '**Create Template**' button on the right hand side and a pop up box will appear for you create the rule.

<figure><img src="/files/jleqANurzRpofAGpcXvy" alt=""><figcaption><p>The template creation screen</p></figcaption></figure>

You will need to give the Geo-Blocking Rule a **Name**, this will make it easier to find the rule and make any changes necessary.&#x20;

After you have given the rule a name, you can select if it will be a *Blacklist* (Blocking content in specific regions or countries) or a *Whitelist* (Allowing content in specific regions or countries) rule. \
\
Once you have selected between the two, you can then select which regions or countries you would like this rule to apply to and click the '**Save**' button.

![Geo-Blocking Rule in place](/files/-LzlWdYwjBsBCR4T7ccC)

You will then be taken back to the *Geo-Blocking Templates* page, where you will be able to see your newly created template in the list.&#x20;

To apply this rule to a specific video, please see [edit metadata](/platform-knowledge-base/dve/video/metadata.md) on the video page.&#x20;

#### Geo blocking by Zip code

When creating a new geo blocking template, you can specify regions by US Zip codes if the intent is to block certain US regions from accessing content. This template will then be available for use on the Video Exchange.

### Policies&#x20;

Selecting **Policies** from the dropdown option will take you to the Policies section where you can create geo-blocking policies for your content.

![](/files/-M4yLio5oxGHVeMm5Mc1)

Geo-Blocking Policies consists of various Geo-Blocking templates arranged according to time offsets. They enables precise control over which countries have access to a video, and when they have access to that video, allowing for immediate or delayed viewing. \
This approach ensures granular management of a video's geographical availability.

They can be applied to any VOD asset, and starts taking effect from the *"Policy start time"* option set on the VOD asset page.&#x20;

<figure><img src="/files/QZbqPWK8mve19CntxZCT" alt=""><figcaption><p>A Geoblocking policy</p></figcaption></figure>

To create the Geo-Blocking policy rule, click the '**Create Policy**' button on the right-hand side, and a pop-up box will appear for you to create the rule.

In the pop-up box, you will need to enter a **Name** for the Policy which will be used as a reference when applying it against a VOD asset.

You have the option to add multiple Geo-Blocking templates to a single policy. \
To add in a template, you can select it from the dropdown list under *Template* or you can type in the title of the template.&#x20;

You will also need to see an Offset Delay for when you would like the chosen template to take effect. You have the choice of setting it using Days, Hours or Minutes.

Once you have selected all the templates and timings to be used in the policy, you can click save and will be taken back to the policies page where you will see your newly created policy.

### Time Based Publishing

Once all of the Template and Policy work is done, you are now ready to assign this policy to any Video asset on the Digital Video Exchange (DVE) that you would like.

In order to apply the newly created template and policies, you will need to go to the *Video* section and select the video you would like to have it applied to.&#x20;

From here, you will find the **Update Geoblocking** button where you can apply your template or policy.

<figure><img src="/files/09UvUbVEM6iBNRXb7I4C" alt=""><figcaption><p>Update Geoblocking on the desired VOD asset page</p></figcaption></figure>

This will open up a window where you can choose how to apply your geoblocking restrictions:

<figure><img src="/files/AiIHp46L9SDvYQkxwWcv" alt="" width="375"><figcaption><p>The Geoblocking settings</p></figcaption></figure>

In case you'd like to set a policy before or after a video scheduled time, please follow the corresponding steps below:

**IF SETTING A POLICY&#x20;*****BEFORE*****&#x20;THE SCHEDULED PUBLISHING TIME**

1. Select “Policy Based” as the Restriction Type.
2. For “*Geo-Restrict video until policy starts*”, select “Yes”.
3. Set the "Policy start time" (this should be the time the video should be available in your local timezone)
4. Then click **Save**.

Once saved, you will see the following information under the *geoblocking* section:

<figure><img src="/files/ahO6Q6U0NN3HvxLXCCqn" alt="" width="563"><figcaption></figcaption></figure>

* **Policy Name:** The policy that will be applied at start time.
* **Start Time:** The start time of the policy as seen in point 3 above.
* **Whitelist / Blacklist:** This indicates where the video will be available/blocked when the policy starts.

**IF SETTING A POLICY&#x20;*****AFTER*****&#x20;THE SCHEDULED PUBLISHING TIME**

1. Select “Policy Based” as the Restriction Type
2. For “*Geo-Restrict video until policy starts*”, select “No”.
3. Set the "Policy start time" (this should be the time the video should be available in your local timezone)
4. Then click **Save.**

Once saved, you will see the following information under the *geoblocking* section:

<figure><img src="/files/ahO6Q6U0NN3HvxLXCCqn" alt="" width="563"><figcaption></figcaption></figure>

* **Policy Name:** The policy that will be applied at start time.
* **Start Time:** The start time of the policy as seen in point 3 above.
* **Whitelist / Blacklist:** This indicates where the video will be available/blocked when the policy starts.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/dve/geo-blocking.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
