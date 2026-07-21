> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/licences/licence/licence-card-configuration.md).

# Licence Card Configuration

You can now fully customize the content, styling, and labels of licence cards, ensuring that your offerings are clearly communicated and branded consistently on every device your customers use.

{% hint style="info" %}
This change is rolling out to Vesper web first, and will be enabled on mobile and TV platforms in future Vesper releases.
{% endhint %}

## Key Capabilities

* Deep Customization: Control promotional banners, monthly pricing breakdowns, as well as card background and text colors.
* Marketing Flexibility: Configure clear and compelling messaging to support campaigns and drive conversions directly on the subscription selection screen.
* Platform Consistency: Maintain uniform branding, messaging, and card design across Web, Mobile, and TV with a single configuration set.

{% tabs %}
{% tab title="Purchase flow Example" %}

<figure><img src="/files/Lk0VIendAZJC3aPrUqdv" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Back office preview" %}

<figure><img src="/files/CCjgwZcBqeFIiw9JY8Wo" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

## How To Configure

In back office, navigate via Licences > Package Licences. Under step 1, "Add Licence Metadata" you will see several additional visual customisation options available.

### Subtitle&#x20;

Add a line of small text under the main "Title" heading.&#x20;

This is "This subtitle has markdown formatting" in the screenshot below;&#x20;

<figure><img src="/files/fXRsNJgw3AS1v2kz3p87" alt="" width="188"><figcaption></figcaption></figure>

### Description (Markdown)

Through the use of "Markdown" text, we now allow for better customisation on the description copy included within the licence cards. Residents have the ability to add the following;&#x20;

1. Italics - Wrap the text with a single star ("\*") e.g \*italic\*
2. Bold - Wrap the text with double stars ("\*\*") e.g \*\*Bold\*\*
3. List - Create Tick icons using a dash (-) e.g - This will be a tick icon&#x20;
4. Small text - Start the test with a right arrow (>) e.g > this will be small text
5. Badges - Use single or triple backticks (\`) e.g \`single backtick badge\` or \`\`\`triple backtick badge\`\`\`

See "?" above description box in Back office for more detail

### Promo Text

Add a tag to the top of your licence card highlighting discounts or other benefits of a given licence. Example use cases include highlighting the discount which an annual licence represents over the monthly licence, or explicitly highlighting an [Auto-applied Discounts](/platform-knowledge-base/back-office/licences/promotions/auto-applied-discounts.md) or sale which you are currently offering.

This is "20% off" in the screenshot below;

<figure><img src="/files/1M0fj339wbaVRuO3zVch" alt="" width="188"><figcaption></figcaption></figure>

The promo text background colour will always inherit the same colour as your CTA (e.g. "Select Licence"). Note that this will not show in the preview in back office (where a gold colour consistent with back office will always be used).

#### Auto-applied discounts use case & best practices

If you intend to use this promo text to highlight an [Auto-applied Discounts](/platform-knowledge-base/back-office/licences/promotions/auto-applied-discounts.md), please take note of these best practices:

1. Your auto-applied discount should be available to all customers purchasing through the web. If your promotion/auto-applied discount is not available for a certain region, this promo text will still be shown and would therefore be incorrect
2. If you have IAPs available, and you have not set up the same discounts with the IAP merchants (Apple, Google, Amazon, Samsung, Vizio etc), please exercise caution when using the promo text. The promo text will be shown on all licence cards, whereas [Auto-applied Discounts](/platform-knowledge-base/back-office/licences/promotions/auto-applied-discounts.md) only apply to web purchases. You should either:
   1. Not use the promo text if you have IAPs configured on the licence but won't be discounting your IAPs, OR
   2. Make sure your promo text and/or licence text calls out that this discount is only available through the website

### Monthly Breakdown

An optional breakdown for licences which renew at greater than a 1 month cadence: allows users to visualise the "effective" monthly cost of a given licence.

### Colours

<figure><img src="/files/3W2mI1EskWkQS7503l6h" alt=""><figcaption></figcaption></figure>

Both the background and foreground (text) colour are configurable. This can be used to provide a consistent themed experience for your purchase flow that better matches your brand colours. It will also allow you to better highlight any deals or licences that represent unique value for your end customers.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/licences/licence/licence-card-configuration.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
