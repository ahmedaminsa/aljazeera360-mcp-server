> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/vesper-insights/data-sync/data-sync-feed-file-definitions/user_access_history.md).

# User\_Access\_History

The user\_access\_history provides detailed information about all users (both registered and guest) accessing the platform, including where, when, and on what device the platform was accessed.

There are three types of events that indicate how the user interacted with the platform:

* Whether the user accessed the platform as a guest (guest\_checkin).
* Whether the user logged into their account (successful\_login).
* Whether the token was refreshed while the user was present on the platform (refresh\_token).

### FAQ <a href="#faq.4" id="faq.4"></a>

#### Can we track the number of users who access the platform on a daily basis?

Yes, the primary purpose of user\_access\_history is to track users accessing the platform on a daily basis. This means that if a user performs any of the interactions mentioned above on a given day, they will appear in the user\_access\_history with the corresponding date of activity.

### Data Field Definitions <a href="#data-field-definitions.4" id="data-field-definitions.4"></a>

<table data-header-hidden data-full-width="true"><thead><tr><th width="139">Name</th><th width="114">Type</th><th width="187">Source</th><th>Description</th><th>Comment</th></tr></thead><tbody><tr><td><strong>Name</strong></td><td><strong>Type</strong></td><td><strong>Source</strong></td><td><strong>Description</strong></td><td><strong>Comment</strong></td></tr><tr><td>realm</td><td>character varying 256</td><td><ul><li><code>user_access_history_fact</code></li></ul></td><td>Realm to which the user belongs</td><td> </td></tr><tr><td>customer_exid</td><td>character varying 256</td><td><ul><li><code>user_access_history_fact</code></li></ul></td><td>Unique identifier for the user</td><td> </td></tr><tr><td>access_date</td><td>date</td><td><ul><li><code>user_access_history_fact</code></li></ul></td><td>Date when the user accessed the platform</td><td> </td></tr><tr><td>access_type</td><td>character varying 256</td><td><ul><li><code>user_access_history_fact</code></li></ul></td><td>Denotes how the user accessed the platform</td><td><p>access type:</p><ul><li>login</li><li>refresh token</li><li>guest checkin</li></ul></td></tr><tr><td>country</td><td>character varying 256</td><td><ul><li><code>user_access_history_fact</code></li></ul></td><td>Country where the user was located during their access to the platform (based on the IP address)</td><td> </td></tr><tr><td>town</td><td>character varying 256</td><td><ul><li><code>user_access_history_fact</code></li></ul></td><td>Town where the user was located during their access to the platform (based on the IP address)</td><td> </td></tr><tr><td>device</td><td>character varying 256</td><td><ul><li><code>user_access_history_fact</code></li></ul></td><td>Device used during the user’s access to the platform</td><td> </td></tr><tr><td>client_ip</td><td>character varying 256</td><td><ul><li><code>user_access_history_fact</code></li></ul></td><td>IP address detected during the user’s access to the platform</td><td> </td></tr><tr><td>entitlement_provider_name</td><td>character varying 256</td><td><ul><li><code>user_access_history_fact</code></li></ul></td><td>The name of the external provider that grants the user the entitlement to access the platform</td><td> </td></tr><tr><td>entitlement_provider_id</td><td>character varying 256</td><td><ul><li><code>user_access_history_fact</code></li></ul></td><td>The id of the external provider that grants the user the entitlement to access the platform</td><td> </td></tr><tr><td>entitlement_internal_group_id</td><td>character varying 256</td><td><ul><li><code>user_access_history_fact</code></li></ul></td><td>The internal group id of the external provider that grants the user the entitlement to access the platform</td><td> </td></tr><tr><td>entitlement_external_value</td><td>character varying 256</td><td><ul><li><code>user_access_history_fact</code></li></ul></td><td>The name of the external entitlement that the external provider grants to the user for accessing the platform</td><td> </td></tr><tr><td>external_entitlements</td><td>text</td><td><ul><li><code>user_access_history_fact</code></li></ul></td><td>The JSON object containing an array of all the entitlement fields</td><td> </td></tr><tr><td>authenticate_type</td><td>character varying 256</td><td><ul><li><code>user_access_history_fact</code></li></ul></td><td>The type of the authentication</td><td> </td></tr><tr><td>partition_data</td><td>text</td><td><ul><li><code>user_access_history_fact</code></li></ul></td><td>Access partitions</td><td> </td></tr><tr><td>update_date</td><td>timestamp without time zone</td><td><ul><li><code>user_access_history_fact</code></li></ul></td><td>Date when the data for access was last updated</td><td> </td></tr><tr><td>partition_col</td><td>bigint</td><td><ul><li><code>user_access_history_fact</code></li></ul></td><td>The column used to partition data based on the FNV hash of customer_exid</td><td><code>fnv_hash(customer_exid)</code></td></tr></tbody></table>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/vesper-insights/data-sync/data-sync-feed-file-definitions/user_access_history.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
