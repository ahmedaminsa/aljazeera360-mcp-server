> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/licences/cohorts-and-advanced-licences/travelling-licences.md).

# Travelling Licences

If you want to enable your customer's purchases to "travel" with them outside of a restricted home territory so that they can continue to enjoy a purchase whilst travelling, there are solutions available on the Vesper platform.

## Simple: Licence usability

When [Creating a Licence](/platform-knowledge-base/back-office/licences/licence/creating-a-licence.md), you will set the licence purchasbility restrictions by country (e.g. purchasable only in the USA) in step 2, followed by the usage restrictions in step 6. So, if for example you set the licence purchasbility to the US but included Canada as a "usable" country, anyone who made a purchase in the US, then travelled to Canada, would still be able to access their licence indefinitely.

This option is fully self service in the Vesper platform. It is most commonly applied to EU portability.

## Advanced: "Couch/Travel rights"

We use the term Travel rights to refer to a unique configuration supported by Vesper that allows your licence to be valid for a given time period after you leave the home region. This is possible through [Cohorts & Advanced Licences](/platform-knowledge-base/back-office/licences/cohorts-and-advanced-licences.md).

Taking the example above in the Simple option. You may chose to make your licence purchasable in the US, and then usable in Canada but only for 30 days after the user leaves the US. After 30 days, their access will expire and they will be unable to use the licence.

This setup uses a Vesper platform concept internally known as "cohort licensing". It relies on Vesper detecting the user's country when they access the service, identifying it as being in the home region, and then assigning them a property that will expire after 30 days (in the example above). If the user should access the service again in-region, they will be re-granted that property which will expire after 30 days from that most recent login.

Travel rights can be applied internationally at a country level, or in the US at a zip-code level (whereby a licence is only accessible in a given zip-code list, then travel-able for the rest of the US).

If you wish to set up this advanced travel rights system, please contact your Platform Account Manager, you will need to provide:

1. The list of countries/zip codes you wish to define as the "home region"
2. All countries that you want customers to be able to travel to
3. The number of days you want your licence to remain in a travelling state before it expires
4. Copy explaining a user is out of region, and links to any FAQs you have created

Note that it typically takes 2-4 weeks to configure, test and validate travel rights, depending on the requested complexity.

### Most common user experience

Most of Vesper's customers using the advance travel rights option are using it as follows:

The end-customer can only purchase and watch the content in a specific city/state in the US, as live games can only be watched in that limited region. If the end-customer accesses the service from that region with a specific device, they will be able to travel with that specific device for 30 days and continue watching the live events.&#x20;

After 30 days their access expires and they will be shown a padlock over the live content. Tapping on the padlock will show a [Signposting Licences](/platform-knowledge-base/back-office/licences/cohorts-and-advanced-licences/signposting-licences.md) which informs them that they have lost access until they return to the home region.

Note that if the user signs out from that travelling device, access will also be lost until it returns to the home region.

## A note on georestrictions

Travelling licences never override Vesper's VOD and Live event allow-list and block-list configuration. At a base level, any georestrictions applied on VOD or Live content are treated as a rights issue and will prevent playback in those regions under any circumstance.

If you wish to make live or VOD content accessible outside of a given region, all of those regions must be allowed on the VOD and Live systems. You will be moving your geo-restrictions up from the Content level below, to the Licence level.

<figure><img src="/files/h3mvTzi4HTssCjEj0aKO" alt=""><figcaption></figcaption></figure>

Contact your Platform Account Manager for more information or to discuss how you a travelling licence is best implemented for your use case.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/licences/cohorts-and-advanced-licences/travelling-licences.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
