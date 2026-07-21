> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/analytics-1/business-intelligence-dashboard-mvp.md).

# Business Intelligence Dashboard

Under the Analytics drop-down you will notice an option called BI Dashboard otherwise known as Business Intelligence Dashboard. This dashboards provides real-times results of your business metrics for the platform.

![BI Dashboard aka Business Intelligence Dashboard](/files/-M57ZmlmsZ9uIt0dchnm)

The first section on the Business Intelligence Dashboard it covers highlights from the Revenue and Subscription sections to give you a quick overview of your business metrics. That section includes information on Average Revenue, Average Churn, New Purchases, Active Licences, New Trials, Trial Conversions, Churned Revenue, Average Rev/Purchase and Winbacks

![](/files/-M3RCpiX8xG5h6A5CaMo)

You will notice on the Business Intelligence Dashboard that you have the ability to apply date filters/filters as well as see business metrics relating to your realm.&#x20;

### Date Filter

The date filter includes a set of pre-set dates filters which are;

* **Current date**
* **Weekly**
* **Monthly**&#x20;
* **Month To Date (MTD)**
* **Quarter To Date (QTD)**
* **Year To Date (YTD)**

With these pre-set data filters you also have the ability to define custom primary and secondary date periods, and granularity providing complete flexibility with retrieving your data.

![](/files/-M3RuGQLsd2uZ9IQ7jyw)

### Filters

Along with having the ability to use the date filters you can also use the following to specify what data is shown.

* **Country:** Ability to select from the countries list to see the data for a specific country
* **Licence Type:** Ability to select from All, PPV, Subscriptions and Other to see the data for those specific licence type.
* **Licence Name:** Ability to select from the different licences that have been created to see the data for those specific licence type.
* **Payment Type:** Ability to select from All, Credit Card and Paypal to see the data for those specific payment type.

![](/files/-M3RuedFBHq2GaYd0G--)

### **Headlines**&#x20;

The metrics displayed at the very top of the dashboard are the topline metrics, that aim to give clients a quick overview of whats available.&#x20;

<figure><img src="/files/S2tXqw9xS2no55GDMjZo" alt=""><figcaption></figcaption></figure>

