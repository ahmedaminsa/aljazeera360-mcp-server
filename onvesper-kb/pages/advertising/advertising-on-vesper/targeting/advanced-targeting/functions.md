> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/advertising/advertising-on-vesper/targeting/advanced-targeting/functions.md).

# Functions

The most advanced configuration options available to Vesper customers utilise functions within your VAST tag to introduce simple logic statements that extend existing [Advertisement Macros](/platform-knowledge-base/advertising/advertising-on-vesper/targeting/advanced-targeting/advertisement-macros.md) to generate entirely new outputs.

{% hint style="warning" %}
**If you wish to test out using Functions in your VAST tag, we always recommend contacting a Technical Account Manager to discuss your use case.**
{% endhint %}

#### Encode

The most used function which you will have seen on [Advanced targeting](/platform-knowledge-base/advertising/advertising-on-vesper/targeting/advanced-targeting.md) is `{{#`**`url_enc`**`}}key=value&anotherkey=value{{/`**`url_enc`**`}}` this function is useful for Google Ad Manager's cust\_params key, where additional keys must be passed to Google as [URL-encoded](https://www.w3schools.com/tags/ref_urlencode.ASP) values. The **url\_enc** function achieves this for you, replacing & and = with %26 and %3D, keeping your custom parameters human readable.

## Deltatre Supported Functions

These functions have been tested and utilised with existing customers and are available on this documentation for re-use as the use case may be common. Please contact your Technical Account Manager before implementing these functions to ensure your platform configuration is compatible with them.

### "Subscriber Level"

This function provides a key-value pair that simplifies defining a customer's "level" within the platform. It is useful for Vesper configurations that allow customers to watch some content as an unregistered guest, different content as a registered free user, and then all content as user who has paid for one of your licences on the Vesper platform. It combines the guest and subscriber level macros.

{% code overflow="wrap" %}

```handlebars
&cust_params={{#url_enc}}subscriberLevel={{#if user.jwt.isGuest}}guest_user{{else eq user.purchasedEntitlement 'NOT_PURCHASED'}}free_user{{else}}paid_user{{/if}}{{/url_enc}}
```

{% endcode %}

**Key** = subscriberLevel&#x20;

**Value** = guest\_user | free\_user | paid\_user

### "Advertising Tier"

This function allows you to convert the numeric licence RIDs into a friendly string representation that your SSP may be expecting. For example, if you have 3 licences that can be purchased to offer reduced advertising, you can use this contains-then function to simply return "reduced\_ads" for those three, then "full\_ads" for all other licences.

{% code overflow="wrap" %}

```handlebars
&cust_params={{#url_enc}}{{contains-then user.licenceIds '1234=reduced_ads' '4567=reduced_ads' '8910=reduced_ads' 'else=full_ads'}}{{/url_enc}}
```

{% endcode %}

**Key** = adsTier&#x20;

**Value** = reduced\_ads | full\_ads

## Full list of Operators

A full list of the available functions and operators is available below. Endeavor Streaming cannot provide support for debugging functions implemented by our customers.

### Logical Operators

