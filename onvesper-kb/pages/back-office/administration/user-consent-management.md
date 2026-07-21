> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/administration/user-consent-management.md).

# User Consent Management

Vesper Back Office empowers our customers to manage the consent form which is shown when users first sign up to a service. This self-service tool is available under the "Administration" menu. Note that if you are using an Single Sign-on system, you should collect relevant consent in that system.

There are three options available:

* Do not display consent forms
* Display consent forms in a popup
* Display consent forms inline

<figure><img src="/files/h0OUWPEMm6tFgOvL296V" alt=""><figcaption><p>Options available for Consent Forms</p></figcaption></figure>

By clicking on "Create New Consent Form" or "Add a Consent Option", a a popup window prompts the resident user to fill the following fields:

* **Localized Text:** choose from the languages already added to the platform
* **Content:** enter the text to be displayed to the final user in the provided text box
* **Format:** select whether the form is only informative or whether it needs user acknowledgment (opt in or out)
  * **Text only**
  * **Checkbox:** if selected, new options are enabled:
    * **Required:** makes the checkbox mandatory for the user
    * **Checked by default:** sets the checkbox as selected by default, giving priority to this option
    * **Purpose:** used for internal records
* **Display settings:**
  * **Enabled**: toggle to be set as enabled when the resident is ready to display the item to end users
  * **Order**: field to rank in numerical order the consent forms as they should appear to the end users

<figure><img src="/files/Ebh9YRpiWbNFbJvsFPW2" alt="" width="550"><figcaption><p>Create Consent Option</p></figcaption></figure>

The dashboard of this tool allows resident users to edit, disable or delete individual forms that have already been added.

#### Links in terms of service

The Text for terms of service supports entering links in the markdown format, for example:

```
[Vesper Knowledgebase](https://docs.onvesper.com/platform-knowledge-base)
```

Would display as [Vesper Knowledgebase](https://docs.onvesper.com/platform-knowledge-base).


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/administration/user-consent-management.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
