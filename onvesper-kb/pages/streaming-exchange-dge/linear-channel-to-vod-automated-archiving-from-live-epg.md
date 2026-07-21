> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/streaming-exchange-dge/linear-channel-to-vod-automated-archiving-from-live-epg.md).

# Linear Channel to VOD: Automated archiving from Live EPG

As part of our ongoing efforts to enhance and simplify the workflow for content curators, Vesper introduces a new content harvesting tool that automatically clips live linear content based on EPG data.

This tool leverages specific EPG fields to clip linear automatically. It determines precise clipping points utilizing the start and end times in the EPG metadata, and populates the asset metadata with the program title and description.

The required EPG fields are:  &#x20;

* **"harvestProgram"**:true
* **"harvestName"**:"Champions League: Final"

See below an example of an EPG JSON representation of a programme that has been enabled for harvesting:

```
{
      "startTime": "2025-04-01T21:10:00Z",
      "endTime": "2025-04-01T23:55:00Z",
      "contentRating": {
        "rating": "G",
        "descriptors": []
      },
      "description": "Nets vs. Knicks: The Exciting New Crosstown Rivalry Game Between New York's NBA Teams",
      "episode": "Live: NBA",
      "genre": "Basketball",
      "thumbnailImage": "http://nba.com/teams/netsvknicks.jpg",
      "program": "Live: NBA",
      "live": true,
      "harvestProgram": true,
      "harvestName": "NBA: Nets vs. Knicks"
    }
```

Once clipped, the program becomes instantly available in Vesper VOD, allowing content curators to add additional metadata or schedule its publication. If the program includes ad breaks, the automation detects and removes them from the final VOD asset.

Additionally, detailed clipping and archival logs are recorded for future troubleshooting.

{% hint style="info" %}
Please reach out to your Platform Account Manager to enable this feature
{% endhint %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/streaming-exchange-dge/linear-channel-to-vod-automated-archiving-from-live-epg.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
