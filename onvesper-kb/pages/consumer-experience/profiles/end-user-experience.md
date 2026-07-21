> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/consumer-experience/profiles/end-user-experience.md).

# End User Experience

## Account / Profile Creation <a href="#id-1.-profile-details-and-preferences" id="id-1.-profile-details-and-preferences"></a>

When a user first signs up for the service a "Default profile" will automatically be created. The steps are as follows;&#x20;

1. User navigates through sign up flow&#x20;

<figure><img src="/files/zMgPvk8tnpuTyTFOtNf7" alt=""><figcaption><p>Example;  Sign Up Flow </p></figcaption></figure>

2. Once sign up flow is complete&#x20;

3. User will be taken to a profiles home page where a "Default profile" would have already been created

   * When User Profiles are enabled, there will always be a default profile (this is linked on the back end to the account)
   * This profile is always set to an adult profile type
   * Default Profiles can not be deleted, however all other profile details and preferences can be edited
   * In the case of turning on profiles for active subscribers, they will automatically see their default profile upon logging in (with the default avatar in place)

4. *When Kids Profiles are Enabled:*
   * Default profile can not be changed to a Kids Profile type

<figure><img src="/files/dxTzrQEo6YpMXXAcEmVn" alt=""><figcaption><p>Example; Profile Home Page </p></figcaption></figure>

5. From here the user has a couple of options;&#x20;
   * Click into the default profile - No settings will be specifcally applied to this profile&#x20;
   * Click "Edit" - The user will be taken to the "Profile details and Preferences" page below&#x20;
   * Create a new profile - Again the user will be taken to the "Profile details and Preferences" page for this other profile - also shown below

### Profile Details and Preferences  <a href="#id-1.-profile-details-and-preferences" id="id-1.-profile-details-and-preferences"></a>

For each individual profile, the following can be set:

* Name
* Avatar
* Profile Type (Kid, Adult)
* Preferred Language (Application Text)
* Subtitle Language
* Audio Language
* Autoplay Enablement

Additionally, the device specific preferences will still be in place (as enabled today), such as:

* push to phone
* user mobile data
* playback quality
* download quality
* enable Wifi only downloads

<figure><img src="/files/UAdCfrBDlq1754zXmK7W" alt=""><figcaption><p>Example: Profile Details and Preferences </p></figcaption></figure>

## Profile Management  <a href="#id-1.-profile-details-and-preferences" id="id-1.-profile-details-and-preferences"></a>

In order to edit, delete, or create profiles, the user must navigate to the ‘Edit Profiles’ screen.

This screen will allow the user to see all available profiles and take any necessary action.

<figure><img src="/files/isLhzdxElgoHuecvOTOR" alt=""><figcaption><p>Example; Edit Profile </p></figcaption></figure>

<figure><img src="/files/rA8kM7joqV89pP4qQ1vY" alt=""><figcaption><p>Example; Edit Profile Page </p></figcaption></figure>

#### **In the case of a kids profile;**

* Users within a Kids Profile will not be shown the ‘Edit Profiles’ menu item
* Only user within an Adult Profile will be able to see this menu item

<figure><img src="/files/nIE0uSkh0x0ctMp8H2b5" alt=""><figcaption><p>Example; Profile Management - Kids Profile </p></figcaption></figure>

## Profile Switching

* (Web) End Users will be able to easily navigate to different profiles from within the menu, where profile name and avatars are shown within a drop down
* (TV & Mobile) End Users will be able to select to switch profiles from the menu, where they are taken back to the ‘who’s watching' screen and can select the profile they wish to enter

*When Kids Profiles & Pin Protection are Enabled:*

* If the user wishes to enter into an adult profile, they must correctly enter in the pin value

<figure><img src="/files/1gcKqTJaxaimvCSfN2lX" alt=""><figcaption><p>Swtiching Profiles - Drop Down Menu </p></figcaption></figure>

## Profile Content&#x20;

Recommendations, watchlists, and continue watching are tied to a given user profile.

*For Kids Profiles:*

* Content with restricted maturity ratings are hidden from search and from view
* Recommendations only consider content with unrestricted maturity ratings
* HEROS, Rows, or Promo Notifications that have been targeted to Kids profiles will appear and those targeting Adult only profiles will **not** appear.

## Acccount Management&#x20;

Account management will continue to exist under the user’s menu (as it is today).

**Note**: there is a single email address and subscription that exists at the account level. Individual profiles do not have unique emails/subscriptions.

*For Kids Profiles:*

Kids will not be able to access critical account information such as account details, subscription details, payment details, or access account settings such as pin protection.

### Account Setting: Pin Protection&#x20;

This is only applicable when the Kids Profiles are enabled;

* An adult profile user can enable pin protection, where they will set a 4 digit pin - this protection mechanism is then enforced on **all** kid profiles that are created under the account
* When set, users trying to exit a kid’s profile and enter an adult profile must first enter the correct pin
* In the case that a pin value has been forgotten an email will be sent to the account holder to reset
* Pin Protection Logic:
  * Given the user is within a kid’s profile and pin protection is **enabled**:
    * the user is only able to switch to other kid profiles, thus can only continue to see unrestricted content
    * if the user wants to switch to an adult profile, the correct pin must be entered&#x20;
  * Given the user is within a kid’s profile and pin protection is **disabled:**
    * the user can switch to any profile type (therefore, if they switch to an adult profile they unlock access to mature content, can view account details, and can edit profiles)
    * this option is well suited for when the adult is controlling the device/remote and they simply want a profile for kid friendly content

&#x20;

<figure><img src="/files/HbfOQwPw541UMK8whJv3" alt=""><figcaption><p>Example; Set Pin Protection </p></figcaption></figure>

<figure><img src="/files/3rFwoE0EKq76SDfDNUZw" alt=""><figcaption><p>Example; Enable Pin Protection </p></figcaption></figure>

### Pin Entry Upon Login&#x20;

* End user will see the ‘who’s watching' screen, in which all available profiles are shown
* End user can then select which profile they wish to enter

**In the case of Kids profile & Pin protection are enabled**

* If the user wishes to enter into an adult profile, they must correctly enter in the pin value

<figure><img src="/files/wNSSWcIYhNZmNpaA7r97" alt=""><figcaption><p>Example; Pin Protection Logic - Kids </p></figcaption></figure>

## Kids Profiles Summarized <a href="#kids-profiles-summarized" id="kids-profiles-summarized"></a>

* Profile Content:&#x20;
  * Content with restricted maturity ratings are hidden from search and from view
  * Recommendations only consider content with unrestricted maturity ratings
  * HEROS, Rows, or Promo Notifications that have been targeted to Kids profiles will appear
* Profile Navigation & Pin Protection:
  * Given the user is within a kid’s profile, they will not be able to readily navigate to the account pages or edit profiles (these are hidden from view)
  * Pin Protection Logic:
    * Given the user is within a kid’s profile and pin protection is **enabled**:
      * the user is only able to switch to other kid profiles, thus can only continue to see unrestricted content
      * if the user wants to switch to an adult profile, the correct pin must be entered&#x20;
    * Given the user is within a kid’s profile and pin protection is **disabled:**
      * the user can switch to any profile type (therefore, if they switch to an adult profile they unlock access to mature content, can view account details, and can edit profiles)
      * this option is well suited for when the adult is controlling the device/remote and they simply want a profile for kid friendly content


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/consumer-experience/profiles/end-user-experience.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
