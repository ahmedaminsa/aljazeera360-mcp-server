> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/administration/user-consent-management/content-consent-management.md).

# Content Consent Management

Vesper platform allows for residents to capture user consent, post sign-up, from within a VOD asset or live event, allowing for targeted consent gathering based on a user's content viewing preferences.

This feature functions via a plug-in overlay, which allows you to gather a user's marketing consent based on a simple Yes / No prompt triggered at the point of video playback:

<figure><img src="/files/rOZhGzOkzzqGGVZHMR31" alt=""><figcaption></figcaption></figure>

To enable this feature, please discuss with your account management team. Once it has been enabled on your realm, you can start configuring your consent entities and enable the plug-in against the content of choice, either via typed tags for VOD or directly to live using the consent ID as a key.

### User Consent Management: Content Consent Entities

The first step involves creating the consent entities, which are what define the inputs to a given consent prompt.

In Vesper Back Office, navigate to Administration > User Consent Management > Content tab > Add Consent Option.

You will be presented with these fields to define:

<figure><img src="/files/fMhuWzL08luNvqr4cfQm" alt="" width="563"><figcaption></figcaption></figure>

**Field Definitions**

| Field                   | Definition                                                                                                                                                                          |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Consent ID              | Required unique ID for the content consent entity. Use this value to map consent to VOD through typed tags and to Live through plugin configuration.                                |
| Display Name            | Internal label used to identify the consent entity in Back Office.                                                                                                                  |
| Entity Name             | Label used for alphabetical sorting within a consent group. It can also be shown on smaller screens.                                                                                |
| Re-prompt Consent after | Time period before the user is prompted again after an explicit **Yes** or **No** response. Recommended to set a long time period (eg. 365 days), should you not want to re-prompt. |
| Title                   | Main heading shown on the consent prompt.                                                                                                                                           |
| Description             | Supporting text shown below the title.                                                                                                                                              |
| Status                  | Set to **Enabled** to show the prompt to end users. Set to **Disabled** to hide it.                                                                                                 |
| Main Logo               | Primary logo used on larger devices and on web prompts.                                                                                                                             |
| Supplementary Logo      | Simplified logo for smaller-screen layouts, often shown with the entity name.                                                                                                       |

**Landing Hub**

Once specific consent entities have been created, they will appear in the landing hub in a snapshot view, making it easy to access the information required for implementation.\ <br>

<figure><img src="/files/p36PoLyovzfiH9ptWh1E" alt=""><figcaption></figcaption></figure>

#### **Add Content Consents Plugin**

This feature utilises Vesper's Plugin solution. For more details, please see the [Vesper Plugin page](/platform-knowledge-base/back-office/content/plugins.md).

After the Content Consents realm setting is enabled, a new configuration option becomes available in the **Plugins Register** section of Vesper when creating plugins.

To set up a new Content Consents plugin, navigate to the **Plugins Register** section and select **Add Plugin,** this will display the **Configure Plugin** screen.

<figure><img src="/files/vtYzA3hwL8vfLMv4OhmS" alt=""><figcaption></figcaption></figure>

In the Add Plugin configuration screen, resident users can specify the plugin name using the **Plugin Name** field and choose the plugin type from the **Type** selector.

For this configuration, select **Content Consents** as the plugin type.

Confirm the changes and proceed to the **Customise Plugin** with the next button.

<figure><img src="/files/RYQifncj8vVG05DmnBSR" alt=""><figcaption></figcaption></figure>

In the Customise Plugin configuration screen, Residents can specify the path to the plugin code file using the **Plugin Source** field. For production use, this should always be set to:

```
https://plugins.onvesper.com/content-consents-plugin/modern/index.js
```

Residents can also define the **Consent Re-prompt Delay**, which will be applied to all plugin instances associated with this plugin configuration, this is how long after a given Content Consent Entity was dismissed will it be shown again.

<figure><img src="/files/uOx6qXmAEr6nm5FOr4AH" alt=""><figcaption></figcaption></figure>

Once set up and published, this plugin will show up under **Plugin Register**.

<figure><img src="/files/1ThD53pCxphYtjpNufcf" alt=""><figcaption></figcaption></figure>

### **VOD & Live Enablement**

Depending on the content type for which consent is being collected, there are two distinct plugin instance configurations and corresponding enablement paths.

#### **Configuration for VOD Content**

**Creating a Plugin Instance**

After completing the plugin definition, a single plugin instance can be created to cover all VOD content where typed tags are configured. Selecting the newly created plugin will navigate you to the Plugin Instances screen.

Click **Add Instance** to open the **General** tab.

<figure><img src="/files/lHQzl9apeRkQWEDHa6wC" alt=""><figcaption></figcaption></figure>

Here, you can configure the instance name and, if required, override the plugin definition's default **Override Consent Re-prompt Delay**. For the VOD configuration, there is no need to specify primary or secondary content consent IDs, as these are read directly from the typed tags configured within the VOD platform.

<figure><img src="/files/u0NapB5QgGTdUjeEKGZl" alt="" width="522"><figcaption></figcaption></figure>

Next, navigate to the **Restrictions** tab to define the conditions under which Content Consent(s) applies. To enable the plugin across all VOD content in the catalog, disable the **Restrict VODs** control.

This can be used in combination with **Restrict Languages** and **Restrict Licences** to achieve the desired configuration.

