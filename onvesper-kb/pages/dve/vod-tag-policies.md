> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/dve/vod-tag-policies.md).

# VOD Tag Policies

## **Overview** <a href="#overview" id="overview"></a>

Tag Policies automate tag updates for VODs according to a set schedule. The feature:

* Will eliminate the need for tag manual updates once the VOD is published.
* Will reduce the potential for human error.

This becomes significant when we consider the purposes for which tags are used, such as configuring licenses and curating content rows. See more information on tags here.&#x20;

***

### **Tag Policy: Creation & Management** <a href="#tag-policy-creation-and-management" id="tag-policy-creation-and-management"></a>

#### **Tag Policy: Creation** <a href="#tag-policy-creation" id="tag-policy-creation"></a>

The Tag Policies page can be accessed within the DVE via the following path:

<figure><img src="/files/2qaRebtDpbJhVToZ9k1l" alt=""><figcaption></figcaption></figure>

If no tag policies are set up, the empty state page indicated in the screenshot below is presented. Once tag policies have been set up, they are all displayed in the Tag Policies page:

<figure><img src="/files/6iryl6QEzqjjGZaXXbOV" alt=""><figcaption></figcaption></figure>

To create a Tag Policy, click the “Create Tag Policy” button and provide the necessary information in the modal. A user needs to provide the following information when creating a tag policy:

* Name
  * This name field is required with a maximum of 50 characters.
* Specify Tag Actions
  * A user can configure actions for tags and set schedules for their execution.
    * The user can specify what tags can be added and/or removed and the timeframe when the tags are to be applied.
    * To create a tag policy, a user must include at least one tag action.

<figure><img src="/files/qSGIsDZBJrw5WvlvEADa" alt="" width="563"><figcaption></figcaption></figure>

The example below will illustrate this feature in both sections: setting up the tag policy and applying the tag policy to a VOD.

> Imagine the hotly contested UFC 300 fight between Pereira & Hill goes through this workflow. The fight is introduced to the platform as a PPV. 7 days after, it’s available to users on a fight pass subscription then after another 7 days, it’s available to all for general access.

To remove the overhead on a content manager to remember to make these changes, a tag policy can be set up to schedule the changes to the tags. The tag policy will look something like what’s indicated below:

<figure><img src="/files/SAlUaXbhoy0xZ8U1pBue" alt=""><figcaption></figcaption></figure>

* The tag policy was named: UFC 300: Pereira v Hill.
  * When appropriate, we suggest naming the policy in an easily recognisable way, especially if it's a standard workflow applicable to multiple VODs
* The tag actions identified are the addition and removal of tags to align with the user access workflow.
  * Adding the “PPV” tag a minute after it’s applied to the VOD so it’s available for users on the Pay Per View licence.
  * Removing the “PPV“ tag and adding the “fight-pass-sub“ tag 7 days after so the VOD is available to users on the Fight Pass subscription.
  * Removing the “fight-pass-sub“ tag and adding the “free“ 14 days after so the VOD is available to all users on a Free subscription.

#### **Tag Policy: Management** <a href="#tag-policy-management" id="tag-policy-management"></a>

<figure><img src="/files/UXWrLy4q70cRnLeYzjO2" alt=""><figcaption></figcaption></figure>

After creation, tag policies can be edited and deleted from the Tag Policies page as indicated above.

* Edit: Clicking on this navigates the user to the modal so the tag policy can be reviewed and edited as appropriate.
* Delete: Clicking on this navigates the user to the confirmation modal below requesting the user to confirm the request to delete the tag policy.

<figure><img src="/files/sp4bWuc5AIykIWo9Zlo4" alt="" width="375"><figcaption></figcaption></figure>

### **Apply a Tag Policy to a VOD** <a href="#apply-a-tag-policy-to-a-vod" id="apply-a-tag-policy-to-a-vod"></a>

Once a tag policy has been created, it has to be applied to a VOD to take effect. To do this:

* Go to the VOD detail page of the respective video where the policy is intended to be applied.
* Edit VOD metadata

<figure><img src="/files/gRuI4rkwQVlvO8pURPnf" alt=""><figcaption></figcaption></figure>

* Scroll to the Tag Policy section *(refer to the screenshot below)*, search for the desired tag policy and choose a start time for the tag policy to be applied to the VOD.
* Save Changes

&#x20;

To illustrate this, let's refer back to the UFC 300: Pereira v Hill example.

* Since I've already created my "UFC 300: Pereira vs. Hill" tag policy, I'll locate the VOD I wish to apply the policy within my catalogue.
* Then, I'll edit the metadata for the VOD
  * Search for the tag policy
  * Apply it also specifying a start time for the policy.

<figure><img src="/files/iBUMWazjubRuQAKlghda" alt=""><figcaption></figcaption></figure>

Note:

* A VOD can be associated with a **single** tag policy.
* If a tag policy applied for a VOD is edited:
  * tag actions will only affect future actions.
  * past actions will not be retrospectively updated.
* If a tag policy applied a VOD is deleted:
  * any tag actions scheduled for the future will be cancelled *(ie not actioned)*.
  * any tag actions performed in the past will remain unchanged.

<br>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/dve/vod-tag-policies.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
