> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/administration/marketing-partner-management/post-back-url.md).

# Post-back URL

Post-back URLs are a type of web URLs designed to accept incoming data from another server and used to programmatically pass information back to the referral partner to alert them of a conversion.

These are favoured by some web marketing providers who want to receive conversion data as quickly as possible so that when a campaign uncovers successful audience(s), the traffic they generate can be optimised.

Post-back URLs are an **optional** feature of the Marketing Partner Management hub. Please consult with your advertiser to confirm if they will provide one.

{% hint style="info" %}
We can also deliver marketing conversion events through our MailMan data stream service for analysis by your teams if you wish to use the data for another purpose.
{% endhint %}

## Anatomy of a post-back URL

<figure><img src="/files/FUtgwmfwde2OJQsxTM5I" alt=""><figcaption><p>The value captured</p></figcaption></figure>

**Post-back URLs are dictated by the advertiser:** you should refer to their documentation on how to build and obtain them so they can be implemented into the Vesper platform. As an initial guide, post-back URLs:

* can include any unique campaign identifiers (above, `https://my-referral-partner.com`)
* must contain the path to  `/postback`&#x20;
* must contain the Endeavor Streaming macro `{{clickID}}` as a value set against a designated parameter to capture the unique data string passed to Endeavor Streaming via the esclickd parameter on the Redirect URL - you can copy this macro from the Marketing Partner Management dashboard in Vesper Back Office

<figure><img src="/files/FMJw73u2Q532LEgJrDjP" alt=""><figcaption><p>Provide this macro to your advertiser so they can construct the post-back URL</p></figcaption></figure>

* Must have a designated HTTP method for data transfer: GET or POST

Once the advertiser constructs the post-back URL considering the `esclickid` parameter, they will share it with you. You are now ready to integrate it into Vesper Back Office to ensure the conversion events are communicated back to the advertiser's server.

## Post-back URL implementation in Vesper Back Office

1. Navigate to the Marketing Partner Management dashboard
2. Enable Post-Back URL Construction
3. Insert the post-back URL provided by your advertiser - ensure that `{{clickID}}` appears as a value against the designated partner parameter&#x20;
4. Select a Post-Back Method (GET or POST)
5. Hit Save

Your advertiser will now start receiving conversion events in real-time. Enjoy seeing your marketing campaigns bringing more users to your platform!


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/administration/marketing-partner-management/post-back-url.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
