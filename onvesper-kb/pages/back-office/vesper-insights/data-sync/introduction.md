> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/vesper-insights/data-sync/introduction.md).

# Introduction

Data Sync Feeds allow you to setup systems on your side that will receive batch updates of the same data that is in Endeavor Streaming’s Data Warehouse that also powers Vesper Insights as well as any Vesper Self-service Reports.

The following data sync feeds are available:

1. cutomer\_profile
2. customer\_licence
3. revenue
4. view\_session
5. user\_access\_history
6. guest\_profile

Data Sync feeds uses the update\_date field of the data sync feeds you receive to determine when a record gets exported. If a record is updated for any reason, such as a customer\_licence status change, then the update\_date field is updated and that record will be picked up to be exported the next time the data sync schedule runs. This update\_date field exists in each data sync feed file.

{% hint style="info" %}
Even if you elect to have incremental delta feeds sent exported on a regular cadence, it still quite possible the file can be very large. Your pipeline must be able to support ingesting files with large number of records and file sizes. For instance, it’s quite possible that a bulk update could be made to a large number of records, or during a large event that a large number of customer\_profile records could be updated with the last watch date, etc. In such cases, large number of records will have their update\_date field updated and will be selected for exporting in the next data sync run.
{% endhint %}

### Time Zones

The data sync feeds are scheduled to export in the time zone of the User that scheduled the data sync in the Vesper Admin. But the data in the data feeds will always be exported in UTC time zone.

For example:

Assume you log into Vepser Admin, and your current timezone is set to America/New\_York. When you schedule the data sync feed for 12:00AM, the data sync will begin at 12:00AM EST. Let’s assume it runs on 8/24/2023 12:00AM EST, but because UTC is +5:00 hours ahead, it will export all data since the last data sync up to but not including 8/24/2023 05:00 UTC. All the date fields in the data sync feed will also be in UTC and you will see records with dates leading up to that same end date of 8/24/2023 05:00 UTC. In other words, update\_date < 8/24/2023 05:00 UTC.

### File Naming Convention & Formats

The data sync feeds you receive will be named as follows:

`YYYY_MM_DD_HH_{realm}_data_sync_{feed name}_{pii || nopii}_{delta || full || resync}_{unique identifier}.csv`

Where:

* `YYYY_MM_DD_HH` - the year, month, day, hour the feed is generated
* `{realm}` - The name of your realm associated to your service, such as dce\_myrealm
* `data_sync` - to differentiate these feed files from other files from Endeavor Streaming if you use same folder, such as for reports
* `{feed name}` - the name of the data sync feed that is sent, such as revenue
* `{pii || nopii}` - If the feed is configured to send PII data such as email, etc, then this file name will have pii in it, otherwise nopii
* `{delta || full || resync}` - This defines what data we send in the data sync feeds.
  * delta is for feeds with only incremental updates since the last sync.
  * full is for feeds that will always contain the full set of data every time it’s sent.
  * resync is for when the realm wants to resync their data storage with the full set of data in ES DWH and resume delta afterwards.
* `{unique identifier}` - this is used to uniquely identify one data sync from another of the same kind without overwriting. This value is the timestamp it ran in epoch time.

Example:

`2023_08_24_05_dce_myrealm_data_sync_revenue_nopii_delta_1692853200.csv`

#### Large files/multi-part delivery

Under 5GB of data, you will receive a single CSV file containing the data. If the file to be delivered exceeds 5GB, we need to break the file into multiple CSVs. In this instance you will see 2 new components to the file name:

`{current index}_{total files}`

Where:

* `{current index}` - will be the current number of the files being delivered; e.g. "001"
* `{total files}` - the total files to be delivered for this drop: e.g. "003"

In the example above, the file would be number "001" of "003" total.

Example large drop:

`2023_08_24_05_dce_myrealm_data_sync_revenue_nopii_delta_1692853200_001_003.csv`

{% hint style="info" %}
For both large files and smaller/single files all CSVs are compressed (.zip) before transmission. You will receive all files as a .zip containing a single CSV file.
{% endhint %}

### File Format Convention

* Data sync feeds contain a column header, and rows where fields are comma separated.
* All column header fields are in lower case.
* String fields containing commas are enclosed in double quotes. Such as a list of countries, partitions team, etc. where there are multiple values in that field, these will be comma separated and enclosed in double quotes.
* When a feed contains no records, it will still contain the column header.
* Column fields may be appended with no notice
* Non-documented fields may be removed with no notice if they are the last field on the list of fields
* Documented fields will never be removed without notice
* If a non-documented field is not the last field on the list, it will never be removed without notice

### How Data is Sorted

The output of each of the data sync feeds described in the following sections will be exported to you sorted by dates sensible for systems that take advantage of sorted data sets for efficient handling of date range restricted operations and ingestions.

Sort order of data sync feeds:

* customer\_profile - order by last\_access\_date desc
* guest\_profile - order by last\_access\_date desc
* customer\_licence - order by order\_date desc
* revenue - order by txn\_date desc
* view\_session - order by started\_at desc
* user\_access\_history - order by access\_date desc

### PII Data

Generally, Vesper Data Sync will be configured to send PII data in the customer\_profile feed which is an appropriate place to send it. The other feeds do not include PII data and it’s discouraged if asked.

If a feed is configured to include PII data, these PII columns will appear as the first few columns of the data feed.

Example: the customer\_profile data feed with PII data, would have columns in the following order:

```
// email,full_name,preferred_name,dob,phone_number,customer_profile_id,real,customer_exid..... 
```

{% hint style="info" %}
PII data updates are not included in the data sync feed until a significant action occurs, such as a video being played or a new transaction. At that point, the customer\_profile feed will incorporate the PII data update, but it will not be shared alone. Example: if a user updates his date of birth, the data sync feed won't include that change until the user watches a video.
{% endhint %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/vesper-insights/data-sync/introduction.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
