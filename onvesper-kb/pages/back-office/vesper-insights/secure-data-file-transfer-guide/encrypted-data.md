> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/vesper-insights/secure-data-file-transfer-guide/encrypted-data.md).

# Encrypted Data

The following are the steps you will need to take for receiving Encrypted Data Files from Data Services using an Asymmetric Key (ie: PGP)

1. Generate a public PGP key (**Resident**)
2. Provide the public PGP key in a B2B helpdesk ticket using the following template:\
   \---\
   Hi,\
   \
   I have generated this PGP public key that should be used when encrypting my sensitive data files. Please provide this key (attached as a file) to the data services team for my realm: dce.\[your realm].\
   \
   \---\
   This will be routed to the correct team. (**Resident/Support teams**)
3. Data Services will configure Scheduled Reports and Data Sync Feeds with the public PGP key provided (**ES**)
4. Scheduled reports and Data Sync Feeds are delivered to your configured location, ie: S3, Azure Blob, FTPS, etc - contact your Account Manager if this has not been configured (**Resident/TAM**)
5. Decrypt the encrypted data files with your private PGP key (**Resident**)

Below we will discuss how you can create a public PGP key and how to decrypt an encrypted data file you receive from ES.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/vesper-insights/secure-data-file-transfer-guide/encrypted-data.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
