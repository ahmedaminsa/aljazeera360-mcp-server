> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/self-service-live-streaming/edit-scheduling.md).

# Edit Scheduling

## **Editing an Event**

To edit an existing event, select **Edit Event** from the three-dot actions menu on the event row. This opens a wizard flow similar to the event creation process, allowing you to update any of the following:

* Event details (name, start/end times, description)
* Optional settings, audio tracks, captions, and geo-restrictions

Work through the relevant steps and confirm your changes on the final **Review & Save** screen.

### **Editing a Tournament**

To edit a Tournament, navigate to the **Tournaments** tab and select **Edit** from the three-dot actions menu on the Tournament card. This opens an 8-step wizard covering:

1. Tournament Details — name, poster, and date range
2. Launch Configuration — launch behaviour and automation settings
3. Bitrate Ladder
4. DRM Settings *(optional)*
5. Optional Settings *(optional)*
6. Captions *(optional)*
7. Geo Restrictions *(optional)*
8. Review & Save — review and confirm your changes

{% hint style="info" %}
When "follow Tournament" has been selected, Tournament settings are inherited by all events within it. Changes made here may affect existing and future events, so review carefully before saving.
{% endhint %}

#### **Deleting an Event or Tournament**

To delete an event, select **Delete event** from the three-dot actions menu on the event row. To delete a Tournament, select the equivalent option from the Tournament card actions menu. In both cases you will be prompted to confirm before the item is permanently removed.

> ⚠️ **Important:** Deletion is permanent and cannot be undone. Ensure any associated infrastructure has been terminated before deleting an event.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/self-service-live-streaming/edit-scheduling.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