* **Average Revenue**: Average revenue accrued for all Stripe and PayPal purchases for the reporting period.
* **Average Churn:** Average churn, over a rolling 30-day period, due to expiries, revocations and cancellations.
* **New Purchases:** The number of new purchases, across all payment providers, within the reporting period.&#x20;

  * It includes all confirmed purchases for purchases where payment is "managed by our platform" and for in-app purchases "payment managed by the app stores"
  * It includes purchases for subscriptions, PPV, and rentals (but you can filter to see which one you're interested in)
  * It includes free trial purchases
  * It includes free purchases (ie: price is 0 such as paid with a voucher discount)
  * It does not include unconfirmed purchases (see note below)
  * It does not count each month's subsequent successful renewal of prior purchases as a new purchase. monthly renewals are just existing subscriptions for previous purchases that are still active and would not be counted as new.

Note: think of unconfirmed purchases as orders placed and user has access while we confirm their payment processes. Once processed the order/purchase is confirmed and will show up in the new purchases metric.

* **Active Licences**: Total number of users with an active entitlement granted by a subscription licence.

  * It includes all confirmed purchases that have not yet expired (ie: still active)
  * It includes licences still active that are "payment managed by our platform" and licences of in-app purchases "payment managed by the app stores"
  * It includes licences that are actively on a free trial
  * It includes Rentals&#x20;
  * It does not include PPV
  * It does include subsequent successful monthly renewals of prior purchases. monthly renewals are just existing subscriptions for previous purchases that are still active.

* **New Trials**: The number of new trials purchased within the reporting period.

* **Trial Conversions:** The number of users who have converted from a free-trial user to a paying subscriber.

* **Churned Revenue:** Estimated revenue lost, over a rolling 30-day period, due to expiries, revocations and cancellations.

* **Average Revenue / Purchase:** Average revenue made on Stripe and PayPal, per purchase.

* **Winbacks:** Total number of EXIDs that had previously had a subscription licence, churned and then repurchased.

* **Life Time Value (LTV)**: An estimate of the average revenue that a customer will generate throughout their lifespan as a customer. This 'worth' of a customer can help determine many economic decisions for a company including marketing budget, resources, profitability and forecasting.

* **Monthly Recurring Revenue (MRR):** Your normalized monthly revenue from all active and past-due subscriptions. It’s the best single measure of the health and trajectory of a recurring revenue business.

### **Revenue**&#x20;

Under the highlights section of the dashboard, the next section is Revenue and this will show an in-depth look at all revenue-related metrics for your platform.

* **Average Revenue:** Average revenue accrued for all Stripe and PayPal purchases for the reporting period
* **Churned Revenue:** Estimated revenue lost, over a rolling 30-day period, due to expiries, revocations and cancellations.
* **Average Revenue/Purchase:** Average revenue made on Stripe and PayPal, per purchase
* **Average Churn:** Average churn, over a rolling 30-day period, due to expiries, revocations and cancellations.
* **Refunded Revenue**: Amount of money refunded via stripe and paypal within the reporting period.&#x20;
* **Refunds:** No of refunds issued via stripe and paypal within the reporting period.&#x20;
* **Soft Failed Transactions:** Number of pending transactions in a soft fail state.&#x20;
  * Stripe leverages its smart retry logic to determine the optimal times to retry failed invoice payments based on customer, card, and charge-specific properties&#x20;
* **Soft Failed Revenue**: Pending revenue, caused by transactions currently in a soft-fail state.&#x20;
* **Revenue vs. Churn:** A stacked chart comparing current churn and revenue, with a view of your current net position.

![](https://s3.amazonaws.com/release-assets/production/team-2034/5e751b702f861_Screen%20Shot%202020-03-20%20at%2018.31.51.png)

### **Subscriptions**&#x20;

Under the Revenue section of the dashboard, the last section is Subscriptions and this will show an in-depth look at all subscription-related metrics for your platform.

* **Active Licences:** The number of users that currently own an active Subscription or Rental licence within the reporting period.

  * It includes all confirmed purchases that have not yet expired (ie: still active)
  * It includes licences still active that are "payment managed by our platform" and licences of in-app purchases "payment managed by the app stores"
  * It includes licences that are actively on a free trial
  * It includes Rentals&#x20;
  * It does not include PPV
  * It does include subsequent successful monthly renewals of prior purchases. monthly renewals are just existing subscriptions for previous purchases that are still active.

* **New Purchases:** The number of new purchases within the reporting period.

* **Pending Churn:** The number of licences pending churn after the licences have been deactivated within the reporting period.

* **Reactivations:** The number of licences pending churn that have been reactivated within the reporting period.

* **New Trials:** The number of new trials purchased within the reporting period.

* **Trial Conversions:** The number of users who have converted from a free-trial user to a paying subscriber within the reporting period.

![](/files/-M64iUaDLqP8LpPI44IS)

![](/files/-M64iXR0rZ8-uFifdPI4)

### Package Purchases:  <a href="#life-time-value-ltv" id="life-time-value-ltv"></a>

The metrics displayed here are the same as displayed above by broken down by licences.

### [Top Content](#user-content-fn-1)[^1]

* **Average time:** Total watch duration / Total views&#x20;
* **Total Views:** Total number of view sessions&#x20;
* **Unique Viewers:** The distinct customerID's across views &#x20;

### **Data points NOT included in the BI Dashboard:**  <a href="#life-time-value-ltv" id="life-time-value-ltv"></a>

**Active Trials -** The number of free trials that are currently Active&#x20;

Source: Customer summary report&#x20;

How: Filter by LICENCE\_STATUS = TRIAL\_ACTIVE&#x20;

Caveat:&#x20;

* Does not include IAP's&#x20;
* This data only reports on a snapshot in time

NB// The metric on the BI Dashboard only includes "New Purchases"&#x20;

**Paid Active licences** - The number of users who are currently on a paid active licence (this does NOT include free trials)

Source: Customer summary report&#x20;

How: Filter by LICENCE STATUS = ACTIVE&#x20;

Caveat:&#x20;

* This date only reports on a snapshot in time

NB// The metric on the BI dashboard "ACTIVE LICENCES" includes Free Trials

**Total Subscriptions** - Unique list of customers (by customer ID) with an active licence status. It does not include customers with just an active trial licence&#x20;

Source: Customer summary report&#x20;

How: Filter by LICENCE\_STATUS = ACTIVE. Copy the filteres exID to another sheet and dedup the exID to get unique subscriber count&#x20;

Caveat:&#x20;

* This would include customers that might also not be paying, such as 100% discount or otherwise&#x20;

**Retention - Cancelled Licence (aka cancelled / revoked)** - The number of subscriptions that have been cancelled and no longer grants access on the date you are interested in&#x20;

Source: Transaction Report&#x20;

How:&#x20;

* Filter by "PAYMENT\_STATUS" = Cancelled / Revoked
* Sort by "Date of Order"&#x20;
* Count the records for the time frame you are looking for&#x20;

#### &#x20;<a href="#winbacks" id="winbacks"></a>

[^1]:


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/analytics-1/business-intelligence-dashboard-mvp.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
