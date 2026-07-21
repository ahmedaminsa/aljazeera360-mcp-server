> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/licences/licence.md).

# Licences Types & Guides

This section will be going over the different types of licences, their attributes, the Pay-Per-View (PPV) & Rentals flow, and an explanation of what a family licence is and how it works.

<figure><img src="/files/BuycrQovFms9uiq840QQ" alt=""><figcaption></figcaption></figure>

### Basic Licence Types

There are 4 basic types of licences available on Vesper:

1. **Subscription** - This allows you to create daily, weekly monthly, annual or biannual subscription service for users to view content.
2. **Pay-Per-View (PPV)** - This allows you to create a subscription for a single event in advance of the event taking place and would expire on the dates that you set. See the image below to find out how the Pay-Per-View (PPV) licence flow would work.
3. **Rental**  - This allows users to purchase content and view it for a certain amount of time.&#x20;
4. **Free** - Allows users to watch content with no active subscription/PPV/Rental. A free licence can be configured in several ways, depending on your realm's configuration for Guest access (i.e. users that have no login)\
   If you wish to setup multiple levels of Free licensing, you should *contact your Platform Account Manager* to assist in configuring your realm.
   * **Guest Free** - A free licence that's granted to all users, whether signed in or not. This allow users to go onto the Realm without having to sign up. A resident can choose if they want to show them free content or locked content.
   * **Registered Free** - This allows users to watch content that they don't have to pay for, but requires registration (i.e. providing their e-mail address).&#x20;

The basic types are available to all Vesper residents with no further setup (excluding initial setup of a merchant account and/or IAP accounts for apps).

### Advanced Licence Types

In addition, there are advanced licence types documented under [Cohorts & Advanced Licences](/platform-knowledge-base/back-office/licences/cohorts-and-advanced-licences.md) which require more setup and potentially integrations with third parties. Some examples of these include:

1. [Externally Acquirable Licenses](/platform-knowledge-base/back-office/licences/cohorts-and-advanced-licences/externally-acquirable-licenses.md) - A type of **Free** licence in the Vesper system which is acquired outside of Vesper. Utilising an externally acquirable licence requires an integration with a supported licence or identity provider that can pass information about a given user to Vesper.
2. [Signposting Licences](/platform-knowledge-base/back-office/licences/cohorts-and-advanced-licences/signposting-licences.md) - The use of the licence cards to indicate to a user that content is locked and cannot be unlocked directly on their current platform. Used to provide signposting information about what steps the user needs to take to unlock the content.
3. [Travelling Licences](/platform-knowledge-base/back-office/licences/cohorts-and-advanced-licences/travelling-licences.md) - An advanced configuration that allows end customers to travel outside of a services' market area whilst still maintaining access to their content for a defined period of time.

&#x20;


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/licences/licence.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