| **Logical Operator**                                                                          | **Description**                                                                                                                                                                                                                                                               |
| --------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `{{#myProperty}}Hello{{myProperty}{{/myProperty}}`                                            | Prints `Hello + myProperty` value only if it exists                                                                                                                                                                                                                           |
| `{{^notMyProperty}}Not present{{/notMyProperty}}`                                             | Prints `Not Present` if property is not present                                                                                                                                                                                                                               |
| `{{#if (greeting 'bye')}}Tchau{{else if (eq object.greeting 'hello')}}Olá{{/if}}`             | If else statements                                                                                                                                                                                                                                                            |
| `{{#eq object.id 1}}...`                                                                      | Equals                                                                                                                                                                                                                                                                        |
| `{{#neq object.id 1}}...`                                                                     | Not equals                                                                                                                                                                                                                                                                    |
| `{{#gt object.id 10}}...`                                                                     | Greater than                                                                                                                                                                                                                                                                  |
| `{{#gte object.id 10}}...`                                                                    | Equals or grater than                                                                                                                                                                                                                                                         |
| `{{#lt object.id 10}}...`                                                                     | Less than                                                                                                                                                                                                                                                                     |
| `{{#lte object.id 10}}...`                                                                    | Equals or less than                                                                                                                                                                                                                                                           |
| `{{#and object.accepts object.wrapperAccepts}}Yes{{else}}No{{/and}}`                          | And both booleans are true                                                                                                                                                                                                                                                    |
| `{{#or object.absent object.accepts}}Present{{else}}Absent{{/or}}`                            | Or one of the expressions are true                                                                                                                                                                                                                                            |
| `{{#not object.accepts}}Not accepted{{else}}Accepted{{/not}}`                                 | Not true at all                                                                                                                                                                                                                                                               |
| `{{numberFormat object.cost format="999,00"}}`                                                | Number is formatted                                                                                                                                                                                                                                                           |
| `{{dateFormat object.date format="dd/MM/yyyy"}}`                                              | Date is formatted                                                                                                                                                                                                                                                             |
| `{{dateFormat object.instant format="yyyy/MM/dd-HH:mm:ss"}}`                                  | Instant is formatted                                                                                                                                                                                                                                                          |
| `{{#with user.jwt.location}}{{#eq city 'London'}}expensive-ads{{/eq}}{{/with}}`               | Creates a local starting point for other variables inside the block.                                                                                                                                                                                                          |
| `{{#each object.licencesMap as \|e\|}}{{#if (eq @key '1')}}Contains {{@key}}{{/if}}{{/each}}` | Iterates over a Collection or Map using e as the object. You can also use @Key and @Value as helpers.                                                                                                                                                                         |
| `{{#object.licenceIds}}{{.}}{{#unless @last}},{{/unless}}{{/object.licenceIds}}`              | <p>1 - Prints all licence ids comma separated.</p><p>2 - Will print the current value with <code>{{.}}</code> but can be also <code>{{this}}</code>.</p><p>3 - Will skip adding a comma <code>#unless</code> is the <code>@last</code> (or <code>@first</code>) iteration</p> |

More details: [![](https://handlebarsjs.com/images/favicon.png)Block Helpers | Handlebars](https://handlebarsjs.com/guide/block-helpers.html)

### String Operators

| **String Operator**                                                             | **Description**                                                                                                                                                                                        |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `{{capitalizeFirst value}}`                                                     | If value is "handlebars.java", the output will be "Handlebars.java".                                                                                                                                   |
| `{{cut value [" "]}}`                                                           | If value is "String with spaces", the output will be "Stringwithspaces".                                                                                                                               |
| `{{defaultIfEmpty value ["nothing"] }}`                                         | If value is "" (the empty string), the output will be nothing.                                                                                                                                         |
| `{{join value " // " [prefix=""] [suffix=""]}}`                                 | If value is the list \['a', 'b', 'c'], the output will be the string "a // b // c".                                                                                                                    |
| `{{substring value 0 10 }}`                                                     | If value is Handlebars.java, the output will be "Handlebars".                                                                                                                                          |
| `{{lower value}}`                                                               | If value is 'Still MAD At Yoko', the output will be 'still mad at yoko'                                                                                                                                |
| `{{upper value}}`                                                               | If value is 'Hello', the output will be 'HELLO'.                                                                                                                                                       |
| `{{stripTags value}}`                                                           | Strips all \[X]HTML tags.                                                                                                                                                                              |
| `{{now ["format"] [tz=timeZone\|timeZoneId]}}`                                  | Prints the current datetime (formatted optionally)                                                                                                                                                     |
| `{{contains-then value 'example1=option1' 'example2=option2' 'else=option3' }}` | Check if value contains any of the defined possible string values (e.g. example1 or example2) and output the value defined (e.g. option1 or option2). *Optional:* Otherwise output the defined "else". |

More details here: <https://github.com/jknack/handlebars.java/blob/master/handlebars/src/main/java/com/github/jknack/handlebars/helper/StringHelpers.java>

### Hashing Operators

| <p>Hashing Operator<br></p>              | <p>Description<br></p>                                                                                |
| ---------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| <p><code>{{md5 value}}</code><br></p>    | <p>Applies the MD5 hashing function to the given parameter and returns the hashed value.<br></p>      |
| <p><code>{{sha1 value}}</code><br></p>   | <p>Applies the SHA1 hashing function to the given parameter and returns the hashed value.<br></p>     |
| <p><code>{{sha256 value}}</code><br></p> | <p>Applies the SHA256 hashing function to the given parameter and returns the hashed value.<br></p>   |
| <p><code>{{sha512 value}}</code><br></p> | <p>Applies the SHA512 hashing function to the given parameter and returns the hashed value.<br></p>   |
| <p><code>{{base64 value}}</code><br></p> | <p>Applies the Base64 encoding function to the given parameter and returns the encoded value.<br></p> |


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/advertising/advertising-on-vesper/targeting/advanced-targeting/functions.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
