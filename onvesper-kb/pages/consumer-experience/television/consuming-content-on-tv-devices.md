> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/consumer-experience/television/consuming-content-on-tv-devices.md).

# Consuming Content on TV Devices

Whether it is live sports, entertainment or instructional videos; many customers will prefer to consume their video content on the big screen.&#x20;

We often refer to Television content as the "10 foot" devices, because customers are normally sat approximately 10 foot from the device.

If you want to bring your content to customers on the big screen, Vesper can offer a number of solutions. Which ones make sense for you will depend on budget and your target demographics.

The first and simplest option, is to allow your customers to cast video content to the big screen, which can be achieved through Google Chromecast, Apple Airplay, or Screen mirroring.

## **Casting**

**What is Casting?**

Casting is sending video content from one device such as a mobile device, PC (Laptop, Desktop) to display on a big TV screen. The receiving device (TV) is told where the video content is located on the internet, and how to play it, then plays it directly.

### **Chromecast**

Customers can stream video content, using Chromecast. ChromeCast requires a compatible receiving device, either a dedicated ChromeCast HDMI dongle, or if the ChromeCast protocol is inbuilt into a Smart TV operating system (see the table above, or [this Google page](https://www.google.com/chromecast/built-in/tv/)).&#x20;

ChromeCast is available from following Vesper platforms:

* We&#x62;**\*** (Windows, MacOS, Android; using the Chrome browser only)&#x20;
* Android mobile Application
* iOS mobile Application

Chromecast will only be offered if the user is on the same network as a Chromecast receiving device. When a device is detected, the Vesper application will offer a casting icon in the video player. <img src="/files/jd6a2EfXNLBPHayC7t7s" alt="" data-size="line"> A common troubleshooting step if you cannot see this icon is to restart the Chromecast device so that it re-registers on your network.

**\*Note:** The Chrome browser also has an ability to "cast the current tab" to a ChromeCast receiver. This method is akin to [#mirroring](#mirroring "mention") and does not use Vesper technologies, therefore is not supported by Vesper. You should encourage customers to cast using the icon in the video player.&#x20;

### **AirPlay**

Airplay is Apple's proprietary casting protocol. It is available from iOS/iPadOS devices only, using the Vesper native iOS application only.

Airplay can cast to any AirPlay supported device, see the table below for more detail.

\***Note:** Airplay can also be used for screen mirroring (see below [#mirroring](#mirroring "mention")).

### Casting receiver devices

Listed below are compatible TV devices for each casting protocol.

<table><thead><tr><th width="235">Device/Operating System </th><th width="348">Apple Airplay</th><th>Google Chromecast</th></tr></thead><tbody><tr><td>LG TV (Web OS)</td><td>✓</td><td>!* (2024 and newer models only)</td></tr><tr><td>Samsung TV (Tizen) </td><td>✓</td><td>x</td></tr><tr><td>HiSenseTV (VIDAA OS)</td><td>✓</td><td>x</td></tr><tr><td>Apple TV</td><td>✓</td><td>x</td></tr><tr><td>Android TV/Google TV (Sony, TCL, Toshiba, Phillips) </td><td>x</td><td>✓</td></tr><tr><td>Roku TV</td><td>✓</td><td>x</td></tr><tr><td>Chromecast HDMI </td><td>x</td><td>✓</td></tr><tr><td>Fire TV </td><td>x</td><td>x</td></tr></tbody></table>

## Mirroring

**What is Screen mirroring?**

Screen mirroring involves the exact content on a device's screen being mirrored on to a big TV screen. It is essentially a wireless HDMI cable between your mobile device and the TV.

Screen mirroring is possible on some operating systems, and is not part of the Vesper applications. Whereas Casting is part of the application code which is developed by Deltatre.

### **Samsung TVs/Miracast**

Customers whom are consuming content on a Samsung TV are able to connect from an Android device to the big TV screen using a feature called Miracast.

Miracast is a wireless display standard that is used for sharing smartphone, tablet, or PC’s screen to a TV and Miracast creates a direct connection between your Android and the display.&#x20;

### **Airplay**

Apple's Airplay technology can also be used to screen mirror, the same restrictions and caveats as Miracast and other screen mirroring technologies applies.

Mirroring is not directly supported by Vesper as the feature is incorporated within the operating system on particular devices, and content may not be visible on the TV if it is protected by DRM.

**What is DRM?**

DRM is a method of securing digital content to prevent unauthorised use and piracy. It ensures that video content is stored and streamed in an encrypted form. Whichever video player then tries to open and play the video and must have the decryption keys in order to render the video content.

**Is Youtube Using Chromecast?**

The Youtube application have a built-in casting button which has been developed by Google. It which will automatically cast the video you're watching to your Chromecast. As this is proprietary Google technology, Vesper cannot utilise it.&#x20;

***

## Native Applications

If you wish to provide a premium experience on the user's big screen, which they will not require a secondary device to operate, Deltatre can publish applications on Connected TV or Smart TV devices. It is best to speak to your account managers about your options here. Connected TV devices can be self-published, however Smart TV applications on devices such as Samsung or LG may require commercial agreements with those manufacturers before you can publish.

**Connected TV Devices** - Apple TV, Google TV, Fire TV, Roku&#x20;

**Smart TV Applications:**

<table><thead><tr><th width="200">Device </th><th width="314">Commercial Agreement Requirement</th><th>Application Build Request</th></tr></thead><tbody><tr><td>LG TV </td><td>✓</td><td>✓</td></tr><tr><td>Samsung TV (Tizen) </td><td>✓</td><td>✓</td></tr><tr><td>HiSenseTV (VIDAA OS)</td><td>✓</td><td>✓</td></tr><tr><td>PlayStation 5</td><td>✓</td><td>✓</td></tr><tr><td>Xbox</td><td>x</td><td>✓</td></tr></tbody></table>

* Customers area able to consume content for applications built, accessible within Application stores.
* Deltatre can produce an application specifically for devices listed above which is then submitted for approval to the manufacturer.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/consumer-experience/television/consuming-content-on-tv-devices.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
