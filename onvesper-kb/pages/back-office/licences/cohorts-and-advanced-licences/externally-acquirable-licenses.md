> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/licences/cohorts-and-advanced-licences/externally-acquirable-licenses.md).

# Externally Acquirable Licenses

Externally acquirable licenses enable granting users access to content or services on your Vesper platform even when their entitlement originates and is managed by a third-party system, rather than through Vesper's native checkout.

## **What Are Externally Acquirable Licenses?**

These licenses are designed for scenarios where users obtain access to your content through an external process. This could involve:

* Third-Party Purchases: A user buys a service from a partner, like a telecommunications provider, who then grants access to your content.
* SSO Integrations: Access is granted when a user authenticates through a partner's Single Sign-On (SSO) system.
* Promotional Bundles: Your content is included as part of a larger package or promotion managed by an external entity.

On the Vesper platform, such a license is configured as a "Free" license, with its actual acquisition process managed by the designated external provider.

## **Why Use Externally Acquirable Licenses?**

* Expand Reach: Integrate your content seamlessly into external partner ecosystems and distribution channels. The system can also be used to sell your subscription as part of a bundle outside of Vesper.
* Streamlined User Access: Users acquire their entitlement externally and then seamlessly transition to direct content access on the Vesper platform, as their acquisition process is already complete.

## **Steps to Configure an Externally Acquirable License in Vesper**

To set up a license that is acquired externally within the Vesper License creation/edit interface:

{% stepper %}
{% step %}
**\[Prerequisite] External License Provider Setup:**

* For assistance with provider setup, you should consult with your *Platform Account Manager*. Once it has been completed, you can continue setting up the licence.
  {% endstep %}

{% step %}
**Define License Type:**

* Navigate to the "Define license type" section when creating a license. (For general steps on creating a license, refer to the documentation outlined [here](/platform-knowledge-base/back-office/licences/licence/creating-a-licence.md).)
* Select `Free` for the License Type. This indicates that the license does not require a purchase directly within Vesper or through In-App Purchases (IAPs) for a user to unlock.
  {% endstep %}

{% step %}
**Enable External Provider:**

* Within the same "Define type of license" section, toggle External License provider option to `Yes`.&#x20;
  {% endstep %}

{% step %}
**Link to External Provider and Group ID:**

* From the "Select provider" dropdown, choose the specific External License Provider.

<figure><img src="/files/T3IAYZ0EzsdMYJyFfuXG" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

#### \[Optional] Provide the CTA link for acquiring the licence

* Enable external acquisition by selecting `Yes` to the 'Acquirable via the realm' setting.&#x20;

<figure><img src="/files/tnf7xJGZ2lXAQ1voT8nl" alt=""><figcaption></figcaption></figure>

* In the "Acquisition URL" field, you can provide a direct link where users can go to acquire this license externally.&#x20;
* You can also customize the text that appears on the acquisition button (found in the first step of creating a license `Add License Metadata` in the field `CTA Title`)

<figure><img src="/files/El4AqjgOHldtx9BtOaWD" alt=""><figcaption></figcaption></figure>

{% endstep %}
{% endstepper %}

## **Important Considerations for Externally Acquirable Licenses**

* **Usage Restrictions:** You can apply Cohort usage restrictions to Externally Acquirable Licenses. This allows you to control who can *use* the content associated with an acquired license based on dynamic criteria (e.g., geographical location, membership status).&#x20;


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/licences/cohorts-and-advanced-licences/externally-acquirable-licenses.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
