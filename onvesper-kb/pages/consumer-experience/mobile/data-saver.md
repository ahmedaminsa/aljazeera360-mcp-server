> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/consumer-experience/mobile/data-saver.md).

# Data Saver

Data Saver is an option available in the Vesper Mobile application's settings to allow end-users more control over their data usage.

Vesper mobile by default disables video consumption on mobile data networks (preferring WiFi) in order to prevent unintentionally using up a customer's mobile data plan. However, should a user opt to enable streaming over mobile data, this setting allows them more control.

<figure><img src="/files/6Uyjv9kpCx6JMamPIiFG" alt="" width="345"><figcaption><p>The data saver options in Vesper Mobile</p></figcaption></figure>

### Quality Definitions

#### High (default)

By default, Vesper mobile applications will automatically adjust the playback quality of the video to the maximum supported by the device (based on the detected network conditions at the time). This is known as Adaptive Streaming in the industry. As an example, a 9.7Mbps video stream, watched for an hour, may consume over 4GB of data.&#x20;

#### Low

With Data saver enabled and set to "Low", the bandwidth is capped at 1.5Mbps. The same hour of streaming would consume approximately 620MB of data, an 85% saving.

#### Auto

The "Auto" mode respects the designation of the network provided by the operating system. If a "low data mode" has been enabled ("Data Saver" in Android, "Low Data Mode" in iOS), for a given network, the application will respect it, at switch to "low" mode operation when on that network.

### How to Configure Enhanced Data Saver in Vesper Back Office (New)

With the enhanced Data Saver functionality, operators can now define bitrate caps and default playback quality per realm. This ensures viewers always receive the most efficient video settings for their network conditions.

#### Steps to Configure

1. **Set the Data Saver Threshold (Mbps)**
   * Select the maximum bitrate you want to allow when Data Saver is enabled (e.g., `1.5 Mbps`).
   * This defines the cap applied to the “Low” playback option.
2. **Choose the Default Data Saver Mode**
   * Select one of the following options:
     * **Auto** → Playback adjusts dynamically based on network.
     * **Higher Bandwidth** → Prioritizes video quality, even if it uses more data.
     * **Data Saver** → Optimizes for lowest data consumption.
3. **Contact Account Management Team for configuration**\
   Confirm and provide your desired configuration to your Account Management team for implementation

### Key Notes

* **Configurable “Low” Bitrate Cap** → The threshold you set ensures “Low” mode aligns with your desired data savings.
* **Configurable Default Playback Quality** → The default quality (Low, Auto, or High) can now be aligned with the typical connectivity of your region’s audience.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/consumer-experience/mobile/data-saver.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