{% hint style="info" %}
Note that all toggles default to the maximum level of restriction and the plugin will not work without a specific setup. To allow this plugin to work, you must explicitly enable VODs and either select the specific Languages and Licences to restrict, or set the toggle to **No** to enable all without restriction.
{% endhint %}

<figure><img src="/files/Gq9O93BT3kUlqiWfOxes" alt="" width="511"><figcaption></figcaption></figure>

**Assigning Content Consents IDs to VOD Content**

For VOD content, Content Consent IDs are entered in the Vesper VOD platform using the typed tag inputs. Two specific typed tags must be configured for each Resident so they can be selected when configuring VOD content to prompt users for content consent. Typed tag definitions are managed in the **Typed Tag Manager** within the Vesper VOD platform.

The two typed tags that must be configured are:

* `primaryContentConsentIds` — Used for the primary group of consent options, which are presented to the user first.
* `secondaryContentConsentIds` — Used for the secondary group of consent options, which are presented after the primary group.

{% hint style="info" %}
For the plugin to function correctly, these values must be entered exactly as written in the typed tag name field.
{% endhint %}

**Set up the typed tag:**

* Typed Tag Name: either `primaryContentConsentIds` or `secondaryContentConsentIds` depending on which one you are setting up.
* Visibility: Normal
* Select Tag Type: ENUM
* Validation Requirement: Blank

Utilising an ENUM allows for tighter control and helps prevent implementation errors by explicitly defining the set of Content Consent Entity IDs available for type tagging.

The Typed Tag Keys should then consist of the specific Content Consent Entity IDs you intend to assign to either the primary or secondary Content Consents groups.

<figure><img src="/files/YlwJCPRDGfgd6DpiW7LR" alt=""><figcaption><p><em>Image on Left is the Typed Tag Manager, on Right the User Content Consent Hub</em></p></figcaption></figure>

From there, navigate to specific VODs and apply the typed tag (as is done today).

Once the VOD is tagged, the plugin will render the corresponding Content Consent Entities based on the established mapping between the typed tag key values and the Content Consent IDs.

<figure><img src="/files/NRDWshZuHdaFtESn0VcS" alt=""><figcaption></figcaption></figure>

#### **Configuring for LIVE Content**

**Creating a Plugin Instance and Assigning Content Consent IDs to Content**

After completing the plugin definition, a separate plugin instance is required for each LIVE event where content consent must be captured. Selecting the newly created plugin will navigate you to the Plugin Instances screen.

Click **Add Instance** to open the **General** tab. Here, you can configure the instance name and, if required, override the plugin definition's default **Override Consent Re-prompt Delay**.

For LIVE configurations, the primary and secondary content consent IDs are configured directly on the plugin instance for the specific LIVE event it will be associated with.

<figure><img src="/files/TnYrjd8sQp484OVRcDv4" alt=""><figcaption></figcaption></figure>

Next, navigate to the **Restrictions** tab to define the conditions under which content consent applies. To enable the plugin for a LIVE event, enable the **Restrict live events** control and select **Choose specific liveEvent** to add events to the allowlist. This will display an input field where you can specify the LIVE event IDs to which the plugin should apply.

<figure><img src="/files/tykYI6XL0eNWqBu9pVxq" alt="" width="484"><figcaption></figcaption></figure>

#### **Outcome of Enablement**

This feature will work as follows:

When a user is eligible to be shown a Content Consent Entity and navigates to a VOD or Live event that has been explicitly tagged to display that entity, the Content Consent Entities are presented sequentially, ordered first by **primary**, then by **secondary**.

If multiple entities qualify within the same group (primary or secondary), they are displayed in alphabetical order based on the Entity Name.

After the user selects **Yes**, **No**, or dismisses the prompt for a given entity by clicking the **"X"**, the next qualifying entity (if any) is displayed.

The user experience is not paused; the prompt remains on screen until the user takes action.

<div data-with-frame="true"><figure><img src="/files/kspO6rjFViRvKjnx7A5h" alt=""><figcaption></figcaption></figure></div>

### **Reporting**

#### **Vesper Insights**

Within the [Customer Profile Report](/platform-knowledge-base/back-office/vesper-insights/analytics-dashboards/dashboard-deep-dive/customer-insights.md), you are easily able to see the status of consent opt-in or out. This is represented in a column called "Content Consent."

This will be populated with the explicit consent that was granted by the End User, so either True (yes) or False (no). It will appear in the following manner:

```
consentID:True,consentID:False
```

Where the consentID is what has been defined under the Content Consent management portal.

<figure><img src="/files/NzttlSlNMjPVZfASAxZl" alt=""><figcaption></figcaption></figure>

#### **Behavioural Analytics**

The Content Consents plugin supports behavioural analytics, allowing you to track how customers interact with consent prompts. The events would need to be configured to support behavioural analytics so they can be sent to a third-party analytics platform, such as [Google Analytics](/platform-knowledge-base/consumer-experience/google-analytics-integration.md), to enable capture of the following events:

* **content.consent.view** — Triggered when a content consent prompt is presented to the customer.
* **content.consent.accept** — Triggered when the customer accepts the content consent.
* **content.consent.decline** — Triggered when the customer declines the content consent.
* **content.consent.dismiss** — Triggered when the customer dismisses the consent prompt without making a selection.

<figure><img src="/files/P65B4545nj5kaBrrgwdy" alt=""><figcaption></figcaption></figure>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/administration/user-consent-management/content-consent-management.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
