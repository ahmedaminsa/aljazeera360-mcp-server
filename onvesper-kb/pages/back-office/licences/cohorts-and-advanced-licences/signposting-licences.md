> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/licences/cohorts-and-advanced-licences/signposting-licences.md).

# Signposting Licences

An advanced configuration of the vesper product: **signposting licences** are a form of externally acquirable licence that can be set up to give guidance to your customers about why they can't currently access some of your content.

Consider that you have content which cannot be unlocked by a customer on the device they are currently utilising. For example, you are not selling an in-app purchase on Android that unlocks the licence, but the user could upgrade on your website.

Without signposting licences:

* The user will never see the locked content, because there is no way to unlock it

With signposting licences:

* The user will see locked content, when they tap on the locked content they will be taken to the "purchase" flow but shown a licence which they cannot acquire. The licence text and CTA can include instructions on how to unlock the content, or link out to more information

{% hint style="warning" %}
**Important**: When considering using a signposting licence, you must ensure you are compliant with the app store agreements you accepted by publishing with Apple/Google/Amazon etc. Please ensure you have reviewed and are able to abide by those agreements, otherwise your app may be pulled by those publishers or further action taken against you as the account holder.
{% endhint %}

### Example use cases for Signposting licences

1. Content can't be purchased on this current device (no IAP), but could be purchased online
2. Content can't be purchased directly or via Vesper, but is unlocked via upgrading your licence with your mobile phone carrier
3. Content is not available in your region, or not available to your current session due to licensing agreements (i.e. you have been away from the allowed region for more than 30 days)

## How to set up a signposting licence

{% hint style="info" %}
Signposting licences are an advanced feature of Vesper. You should consult with your *Platform Account Manager* before implementing them.
{% endhint %}

Follow the step by step guide below to set up a signposting licence. In this example we will be setting up a licence to instruct customers to "upgrade their package" if they encounter locked content on an Android TV device.

1. Request your *Platform Account Manager* (or helpdesk) set up a new External Licence Provider with the name "Signposting" or "UnAcquirable". This will create a provider that does not exist, so that you can use [Cohorts & Advanced Licences](/platform-knowledge-base/back-office/licences/cohorts-and-advanced-licences.md) to set up an externally acquirable licence that can not be acquired.\
   &#x20;

   <figure><img src="/files/dqRwFDBnGEkrR9mML329" alt=""><figcaption><p>Admin-only screen for Licence Provider creation, demonstrating the creation</p></figcaption></figure>

2. Begin creating your signposting licence, set it up as a free licence and limit the availability to the platform you wish to include a signpost on.<br>

   <figure><img src="/files/DHQ1VJWcnXRt3lvvxPdY" alt=""><figcaption><p>Example configuration. Using a hidden CTA</p></figcaption></figure>

   \
   You can chose to hide the Call To Action (best if you are asking for the user to purchase somewhere else) or use a text-style CTA if you want to link to more details or an FAQ. **Note that external links are not supported on TV devices, the CTA will show but cannot be actioned.**\
   ![](/files/GzN93jzVJhyvx8eHI5XN)\
   \
   Set the licence to only be visible behind locked content (not standard checkout flow) and ensure that locked content will be visible to guest users.\
   ![](/files/cdADWRLQVoMnKJbieSuE)![](/files/yRGjsJJu6yNpecSplkDU)

3. Set the licence type to "Free", external licence provider, and acquirable via the realm "yes". You will then need to mark the licence provider as the provider created in step 1.<br>

   <figure><img src="/files/J69BsYM8VBxHemFgrjlJ" alt=""><figcaption><p>A Signposting licence configuration example</p></figcaption></figure>

   \
   If you chose to keep your CTA in step 2 (rather than hiding it), put the location you want it to navigate to in "Acquisition URL". You should also fill out acquisition description with the same description as you used in step 2.<br>

   <figure><img src="/files/yaf85bWRlndsfMOjbL72" alt=""><figcaption><p>This example keeps the CTA, and will link to the FAQ page entered above</p></figcaption></figure>

4. Optionally: add the licence to a family (not normally required).

5. Set the content you wish to target with this signposting licences. If you only want to signpost for certain live or VOD content, set the restrictions. Alternatively, you can set the content to grant access to all VODs and Live streams. Remember, this licence can never be acquired, so in this step you are instead selecting which content you want to show as locked, and with this signposting licence behind it.

6. Ensure there are no usage restrictions. Once again because this licence can never be acquired, this section has no impact, so you simply need to make sure it can be saved by marking it as available in all countries and devices.

7. Save the licence

8. Test!

If you have set things up as above, customers on your chosen platform should now see locked content where they previously saw no content. Note that the CTA for such content will likely still say "Purchase" or similar. When the user selects the licence, they will be shown your signpost.

<figure><img src="/files/VrdFnuWc6Q2gzxkYJyXp" alt=""><figcaption><p>Locked live content with a CTA, when behind a signposting licence</p></figcaption></figure>

<figure><img src="/files/DMQJxExa5jpNcLU3FML6" alt=""><figcaption><p>Example of a Signposting licence that cannot be acquired (shown on Vesper web)</p></figcaption></figure>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/licences/cohorts-and-advanced-licences/signposting-licences.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
