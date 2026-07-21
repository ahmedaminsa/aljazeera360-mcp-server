> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/licences/promotions/promo-code-search-and-invalidation.md).

# Promo code Search & Invalidation

Users of Back Office with "Resident" privileges are able to search for single use promo codes in Back Office > Licenses > Promo tab. They can also invalidate an unredeemed promo code.&#x20;

![](/files/2retk9o5REKBhwVXwA3o)

In the Promo tab, there is a "Find a promotion code" box that can be used to search. Entering a single use promo code in that box will begin the search and display information about it.

### Redemption & Status

If the promo code is ***Redeemed*** you will see the expiration date, name of promo, and user details of the user associated with the promo:

<figure><img src="https://s3.amazonaws.com/release-assets/production/team-2034/630692fbbd6cb_Screen%20Shot%202022-02-01%20at%202.08.49%20PM.png" alt=""><figcaption></figcaption></figure>

If the promo code is *<mark style="color:green;">**Unredeemed**</mark>* When searching for a promo code that is *,* you will see the expiration date and name of the promo only.

If you search for a promo code that does not exist in the search bar you will be shown this popup:

<figure><img src="https://s3.amazonaws.com/release-assets/production/team-2034/630691b5a9c8f_Screen%20Shot%202022-02-01%20at%202.03.27%20PM.png" alt=""><figcaption></figcaption></figure>

### Invalidation

Invalidation allows a specific single use promo code to be de-activated without needing to cancel/end the entire promotion.

If you need to invalidate an *<mark style="color:green;">**unredeemed**</mark>* promo code, the red button shown on a currently valid promo code search enables that feature. You will first be prompted to confirm to make sure you want to invalidate, note that after confirming, this **action cannot be undone**. Once confirmed, that promo code will now be *invalidated* and will show up as such when you search for it:

<figure><img src="https://s3.amazonaws.com/release-assets/production/team-2034/630693eac9269_Screen%20Shot%202022-02-01%20at%202.16.06%20PM%20(1).png" alt=""><figcaption></figcaption></figure>

If a promo code is already *<mark style="color:red;">**Invalidated**</mark>*, you will see the expiration date, name of promo, and the user details of the user that invalidated the promo code:

<figure><img src="https://s3.amazonaws.com/release-assets/production/team-2034/630692910283e_Screen%20Shot%202022-02-01%20at%202.16.06%20PM.png" alt=""><figcaption></figcaption></figure>

**Notes:**

* This feature only works for single use promo codes, not multi-use (generic) promo codes
* When status of the promo code is *Invalidated*, the user details will be that of the user that **invalidated the promo code**, not the user that is associated with it
* No user details are available for *Unredeemed* promo codes


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/licences/promotions/promo-code-search-and-invalidation.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
