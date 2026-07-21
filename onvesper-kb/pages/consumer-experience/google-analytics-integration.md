> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/consumer-experience/google-analytics-integration.md).

# Google Analytics Integration

Supported platforms: **Web**, **Mobile**

Vesper's mobile and web applications can be optionally connected to Google Analytics. This functionality is available to you to manage, configure and self-service. For Endeavor Streaming's supported analytics solutions, see [Vesper Insights](/platform-knowledge-base/back-office/vesper-insights.md).

## Events

There are a series of custom events that are available on the web and mobile platforms. These events will fire as an end-user interacts with the apps. Details about how these can be logged in GA are in the headings further down this page. To review the list of available events, please contact your account manager.

## Web configuration

Google Analytics (GA4) is available through a connection with Google Tag Manager (GTM). Once connected, you will receive basic analytics information about the web app. Events are fired into the GTM container, you are then able to add new GTM tags to trigger based on those events and fire custom GA4 analytics events back into Google Analytics. In this way, you are in complete control of the data you track, and you are also in control of the data you send to Google Analytics for your web users.

**Pre-requisites**: (1) You will need to have a GA4 property set up, which you have admin access to. (2) You will need access to your GTM container.

1. Add a new “data stream” for the web analytics to be sent to. In the analytics dashboard, go to the “admin” section (it’s a cog icon), then “Data Streams"<br>

   <figure><img src="/files/OgRdo6OfiI3ZJ7Zw42rO" alt=""><figcaption><p>An example of the Admin section of Google Analytics, highlighting Data Streams</p></figcaption></figure>
2. Create a “Web” data stream - if you do not already have one. When creating, please note that we can support Page Views, Scrolls, and Outbound clicks for “Enhanced measurement”.
3. Once you have a stream, make note of the measurement ID. It will show on the stream details page and look like this: G-XXXXXXXXXX
4. Follow this guide from Google: [![](https://support.google.com/favicon.ico)Set up Google Analytics in Tag Manager - Tag Manager Help](https://support.google.com/tagmanager/answer/9442095?hl=en) on how to set up the GA4 Configuration tag in your Google Tag manager.
5. You can now test this new configuration before publishing the new tag. You can use [Google Tag Assistant](https://tagassistant.google.com/) to check that you can see events being fired, you should be able to see the GTM container and the GA item.
6. Whilst testing using the tag assistant, you should also be able to see your session in realtime in Google Analytics dashboard.
7. Once you are happy, you can publish the GTM change

### Optional: Track custom events

To react to one of our custom events, you first need to create a **trigger** in Google Tag Manager. Set the trigger type to be "custom event" and then set the event name to match the one you want to react to.

<figure><img src="/files/VD5U2H03kWfYNfLWcBtY" alt=""><figcaption><p>Example of a trigger that fires on dice_login.success custom event</p></figcaption></figure>

Once you have a trigger, you can configure a custom GA4 Event tag to react to this trigger

<figure><img src="/files/qPLVBeqRpsHbOG7KQfyx" alt=""><figcaption><p>Example GA4 event tag reacting to the trigger</p></figcaption></figure>

Note that in the example above, we are also populating a parameter from the using a GTM Variable. You are able to create GTM Variables that expose data layer variables per the example below. You can confirm the variables available in the data layer through the [#events](#events "mention") list or by using <https://tagassistant.google.com/>.&#x20;

{% hint style="info" %}
Please ensure you are honouring customer consent and your local privacy laws when passing information to third parties from the Vesper platform.
{% endhint %}

<figure><img src="/files/iCVTmh1TH4oImQ6QuWiO" alt=""><figcaption><p>Example Variable configuration to pull a data layer variable into GTM</p></figcaption></figure>

## Apps configuration

For mobile apps, [#events](#events "mention") can be passed to Google Analytics through a connection to your Firebase project. Unfortunately, due to the nature of the Firebase connection, we are unable to offer "selection" of events to pass into Google Analytics in the same way as we can through GTM for web. Therefore once connected, all events will be passed to Google Analytics.

**Pre-requisites**: (1) You will need to have a Google Analytics (GA4) property set up, which you have admin access to. (2) You will need access to your Firebase project.

1. In Firebase, open Project Settings (the cog wheel), and look under “general” → “your apps”. Leave this tab open, you will need the information about the Android and Apple apps later. It should look something like this:<br>

   <figure><img src="/files/U0UAfBH3pZq3ugQ4mKjK" alt=""><figcaption></figcaption></figure>
2. Click the integration tab
3. Click Google Analytics
4. From here, you should be able to chose to link to the GA4 property you have set up.\
   Once complete, it should look like this:<br>

   <figure><img src="/files/qUDLoRfEm1BeCrgAkneR" alt=""><figcaption></figcaption></figure>
5. Now, open the linked Google Analytics account (using the handy link)
6. You’ll be taken to the Admin section of the account, where you should be able to select the “Data Streams” option
7. There, you will need to create 2 new data streams, one for iOS and one for Android
8. Add the streams, when asked for app ID or bundle ID for each, refer the screen you left open in **step 1**
9. Don’t worry if you see an error and get told to refresh the page, you just need to create the data streams, not follow every single step in the screen.
10. Once the streams are created they will look something like this:<br>

    <figure><img src="/files/0Fdzv2KJ2a0oCsr6mjFO" alt=""><figcaption></figcaption></figure>
11. Data will start to flow within an hour
12. To test: go to “Home” in Google Analytics and click “View Realtime”, if you open the app (fresh launch) you should start to see data appearing:<br>

    <figure><img src="/files/GD5mCWtNWOgluAhYax1t" alt=""><figcaption></figcaption></figure>

<br>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/consumer-experience/google-analytics-integration.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
