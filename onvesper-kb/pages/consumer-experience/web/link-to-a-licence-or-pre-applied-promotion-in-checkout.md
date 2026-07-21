> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/consumer-experience/web/link-to-a-licence-or-pre-applied-promotion-in-checkout.md).

# Link to a licence or pre-applied promotion in checkout

### **Link to Sign up**

```html
/signup
```

Query string parameters are useful if a marketeer is advertising a specific licence, or common group of licences. In this scenario, they don't necessarily want a user to arrive at `/signup` and be presented with ALL available licences for purchase. Rather, they want to present just a subset. Typical example:

* There are x3 licences on-sale in `/signup` - a monthly, an annual and a PPV
* You wish to advertise the PPV (not the monthly or annual)
* So they would like a dedicated URL that returns only the PPV

To do this, simply add  `?licences=licence ID` to the `/signup` URL, e.g.:

```html
/signup?licences=1897
```

The full URL would look like this:

```
https://app.myawesomestreamingservice.com/signup?licences=1897
```

The user will then land straight on the checkout flow of said licence without having the option to select any other plans.

<figure><img src="/files/lxYj9TKKk4qmZnC31tTt" alt=""><figcaption><p>User lands on the order summary for the licence targeted</p></figcaption></figure>

You can retrieve the licence ID from **Vesper Back Office -> Licences -> Package Licences**

It will be the first 4-digit number on the top right corner of the licence:

<figure><img src="/files/HM9d5KdN8Xknx7mtTP1i" alt=""><figcaption><p>Licence ID</p></figcaption></figure>

You are not limited to link to a single licence, however: you can append more licences by separating them with a comma (do **not** add a space!):

```
https://app.myawesomestreamingservice.com/signup?licences=1234,9876
```

<figure><img src="/files/tqoeVJa9DSdsmZxtPljF" alt=""><figcaption><p>You can deep link to a subset of licences by appending their IDs to the URL</p></figcaption></figure>

### Link to Purchase

```
/purchase
```

You can also link authenticated **and** unauthenticated users to purchase a specific licence through a call-to-action in a Hero creative, for example. This is useful if you wish to offer additional licences, such as add-ons, only to a subset of users that have already been granted an entitlement to the platform.&#x20;

To do this, simply add  `?licences=licence ID` to the `/purchase` URL, e.g.:

```
/purchase?licences=105390
```

The full URL would look like this:

```
https://app.myawesomestreamingservice.com/purchase?licences=105390
```

The authenticated user will then land straight on the checkout flow of said licence without having the option to select any other plans.

## Include a Promotion

You can additionally include a promotion to be pre-applied at checkout by appending  `&voucher=voucher ID` to the above URL(s)

This is best done with a single licence unless the promotion is valid across all licences set in the string parameters&#x20;

The full URL would look like this:

```
https://app.myawesomestreamingservice.com/signup?licences=1897&voucher=1234
```

You can quickly get a promotional URL deeplink by following this guide: [Promotions / Promo Codes](/platform-knowledge-base/back-office/licences/promotions.md#fast-redeem-linking-directly-to-the-promotion-in-marketing)

### Users

There are two types of users that can use these links:&#x20;

1. New Users - They simply click the link, sign up and will be presented with the relevant licence / licences.&#x20;
2. Current Users - It's important for this cohort of users that they are logged in to access the relevant licence / licences. They can do this either by:&#x20;
   1. Logging in and then clicking on the deep link&#x20;
   2. Clicking on the deep link and then clicking the top right hand corner to "Sign in" to the service (rather than signing up).&#x20;

If the user attempts to sign up again they will be shown the following error "User already exists" - If you would like to change this error message to make the experience more seamless, please reach out to your account management team.&#x20;

{% content-ref url="/pages/-M57k5jiEXjZDjOZ8IYz" %}
[Licences & Promotions](/platform-knowledge-base/back-office/licences.md)
{% endcontent-ref %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/consumer-experience/web/link-to-a-licence-or-pre-applied-promotion-in-checkout.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
