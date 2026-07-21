> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/consumer-experience/mobile/push-notifications-firebase.md).

# Push Notifications (Firebase)

## **Creating your first push notification campaign**

Log into your [Firebase](https://console.firebase.google.com/) project and navigate to **All Products** section and select **Cloud Messaging (FCM).**

<figure><img src="/files/25mqdh3m01INisJGEm20" alt=""><figcaption><p>Select All Products</p></figcaption></figure>

<figure><img src="/files/EnPT2fk1y8iXI7XdpM7f" alt=""><figcaption><p>Select Cloud Messaging</p></figcaption></figure>

### Click on C**reate Your First Campaign**&#x20;

<figure><img src="/files/q3NJro0JPmDFm0Tyjcad" alt=""><figcaption></figcaption></figure>

### Choose "Firebase Notifications messages"&#x20;

{% hint style="warning" %}
Vesper does not support "In-app messaging" at the given time&#x20;
{% endhint %}

<figure><img src="/files/BZvk94ETYVp5oiMM7iLN" alt=""><figcaption></figcaption></figure>

The interface on the right-hand side gives a real-time preview of the formulated message

·      You can use emojis in the title and body of the text message

·      We advise filling out notifications names to help identify messages in the Firebase console, and notification reports (this name is not shown to users).

<figure><img src="/files/5aoQMRBu5aLIjfr7VR9O" alt=""><figcaption></figcaption></figure>

### **Target your audience (optional)**

<figure><img src="/files/9VENYQU16gXpPQwuLxPM" alt=""><figcaption><p>Target Android or iOS as an example </p></figcaption></figure>

·      If you wish to target only Android or iOS, you can select which operating system to target. Leave this unselected to send the notification to all users. Alternatively, target iOS then click "and" to send a target to iOS and Android.

·     If you want to target only a segment of your users based on variables as App Version, Language or Country/Region (aka Geo-targeting), you can click on "and" next to each iOS or Android row and select the conditions you want to use to create your audience.

·      A real-time end user estimation will be calculated as you set these values

<figure><img src="/files/9XwuBv0u3whUM9w7tUe2" alt=""><figcaption></figcaption></figure>

### **Scheduling**

Select the time you would like to send your notifications

<figure><img src="/files/T9gdhq1wkivamGM1c3Pl" alt=""><figcaption></figcaption></figure>

### **Conversion Events (Skip Step)**

{% hint style="warning" %}
Skip this step, Endeavor Streaming apps do not currently support conversion events
{% endhint %}

### **Additional options (Deep link to content/app section)**

'Additional Options' is the field where the deep linking e.g., specific VOD content is supported. Use the 'Custom data' fields to add in the key and value.

The 'Key' will always be 'url' in this instance, the format of the 'Value' will depend on the type of notification that is being pushed, for a full list of supported deep links please go [here](/platform-knowledge-base/consumer-experience/mobile/linking-directly-to-content-in-mobile-apps/push-notification-deeplinks-and-custom-protocols.md)

Example of a deep link directing to a VOD content:

·      Select the content you would like direct your users and copy the URL

![](/files/Fk8VDPHJ918rutqxtD9M)

• Paste your content URL into Firebase below

{% hint style="info" %}
Note that the key and value are case sensitive! They should be in lower case.
{% endhint %}

<figure><img src="/files/aybfBOc8GwyPKV9wIfti" alt=""><figcaption></figcaption></figure>

## **Testing push notifications with a limited device set before sending**

If you wish to test your push app notifications with a specific device (rather than sending them to all your customers), you can use Firebases' test system at any time in the process. For example, you could complete the step above to configure a push notification to point to video/85158, then go back to Step 1 to test that notification.

Firebase uses P/N tokens to identify devices, you can retrieve the P/N token from your app install by following these steps:

·      On your iOS or Android device, open your app, and select the menu on the top left corner.

·      Tap 10 times on the version number e.g., 1.5.0 (35) (highlighted in red below) on the bottom right until **ADMIN** option appears.

·      Press on the new menu option and copy P/N Token this token is linked to your testing device.

![](/files/vB0xjzDjVvaWnHOc2rPa)![](/files/BTPQByIimPwpewpZ11Ud)

Once you have your token copied over – go to Cloud Messaging Compose notification and select **Send  test message.**

<figure><img src="/files/iGr9tH9RGfx7giBFWHoM" alt=""><figcaption></figcaption></figure>

·      In Add FMC registration token – this is where you copied paste P/N Token from your test device

·      Click on the + icon to use the P/N token you just pasted&#x20;

·      When ready, click on TEST&#x20;

<figure><img src="/files/sMAmPKbDhQWg3Y8jPsEf" alt=""><figcaption><p>Click on the + icon once you pasted the token in</p></figcaption></figure>

Your notification will be sent only to the devices you selected in the test stage. If you are finished testing, you can close this panel and send/schedule the notification for your entire user base.

### Having trouble locating the P/N token?&#x20;

Make sure you are on the latest app version. Delete your app and redownload to ensure you're on the latest version. Once redownloaded, **ensure you have allowed to receive notifications** from the app on your phone/app settings.&#x20;

Once you have confirmed you are on the latest app version and have enabled notifications, repeat the steps to retrieve the P/N token.&#x20;

## Images

If you wish to send images with push notifications, please note that Vesper does not formally support this capability. It is possible to include an image on Android devices, provided that you follow Firebase's guideline below:

> Images for notifications are limited to 1MB in size, and otherwise are restricted by native Android [image support](https://developer.android.com/guide/topics/media/media-formats#image-formats).

Images are not supported for push notifications on iOS at the time of publishing this documentation.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/consumer-experience/mobile/push-notifications-firebase.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
