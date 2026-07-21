> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/overview/global-labels.md).

# Global Labels & Languages

The Platform uses a label system to allow for any language to be supported across all user-facing applications. If you are launching with us using a language we already have translations for, these will be available for use with no further work required.

If you wish to add a currently unsupported language, you can provide translations via your Technical Account Manager.

You can also ask to change a label on your instance of the platform if you don't like the wording of the current/global value - allowing complete customisation of prompts and copy shown to your customers.

During the on-boarding process you will be sent a Google spreadsheet link where you will be asked to fill in any abbreviations or other languages you would like displayed on the platform.

![Global Labels Document Example](/files/-M69LqSd1nzgRBOs183m)

The first column on the spreadsheet will always stay the same as these are our APIs Keys which will always show in English.

The second column in the spreadsheet displays the text that will be used on the platform. If this text needs to be in a different language or requires any changes, please do so in the third column.

The third column will be either any changes you would like to make to the wording or make the wording more bespoke to your platform. Or you can use this column to input the translated wording of the language you would like used on the platform. Please keep in mind that if do wish the platform to use another language then this will be up to you to translate all the relevant words needed.

### Supported Languages

Currently our platform has translations for the following languages:

* English (US)
* English (UK)
* Portuguese
* Brazilian (Portuguese)
* French
* Japanese
* Italian
* Thai
* Dutch
* Arabic
* Georgian
* Ukrainian
* Russian

If you wish to add a new language, contact your Technical Account Manager.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/overview/global-labels.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
