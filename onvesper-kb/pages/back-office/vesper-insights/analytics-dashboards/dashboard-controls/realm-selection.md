> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/vesper-insights/analytics-dashboards/dashboard-controls/realm-selection.md).

# Realm Selection

## Overview

In Vesper Insights, users who manage or interact with data across multiple realms have the flexibility to quickly filter and view relevant data using the *Realm Selection* dropdown within the Shortcut Panel.

This feature is particularly useful for users who operate in environments where data is segmented by realm, allowing for efficient data comparison and analysis.

## Accessing the Realm Selection Filter

The Realm Selection filter can be found within the Shortcut Panel on the left side of the interface. This dropdown allows users to toggle between different realms or select multiple realms simultaneously. The selection made here directly influences the data displayed in the dashboard and visualizations.

<figure><img src="/files/YgyTez0iqnWge7vjuUYS" alt=""><figcaption></figcaption></figure>

## Functionality and Use Cases

Single Realm View

When a user selects a single realm from the dropdown, the data displayed is specific to that realm. This is useful for focused analysis within a particular area.

Multiple Realm View

Users have the option to select multiple realms simultaneously. When multiple realms are selected, Vesper Insights provides powerful comparison tools. Users can then decide to break down data via realm by selecting "Realm" as the 'List-by' or 'Color-by' options.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/vesper-insights/analytics-dashboards/dashboard-controls/realm-selection.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
