> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/consumer-experience/payments-and-subscription-management/in-app-purchase-iap.md).

# In-app purchase (IAP)

Building IAPs via stores for your service requires an [active licence](/platform-knowledge-base/back-office/licences.md) configured in [Back Office](https://backoffice.onvesper.com) platform and Admin permissions.

There are two possible IAP purchase types in both stores, a "Subscription" (a recurring payment) and an "In-app product", a single purchase that does not automatically review.

Please note - the first “Subscription” and “In-app product” will have to be submitted for review with a binary app, even if the app is in the market.

## Apple

### [**Apple**](https://appstoreconnect.apple.com/login) **- In-App Products**

Endeavor recommends using "In-app products" for Pay-Per-view licences

* Select “In-App Purchases” in the side menu in App Store Connect
* Click “+” in the top
* You will be asked to complete:
  * Type: Non-Consumable for PPV. Consumable for Rentals.
  * Reference Name: **myserviceannual.iap.2022.v1** (example)
  * Product ID: **myservivceannual.2022.v1** (example)
* Complete the relevant metadata:

  * Price Schedule - Note: you are restricted to “Tiers” so the price has to be to the closest $0.99
  * Tax Category = Match to parent app
  * App Store Localisation -
    * Localization
    * Display Name
    * Description
  * Screenshot of licence - To be provided by your TAM via Figma file

  ![](/files/nuRjtbVhyopPoqpbGmr4)

&#x20;

### [Apple ](https://appstoreconnect.apple.com/)- Subscriptions  <a href="#apple-subscriptions" id="apple-subscriptions"></a>

Subscriptions are Auto-renewing Licences, and should be used when creating an IAP for an Endeavor subscription product.

* Navigate to App Store Connect
* Navigate to the App you would like to create a subscription for
* Navigate to Left hand side bar
* Click on “Subscriptions”
* Click “+” on Subscription Groups
* Enter Subscription Group e.g “My Service Subscription Licences”
* Click “+”
* Enter “Reference Name” and “Product Code” e.g **myservivceannual.2022.v1** (NB// we typically follow the above format - ensure that you do not use capital letters (You can use the same for both).
* Complete the relevant metadata:
  * Subscription Duration - Monthly vs Annual
  * Subscription Pricing
    * Click “+”
    * Set the pricing for each territory
    * Click “+” again
    * Set Introductory Offers - If a Free Trial is required
  * Tax Category = “Same as parent app”
  * App Store Localization
    * Click “+”
    * Localisation = Language
    * Display Name
    * Description
  * Review Information
  * Add Review notes - This can be description of licence
* Once complete the status of the licence should be “Ready for Review” - this should allow you to test the IAP’s in Testflight

See the example of the End Result:

<img src="/files/PRpwaWAlNPw5hb7aEza0" alt="" data-size="original">

### [Apple](https://appstoreconnect.apple.com/) - Non-Renewing Subscriptions  <a href="#apple-subscriptions" id="apple-subscriptions"></a>

Non-Renewing Subscriptions are one off payments that will grant access for a specific time period and should be used for Rental licenses

* Navigate to App Store Connect
* Navigate to the App you would like to create a subscription for
* Navigate to Left hand side bar
* Click on “Subscriptions”
* Click “Manage” under Non-Renewing Subscriptions
* Click “+”
* Enter “Reference Name” and “Product Code” e.g **myservice.rental.2022.v1** (NB// we typically follow the above format - ensure that you do not use capital letters (You can use the same for both).
* Complete the relevant metadata:
  * Price Schedule
    * Click “+”
    * Set the pricing for each territory
  * Tax Category = “Same as parent app”
  * App Store Localization
    * Click “+”
    * Localisation = Language
    * Display Name
    * Description
  * Review Information
  * Add Review notes - This can be description of licence
* Once complete the status of the licence should be “Ready for Review” - this should allow you to test the IAP’s in Testflight

See the example of the End Result:\
![](/files/Czwyf9XfWsBmrjMEFdGZ)

## Google

### [Google](https://play.google.com/console/) - In-app product  <a href="#google-in-app-product" id="google-in-app-product"></a>

Endeavor recommends using "In-app products" for Pay-Per-view licences.

Pricing Template:

1. Navigate to main dashboard - do not click directly in the app
2. Left hand side menu - “Set up”
3. Click “Pricing Template”
4. Create Pricing Template
   1. Name: Name of licence
   2. Price: Set default price - The currency for this price will be based on the location of the app store itself
5. Once Pricing Template has been created then navigate to the App
6. Click into the app
7. Navigate down the left hand side menu to - “In-App Products”
8. Click “Create Product”
   1. Product ID: **myservivceannual.iap.2022.v1** (Example)
   2. Product Details
      1. Name: Name of licence
      2. Description: Short Description of licence
   3. Price
      1. Add Pricing Template
   4. Tax Compliance - Do check this on a per client basis
      1. Digital Content
      2. Reduced VAT Rates
      3. Streaming
9. Activate In-app product

### [Google](https://play.google.com/console/) - Subscriptions  <a href="#google-subscriptions" id="google-subscriptions"></a>

Subscriptions are Auto-renewing Licences (including Rentals which have an auto-renewing period of 0 i.e. never renew) and should be used when creating an IAP for an Endeavor subscription product.

Google subscriptions follow a package heirarchy as follows in the below example:

{% hint style="info" %}
Product-ID-1

-> BasePlan1 (Weekly rental, one off payment non-renewing plan)\
-> BasePlan2 (Monthly subscription renewing plan)\
-> BasePlan3 (Annual subscription renewing plan)
{% endhint %}

The product ID can be equated to a Vesper Platform Licence family (further reading here: [Licence Family Architecture & Upgrades/Downgrades](/platform-knowledge-base/back-office/licences/licence/licence-family-architecture-and-upgrades-downgrades.md)) as you are able to upgrade downgrade between baseplans contained inside this product ID.

Base plans can be equated to a Vesper Platform Licence package with a one-to-one relationship, i.e. each unique base plan code can only be applicable to a unique licence package on the Vesper Platform.

* Navigate to Google Play Console
* Click the app you would like to create a subscription for
* Navigate to the left-hand side bar
* Click on “Subscriptions”
* Create a Subscription
* Enter “Product ID” and “Name”

<figure><img src="/files/xi4DlaeqdatA1oxyCN9r" alt=""><figcaption></figcaption></figure>

* The product ID entered here will need to be applied to your given license family on Vesper Backoffice&#x20;

<figure><img src="/files/dwId0fMFetasXVX6oBHV" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/SbXZHGCkLgSNxoiNj6wV" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/eR5WZ2ChEYRu2zjXqG7g" alt=""><figcaption></figcaption></figure>

* Click on “Edit subscription details”
* Enter Subscription Details:
  * Benefits - Optional
  * Description - Licence Description
  * Tax Compliance
    * Click “Manage settings”
    * Click Digital Content - but if concerned reach out to your manager to confirm
    * Manage reduced tax rates - optional
    * Click “This is a streaming product”
  * Click “Save changes”
* Add a Base Plan
  * Enter Base plan ID
  * Set Type - Auto-renewing for renewing subscriptions or Prepaid for rentals
    * Set Billing period/duration
    * set Grace period for subscriptions
    * set Allow Extension to Don't Allow for rentals
  * Tags - Optional
  * Click on “Manage country / region availability”
    * Select appropriate countries of availability
    * Click “Apply”
  * Click on “Set prices” - this is grey and doesn’t look like a button
    * select regions to bulk apply a price to (Google will calculate the currency conversion from the base price)
    * Click “Set price”
    * Enter in price and select the relevant currency
  * Click “Save”
  * Click “Activate”

<figure><img src="/files/tMAzGzkWtYPFJ8pd1jp3" alt=""><figcaption></figcaption></figure>

* Apply base plan ID to the applicable license on back office

<figure><img src="/files/y90p7XqWrmEAoJ0V0Pjr" alt=""><figcaption></figcaption></figure>

## Amazon

### [**Amazon**](https://developer.amazon.com/dashboard) **- Subscriptions / PPV**

* Navigate to Amazon Developer Console and select My Apps&#x20;

<img src="/files/vJoKV4LGKMcYvL3siHtW" alt="" data-size="original">

* Select the App for which you’d like to create the Subscription

<figure><img src="/files/yxqy3wQK3f4gSdZ7bNkQ" alt=""><figcaption></figcaption></figure>

* Navigate to Left hand side bar
* Click on “In-App Items”
* Click on “Add Single IAP”
* Click on “Add a Subscription”
* Enter Subscription Title e.g “Monthly+”
* Enter the SKU (this is not linked to DCE)
* Click “Add Subscription”

<figure><img src="/files/spYL0zoShSJx31DnvfWz" alt=""><figcaption></figcaption></figure>

Subscription Pricing and Term(s)

* Click “Add New Term”

<figure><img src="/files/ttZnFIa4ikkJZL57DUCz" alt=""><figcaption></figcaption></figure>

* Select the Term (Monthy, Annual, etc)

![](/files/bMejVqIXK08sgFfAcHBD)

* Enter the SKU (Linked to DCE per term/licence) and Create a Term

![](/files/OoMZQqUyrfKTLGA15Ji7)

* Confirm SKU as a paid subscription

![](/files/YMExGAnbHAgItj9HeB1q)

* Select Set Pricing and Save

![](/files/MiBAsau5OfO7TO1TcmVY)

* *For PPV all select Consumable so you are not required to select the term*

![](/files/bhcEOtabrplc3EcFhQhn)

## Roku

### [**Roku** ](https://my.roku.com/signin?next=https%3A%2F%2Fdeveloper.roku.com%2F)**- New Products**

Products are subscriptions and PPV

![](/files/EN8OtqksEF39tCJff1QC)

* **Navigate to the Dashboard in the Roku Console**

<figure><img src="/files/TeqVTtJfSxrcOgE1YlAM" alt=""><figcaption></figcaption></figure>

* **Select Monetisation → Products → Add New Product**

<figure><img src="/files/Ma0VhZk1m0O2M5nkuEPM" alt=""><figcaption></figcaption></figure>

Fill in the required data:

<figure><img src="/files/aJvo9U6C5QydLBXXYJwM" alt=""><figcaption></figcaption></figure>

* **Select Channels**: Beta (for testing the sub/IAP) and the channel to which you’ll be publishing to.&#x20;
* **Select:** Video
* **Product name**: Customers will see - Licence Name ( e.g PPV - Event name or Monthly Subscription - Monthly +)
* **Product identifier**: your Back Office Licence Code (e.g myservice\_PPVprod1)
* **Purchase type:**

**→ One-Time Purchase:** A movie rental/purchase, sporting event, pay-per-view, or other product that may only be purchased a single time from an SVOD channel. The publisher controls entitlements (number of viewings and permitted viewing time) for one-time purchase products in their backend system.

**→ One-Time Purchase,** Consumable - Quantity: A “packet” of identical items (such as game points, number of viewings permitted ). Enter the size of the packet in the Quantity field.

If you are creating a [TVOD-exclusive channel](https://developer.roku.com/docs/developer-program/roku-pay/implementation/tvod-channel.md), select this option and select 1 for quantity. This is because you create a single generic in-channel product per product type for a TVOD channel (rather than a product per content item as in a SVOD channel), and this setting allows that generic in-channel product to be purchased multiple times. For example, if you plan on offering movie rentals, you only need to create a single one-time purchase consumable video product. See [Creating TVOD channels](https://developer.roku.com/docs/developer-program/roku-pay/implementation/tvod-channel.md) for more information.

**→ Monthly subscription:** A product requiring a monthly charge for continued access.

**→ Yearly subscription:** A product requiring an annual charge for continued access.

* **Choose your price tier:** the price tier populates on how much your product is&#x20;

→ A chart under the Price tier field displays the price, in appropriate local currency, for each Roku Channel Store where the product will be available.

→ The Purchase price reflects the amount to be paid by the customer. The purchase price for EU Channel Store countries include VAT. Proceeds are based on pre-tax (net) prices.

→ The Your proceeds field displays the amount that you receive from Roku for the sale of the product. Based on exchange rate fluctuations, the proceeds in one Channel Store may not equal the amount to be received in another.

From the Price tier list, select one of the predefined prices for the product.

* Tiers are used to enforce 99 cent or 49 cent pricing on channel products.
* One to three-digit tier numbers are used for 99 cent pricing. Subtract 1 cent from a tier to get the corresponding price. For example, Tier 1 is 99 cents, Tier 2 is $1.99, Tier 10 is $9.99, Tier 100 is $99.99 and so on. The highest tier is 400 ($399.99).
* Four-digit tier numbers are used for 49 cent pricing. Append 49 cents to the last digit or last two digits in the tier to get the corresponding price. For example, Tier 1000 is 49 cents, Tier 1001 is $1.49, Tier 1010 is $10.49, Tier 1020 is $20.49 and so on. The highest tier is 1030 ($30.49).

![](/files/u2ZvjbtW3P6TQM8AuouT)

* **Select the clear for sale box and save**&#x20;

<div align="left"><figure><img src="/files/1hsGJkNHqMUYaw76W1No" alt=""><figcaption></figcaption></figure></div>

* *Please note that we do not support base offers*


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/consumer-experience/payments-and-subscription-management/in-app-purchase-iap.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
