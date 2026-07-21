> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/licences/licence/minimum-commitment-licences.md).

# Minimum Commitment Licences

Minimum commitment licences let you lock end-users into a set number of renewal cycles on a subscription before a cancellation can take effect — for example, requiring six monthly renewals before a customer is able to cancel.

### Why you'd want it

Committed-term pricing is a well-established way to retain subscribers at a discount: you offer a lower rate in exchange for a guaranteed renewal period, which improves revenue predictability and reduces early churn. The commercial terms are enforced automatically rather than relying on the honour system, and customers are told exactly what they're agreeing to at checkout and by email, so there's no surprise when they try to cancel early.

### How it works

Minimum commitment can be applied to a renewing licence e.g. a subscription.

{% hint style="info" %}
Minimum commitment licences is a realm-level capability. Contact your account team if you are interested in this feature. There are prerequisites and config changes required before it appears in the licence configuration UI, including updates to e-mail templates sent to customers.
{% endhint %}

Once enabled, configure it directly on a licence:

1. Create or edit a licence in Creating a Licence.
2. In the **Define licence type** section, set a value for **Minimum commitment** — this is the number of billing cycles the customer must complete before a cancellation can take effect.

<table><thead><tr><th width="172.75390625">Value</th><th>Effect</th></tr></thead><tbody><tr><td><code>0</code> or blank</td><td>No minimum commitment — standard cancellation rules apply</td></tr><tr><td><code>2</code></td><td>The customer is charged twice (the initial purchase plus one renewal) before a cancellation can take effect</td></tr><tr><td><code>12</code></td><td>The customer is charged 12 times (the initial purchase plus 11 renewals) before a cancellation can take effect</td></tr></tbody></table>

**Example:** a customer purchases and is charged on 1 January 2026 with a minimum commitment of 12. They request to cancel on 5 March. The cancellation takes effect on 1 January 2027, once the 12th charge has been collected.

Once the commitment period ends, the subscription renews as normal — the customer is not automatically placed into a new commitment, and can cancel at any time from that point.

{% hint style="warning" %}
Recurring commitment periods — where a subscription automatically rolls into a new commitment once the first one ends — aren't currently supported.
{% endhint %}

#### Good to know

* If a customer redeems a free trial against a commitment licence, the commitment period starts after the trial — the trial cycle doesn't count towards it. See [Free Trial Eligibility Checks](/platform-knowledge-base/back-office/licences/customer-payment-flows/free-trial-eligibility-checks.md) for more on trial behaviour.
* Minimum commitment doesn't block upgrades or downgrades on its own. If a customer could downgrade to a licence without a commitment, that would let them break out of it — use licence restrictions to close this off. See also [Licence Family Architecture & Upgrades/Downgrades](/platform-knowledge-base/back-office/licences/licence/licence-family-architecture-and-upgrades-downgrades.md).
* Once a licence is live, the Minimum commitment value can't be changed via the UI. Contact your account team if it needs to change — updates only apply to new orders, not existing subscribers.

{% hint style="danger" %}
**Disclaimer:** Neither Vesper nor Deltatre can operate a debt collection agency. If an end customer does not have the funds to meet the commitment, cancels their card, or otherwise disputes the payment, the licence will be revoked and the committed monies will not be collected. A commitment licence is riskier for revenue purposes than a traditional annual or other long-period subscription.
{% endhint %}

### What the customer sees

* **At checkout** — customers see a message confirming the commitment they're agreeing to, the charge amount, and the billing frequency.

<figure><img src="/files/QdufvOOBgw52v3Er9ec0" alt=""><figcaption></figcaption></figure>

* **By email** — the purchase confirmation (or free trial welcome email, if applicable) includes a line confirming the commitment period and when it ends.

<figure><img src="/files/2MEmnMGEPajYCupowAhb" alt=""><figcaption></figcaption></figure>

* **When cancelling during the commitment** — customers are shown the date their cancellation will actually take effect, rather than an immediate cancellation. An e-mail to the same effect will be sent to the customer.

{% tabs %}
{% tab title="Cancellation check" %}

<figure><img src="/files/htt481B31CMdiooGtQdp" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="E-mail confirmation" %}

<figure><img src="/files/4DcrvI6LR8PXU3ZX19H6" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

* **On their account page** — while in a commitment, customers see the date the commitment ends. If they've requested cancellation but are still within the commitment, the account page reflects that the subscription will continue billing until the commitment ends, then cancel.

<figure><img src="/files/aVASm27518kKEtSAKtnm" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/T6ZtCqoaYjyrZivwiawG" alt=""><figcaption></figcaption></figure>

### Subscription actions during a commitment

<table><thead><tr><th width="140.734375">Action</th><th>What happens</th></tr></thead><tbody><tr><td>Cancel</td><td>Deferred to the end of the commitment period. The customer is told the effective cancellation date.</td></tr><tr><td>Upgrade</td><td>Takes effect immediately, as normal.</td></tr><tr><td>Downgrade</td><td>Takes effect at the next billing cycle, as normal — commitment doesn't block it, so use licence restrictions if that's not desired.</td></tr><tr><td>Pause</td><td>Takes effect at the next billing cycle, as normal. Paused time still counts, and the remaining commitment cycles are honoured.</td></tr><tr><td>Reactivate</td><td>Available at any point after a cancellation, provided the commitment period hasn't ended.</td></tr></tbody></table>

For general subscription behaviour (promo codes, payment method changes, and so on), the usual rules apply — a minimum commitment only changes what happens on cancellation.

### Reporting

Minimum commitment adds two fields to Vesper Insights, under Order management:

* `commitment_periods_remaining` — the number of billing periods still required to fulfil the minimum commitment. `0` once the commitment has been fulfilled.
* `minimum_commitment_voluntary_churn` — whether the customer voluntarily requested to cancel while still within their commitment.

Some useful filters:

Some useful reporting queries:

1. **Subscriptions currently within their commitment window**
   * `Is Active` = `True`
   * `Commitment Periods Remaining` > `0`
2. **Subscriptions cancelled within the commitment window by an admin**

   * `Licence Status` = `Cancelled`
   * `Commitment Periods Remaining` > `0`

   Use this when an admin cancellation has taken effect before the commitment was fulfilled. This covers cancellations applied immediately, or period-end cancellations once that end date has passed.
3. **Subscriptions that were configured with minimum commitment, and have now fulfilled it**

   * `Commitment Periods Remaining` = `0`

   Use this against licences known to have minimum commitment configured.
4. **Subscriptions still active within the commitment window, but already scheduled to cancel at the end of the commitment**

   * `Is Active` = `True`
   * `Commitment Periods Remaining` > `0`
   * `Minimum Commitment Voluntary Churn` = `True`

   This is the deferred customer-cancellation case. The subscription remains active until the commitment ends, then cancels.

### Related features

Minimum commitment is one of several tools available for managing retention and churn — see also Cancellation Discounts and Time Based Subscription Pause & Resume.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/licences/licence/minimum-commitment-licences.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
