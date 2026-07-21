> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/licences/cohorts-and-advanced-licences.md).

# Cohorts & Advanced Licences

The Vesper identity cohorts system (not to be confused with cohorts in Vesper insights) can be utilised to unlock advanced licence restrictions and use cases.

At it's simplest explanation: using cohorts it is possible to define that "only customers that meet a defined criteria can ***purchase*** or ***access*** this licence" or "whilst anyone can purchase this licence, a certain customer criteria may restrict using the licence".

## Identity Cohorts: Overview

Identity cohorts can be used as a method to assign a property or identifier to an end customer by tagging them as being in a defined cohort. In most instances those identifiers are provided by third parties outside of Vesper, such as an external SSO, or an external party that is selling access to your service outside of the Vesper platform.

Examples of cohorts:

1. An external licence provider is set up on the platform, they assign a cohort to a user once they have purchased access to the service through the provider's external system (for example, a telecommunications operator bundling a service with a mobile service plan)
2. Vesper engineering teams set up a set of cohort rules to identify when users are in certain geographic locations ( [Signposting Licences](/platform-knowledge-base/back-office/licences/cohorts-and-advanced-licences/signposting-licences.md)). The cohort applied to the user identifies if they are inside or outside of those defined regions.
3. A third party is granted access to assign a cohort to users once they have completed checks on that user outside of the platform (for example, they have performed an identity verification check)

Each of the above is a different "Cohort provider". An entity able to provide information about the user. A cohort provider can have multiple group IDs. For example provider 1 in the first example may have 3 IDs to indicate the level of access the user has purchased

* Basic Tier
* Reduced Ads Tier
* Premium Tier

Each group ID and provider ID will have a three letter acronym associated with it during setup.

In the Vesper system, were provider 1 called "MobileCo" (MOB) then we may represent these cohorts with three letter acronyms such as:

MOB: BAS\
MOB: RED\
MOB: PRM

Where the format is: \<providerID> : \<groupID>. These representations will change from provider to provider, for now it is only important to understand that a provider can have multiple cohort groups, and that they are represented in this format.

## Guide

How to utilise the cohort restriction system in Vesper licensing.

### Prerequisite: Set up cohort providers

This step of the process is not available in self-service.

Work with your Platform Account Manager to ensure your cohort providers are correctly set up. If a third party is providing your cohorts, it may require that third party to integrate with Vesper's APIs in order to pass the relevant information.

If there is no third party involved, you will either be leveraging existing Vesper cohort capabilities or requesting a change to introduce new&#x20;

### Definitions: Licence restriction

#### Acquisition

Means will the user be able to see the licence to acquire it.&#x20;

For *free* licences, this is the same as use. As free licences are granted to all customers who are entitled to acquire them.

For *paid* licences, this defines whether or not the customer can see the licence in the checkout flow to make the purchase.

#### Usage

This concept applies to paid licences only. Even if the user has acquired the licence, are they able to use it given their current circumstances.

### Step by Step

With a set of cohorts defined, it is now possible to assign logic to whether or not a customer is able to **acquire** and/or **use** any given licence.

#### **Restricting the acquisition of a licence by cohort**

During the second step of the [Creating a Licence](/platform-knowledge-base/back-office/licences/licence/creating-a-licence.md) screen, the following configuration will determine if a user is able to acquire/purchase a licence.

<figure><img src="/files/uTJ8cBtuSKdYuUzEFAkj" alt=""><figcaption></figcaption></figure>

1. All licence types (free or paid) can have acquisition restrictions applied. See [#acquisition](#acquisition "mention")for more detail.
2. Toggle the setting `Cohort acquisition restrictions` to `yes`, within `Set licence availability`
3. Set the condition:
   1. `Any` - If any of the rules match, grant access to acquire. If no rules have been configured the user will not be granted access to acquire.
   2. `All` - All rules must match in order to grant access to use. If no rules have been configured the user will be granted access to acquire.
   3. `None` - If any of the rules match, do not grant access to use. If no rules have been configured the user will be granted access to acquire.
4. Select a `provider` and click the plus symbol “+”
5. Select a `group id` and click the plus symbol “+”
6. Set either `allow` or `block`
   1. `Allow` - If set to allow list, only users with the provider group id assigned to their account will be able to acquire this licence.
   2. `Block` - If set to block list, all users expect those with the provider group id assigned to their account will be able to acquire this licence.

#### **Restricting the usage of a licence by cohort**

During the sixth step of the [Creating a Licence](/platform-knowledge-base/back-office/licences/licence/creating-a-licence.md) screen, the following configuration will determine if a user is able to use a licence/watch content.

<figure><img src="/files/1zHM5b7XWt2tLPmwaeLV" alt=""><figcaption></figcaption></figure>

1. The licence type should be either Subscription, Rental, PPV or Fixed date licence (a paid licence)
2. Toggle the setting `Cohort usage restrictions` to `yes`, within `Define usage restrictions`
3. Set the condition:
   1. `Any` - If any of the rules match, grant access to use. If no rules have been configured the user will not be granted access to use.
   2. `All` - All rules must match in order to grant access to use. If no rules have been configured the user will be granted access to use.
   3. `None` - If any of the rules match, do not grant access to use. If no rules have been configured the user will be granted access to use.
4. Select a `provider` and click the plus symbol “+”
5. Select a `group id` and click the plus symbol “+”
6. Set either `allow` or `block`
   1. `Allow` - If set to allow list, only users with the provider group id assigned to their account will be able to use this licence.
   2. `Block` - If set to block list, all users expect those with the provider group id assigned to their account will be able to use this licence.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/licences/cohorts-and-advanced-licences.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
