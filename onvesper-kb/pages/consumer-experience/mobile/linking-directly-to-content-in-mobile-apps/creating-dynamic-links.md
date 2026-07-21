> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/consumer-experience/mobile/linking-directly-to-content-in-mobile-apps/creating-dynamic-links.md).

# Creating Dynamic Links

{% hint style="danger" %}
Google has announced they are Deprecating Dynamic links in August 2025. Endeavor Streaming does not recommend the use of this product.
{% endhint %}

Dynamic links are a Firebase product that allow the creation of a single link address which behave in different ways depending on the context of the device they've been tapped from.

In practice, that means a dynamic link can be used to link to specific content, opening that content directly in the user's mobile application if tapped from a phone, or pushing them to the app store to get your app if it is not installed.

For more about Dynamic links, watch this video from Firebase:

{% embed url="<https://www.youtube.com/watch?ab_channel=Firebase&list=PLl-K7zZEsYLmOF_07IayrTntevxtbUxDL&v=LvY1JMcrPF8>" %}

In order to use Dynamic links with your Endeavor Streaming product, you will need to contact your Technical Account Manager, so that your apps can be configured to support the domain you chose to host dynamic links at. Your Technical Account Manager will guide you through that process, this guide assumes that configuration is complete, and you are now ready to create links.

## Step by step: Creating a dynamic link

It is possible to build your own integration with Firebase to generate your own links, if you have a development team or data provider able to build such an integration, please see the Firebase documentation here: <https://firebase.google.com/docs/dynamic-links/create-links>. The steps below assume you are creating links through the Firebase console directly.

#### Navigate&#x20;

After logging in to your Firebase project, navigate to the "Engage" menu section in the left menu, then click "Dynamic Links".

### Setup a URL prefix

Your Technical Account Manager will help you with this step. Endeavor Streaming supports a single URL prefix, you can use the free Firebase option (\<yourname>.page.links) or you can configure a custom subdomain (e.g. links.myservice.com).

Configuring a custom subdomain is a process that can take weeks, so please allow sufficient time ahead of your planned dynamic links. Configuration is a one-time process.

### Create a link

Once you have a URL prefix, you can click "new dynamic link" to create a new link.

The first step is to create the full link address. This is the address after your URL preview which can be used. **This cannot be changed in future** so make sure you use a unique address, for example your promotion link could include the date, or you can use Firebases' automatically generated defaults.

<figure><img src="/files/DPgSdV2vu1lPyBncVXcx" alt=""><figcaption></figcaption></figure>

Step 2 will allow you to specify the content you wish to link to. If you are linking to the homepage of your streaming service, you can enter the full URL of your service and continue.

#### Deeplinks

If you wish to deeplink to content, such as live and VOD content directly in the apps, the link entered here must match the formats defined in [Push Notification deeplinks & Custom protocols](/platform-knowledge-base/consumer-experience/mobile/linking-directly-to-content-in-mobile-apps/push-notification-deeplinks-and-custom-protocols.md#app-deep-link-options).

The simplest way to do this is to navigate to the content on your webapp, and ensure that the URL ends with a numeric ID.

For example, this is the public link on our streaming service ends with a numeric video ID, and can be used for Firebase dynamic links:

<https://endeavorstreamingshowcase.com/video/674372>

The URL will work as a deeplink with Firebase Dynamic links, and users who open the link with the app installed can be directed straight to the video! The web link is also intact, ensuring that customers on web browsers without any apps available will still see the right content.

<figure><img src="/files/TTdhdGW9ucJLLBhJLqAf" alt=""><figcaption></figcaption></figure>

#### Link Behaviour

Links can be configured to always open in the browser, regardless of whether the user has your app installed. Alternatively, you can chose to direct the user to your iOS / Android app, including detecting whether the app is installed and directing the user to an App Store to download the app if they don't have it installed. This is a great way to increase your install base for future push notification campaigns.

<figure><img src="/files/ikYA88TF7PnpMG6QicAS" alt=""><figcaption></figcaption></figure>

Apple links can also be linked to App Store campaign or affiliate parameters, to help track how your marketing links affect app acquisitions. You'll also see that if you prefer to send users without your app installed straight to the content, that option is achieveable through the "Custom URL" option for Android and iOS.

<figure><img src="/files/wytQ8YptQCMxep87UoA0" alt=""><figcaption></figcaption></figure>

Android apps can also force the user to update their app if it is older than a given version.

#### Campaign tracking & previews

The final section allows you to define what content will show in social media sites and messaging services when a user sees your link. You can define a title, description, and a link to a static image that will be shown as a preview.

<figure><img src="/files/eQDNSwOpFiCsshYGcSJC" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/Gzf3RpZRz6qOrHyKVJXL" alt=""><figcaption><p>Sample link from Facebook's Sharing Debugger</p></figcaption></figure>

If your Firebase account is linked to your Google Analytics account, the campaign parameters will be automatically captured against app opens and conversions. Try looking in your analytics dashboard for the event "dynamic\_link\_app\_open" to see every event which was logged, and find the campaign metadata logged against those opens.

You can read more on the analytics events in Firebase's documentation: <https://firebase.google.com/docs/dynamic-links/analytics>&#x20;

### Configuring the link

Link behaviour can be changed after it has been created, so if you want to add additional campaign tracking or social tags, or even change the content the link goes to, you can do so!

The only thing which cannot be changed after link creation, is the link address itself.

It can take an hour for the new behaviour to propagate out, as the old link data will be cached across the web.

<figure><img src="/files/dC2IyNlXzRjqjWyCU2Wu" alt=""><figcaption></figcaption></figure>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/consumer-experience/mobile/linking-directly-to-content-in-mobile-apps/creating-dynamic-links.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
