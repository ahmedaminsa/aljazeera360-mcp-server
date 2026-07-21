> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/licences/licence/licence-family-architecture-and-upgrades-downgrades.md).

# Licence Family Architecture & Upgrades/Downgrades

When creating subscription licences you may want to group them into a 'family' so that users can upgrade or downgrade without having to cancel and repurchase.

### Creating a family

In order to create a licence family, click licence family under the dropdown.

<figure><img src="/files/MbfAmWm9zihFoaM9ZJKZ" alt=""><figcaption></figcaption></figure>

### Add a family to your licence&#x20;

Click create/edit your licence and search for your family name ' ULTIMATE BUNDLE'

<figure><img src="/files/mBKMVgBO0KNGm6OhTJpS" alt=""><figcaption></figcaption></figure>

Add the family rank, e.g. your ultimate monthly licence may have a rank of 10.&#x20;

Your ultimate annual licence would then have a rank of 20, meaning you 'upgrade' to the higher rank & licence.&#x20;

Any new licences that have been created once a licence family has been set up can still be added into the licence family. The ranking of the licence will then change depending on how you would like them to sit in the table.

An example of how the upgrade & downgrade logic would work in a licence family;

<figure><img src="/files/dCiwiBuDFFgLemz5N2pZ" alt=""><figcaption></figcaption></figure>

"Downgrades" where a user moves to a lower tier licence normally only take place after the current billing cycle has ended. So if the user is on a premium tier and opts to downgrade to a cheaper tier, they will continue to have their premium tier benefits for the remaining billing cycle (e.g. month) that they already paid for, then be moved down to the cheaper tier at the start of their next billing cycle.

#### Immediate downgrades

If you have a use case where you wish to allow customers to immediately "downgrade" their licence and receive a pro-rata refund for the remainder of the billing cycle, Vesper can support this for managed payments (e.g. web based credit/debit card transactions), but this is a special case that you need to consider and understand the impact of. Contact your account manager to discuss this option.

### Pay-Per-View & Rental licences&#x20;

PPVS & Rentals will not follow upgrade/downgrade paths in a licence family as these are temporary assets compared to subscription licences.&#x20;

*If you add PPVs or rentals to a licence family, an end user may not be able to purchase multiple PPVs or Rentals within the same family*. **We recommend excluding PPVs/Rentals from a licence family**.&#x20;

<figure><img src="/files/qHvzKsSKtpiGjodHfr3x" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/hBT3hQ6LthpkbmZjqESW" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/tEe2YYgInJrRs7WStZ3k" alt=""><figcaption></figcaption></figure>

#### **Duplicate Licences**

In theory, a user should **NOT** be able to buy 2 licences if the licences are in the same family.&#x20;

However, the only scenario where a user might be able to is:&#x20;

1. User purchases a licence on Web&#x20;
2. User purchases a licence on Mobile (IAP)&#x20;

There will be nothing to stop the user from purchasing that second licence on mobile as Apple / Google do not have any knowledge that the user has already purchased a licence on Web.&#x20;

Please be aware that you can **NOT** do it the other way round - buy an IAP and then a Web licence as we will stop you from buying a web licence if you already have an IAP on the service.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/licences/licence/licence-family-architecture-and-upgrades-downgrades.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
