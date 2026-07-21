> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/licences/price-version-migration.md).

# Price Version Migration

{% hint style="warning" %}
At the given time, **coordinate with your Account Management team to configure and schedule in a Price Version Migration.**&#x20;

* Provide your Account Management team with minimum one months notice to schedule a price version migration&#x20;
* **Coordinate with your legal team on:**
  * Applying a new price change for both new and existing users&#x20;
  * Consent type (opt in/out)&#x20;
  * Notification timeframe (e.g. notify users 30-60 days in advance of price update)

Vesper's Price Version Migration process excludes In App Purchases (IAP). Price changes for IAPs need to be managed by the Resident directly within the app stores.&#x20;
{% endhint %}

{% hint style="info" %}

{% endhint %}

## How to update an existing price point (SKU) for <mark style="color:blue;">new users</mark>

For you to schedule a price version migration for <mark style="color:purple;">existing users</mark>, you need to ensure that the price version you are migrating users **to** is available and <mark style="color:green;">purchasable</mark>.&#x20;

* Identify the license you want to update a price for. Hover over the license and select the triple dot menu to edit the licence&#x20;

<figure><img src="/files/9QdKN6YmQqk49yYtWMlq" alt=""><figcaption><p>Click on the triple dot menu --> Edit</p></figcaption></figure>

* Scroll down to identify the **Pricing Per Territory** section to update the SKUs (price points)&#x20;

<figure><img src="/files/zphK9nwCELq6eo8gire8" alt=""><figcaption></figcaption></figure>

* Click on **Configure** --> select the triple dot menu next to the SKU to schedule in a price update &#x20;

<figure><img src="/files/9EHeVGzNAEvLPpFr9agQ" alt=""><figcaption></figcaption></figure>

* Provide the **Valid From date** and **Amount**. Click **Confirm** to schedule in the new price point for <mark style="color:blue;">new users</mark>
* Once the new price point is scheduled, at the date and time of **Valid From Date** is reached, the platform will automatically update the SKU to the new price point for <mark style="color:blue;">new users.</mark> In Vesper, the former price point will now be <mark style="color:red;">Unpurchasable</mark> and the price point you scheduled in will now be <mark style="color:green;">Purchasable.</mark>&#x20;
* <mark style="color:blue;">New users</mark> that will be subscribing to your service will be purchasing at the 12.99 EUR price point, instead of the 9.99 EUR price point as an example below&#x20;

<figure><img src="/files/h3jp2lmJIAS5vi75KnEK" alt=""><figcaption></figcaption></figure>

## Schedule a Price Version Migration&#x20;

{% hint style="warning" %}
At the given time, the following steps are required to be coordinated with your Account Management Team. &#x20;
{% endhint %}

{% hint style="info" %}
Once you have scheduled in a price update on your SKUs for <mark style="color:blue;">new users</mark> and the former price point has been marked as <mark style="color:red;">unpurchasable</mark>, you can now configure a price version migration&#x20;

* You can only migrate the SKU for an <mark style="color:red;">unpurchasable</mark> price point

* The price point (SKU) of <mark style="color:purple;">existing users</mark> are migrating **to** must be <mark style="color:green;">purchasable</mark>&#x20;

* You can only migrate the SKU for web users
  * IAP price migrations must be done within the app store platforms and managed by the Resident&#x20;

* Coordinate with your Account Management team on enabling consent email templates (Opt In/Out)&#x20;

* Once you schedule a price version migration with consent email turned ON, *it will send all affected users an email **on the day** you configure the price change*&#x20;
  {% endhint %}

* Head into the license you want to perform a price version migration for

* Scroll down to **Pricing Per Territory** and select **Configure.** From there, toggle **Show Unpurchasable**&#x20;

* Identify the <mark style="color:red;">unpurchasable</mark> SKU and click on the triple dot menu to perform a migration&#x20;

<figure><img src="/files/0vD48YOJQM5SztYUDdf4" alt=""><figcaption><p>Click on Migrate Customers</p></figcaption></figure>

* A pop up modal will appear for you to fill in the following

<figure><img src="/files/gLHbaD0rbeQwGdFZSQDd" alt=""><figcaption></figcaption></figure>

* Confirm the former price point the <mark style="color:purple;">existing users</mark> are on and the price point they are migrating **to**
* Provide the **Price effective from date**
  * This is the date and time the price change will come into effect for <mark style="color:purple;">existing users.</mark> On and after this date, <mark style="color:purple;">migrated users</mark> *that have consented* will renew on the new price point&#x20;
* Select how **Discounts** should be handled&#x20;
  * **Keep discounted price**
    * Will honor the existing discount price. Once the discount period has finished, the user will move to the new price&#x20;
  * **Recalculate discounts**&#x20;
    * Will recalculate the discounted price based on the new price&#x20;
