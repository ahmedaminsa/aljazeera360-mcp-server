> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/back-office/analytics-1/reports.md).

# Reports

Under the Analytics drop-down you will notice an option called Reports, in this section you can find the five types of reports: Transaction, Customer, Promo Code, Licence, VOD and Live Event.

![Reports](/files/-M57ZmlmsZ9uIt0dchnm)

{% hint style="info" %}
The Transaction and Customer reports are generated every 6 hours (from 6am), whilst Promo Code, Licence, VOD and Live Event are generated once a day.
{% endhint %}

![](https://i1.wp.com/docs.dice.technology/wp-content/uploads/2019/09/Screen-Shot-2019-07-04-at-11.57.49-AM.png?resize=835%2C307\&ssl=1)

After selecting ‘Download Report’ you will be taken through to the Reporting page where it will show all the available reports for downloading;

### **Transaction List**

A transaction report will encompass top-line financial reporting of all the transactions made within a given time period for a given realm.

| Field                         | Description                                                                                                                  |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| CUSTOMER\_EXID                | Unique Identifier of the customer on Vesper platform.                                                                        |
| CUSTOMER\_EMAIL               | The email address of the user.                                                                                               |
| CUSTOMER\_FULL\_NAME          | The full name of the user stored in their account.                                                                           |
| CUSTOMER\_PREFERRED\_NAME     | The preferred name of the user stored in their account.                                                                      |
| BILLING\_COUNTRY              | Billing address country                                                                                                      |
| BILLING\_POSTCODE             | Billing address postcode                                                                                                     |
| BILLING\_STATE                | Billing address state (administrativeLevel1)                                                                                 |
| BILLING\_TOWN                 | Billing address town                                                                                                         |
| BILLING\_LINE1                | Billing address line 1                                                                                                       |
| REALM                         | Denotes the realm that this event relates to. This will be constant for all records in the report.                           |
| TRANSACTION\_NUMBER           | Payment Event ID, unique for every payment                                                                                   |
| PURCHASE\_ID                  | Order ID, unique for every continuous subscription of a customer                                                             |
| DATE\_OF\_ORDER               | The timestamp a payment event is initiated by the platform                                                                   |
| LICENCE\_NAME                 | Name of the licence.                                                                                                         |
| LICENCE\_SKU                  | Corresponding SKU for the licence in this transaction                                                                        |
| LICENCE\_IAP\_PRODUCT         | Corresponding IAP product identifier for the licence in this transaction                                                     |
| PAYMENT\_PROVIDER             | Payment provider used in this transaction.                                                                                   |
| PAYMENT\_STATUS               | <p>Payment status:<br>CONFIRMED <br>RENEWAL <br>CANCELLED<br>REFUND</p>                                                      |
| QUANTITY                      | Number of items licences purchased in this transaction.                                                                      |
| CARD\_LAST\_FOUR\_DIGIT       | Last 4 digits of credit card used in this transaction                                                                        |
| CARD\_EXPIRY\_DATE            | Month and Year of card expiry date (MMYY)                                                                                    |
| CARD\_TYPE                    | Type of card                                                                                                                 |
| CARD\_IDENTIFIER              | Unique identifier for the card.                                                                                              |
| PRICE                         | Amount charged in this transaction.                                                                                          |
| CURRENCY\_CODE                | Currency that the transaction was made.                                                                                      |
| TAX                           | Tax charged in this transaction.                                                                                             |
| TAX\_INCLUSIVE                | Denotes whether tax in inclusive/exclusive.                                                                                  |
| VOUCHER                       | Denotes whether voucher was used in this purchase                                                                            |
| VOUCHER\_NAME                 | Name of voucher campaign to correlate with voucher metadata                                                                  |
| VOUCHER\_CODE                 | Code used to redeem voucher                                                                                                  |
| GIFT\_CARD                    | Denotes whether a gift card was used with this purchase                                                                      |
| GIFT\_CARD\_PROVIDER          | Name of the gift card provider                                                                                               |
| GIFT\_CARD\_CODE              | Code used to redeem gift card.                                                                                               |
| SCHEDULED\_BILLING\_DATE      | The timestamp scheduled to next bill the customer                                                                            |
| TRANSACTION\_DATE             | The timestamp that this transaction was initiated                                                                            |
| PENDING                       | Denotes a transaction has not completed.                                                                                     |
| TRANSACTION\_COMPLETION\_DATE | The timestamp that this transaction was completed (this will only be present on transactions with managed payment providers) |
| FREE TRIAL                    | Where a CONFIRMED transaction was actually for a free trial, we'll flag this in the new FREE\_TRIAL column.                  |

### **Customer Summary**

A customer report will show a list of all customers registered for a given realm and the current licence (subscription) status.

1. If the user has 1 ACTIVE licence, we'll show that licence
2. If the user has more than 1 ACTIVE licence, we'll show all ACTIVES
3. If the user has 1 ACTIVE licence and 1 EXPIRED licence, we'll show just the 1 ACTIVE
4. If the user has 0 ACTIVE licences but 1 or more EXPIRED licences, we'll show the most recent expired licence
5. If the user has 0 ACTIVE licences and 0 EXPIRED licences, we'll show their EXID to denote them as a user known to the platform that has never been converted.

| Field                            | Description                                                                                                                                                                                                                                |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| CUSTOMER\_EMAIL                  | The email address of the user.                                                                                                                                                                                                             |
| CUSTOMER\_EXID                   | Unique Identifier of the customer on Vesper platform.                                                                                                                                                                                      |
| CUSTOMER\_BILLING\_COUNTRY       | The country that user has their billing address in.                                                                                                                                                                                        |
| CUSTOMER\_FULL\_NAME             | The full name of the user stored in their account.                                                                                                                                                                                         |
| CUSTOMER\_PREFFERED\_NAME        | The preferred name of the user stored in their account.                                                                                                                                                                                    |
| CUSTOMER\_CREATED\_DATE          | The date the customer first registered their account.                                                                                                                                                                                      |
| LICENCE\_NAME                    | Name the licence associated with this account if the customer has a subscription.                                                                                                                                                          |
| LICENCE\_TYPE                    | <p>Licence type:</p><ul><li>SUBSCRIPTION</li><li>RENTAL</li><li>PPV</li></ul>                                                                                                                                                              |
| LICENCE\_STATUS                  | <p>Current licence status (TRIAL\_ACTIVE / TRIAL\_EXPIRED will only be present on managed payments, not IAP payments):</p><ul><li>ACTIVE</li><li>TRIAL\_ACTIVE</li><li>TRIAL\_EXPIRED</li><li>EXPIRED</li><li>REVOKED</li><li>NA</li></ul> |
| LICENCE\_SUBSCRIPTION\_PERIOD    | The subscription period that licence will be renewed.                                                                                                                                                                                      |
| PAYMENT\_PROVIDER\_TYPE          | Payment provider associated with this account if the customer has a subscription.                                                                                                                                                          |
| LICENCE\_TRIAL\_PERIOD           | Number of days given as trial period for this licence.                                                                                                                                                                                     |
| LICENCE\_RENEWAL\_DATE           | Date of licence renewal.                                                                                                                                                                                                                   |
| PURCHASE\_DATE                   | Date that the licence was originally purchased.                                                                                                                                                                                            |
| THIRD\_PARTY\_MARKETING\_ALLOWED | Denotes whether customer has consented to third party marketing.                                                                                                                                                                           |
| RESIDENT\_MARKETING\_ALLOWED     | Denotes whether customer has consented to marketing from client.                                                                                                                                                                           |
| TARGETED\_ADS\_ALLOWED           | Denotes whether customer has consented to targeted ads.                                                                                                                                                                                    |
| VIP\_STATUS                      | Denotes whether customer has VIP Status, which removes any geo or licence restrictions.                                                                                                                                                    |
| LICENCE\_EXPIRY\_DATE            | Date the current licence will expire, or the date the most recent licence the customer had expired.                                                                                                                                        |
| LICENCE\_SKU                     | Corresponding SKU to the licence                                                                                                                                                                                                           |
| LICENCE\_IAP\_PRODUCT            | Corresponding IAP product identifier to the licence                                                                                                                                                                                        |
| AUTO\_RENEWAL                    | Denotes whether the customer has an auto-renewing licence                                                                                                                                                                                  |
| ACTIVE\_THIS\_MONTH              | Denotes whether customer was active on the platform within the last month (covering this report)                                                                                                                                           |
| LAST\_ACTIVE                     | Date that the user was last active                                                                                                                                                                                                         |
| CUSTOMER\_PREFERRED\_LANGUAGE    | Preferred language of the user interface (if applicable)                                                                                                                                                                                   |
| STREET\_LINE\_1                  | Billing address line 1                                                                                                                                                                                                                     |
| STREET\_LINE\_2                  | Billing address line 2                                                                                                                                                                                                                     |
| TOWN                             | Billing address town                                                                                                                                                                                                                       |
| STATE                            | Billing address state (administrativeLevel1)                                                                                                                                                                                               |
| POST\_CODE                       | Billing address postcode                                                                                                                                                                                                                   |
| EXTERNAL\_AUTH\_PROVIDER         | External authentication provider                                                                                                                                                                                                           |
| EXTERNAL\_AUTH\_ID               | External identifier in the case that an external authentication provider is used                                                                                                                                                           |
| CUSTOMER ID                      | We now list a customer's ID (in addition to their contact email address). On occasions, they are not (sometimes by design) and this will allow you to spot differences quickly if there are issues.                                        |

### **Promo Code Report**

A promo code report will show a list of Promo campaigns for a given realm.

| Field                       | Description                                                                                 |
| --------------------------- | ------------------------------------------------------------------------------------------- |
| CAMPAIGN\_ID                | The ID of the campaign                                                                      |
| CAMPAIGN\_NAME              | The name of the campaign                                                                    |
| CAMPAIGN\_TYPE              | <p>The type of the campaign:</p><ul><li>generic</li><li>one-off</li></ul>                   |
| CODE                        | The code associated with the campaign (N/A for one-off campaigns)                           |
| REDEMPTION\_CAP             | The total number of redemptions available for this campaign                                 |
| REDEEMED                    | The number of promo codes that have been redeemed at the time that the report was generated |
| START\_DATE                 | The start date of the campaign                                                              |
| END\_DATE                   | The end date of the campaign                                                                |
| GEO\_RESTRICTION\_TYPE      | <p>Geo restriction type:</p><ul><li>BLACKLIST</li><li>WHITELIST</li></ul>                   |
| GEO\_RESTRICTION\_COUNTRIES | Comma separated list of countries to be included in the geo restriction type above          |
| LICENCE\_RESTRICTION\_TYPE  | <p>Licence restriction type:</p><ul><li>BLACKLIST</li><li>WHITELIST</li></ul>               |
| LICENCE\_RESTRICTION        | Comma separated list of countries to be included in the licence restriction type above      |
| LIFETIME\_REPEAT            | Denotes whether the promo campaign rules are to be applied indefinitely                     |

### **Licence Catalog**

A licence report will show a list of licences for a given realm.

| Field                                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ---------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| NAME                                     | The name of the licence                                                                                                                                                                                                                                                                                                                                                                                                                       |
| LICENCE\_TYPE                            | <p>The type of the licence:</p><ul><li>BLANKET</li><li>FREE</li><li>STANDARD</li></ul>                                                                                                                                                                                                                                                                                                                                                        |
| GEO\_RESTRICTION\_TYPE                   | <p>Geo restriction type:</p><ul><li>BLACKLIST</li><li>WHITELIST</li></ul>                                                                                                                                                                                                                                                                                                                                                                     |
| GEO\_RESTRICTION\_COUNTRIES              | Comma separated list of countries to be included in the geo restriction type above                                                                                                                                                                                                                                                                                                                                                            |
| AVAILABILITY\_START\_DATE                | The start date the licence becomes available                                                                                                                                                                                                                                                                                                                                                                                                  |
| AVAILABILITY\_END\_DATE                  | The end date the licence becomes no longer available                                                                                                                                                                                                                                                                                                                                                                                          |
| PURCHASE\_START\_DATE                    | The start date the licence becomes purchasable                                                                                                                                                                                                                                                                                                                                                                                                |
| PURCHASE\_END\_DATE                      | The end date the licence becomes no longer purchasable                                                                                                                                                                                                                                                                                                                                                                                        |
| SUBSCRIPTION\_TYPE                       | <p>Subscription type:</p><ul><li>NONE</li><li>SUBSCRIPTION</li><li>PPV</li></ul>                                                                                                                                                                                                                                                                                                                                                              |
| SUBSCRIPTION\_PERIOD                     | Duration of the subscription period                                                                                                                                                                                                                                                                                                                                                                                                           |
| DEVICE\_RESTRICTION\_TYPE                | <p>Device restriction type:</p><ul><li>BLACKLIST</li><li>WHITELIST</li></ul>                                                                                                                                                                                                                                                                                                                                                                  |
| DEVICE\_TYPES                            | <p>Comma separated list of device types to be included in the devices restriction type above:</p><ul><li>BROWSER</li><li>IOS\_PHONE</li><li>IOS\_TABLET</li><li>ANDROID\_PHONE</li><li>ANDROID\_TABLET</li><li>TV</li><li>XBOX</li><li>PSX</li><li>ROKU</li><li>FIRE\_TV<br></li><li>APPLE\_TV<br></li><li>ANDROID\_TV</li><li>LG\_TV</li><li>PANASONIC\_TV</li><li>SAMSUNG\_TV</li><li>SONY\_TV</li><li>TIVO\_TV</li><li>TIZEN\_TV</li></ul> |
| ENTITLEMENT\_PROVIDER\_RESTRICTION\_TYPE | <p>Entitlement provider restriction type:</p><ul><li>BLACKLIST</li><li>WHITELIST</li></ul>                                                                                                                                                                                                                                                                                                                                                    |
| ENTITLEMENT\_PROVIDERS                   | Comma separated list of entitlement providers to apply provider restriction above                                                                                                                                                                                                                                                                                                                                                             |
| PERMIT\_GUEST                            | Denotes whether licence permits guest access                                                                                                                                                                                                                                                                                                                                                                                                  |
| PERMIT\_VPN                              | Denotes whether licence permits access over VPN                                                                                                                                                                                                                                                                                                                                                                                               |
| SKU\_TYPE                                | <p>Type of SKU:</p><ul><li>WEB</li><li>APPLE\_IAP</li><li>ANDROID\_IAP</li><li>ROKU\_IAP</li></ul>                                                                                                                                                                                                                                                                                                                                            |
| SKU                                      | SKU of licence that can be purchased, either WEB or an IAP product identifier                                                                                                                                                                                                                                                                                                                                                                 |
| AMOUNT                                   | The amount payable in the above currency for this licence                                                                                                                                                                                                                                                                                                                                                                                     |
| CURRENCY                                 | Currency code that the amount for this licence is listed in                                                                                                                                                                                                                                                                                                                                                                                   |
| TAX\_INCLUSIVE                           | Denotes whether tax is inclusive of the amount                                                                                                                                                                                                                                                                                                                                                                                                |
| LOCAL\_FOR\_COUNTRIES                    | Comma separated list of country codes where is specific SKU for a licence is listed as the 'local' SKU                                                                                                                                                                                                                                                                                                                                        |
| MAX\_CONCURRENCY                         | Maximum concurrent streams permitted with this licence                                                                                                                                                                                                                                                                                                                                                                                        |
| PURCHASE\_DEVICE\_RESTRICTION            | Purchase device restrictions                                                                                                                                                                                                                                                                                                                                                                                                                  |
| PURCHASE\_DEVICE\_RESTRICTION\_TYPE      | <p>Purchase device restriction type:</p><ul><li>BLACKLIST</li><li>WHITELIST</li></ul>                                                                                                                                                                                                                                                                                                                                                         |
| AVAILABLE\_DEVICE\_RESTRICTION           | Availability device restrictions                                                                                                                                                                                                                                                                                                                                                                                                              |
| AVAILABLE\_DEVICE\_RESTRICTION\_TYPE     | <p>Availability device restriction type:</p><ul><li>BLACKLIST</li><li>WHITELIST</li></ul>                                                                                                                                                                                                                                                                                                                                                     |

### **VOD Catalog**

A VOD report will show a list of VOD content for a given realm.

| Field               | Description                                                                                          |
| ------------------- | ---------------------------------------------------------------------------------------------------- |
| REALM               | The ID of the realm                                                                                  |
| VOD\_ID             | The ID of the VOD in Vesper                                                                          |
| VOD\_DVE\_ID        | The ID of the VOD in DVE, this is considered the primary key for the VOD across all reporting.       |
| DGE\_EVENT\_ID      | The ID of the live event in DGE in the case that this VOD was recorded from a live event.            |
| REALM\_OPERATOR\_ID | The ID of the Realm Operator                                                                         |
| TITLE               | The title of the VOD                                                                                 |
| DESCRIPTION         | The description of the VOD                                                                           |
| DURATION            | The duration of the VOD in seconds                                                                   |
| DELETED             | Denotes the VOD has been deleted                                                                     |
| DRAFT               | Denotes the VOD is in Draft state                                                                    |
| IMPORTED\_AT        | Date the VOD was first created in Vesper                                                             |
| UDPATED\_AT         | Date the VOD was last updated in Vesper                                                              |
| TAGS                | Comma separated list of tags that have been applied to this VOD, this will include any licence tags. |
| EXTERNAL\_ID        | External Asset ID                                                                                    |

### **Live Catalog**

A Live Report will show a list of the Live content for a given realm.

| Field               | Type                     | Description                                                                                                  |
| ------------------- | ------------------------ | ------------------------------------------------------------------------------------------------------------ |
| ID                  | number                   | The ID of the live event in DGE, this is considered the primary key for the live event across all reporting. |
| NAME                | string                   | The name of the live event                                                                                   |
| SPORT\_ID           | number                   | The ID of the sport associated with this live event                                                          |
| TOURNAMENT\_ID      | number                   | The ID of the tournament associated with this live event                                                     |
| TOURNAMENT\_NAME    | string                   | The name of the tournament associated with this live event                                                   |
| REALM\_OPERATOR\_ID | number                   | The ID of the Realm Operator                                                                                 |
| TITLE               | string                   | The title of the live event                                                                                  |
| START\_DATE         | string, ISO8601 datetime | Date the live event starts                                                                                   |
| END\_DATE           | string, ISO8601 datetime | Date the live event ends                                                                                     |
| EXTERNAL\_ID        | string                   | External Asset ID                                                                                            |

To view and export the report you want, select ‘Download’ for that report, the report will then be downloaded in a .csv format.

### Peak Concurrency Report

A list of live events that occurred within the last 7 days and their peak concurrency.

| Field             | Type                     | Description                                                                                         |
| ----------------- | ------------------------ | --------------------------------------------------------------------------------------------------- |
| START\_DATE       | string, ISO8601 datetime | Date the live event starts                                                                          |
| REALM             | string                   | Denotes the realm that this report has been generated, will be constant for all rows in the report. |
| PEAK\_CONCURRENCY | number                   | The total number of concurrent users watching this event at it’s peak.                              |
| EVENT\_NAME       | string                   | The name of the live event                                                                          |
| EVENT\_ID         | number                   | The ID of the live event                                                                            |
| END\_DATE         | string, ISO8601 datetime | Date the live event ends                                                                            |

### Channel Catalog Report

A catalogue of programmes scheduled on live channels&#x20;

| Field                  | Type                     | Description                                                                                                                                                       |
| ---------------------- | ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CHANNEL\_ID            | number                   | The ID of the channel                                                                                                                                             |
| CHANNEL\_TITLE         | string                   | The title of the channel                                                                                                                                          |
| DEFAULT\_LOCALE        | string                   | The default locale for the channel                                                                                                                                |
| DGE\_EVENT\_ID         | number                   | The corresponding live event ID that the channel is streamed from.                                                                                                |
| CHANNEL\_ORDER         | number                   | The relative position of the channel in relation of all channels in this report.                                                                                  |
| DCE\_VIDEO\_ASSET\_ID  | Number                   | The ID of the programme scheduled to play on this channel at the time specified in this row. For Virtual Live Linear channels this will be the corresponding VOD. |
| PROGRAMME\_START\_DATE | string, ISO8601 datetime | Date the programme is scheduled to start                                                                                                                          |
| PROGRAMME\_END\_DATE   | string, ISO8601 datetime | Date the programme is scheduled to end                                                                                                                            |

### Content Bucket Report&#x20;

A catalog of content buckets&#x20;

| Field              | Type    | Description                                                                                                                                                                                                            |
| ------------------ | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| BUCKET\_ID         | string  | The EXID of the bucket                                                                                                                                                                                                 |
| BUCKET\_TYPE       | string  | <p>The type of bucket:</p><ul><li>VOD\_VIDEO</li><li>VOD\_PLAYLIST</li><li>VOD\_RESUME</li><li>VOD\_RECOMMENDATIONS</li><li>PLAYLISTS</li><li>UPCOMING</li><li>LIVE</li><li>DATA\_FEED</li><li>SECTION\_LINK</li></ul> |
| METADATA\_LANGUAGE | string  | The default locale for the metadata of the bucket                                                                                                                                                                      |
| BUCKET\_NAME       | string  | The name of the bucket                                                                                                                                                                                                 |
| DRAFT              | boolean | Denotes the bucket is in a draft state.                                                                                                                                                                                |
| ROW\_TYPE          | string  | <p>The display row type of the bucket:</p><ul><li>BASIC</li><li>FEATURED</li><li>INLINE</li></ul>                                                                                                                      |

### Playlist Catalog Report&#x20;

A content catalog of VOD playlists&#x20;

| Field             | Type                     | Description                                                                               |
| ----------------- | ------------------------ | ----------------------------------------------------------------------------------------- |
| DGE\_EVENT\_ID    | number                   | The ID of the live event in DGE in the case that this VOD was recorded from a live event. |
| IMPORTED\_AT      | string, ISO8601 datetime | Date the Playlist was first created in Vesper                                             |
| LANGUAGE          | string                   | The default locale of the Playlist                                                        |
| PLAYLIST\_DVE\_ID | number                   | The ID of the playlist in DVE.                                                            |
| PLAYLIST\_ID      | number                   | The ID of the Playlist in Vesper                                                          |
| TAGS              | string                   | Comma separated list of tags that have been applied to this Playlist.                     |
| TITLE             | string                   | The title of the Playlist                                                                 |
| UDPATED\_AT       | string, ISO8601 datetime | Date the Playlist was last updated in Vesper                                              |

### Season Catalog Report&#x20;

A content catalog of VOD seasons

| Field                | Type   | Description                                                         |
| -------------------- | ------ | ------------------------------------------------------------------- |
| VOD\_SEASON\_ID      | number | The ID of the Season in Vesper                                      |
| VOD\_SEASON\_DVE\_ID | number | The ID of the Season in DVE.                                        |
| TITLE                | string | The title of the Season                                             |
| LANGUAGE             | string | The default locale of the Season                                    |
| TAGS                 | string | Comma separated list of tags that have been applied to this Season. |
| SEASON\_NUMBER       | number | The Season number of the Series that this Season is part of         |
| REALM                | string | The ID of the realm                                                 |
| VOD\_SERIES\_ID      | number | The ID of the Series (Show) this Season is part of                  |

### Series Catalog Report&#x20;

A content catalog of VOD series (show)

| Field            | Type   | Description                      |
| ---------------- | ------ | -------------------------------- |
| SERIES\_ID       | number | The ID of the Series in Vesper   |
| DVE\_SERIES\_ID  | number | The ID of the Series in DVE.     |
| SERIES\_LANGUAGE | string | The default locale of the Series |
| SERIES\_TITLE    | string | The title of the Series          |

### Live Viewership Report&#x20;

A list of all live playback sessions that ended within a give 3 day period.&#x20;

| Field          | Type                     | Description                                                                                                                                        |
| -------------- | ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| REALM          | string                   | Denotes the realm that this event relates to. This will be constant for all records in the report.                                                 |
| CUSTOMER\_EXID | string                   | Unique Identifier of the customer on Vesper platform. This ID can also represent a guest user, a user that has not yet registered for the service. |
| SESSION\_START | string, ISO8601 datetime | Date/time that the playback session started                                                                                                        |
| SESSION\_END   | string, ISO8601 datetime | Date/time that the playback session ended                                                                                                          |
| EVENT          | number                   | The ID if the Live Event                                                                                                                           |
| PARTITION      | string                   | List of partition key:value pairs associated with the customer triggering this playback session.                                                   |
| CITY           | string                   | City of the user for this playback session derived though a geo-lookup on the originating IP address.                                              |
| COUNTRY        | string                   | Country of the user for this playback session derived though a geo-lookup on the originating IP address.                                           |
| DEVICE         | string                   | Device type of the playback session as defined by the x-api-key HTTP header sent in the request.                                                   |
| GUEST          | boolean                  | Denotes whether user for this playback session was a guest user.                                                                                   |

### VOD Viewership Report&#x20;

A list of all VOD playback sessions that ended within a given 3 day period.&#x20;

| Field          | Type                     | Description                                                                                                                                        |
| -------------- | ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| REALM          | string                   | Denotes the realm that this event relates to. This will be constant for all records in the report.                                                 |
| CUSTOMER\_EXID | string                   | Unique Identifier of the customer on Vesper platform. This ID can also represent a guest user, a user that has not yet registered for the service. |
| SESSION\_START | string, ISO8601 datetime | Date/time that the playback session started                                                                                                        |
| SESSION\_END   | string, ISO8601 datetime | Date/time that the playback session ended                                                                                                          |
| VOD            | number                   | The ID if the VOD                                                                                                                                  |
| PARTITION      | string                   | List of partition key:value pairs associated with the customer triggering this playback session.                                                   |
| CITY           | string                   | City of the user for this playback session derived though a geo-lookup on the originating IP address.                                              |
| COUNTRY        | string                   | Country of the user for this playback session derived though a geo-lookup on the originating IP address.                                           |
| DEVICE         | string                   | Device type of the playback session as defined by the x-api-key HTTP header sent in the request.                                                   |
| GUEST          | boolean                  | Denotes whether user for this playback session was a guest user.                                                                                   |

### Cohorts Report&#x20;

A report of all cohorts assigned to users at the time report is generated for a given realm.&#x20;

| Field          | Type                     | Description                                                                                                       |
| -------------- | ------------------------ | ----------------------------------------------------------------------------------------------------------------- |
| EMAIL          | string                   | Email address (Username) that the customer uses to log in to Vesper platform                                      |
| USER           | string                   | Unique Identifier of the customer on Vesper platform.                                                             |
| COHORT\_SOURCE | string                   | The source of the cohort, this has a one-to-one mapping to the SQS queue and credentials provided to add cohorts. |
| COHORT\_NAME   | string                   | The name of the cohort                                                                                            |
| COHORT\_VALUE  | string                   | The value of the cohort (optional)                                                                                |
| CREATED\_AT    | string, ISO8601 datetime | The timestamp that the cohort was added to the user.                                                              |

### Gifting Report

The Gift report represents data about purchases of Gift and their redemption.

**Frequency**: Every 6 hours - 0:00, 6:00, 12:00, 18:00 UTC

| Field                       | Type                     | Description                                                                           |
| --------------------------- | ------------------------ | ------------------------------------------------------------------------------------- |
| id                          | int8                     | Compound identifier of for a gift purchase event                                      |
| date\_of\_order             | string, ISO8601 datetime | Date and time of gift purchase                                                        |
| gift\_purchase\_id          | string                   | Unique identifier for a gift purchase                                                 |
| purchase\_country           | string                   | Country where a purchase of a gift occurred                                           |
| purchase\_town              | string                   | Town where a purchase of a gift occurred                                              |
| purchase\_device\_type      | string                   | Device used to purchase a gift                                                        |
| payment\_provider           | string                   | Payment provider used to purchase a gift                                              |
| payment\_detail\_id         | string                   | Unique identifier for a gift purchase payment                                         |
| gifter\_exid                | string                   | Exid of a gift purchaser                                                              |
| gifter\_email               | string                   | The email address of gift purchaser.                                                  |
| gifter\_price\_without\_tax | number                   | Price of a gift without tax                                                           |
| gifter\_tax                 | number                   | Tax                                                                                   |
| gifter\_currency\_code      | string                   | Currency in which gift purchase occurred                                              |
| gifter\_price\_total        | number                   | Price of a git including tax                                                          |
| recipient\_exid             | string                   | Identifier for the gift recipient                                                     |
| recipient\_email            | string                   | The email address of the recipient of the gift.                                       |
| licence\_source             | string                   | Technical source of the licence                                                       |
| licence\_rid                | number                   | Unique identifier for the licence                                                     |
| licence\_sku                | string                   | Licence SKU                                                                           |
| licence\_name               | string                   | Name of the licence                                                                   |
| licence\_type               | string                   | <p>Type of subscription:</p><ul><li>SUBSCRIPTION</li><li>PPV</li><li>RENTAL</li></ul> |
| licence\_tax                | number                   | Tax                                                                                   |
| licence\_base\_price        | number                   | Price of the licence without tax                                                      |
| licence\_price              | number                   | Price of the licence with tax                                                         |
| gift\_currency\_code        | string                   | Currency in which redemption of the licence occurred                                  |
| gift\_periods               | number                   | Number of periods are gifted (2 monthly → will be 2 months)                           |
| redemption\_exid            | string                   | Exid of a user who redeemed a gift                                                    |
| redemption\_email           | string                   | The email address of the user who redeemed the gift                                   |
| redemption\_date            | string, ISO8601 datetime | Date and time of gift redemption                                                      |
| redemption\_country\_code   | string                   | Country in which gift redemption occurred                                             |
| redemption\_device\_type    | string                   | Device used to redeem a gift                                                          |
| redemption\_code            | string                   | Code used to redeem a gift                                                            |

* There is always a gifter who purchases a Gift and sends it to one or more giftees. Depending on the structure of a Gift, it can be redeemed one or more times. If a Gift is redeemed more than one time, there is more than one row of data corresponding to purchase of this particular Gift and its redemptions.
* There are certain cases, where Gift purchase data is missing, while Gift redemption data is present. This is due to a fact that collection of information in such cases started after the purchase of a Gift occurred.

Notes:

<br>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/back-office/analytics-1/reports.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
