> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/licences/licence/licence-groups.md).

# Licence Groups

**Licence Groups** control how your plans are presented to your end-users. They are displayed on your Select Plan page and behind Locked content.

<figure><img src="/files/9Q68TQkln9o534fog5w5" alt=""><figcaption><p>Plans organized into Tabs</p></figcaption></figure>

They allows you to organise and display your licences by type, frequency, or any custom classification. Groups can be shown as **Tabs** or as a **List,** with each group containing a set of [Licences](/platform-knowledge-base/back-office/licences/licence.md).

Geographic and/or device restrictions can be applied to a configuration, and multiple configurations can be created to tailor different experiences for different audiences and/or devices.

{% hint style="info" %}
Please contact your Platform Account Manager to enable this new feature.
{% endhint %}

## Key Capabilities

* Group licences according to your preferences
* Display licence groups as *Tabs* or in a *List*
* Define the default licence group you want to display
* Show different licence groups based on device or geographic location

## How to Configure

{% stepper %}
{% step %}
In Back Office, navigate to *Licences* > *Select Plan UI Display*

<figure><img src="/files/pLdzwmTB9DCcGyUgJphH" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### Create a new Licence Groups configuration

Click *Add Configuration -* This will open up a new screen shown below.

<figure><img src="/files/iK55M88wKXhCFCCXmc1d" alt=""><figcaption></figcaption></figure>

* ***Configuration name*** - The name of this configuration. This is a system name and won't be displayed
* ***Card alignment** -* Select whether you want the Licence cards Inline or Centered
* ***Landscape/Portrait Background image*** - Upload an image that will display behind a "List" group.
* ***Tab section title** (Available if Tabs groups have been configured, see next steps)* - Title displayed to your users above the Tabs.<br>
  {% endstep %}

{% step %}

### Add and configure Groups

Below these settings, you'll find the list of groups configured.&#x20;

<figure><img src="/files/kEdBRqMw07FspKIOYt9E" alt=""><figcaption><p>Example of Groups configuration</p></figcaption></figure>

Click on the **"Add Group"** button *-* This will open the group configuration screen where you can configure an individual list or tab.

<figure><img src="/files/PMK7PqKYRl5NAK7z57QC" alt=""><figcaption></figcaption></figure>

* ***Group Title** -* This title will be displayed as the Tab or the List name on the Select Plan page and behind locked content
* ***Group display type** -* This can either be a `Tab View` or  a `List View`&#x20;
  * `Tab View`: licence groups are displayed within a single, organised tab structure. Any group configured as a tab will be consolidated under this interface. This is useful to allow the user to quickly compare different types of plans.
  * `List View`: licence groups are presented as separate lists down the page, with each group's title serving as the section heading. They can be used to feature a specific group above the rest.

{% hint style="warning" %}
**TV does not support&#x20;*****List View*** and will automatically fall back to a ***Tab*** **view**
{% endhint %}

* ***Default opened*** *(Available when `Tab View` has been selected)* - If set to Yes, this tab will be opened by default.
* ***Cable provider*** - If your platform allows users to acquire a licence through a cable provider or MVPD, you will need to create a dedicated group for it. If that is the case, check this box and decide how the option to connect to a provider should appear on the Select Plan page.
* ***Card style** -* Select between `Full` and `Simplified`

  * `Full`: default licence card format showing all configurable metadata available on the licence

  <figure><img src="/files/k5nYJFtvhc8oyf2ia4Rz" alt=""><figcaption><p>Example of Full cards in a Tab View</p></figcaption></figure>

  * `Simplified`: streamlined, minimalist option, with a transparent background - ideal for licence groups displayed against a custom background image

<figure><img src="/files/QEJNAJdFi9YV1Za5huGv" alt=""><figcaption><p>Example of Simplified card in a List View</p></figcaption></figure>
{% endstep %}

{% step %}

### Add Licences to groups

Add the *Licence* IDs that should be included in this group:

<figure><img src="/files/lobEFP669AnHZ0nx8aHs" alt=""><figcaption></figcaption></figure>

You can also drag and drop licences to control the order in which they appear to the end-user.

Once you're done, click *Add Group.*
{% endstep %}

{% step %}

### Create all the groups

Repeat steps 3 and 4 for all the groups you want to add.

Once groups are created, you'll be able to reorder and edit or delete them as needed.\
\
When you're finished, click *Next*.
{% endstep %}

{% step %}

### Set Geographic and Device restrictions

Click *Next* and go to `Restrictions` where you can set the `Geo restrictions` and `Device restrictions` for this Licence Groups configuration,

Once those are configured, click *Save*
{% endstep %}

{% step %}

### Enable the newly created config

Your new Licence Groups config has now been created. However, it is currently in *Draft*. To enable it, click the three dots and select *Enable.*

<figure><img src="/files/sUyq884J7RQ3xKnG18xb" alt=""><figcaption></figcaption></figure>
{% endstep %}
{% endstepper %}

## Examples

* Two licence groups in *tabs*

<figure><img src="/files/2FoMG79PrpzIGSGp6BDg" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/47qB8JL6yEZ3qhpscDnH" alt=""><figcaption></figcaption></figure>

* Three licence groups: One *List* group on top of two *tabs* group

<figure><img src="/files/XdhzNtSlVikx5NZil8Lt" alt=""><figcaption></figcaption></figure>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/licences/licence/licence-groups.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
