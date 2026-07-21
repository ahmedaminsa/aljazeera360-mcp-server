> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/administration/exid-injection.md).

# EXID Injection

EXID Injection is a process of identifying pirate streams on external sources which allows the resident to identify the user and suspend the account. This process will explain how to do the EXID injection itself.

## How to do the Injection

1. Open the DCE and select the relevant realm.
2. Click on 'Administration' at the top and select 'Show EXIDs'

![](/files/YEPfghbEl3HbchHo45Rx)

3. After doing this you will be prompted with the following menu (as seen below), which will allow you to inject the watermark into the live stream.&#x20;

![](/files/eTOtNOAioGclPGy6MGbI)

4. &#x20;A few changes will need to be made in order for us to inject a subtle watermark onto a live stream. In this case from the example above we need to change "Content Type " from VOD to LIVE.\
   The " EXID FORMAT" will stay the exact same as we will keep the EXID short to avoid viewers complaining about the watermark and for tracking purposes.
5. &#x20;The "EXID Position" as the heading suggests this will you to choose where you can place the EXID watermark.

![](/files/q6GzLNJ5Se3IZzK9NLd9)

6. Select the event you are looking to inject the EXID into in the LIVE EVENT section. This is a search field for the name of the event- so in the example below you could type Canelo into the field and the full fight event will be suggested. Failing to enter anything into this field will prompt the DCE to inject into all live event assets (if set to live video, it will be all VOD assets if set to VOD).

![](/files/Z6encwBkgs9YcoA6f51C)

7\. Changes can be made if the first attempt to inject the watermark does fail as some illegal streamers are aware of how this technology works and cover parts of the stream. With that in mind, in some cases it will be beneficial to change this to Dynamic or moving to the bottom right or left of the stream.

8\. The "DISPLAY TIME" slider will be used to determine how long the watermark will be in the stream for. You only need to be doing this for 15 -20 secs. However the maximum amount of time this can be done for is 1 minute.

## Shutting Down The Account

1. Obtain the pirates EXID from the stream source you have found.
2. In the DCE, go to Users at the top.
3. Select EXID from the drop down.
4. Enter in the EXID info and it should bring up a user.
5. Under 'Actions' you will click 'Suspend'. This will suspend the account.

![](/files/4dDW0m8KUiCkQLRVltBc)

<br>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/administration/exid-injection.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
