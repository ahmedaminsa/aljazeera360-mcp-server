> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/vesper-insights/analytics-dashboards/dashboard-controls/underlying-data.md).

# Underlying Data

This allows you to view the underlying data for any dashboard.&#x20;

**How do you use this?**&#x20;

1\. View your Dashboard: Navigate to any dashboard within Vesper Insights.&#x20;

2\. Click the 'Underlying Data' Action Button: Look for the new 'underlying data' action button on your dashboard.&#x20;

&#x20;![](/files/yt2o7PpWDX1pMBA8IQfL)

3. Access Immediate Data: Clicking this button will directly show you the underlying data for the dashboard you are currently viewing.

**Haven't I previously been able to navigate to a tab to see the underlying data?**

With the growing number of dashboards being added to Vesper Insights, we recognized the need for a more efficient way to access the correct underlying data. By making this change, we aim to:&#x20;

Simplify Navigation: No more switching tabs! You can now access the underlying data directly from the dashboard you are viewing.&#x20;

Improve Efficiency: Clicking the 'underlying data' action button will instantly show you the relevant data for the current dashboard, saving you time and reducing confusion.&#x20;

Enhance User Experience: This new feature ensures that you are always accessing the correct data, enhancing the overall usability of Vesper Insights.&#x20;

&#x20;


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/vesper-insights/analytics-dashboards/dashboard-controls/underlying-data.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
