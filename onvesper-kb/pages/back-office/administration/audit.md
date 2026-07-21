> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/administration/audit.md).

# Audit

The 'Audit' section of Back Office is where you are able to track the audit history of the platform. You have the ability to see approximately 50 actions which are track in the auditing section.

<figure><img src="/files/tl0HFJhYBTwHyDcmNAqx" alt=""><figcaption></figcaption></figure>

With the audit section you have the ability to search via Admin ExID, User ExID or by specific property verticals e.g. by a specific LicenceID or VodID and slice your search with filters for a particular categor&#x79;**.**

{% hint style="warning" %}
The available Properties to search by are currently being updated on our documentation, please reach out to your Platform Account Manager if you have any specific queries in the mean time.

The most commonly useful Properties by are via the Admin EXID and the Customer EXID. These are detailed below.
{% endhint %}

### **Search Via Admin EXID**

If you use the Admin EXID to search all Resident, Supervisor, Agent and Overflow which means you can for example Search for a Supervisor to see what refund transactions they have been doing.

When searching via Admin EXID, you will need to make sure you already have the EXID of the admin user whose actions that you would like to see. If you don't have the EXID, then you will need to;

1. Go to Users section and search for the user
2. Click into the users account
3. Copy the EXID that is on the left hand side of the page

Once you have the EXID, you can then input the id into the search bar for the Audit section. When you search for the EXID this will show all the activity done by that particular Admin role user from the 1st March 2020 onward.

<figure><img src="/files/5OVK7G8HTplFo1FYvmzF" alt=""><figcaption></figcaption></figure>

### **Search Via User ID**

If you use the User EXID to search it will cover both Admin and Customers roles, as this will help understand what activity they have done or what someone has done on their account e.g. Search for a Supervisor as a User to see what Resident/Admin gave them a VIP status

When searching via User EXID, you will need to make sure you already have the EXID of the admin user whose actions that you would like to see. If you dont have the EXID, then you will need to;

1. Go to Customers section and search for the user
2. Click into the users account
3. Copy the EXID that is on the left hand side of the page

<figure><img src="/files/KgSmnJWgk6tK8uyfuPsz" alt=""><figcaption></figcaption></figure>

### **Filter Search by 'Action Type'**

You also have the ability to filter by audit activities in conjunction with either the Admin or User EXID or you can search by just the audit activity.&#x20;

There are 8 categories which you can filter audit activities.&#x20;

* **Cancel (licence specific)**: Shows the Admin EXID, User EXID, Licence ID and Licence Name
* **Create**: Shows the EXID of the new user along with the email address associated. If an Admin created the user then the EXID and email address of the Admin Role.
* **Delete**: Shows the EXID of the Admin who actioned a delete of any user, licence or content and the requisite EXID of said user, licence or content.
* **Read**: Shows the EXID of the Admin who viewed any users, licences or content. It will also show the ID of the user, licence or content viewed.
* **Refund (licence specific)**: Shows which Admin EXID refunded which Licence and to which end users EXID
* **Update**: Shows the EXID of the Admin and any change actions made to user, licence or content.

### **Filter Search by 'Target Type'**

{% hint style="warning" %}
The available Target Type properties are currently being updated on our documentation, please reach out to your Platform Account Manager if you have any specific queries in the mean time.

The most commonly useful Target Types to filter by are via the User, Licence and VOD. These are detailed below.
{% endhint %}

* User: Filters all actions taken with a Target Type of User, whereby an Admin action (Create, Delete, Read or Update) was taken on a User account.

<figure><img src="/files/t1z5N9JZlhH95QrGHfYg" alt=""><figcaption></figcaption></figure>

* Licence: Filters all actions taken with a Target Type of Licence, Admin action (Create, Delete, Read, Update, Cancel or Refund) was taken on a User account.

<figure><img src="/files/l2bJRVCi71DhvU5UVmSJ" alt=""><figcaption></figcaption></figure>

* VOD: Filters all actions taken with a Target Type of VOD, whereby an Admin action (Create, Delete, Read or Update) was taken on a VOD.

<figure><img src="/files/fU777rct8s5uojua72j4" alt=""><figcaption></figcaption></figure>

### **Search Via Date Filter**

You also have the ability to filter by date in conjunction with Properties, Action Types and Target types.

There are different date  options which audit activity can be searched by:&#x20;

* All Time (default)
* Today
* This Week
* This Month
* Custom Range

{% hint style="info" %}
The role Supervisor, Agent or Overflow will **NOT** have access to this tab.

***Note:** Audit Activity only starts from the **1st March 2020***
{% endhint %}

### VOD Audits

Please note that the exID of an Admin user is not shared between Vesper BackOffice and the Vesper VOD platform. As such, we have linked to the VOD platform directly within the alert.

You can observe where a VOD action was taken:\
Other - refers to actions taken by an Admin EXID via the Onboarder API\
Via the Vesper VOD UI - refers to actions taken by an Admin EXID via the VOD platform UI

<figure><img src="/files/b7oyxHeUt26afqaVtIh1" alt=""><figcaption></figcaption></figure>

Clicking into an event pops up the detail window with further information about the action that was taken and a clickable VOD platform EXID that will take you to the VOD platform and identify the account that took the action:

<figure><img src="/files/ZC83XkIJCqXBRYzQ8Hkp" alt=""><figcaption></figcaption></figure>

Clicking on the EXID will take you to the VOD platform and provide detail on the actioning user details:

<figure><img src="/files/NrmF8hOYr3JW9FWQCFJ5" alt=""><figcaption></figcaption></figure>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/administration/audit.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