* **Notify Customers**
  * **If left unchecked -** you confirm that the users impacted by this price change will be communicated to off platform. Please note, *communicating price changes is a legal requirement and subject to the territory the end-user resides*&#x20;
  * **If checked** - The email template used for this feature should be configured and enabled. Please configure this template before proceeding. <mark style="color:orange;">The email will automatically be sent as soon as the price version migration has been scheduled</mark>
    * Coordinate with your Account Management team on Opt In or Opt Out email templates&#x20;
* **Consent Type**
  * This setting determines how users are handled if a price change occurs, and can now be configured based on user's billing address to meet regional compliance.&#x20;
  * **Opt IN** - Users will churn unless (Their subscriptions will be canceled) unless they explicitly opt in to the price update. This is often required by regulations in certain countries where explicit consent is mandatory for price changes.
  * **Opt OUT -** Users will automatically renew at new price unless they explicitly opt out of the price update. This is typically used in regions where users are assumed to accept the new price unless they actively decline.
  *

<figure><img src="/files/IkJOrxhGUe7n5Ilwj9Gy" alt=""><figcaption></figcaption></figure>

* **Consent deadline**
  * The consent deadline is the date users need to respond to the price version migration. After this deadline, the UI will not display the option to opt in or out. Once this deadline has been reached, the platform will update the user’s payment plan according to the migration date&#x20;
  * The consent deadline should be set before the migration date to ensure the platform has enough time to migrate all users over to the new price ahead of the effective date. **This should be at minimum 48 hours before the price version migration date**
* **Confirm price version migration**&#x20;

  * A pop up modal will appear to confirm your price version migration. Review all details.&#x20;
  * Once reviewed, to confirm the migration, type in **YES SCHEDULE AND EMAIL** in the open text field. Click on **Yes, Schedule and Email** to schedule the migration&#x20;

  <figure><img src="/files/gAq4gv7aETwaMO9R4exz" alt=""><figcaption></figcaption></figure>

{% hint style="danger" %}
Scheduling multiple price migrations within 1 billing period? Read the [FAQ](#i-have-an-annual-subscription-product-and-i-will-be-introducing-2-price-migrations-within-12-months) for important information.
{% endhint %}

### Review a Scheduled Price Version Migration&#x20;

* Once the migration has been scheduled, you will see that there is a new field you can click - **Price Version Migration**

<figure><img src="/files/JF17EQHgliTSP6UsUoKp" alt=""><figcaption></figcaption></figure>

* Once you click on **Price Version Migration**, it will display the Customer Migration details for you to review at any point in time&#x20;

<figure><img src="/files/a29apxZrZAebcEfvJ4xe" alt=""><figcaption></figcaption></figure>

* You can also access the Customer Migration details by toggling **Show unpurchasable** and click on the triple dot menu to **View Migration Details**&#x20;

<figure><img src="/files/SAwuPVDazeqftZNaH5d4" alt=""><figcaption></figcaption></figure>

* You can track user opt in/opt out statuses by clicking on the **View Insights** (screenshot above) menu item that will lead you directly to the Vesper Insights dashboard to monitor&#x20;
* Once the migration is complete, you can click back into the **Price Version Migration** (screenshot above) and review the completed migration

  <figure><img src="/files/FSmHPQnfearC5rvU38Sp" alt=""><figcaption></figcaption></figure>

### Cancel a Scheduled Price Version Migration&#x20;

* If you decide to cancel the *scheduled* migration, select the SKU you're going to cancel the migration for. Toggle **Show unpurchasable** and click on the triple dot menu **Cancel Customer Migration**&#x20;

<figure><img src="/files/DJncMmNpmC6LkKbtOAeB" alt=""><figcaption></figcaption></figure>

* You will receive a pop up modal to confirm you want to cancel the migration. Click **Yes, Cancel** to confirm cancellation&#x20;

<figure><img src="/files/5ZilfQNiMkSfl9YKgCY4" alt="" width="281"><figcaption></figcaption></figure>

* &#x20;Once canceled, you will no longer see the **Price Version Migration** item on the SKU&#x20;

<figure><img src="/files/xSIKM03T7UQq1YbLbqee" alt=""><figcaption></figcaption></figure>

## FAQs

#### I have an annual subscription product, and I will be introducing 2 price migrations within 12 months of each other. Are my users guaranteed to move to the latest price?

No. We recommend not changing your price multiple times within a single billing period, however if you chose to you must be aware of how the system will behave.

Consider the timeline below:

1. **1.1.2025**: Schedule a price change from $10 a year to $20 a year. All existing customers are scheduled to move to the new price.&#x20;
2. **12.12.2025:** Schedule a price change from $20 to $30 a year. All existing customers who are not already pending the price change in point 1 will be scheduled for migration.

Because these migrations happen within 1 billing period (in this case a year) and some customers purchased on say; 31.12.2024, they were not due to migrate to the $20 a year price point until the end of 2025. These customers will not be scheduled for the $30 a year price rise by default, as they are still pending their prior price rise.

Note the examaple above uses 1 year as it's the most likely scenario, but it would also occur if the price was changed twice in a month for a monthly SKU.

If you believe you will encounter this issue with your price plans, contact your Platform Account Manager to discuss your options.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/licences/price-version-migration.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
