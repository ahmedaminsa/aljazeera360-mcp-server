> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/dve/video/typed-tags/typed-tags-enum-batch-upload.md).

# Typed Tags: ENUM Batch Upload

## Feature Overview

The Batch Upload ENUM Typed Tags feature allows content managers to create ENUM Typed Tag values in bulk by uploading a CSV file through the Vesper VOD UI. For example, when creating a “Top 20 UFC Athletes” ENUM Typed Tag, a content manager can upload a CSV containing values such as *Georges St. Pierre*, *Anderson Silva*, *Randy Couture*, *Alex Pereira* and others, rather than adding each value manually.

The feature provides:

* A self-serve CSV upload option alongside manual entry
* Validation and structured error reporting to protect metadata integrity
* Feedback on upload progress and results

This enhancement reduces manual effort while maintaining control, safety, and consistency in metadata creation. Manual entry is still available; batch uploading is simply a quicker way to handle large value sets or multiple languages.

### What's Available

When creating or editing an ENUM Typed Tag in Vesper VOD: Admin → Typed Tags, content managers will see an 'Upload CSV' option.

<div data-with-frame="true"><figure><img src="/files/qDfE3Z5FO0yPvmzskK8K" alt=""><figcaption><p>Typed Tag Creation Page with the 'Upload CSV' Button</p></figcaption></figure></div>

With this feature, a content manager can:

* Create new ENUM values in bulk
* Add new or update localized values to existing keys
* Review changes before confirming

Following validation and review, no changes are applied until the content manager confirms.

## How to Upload ENUM Values

{% stepper %}
{% step %}

### Download the CSV Template

Content managers should start by downloading the provided CSV template from the Upload Page, which ensures the file has the correct structure.

<div data-with-frame="true"><figure><img src="/files/96WUXSv91s2nZSFlHVG3" alt=""><figcaption><p>Upload Page featuring the CSV Template</p></figcaption></figure></div>
{% endstep %}

{% step %}

### Structure the CSV

The CSV must include:

* Column 1: key
* Columns 2 onward: language codes (e.g., en-GB, es-MX)

Each row represents a single value ( a key + translations).

Example:

<figure><img src="/files/k49icGOyxL90qDP6ZfEa" alt=""><figcaption></figcaption></figure>

**Language column rules:**

* Accepted formats: en-GB, en\_GB, en.GB (*case-insensitive*)
* Each language column must be unique
* Invalid language headers are ignored and will trigger a warning
  {% endstep %}

{% step %}

### Prepare the Values

* Keys are case-sensitive (*Rangers and rangers are different*)
* Values are saved exactly as entered - spaces at the start or end are trimmed (*i.e. typing " hello " saves "hello" without the extra spaces*)
* The upload adds new localized values for keys, and updates existing ones **only** when the CSV provides a new value.
  {% endstep %}

{% step %}

### Upload the File

* Content managers can upload one CSV at a time using the Upload CSV button.
* The file is validated for readability, formatting, required columns, and duplicate languages.
* If there are errors, a message will appear so the content manager can fix it before trying again.
* Once uploaded, the file cannot be replaced.
* If no actionable changes are found (*no values to create or update*), the files is discarded and the content manager can upload a new CSV.
  {% endstep %}

{% step %}

### Review & Confirm

Before any changes are applied, content managers will see a summary showing:

<div data-with-frame="true"><figure><img src="/files/envDmksU0cQPLTS17uJq" alt=""><figcaption><p>Approval Page With Summary</p></figcaption></figure></div>

* Number of values to be created
* Number of values to be updated
* Any warnings detected
  * Warnings may include:
    * Duplicate keys with conflicting values
    * Invalid language headers (*ignored*)
    * Missing translations
    * Empty rows and/or columns

After reviewing, the content manager confirms the upload but clicking 'Submit'. New and updated values then appear immediately - no page refresh is required.
{% endstep %}
{% endstepper %}

## Managing ENUM Values After Upload

After confirming the upload, content managers can:

<div data-with-frame="true"><figure><img src="/files/7HtphncMlQoj8PKoLLpj" alt=""><figcaption></figcaption></figure></div>

* Search by key or translated value.
* Switch languages without losing search or filter settings.
* Filter missing translations to see only values that need content.
* Spot gaps quickly with visual indicators for incomplete translations.
* See updates immediately: new or edited values appear without a page refresh.

This keeps the ENUM list east to manage and ensures metadata stay accurate across all languages.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/dve/video/typed-tags/typed-tags-enum-batch-upload.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
