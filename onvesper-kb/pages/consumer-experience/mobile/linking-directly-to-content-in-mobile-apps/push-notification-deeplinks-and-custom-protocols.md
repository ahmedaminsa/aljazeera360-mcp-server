> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/consumer-experience/mobile/linking-directly-to-content-in-mobile-apps/push-notification-deeplinks-and-custom-protocols.md).

# Push Notification deeplinks & Custom protocols

### What is Deeplinking in Firebase?

The deeplink feature drives users directly to a piece of content, a playlist, a VOD within a playlist or somewhere specific within the app such as subscriptions, upcoming events, and news. This is initiated within a push notification via the cloud messaging tool within Firebase.&#x20;

### How to use it

Log into [Firebase ](https://console.firebase.google.com/)

![](/files/D4ULLnO8VvGP2HtMoOLV)

You should be presented with your project overview. If there is more than one Firebase project in your organisation then select the relevant project from the top left hand drop down menu next to the list of Firebase tools.&#x20;

![](/files/vJblmOWJoDcdh8rybWmG)

Once you have found the correct Firebase project, find the list of tools to the left and scroll down to 'Messaging' or 'Cloud Messaging'

![](/files/y3urFVoz0R87a5UdP9rm)

Start a new campaign as you would any notification.

![](/files/N3bPd9Lm1PPFhfOYo3jT)

Fill in the mandatory items as you would for a regular notification:

* Notification Section
* Target (iOS & Android)&#x20;
* Scheduling&#x20;

\
'Additional Options' will be the field where the deeplinking information needs to be. Use the 'Custom data' fields to add in the key and value.&#x20;

The 'Key' will always be 'url' in this instance. The format of the 'Value' will depend on the type of notification that is being pushed.&#x20;

{% hint style="warning" %}
The key ("url") and value (the link) are both case sensitive, make sure you only entering lower case values
{% endhint %}

![This is an example of a deeplink notification for a VOD using the Vesper test environment. ](/files/oL9MO6NTPYvwnQhnndyw)

The Value details will depend on the resident's realm name, as these are deeplinks we can use the url's from resident sites to obtain the values.&#x20;

If you are unsure of your realm name - reach out to your Technical Account Manager for the value which should be used instead of *realm:://* in the examples below.

## App deep link options (Custom protocol links)

Now it's time to decide where in the app you wish to drive the users to. The table below specifies the paths that can be used. Other locations within the apps for Residents with bespoke UI can request paths from their Account Managers.<br>

| Use Case                                                                                        | URL Structure                                       | Example                                    |
| ----------------------------------------------------------------------------------------------- | --------------------------------------------------- | ------------------------------------------ |
| Live Now                                                                                        | /live/{eventid}                                     | realm://live/1234                          |
| Upcoming Live ([For Apple In-App Events)](https://developer.apple.com/app-store/in-app-events/) | /live/{eventid}                                     | realm://live/1234                          |
| VOD                                                                                             | /video/{videoID}                                    | realm://video/1234                         |
| Playlist                                                                                        | /playlist/{playlistID}                              | realm://playlist/1234                      |
| VOD from Playlist                                                                               | /video/{videoId}?playlistID={playlistID}            | realm://video/1234?playlistid=1234         |
| Season                                                                                          | /season/{seasonID}                                  | realm://season/1234                        |
| Section                                                                                         | /section/{sectionPath} **`(must be html encoded)`** | realm://section/This%20Section%20Is%20Live |
| Favourites                                                                                      | /favourites                                         | realm://favourites                         |
| Subscription                                                                                    | /purchase                                           | realm://purchase                           |
| Account                                                                                         | /account                                            | realm://account                            |
| Home                                                                                            | /home                                               | realm://home                               |
| Licence (link to one or many licences)                                                          | /licence?licenceId=\[{licenceId}]                   | realm://licence?licenceId=\[1234,1235]     |

The key information for each item to be reached will be the 'ID' below are a few examples of resident URL's with the ID path.

[https://www.**aVesperCustomer.com/live/148679**/a-great-event](https://www.aDiceCustomer.com/live/148679/a-great-event)

* Highlighted in bold is the exact path that would drive a user to Live content

\
[https://**anothterVesperCustomer.com**/**video/284705**/fight-night-someone-vs-someoneelse-prelims](https://anothterDiceCustomer.com/video/284705/fight-night-someone-vs-someoneelse-prelims)

* Highlighted in bold is the path leading to a specific area of content - these are the values required for this type of deeplink.

\
[https://www.**aVesperCustomer**.com/**playlist/4387**/playlist-name](https://www.aDiceCustomer.com/playlist/4387/playlist-name)

* Highlighted in bold are the values that will direct the user to a playlist.

Once decided on which path the user will be notified with and where they will be directed to within the app you can go ahead and choose the settings for the duration of the notification, review the notification and then send this out to the devices. \
\
The notification when accessed will direct the user to that specific area.&#x20;

Happy Deeplinking via Push notifications! <br>

#### Using custom protocol links from other apps

It is possible to call a custom protocol link (e.g. realm://video/1234) from another app installed on a user's iOS or Android device, to handoff from one app to another. This may be useful if you are trying to link to your OTT product from another app in your portfolio.

However, please note that if the app is not installed, iOS and Android will not be able to process the link. Therefore if you wish to do deeplinking through protocol links in this way, the other app will need to implement logic to test whether or not the user's device can open these links - if not, they will then need to redirect the user to the store. This is logic that must be built on the sending app.

If you are not able to build this logic, we would recommend using [Universal Links](/platform-knowledge-base/consumer-experience/mobile/linking-directly-to-content-in-mobile-apps/universal-links.md) instead for simplicity.

\ <br>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/consumer-experience/mobile/linking-directly-to-content-in-mobile-apps/push-notification-deeplinks-and-custom-protocols.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
