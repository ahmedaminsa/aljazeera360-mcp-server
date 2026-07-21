> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/consumer-experience/profiles/resident-enablement-and-features.md).

# Resident Enablement & Features

The table below breaks outlines the features and functionalities that are available on the basis that you would like one of two options;&#x20;

1. User profiles (No kids profiles) - Kids profiles is disabled&#x20;
2. User profiles & Kids profiles - Kids profiles is enabled&#x20;

| **Setting**                   | **Details**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | **User Profiles (No Kids Profiles)** | **User Profiles & Kids Profiles** |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------ | --------------------------------- |
| User Profiles                 | Toggle to turn on User Profiles                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Enabled                              | Enabled                           |
| Parental Controls             | Toggle; when used in conjunction with user profiles enablement allows for kids profiles                                                                                                                                                                                                                                                                                                                                                                                                                              | Disabled                             | Enabled                           |
| Max Profiles per Account      | Determine how many profiles can be created for a given account (1-10)                                                                                                                                                                                                                                                                                                                                                                                                                                                | Enabled (Required)                   | Enabled (Required)                |
| First time sign in Experience | Determine if end user must first create a profile or if they can click into a default profile and start viewing content upon first sign in                                                                                                                                                                                                                                                                                                                                                                           | Enabled (Required)                   | Enabled (Required)                |
| Default Avatar                | <p>Default avatar that will be applied to a user profile in the case that the end user does not wish to personalize or if no other avatars are uploaded. Avatar image criteria:</p><ul><li>Min 500x500px</li><li>Max file size 1MB</li><li>Format SVG, PNG</li></ul>                                                                                                                                                                                                                                                 | Enabled (Required)                   | Enabled (Required)                |
| Manage Avatars                | <p>Upload avatar images that will be used by end-users within their profile. Avatar image criteria:</p><ul><li>Min 500x500px</li><li>Max file size 1MB</li><li>Format SVG, PNG</li></ul><p>While adding more avatars outside of the default is optional, it is highly recommended to allow end users that ability to personalize their profiles.</p>                                                                                                                                                                 | Enabled (Optional)                   | Enabled (Optional)                |
| Kids Profile Styling          | <p>Optional Kid Styling & Font Size that will be only applied to Kid Profiles.</p><p>Colors available:</p><ul><li>Primary</li><li>Secondary</li><li>Tertiary</li><li>Background</li><li>EPG</li></ul><p>Font size (100%, 150%, 200% of current) is only applicable to Web as font scale can be managed cleanly from the device.</p><p>If no colors are selected, the realm defaults will be in place.</p><p>If only a subset of the colors are changed, then non-changed colors will retain Realm level setting.</p> | Disabled                             | Enabled (Optional)                |
| Restricted Maturity Ratings   | <p>Where to set restricted maturity ratings for Kids Profiles.</p><p>Content with restricted maturity ratings will be hidden from search and view for users within a Kids profile.</p>                                                                                                                                                                                                                                                                                                                               | Disabled                             | Enabled (Optional)                |

### Backend Flow - Examples&#x20;

In order to take advantage of these features and functionalities in Vesper Admin you will need to ensure you have access. Once you have access there will be four key sections that you will want to access;&#x20;

1. Administration > Parental Controls & User Profiles&#x20;
2. Administration > User Preferences&#x20;
3. Content Management&#x20;
4. Reporting&#x20;

Please see the following pages for more detail.&#x20;


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/consumer-experience/profiles/resident-enablement-and-features.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
