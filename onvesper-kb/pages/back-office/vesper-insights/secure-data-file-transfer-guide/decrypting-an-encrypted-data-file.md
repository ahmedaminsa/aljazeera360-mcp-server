> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/vesper-insights/secure-data-file-transfer-guide/decrypting-an-encrypted-data-file.md).

# Decrypting an encrypted data file

If you have created a **key-pair** following the steps on the previous section, a new public key should now be available on **GPG keychain.**

Below we show how to perform this step depending on your OS (Mac, Ubuntu and Windows). Please refer to the OS section below for step-by-step instructions:

#### Mac

To decrypt a file, **right click** on the file, “**services**”, “**OpenPGP: Decrypt File**“

<figure><img src="/files/EoOOdk3jZnrQCz03pA9B" alt=""><figcaption></figcaption></figure>

#### Windows

To decrypt a file, **right click** on the file and select **Decrypt and verify**:

<figure><img src="/files/9HYtSWgSe4jNLPPnvoHe" alt=""><figcaption></figcaption></figure>

#### Linux

1. To decrypt a file:

   `gpg --output <decryptFileOutputName> --decrypt <encryptFileName>`


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/vesper-insights/secure-data-file-transfer-guide/decrypting-an-encrypted-data-file.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
