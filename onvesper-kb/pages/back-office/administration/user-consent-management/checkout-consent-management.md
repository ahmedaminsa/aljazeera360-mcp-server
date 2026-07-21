> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/administration/user-consent-management/checkout-consent-management.md).

# Checkout Consent Management

{% hint style="info" %}
See also [Renewal Notifications](/platform-knowledge-base/consumer-experience/payments-and-subscription-management/renewal-notifications.md)which are often enabled with this feature
{% endhint %}

Vesper is able to support an additional consent agreement in the checkout flow. This feature is intended to aid with legal compliance in territories that require opt-in consent to specific terms when completing a subscription agreement on an online platform.

This feature is self service, but you are advised to contact your Platform Account Manager, as well as your own legal council, to discuss configuration for your realm. This page will outline the options available to you as well as known limitations of this feature.

## Configuration

When creating a checkout consent item, the following fields are available:

1. **Name** - Name can be used to help track the version of checkout consent that was presented to the user at the point of purchase. This value will not be visible to the end-user and is an internal only reference.
2. **Type** - Type is used to define what type of checkout consent is being used for reporting purposes. If a new type of checkout consent needs to be added for reporting please raise a request with your platform account manager. At present "Auto-Renewal" is the only supported type.
3. **Content** - Enter the consent content you would like to display to the end-user within the checkout flow. Please note, this field supports [markdown](https://www.markdownguide.org/cheat-sheet/) for additional links to relevant terms.
4. **Format -** Decide whether you want the user to be presented with the terms and assume consent by completing a purchase, or offer a check a box before purchase, and if that box should be checked by default or not.\
   ![](/files/XmH7NvwLXp0MRMDAmHT2)
5. **Restrictions** - Restrict when the checkout consent should appear based on the user’s billing country / State. This functionality allows presenting different terms and modals depending on geolocation of the user.

#### Priority order <a href="#priority-order" id="priority-order"></a>

If a realm has multiple checkout consent options configured for the same territory the platform will only return one.

A priority order can be configured to control which checkout consent is chosen if multiple are applicable. Priority order is ascending, meaning 1 is higher priority than 2. For example, a lower priority for the entire of the US could be defined, with a higher priority item for California to ensure it will be shown to that region.

## Known limitations

As this feature is intended to aid compliance it is available only on web, where Endeavor manages the payment and checkout process. It is assumed that for In App Purchases, the stores/portals which enable the checkout flow are responsible for these compliance requirements.

This consent is intended for use with renewing subscriptions. It will be shown for subscriptions and fixed-date subscriptions. At this time other purchase types (e.g. rental and PPV) are not supported.

## Reporting

Once checkout consent has been enabled, you will be able to track via the Order Management dashboard via Vesper Insights.

The result is recorded by Consent checkout “type“. As above, the only type available today is “Checkout Consent AutoRenew“.

The values returned and their meaning is as follows:

* `[Consent Name]-CHECKED` = User checked the checkbox
* `[Consent Name]-NOT_CHECKED` = User did not check the checkbox\*
* `[Consent Name]` = Option to check a box was not offered to the user (text only).
* `Null` = No checkout consent was presented
* This new data should be exposed in the Order Management Dashboard.

<br>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/administration/user-consent-management/checkout-consent-management.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
