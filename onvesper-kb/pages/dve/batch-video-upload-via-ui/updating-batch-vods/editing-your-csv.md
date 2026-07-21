> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/dve/batch-video-upload-via-ui/updating-batch-vods/editing-your-csv.md).

# Editing your CSV

{% stepper %}
{% step %}
Make the necessary updates to your file

For example, in the image below I have added the tag "BATCH2" to 3 videos, highlighted in yellow.

<figure><img src="/files/PvC02iYWqGXECzS2iVb4" alt=""><figcaption><p>Update CSV</p></figcaption></figure>
{% endstep %}

{% step %}
Delete rows you did not edit

Once you have added the metadata, you can then delete all the other rows that were not edited.

*IMPORTANT: Deleting the rows that you have not changed will NOT impact the videos. However, you need to ensure that it is ONLY rows that are deleted, NOT columns. For example, if I deleted row 3 in the image above (UFC264) because there were no changes made to this content, then when I go to process the changes the video will remain unchanged.*

*If the row is left in, then the file will process this as a change. This isn't a problem since there have been no changes made to this row in the file, however, it might just take longer for your updates to process.*
{% endstep %}

{% step %}
Save the updated file

Save the file with the new updates. Make sure you use **Save as** so that you keep a version of the catalogue before the updates were made, in case of any issues.
{% endstep %}
{% endstepper %}

### Removing optional values

In order to remove existing values from their respective fields, for select attributes, we allow passing the reserved keyword `{remove}` in the cell that corresponds to the value you wish to remove.\
\
The removal of values is only allowed when updating an asset. Using the {remove} keyword will cause a create record to fail

{% hint style="info" %}
Not all optional fields can make use of the `{remove}` feature
{% endhint %}

<table><thead><tr><th width="398">Header value</th><th width="147">Accepts `{remove}`</th><th>Comments</th></tr></thead><tbody><tr><td>id</td><td><span data-gb-custom-inline data-tag="emoji" data-code="274c">❌</span></td><td></td></tr><tr><td>externalId</td><td><span data-gb-custom-inline data-tag="emoji" data-code="1f7e2">🟢</span></td><td></td></tr><tr><td>published</td><td><span data-gb-custom-inline data-tag="emoji" data-code="274c">❌</span></td><td></td></tr><tr><td>delete</td><td><span data-gb-custom-inline data-tag="emoji" data-code="274c">❌</span></td><td></td></tr><tr><td>language</td><td><span data-gb-custom-inline data-tag="emoji" data-code="274c">❌</span></td><td></td></tr><tr><td>s3Region</td><td><span data-gb-custom-inline data-tag="emoji" data-code="274c">❌</span></td><td></td></tr><tr><td>video</td><td><span data-gb-custom-inline data-tag="emoji" data-code="1f7e2">🟢</span></td><td></td></tr><tr><td>video.audioDescriptor</td><td><span data-gb-custom-inline data-tag="emoji" data-code="1f7e2">🟢</span></td><td></td></tr><tr><td>audio</td><td><span data-gb-custom-inline data-tag="emoji" data-code="1f7e2">🟢</span></td><td></td></tr><tr><td>audio.en-GB</td><td><span data-gb-custom-inline data-tag="emoji" data-code="1f7e2">🟢</span></td><td></td></tr><tr><td>presetId</td><td><span data-gb-custom-inline data-tag="emoji" data-code="274c">❌</span></td><td></td></tr><tr><td>dynamicPresetConfig.d2gStrategy</td><td><span data-gb-custom-inline data-tag="emoji" data-code="1f7e2">🟢</span></td><td></td></tr><tr><td>title</td><td><span data-gb-custom-inline data-tag="emoji" data-code="1f7e2">🟢</span></td><td>As long one title for any language is available</td></tr><tr><td>description</td><td><span data-gb-custom-inline data-tag="emoji" data-code="1f7e2">🟢</span></td><td></td></tr><tr><td>longDescription</td><td><span data-gb-custom-inline data-tag="emoji" data-code="1f7e2">🟢</span></td><td></td></tr><tr><td>title.en-GB</td><td><span data-gb-custom-inline data-tag="emoji" data-code="1f7e2">🟢</span></td><td></td></tr><tr><td>description.en-GB</td><td><span data-gb-custom-inline data-tag="emoji" data-code="1f7e2">🟢</span></td><td></td></tr><tr><td>longDescription.en-GB</td><td><span data-gb-custom-inline data-tag="emoji" data-code="1f7e2">🟢</span></td><td></td></tr><tr><td>publishDate</td><td><span data-gb-custom-inline data-tag="emoji" data-code="1f7e2">🟢</span></td><td></td></tr><tr><td>lastPublishedDate</td><td><span data-gb-custom-inline data-tag="emoji" data-code="274c">❌</span></td><td></td></tr><tr><td>expiryDate</td><td><span data-gb-custom-inline data-tag="emoji" data-code="1f7e2">🟢</span></td><td></td></tr><tr><td>subtitle</td><td><span data-gb-custom-inline data-tag="emoji" data-code="1f7e2">🟢</span></td><td></td></tr><tr><td>subtitle.en-GB</td><td><span data-gb-custom-inline data-tag="emoji" data-code="1f7e2">🟢</span></td><td></td></tr><tr><td>tags</td><td><span data-gb-custom-inline data-tag="emoji" data-code="1f7e2">🟢</span></td><td></td></tr><tr><td>typedTags</td><td><span data-gb-custom-inline data-tag="emoji" data-code="1f7e2">🟢</span></td><td></td></tr><tr><td>countryContentRatings</td><td><span data-gb-custom-inline data-tag="emoji" data-code="1f7e2">🟢</span></td><td></td></tr><tr><td>geoBlocking.templateExids</td><td><span data-gb-custom-inline data-tag="emoji" data-code="1f7e2">🟢</span></td><td></td></tr><tr><td>geoBlocking</td><td><span data-gb-custom-inline data-tag="emoji" data-code="1f7e2">🟢</span></td><td>Column with single purpose: to allow the removal of the additionalGeoBlockingTempalte</td></tr><tr><td>geoBlocking.type</td><td><span data-gb-custom-inline data-tag="emoji" data-code="1f7e2">🟢</span></td><td></td></tr><tr><td>geoBlocking.countries</td><td><span data-gb-custom-inline data-tag="emoji" data-code="1f7e2">🟢</span></td><td></td></tr><tr><td>geoBlocking.postalCodes.countryCode</td><td><span data-gb-custom-inline data-tag="emoji" data-code="1f7e2">🟢</span></td><td></td></tr><tr><td>geoBlocking.postalCodes</td><td><span data-gb-custom-inline data-tag="emoji" data-code="1f7e2">🟢</span></td><td></td></tr><tr><td>geoBlocking.postalCodesCsv</td><td><span data-gb-custom-inline data-tag="emoji" data-code="1f7e2">🟢</span></td><td></td></tr><tr><td>countryContentRating.rating.GB</td><td><span data-gb-custom-inline data-tag="emoji" data-code="1f7e2">🟢</span></td><td></td></tr><tr><td>countryContentRating.ratingAuthority.GB</td><td><span data-gb-custom-inline data-tag="emoji" data-code="1f7e2">🟢</span></td><td></td></tr><tr><td>countryContentRating.ratingSystemType.GB</td><td><span data-gb-custom-inline data-tag="emoji" data-code="1f7e2">🟢</span></td><td></td></tr><tr><td>countryContentRating.descriptor.GB.en-GB</td><td><span data-gb-custom-inline data-tag="emoji" data-code="1f7e2">🟢</span></td><td></td></tr><tr><td>thumbnail</td><td><span data-gb-custom-inline data-tag="emoji" data-code="274c">❌</span></td><td></td></tr><tr><td>titleLogo</td><td><span data-gb-custom-inline data-tag="emoji" data-code="1f7e2">🟢</span></td><td></td></tr><tr><td>poster</td><td><span data-gb-custom-inline data-tag="emoji" data-code="1f7e2">🟢</span></td><td></td></tr><tr><td>cover</td><td><span data-gb-custom-inline data-tag="emoji" data-code="1f7e2">🟢</span></td><td></td></tr><tr><td>adInsertion.midRoll</td><td><span data-gb-custom-inline data-tag="emoji" data-code="1f7e2">🟢</span></td><td></td></tr><tr><td>ssaiConfig.providerName</td><td><span data-gb-custom-inline data-tag="emoji" data-code="1f7e2">🟢</span></td><td></td></tr><tr><td>ssaiConfig.parameters</td><td><span data-gb-custom-inline data-tag="emoji" data-code="1f7e2">🟢</span></td><td></td></tr><tr><td>skipMarkers</td><td><span data-gb-custom-inline data-tag="emoji" data-code="1f7e2">🟢</span></td><td></td></tr><tr><td>watermarkExid</td><td><span data-gb-custom-inline data-tag="emoji" data-code="1f7e2">🟢</span></td><td></td></tr><tr><td>useCustomerWatermark</td><td><span data-gb-custom-inline data-tag="emoji" data-code="274c">❌</span></td><td></td></tr><tr><td>annotation</td><td><span data-gb-custom-inline data-tag="emoji" data-code="1f7e2">🟢</span></td><td>Column with single purpose: to allow the removal of all annotations</td></tr><tr><td>annotation.1</td><td><span data-gb-custom-inline data-tag="emoji" data-code="274c">❌</span></td><td></td></tr><tr><td>parentPlaylist</td><td><span data-gb-custom-inline data-tag="emoji" data-code="1f7e2">🟢</span></td><td></td></tr><tr><td>parentSeason</td><td><span data-gb-custom-inline data-tag="emoji" data-code="1f7e2">🟢</span></td><td></td></tr><tr><td>autoTranscription</td><td><span data-gb-custom-inline data-tag="emoji" data-code="274c">❌</span></td><td></td></tr><tr><td>translateSubtitles.sourceLanguage</td><td><span data-gb-custom-inline data-tag="emoji" data-code="274c">❌</span></td><td></td></tr><tr><td>translateSubtitles.targetLanguages</td><td><span data-gb-custom-inline data-tag="emoji" data-code="274c">❌</span></td><td></td></tr><tr><td>translateSubtitles.targetLanguages.en-GB</td><td><span data-gb-custom-inline data-tag="emoji" data-code="274c">❌</span></td><td></td></tr><tr><td>release</td><td><span data-gb-custom-inline data-tag="emoji" data-code="1f7e2">🟢</span></td><td>Column with single purpose: to allow the removal of all releases</td></tr><tr><td>release.date.1</td><td><span data-gb-custom-inline data-tag="emoji" data-code="274c">❌</span></td><td></td></tr><tr><td>release.type.1</td><td><span data-gb-custom-inline data-tag="emoji" data-code="274c">❌</span></td><td></td></tr><tr><td>release.audioLanguageCodes.1</td><td><span data-gb-custom-inline data-tag="emoji" data-code="274c">❌</span></td><td></td></tr><tr><td>release.subtitleLanguageCodes.1</td><td><span data-gb-custom-inline data-tag="emoji" data-code="274c">❌</span></td><td></td></tr><tr><td>release.name.1</td><td><span data-gb-custom-inline data-tag="emoji" data-code="274c">❌</span></td><td></td></tr><tr><td>release.name.en-GB.1</td><td><span data-gb-custom-inline data-tag="emoji" data-code="274c">❌</span></td><td></td></tr><tr><td>release.contentId.1</td><td><span data-gb-custom-inline data-tag="emoji" data-code="274c">❌</span></td><td></td></tr><tr><td>release.countries.1</td><td><span data-gb-custom-inline data-tag="emoji" data-code="274c">❌</span></td><td></td></tr><tr><td>release.subdivisions.1</td><td><span data-gb-custom-inline data-tag="emoji" data-code="274c">❌</span></td><td></td></tr><tr><td>release.externalId.1</td><td><span data-gb-custom-inline data-tag="emoji" data-code="274c">❌</span></td><td></td></tr><tr><td>participant</td><td><span data-gb-custom-inline data-tag="emoji" data-code="1f7e2">🟢</span></td><td>Column with single purpose: to allow the removal of all participants</td></tr><tr><td>participant.group.key.actor.en-GB</td><td><span data-gb-custom-inline data-tag="emoji" data-code="274c">❌</span></td><td></td></tr><tr><td>participant.name.1.en-GB</td><td><span data-gb-custom-inline data-tag="emoji" data-code="274c">❌</span></td><td></td></tr><tr><td>participant.role.1.en-GB</td><td><span data-gb-custom-inline data-tag="emoji" data-code="274c">❌</span></td><td></td></tr><tr><td>participant.group.1</td><td><span data-gb-custom-inline data-tag="emoji" data-code="274c">❌</span></td><td></td></tr><tr><td>participant.image.1.en-GB</td><td><span data-gb-custom-inline data-tag="emoji" data-code="274c">❌</span></td><td></td></tr><tr><td>participant.description.1.en-GB</td><td><span data-gb-custom-inline data-tag="emoji" data-code="274c">❌</span></td><td></td></tr><tr><td>downloadPolicyIds</td><td><span data-gb-custom-inline data-tag="emoji" data-code="1f7e2">🟢</span></td><td></td></tr></tbody></table>

#### Remove localisations <a href="#remove-localisations" id="remove-localisations"></a>

To remove completely a localisations there are two ways:

* set the `{remove}` keyword for `title`, `description`, `longDescription`
* set the `{remove}` keyword only for `title`. In this case also the `description` and `longDescription` will be removed

This logic is applicable also for the `title.<languageCode>`, `description.<languageCode>`, `longDescription.<languageCode>`

#### Remove country content ratings <a href="#remove-country-content-ratings" id="remove-country-content-ratings"></a>

To remove completely a country content rating there are two ways:

* set the `{remove}` keyword for `countryContentRating.rating.<country-code>`, `countryContentRating.ratingAuthority.<country-code>` and `countryContentRating.ratingSystemType.<country-code>`, `countryContentRating.descriptor.<country-code>.<language-code>`
* set the `{remove}` keyword only for `countryContentRating.rating.<country-code>`. In this case also the `countryContentRating.ratingAuthority.<country-code>` and `countryContentRating.ratingSystemType.<country-code>` will be removed

#### Remove additional geo blocking <a href="#remove-additional-geo-blocking" id="remove-additional-geo-blocking"></a>

To remove completely an additional geo blocking template there are two ways:

* set the `{remove}` keyword for `geoBlocking.type`, `geoBlocking.countries`, `geoBlocking.postalCodes.countryCode` and `geoBlocking.postalCodes` or `geoBlocking.postalCodesCsv`
* set the `{remove}` keyword only for `geoBlocking.type`. In this case also the `geoBlocking.countries`, `geoBlocking.postalCodes.countryCode` and `geoBlocking.postalCodes` or `geoBlocking.postalCodesCsv` will be removed

To remove completely the postal code level of the additional geo blocking template there are two ways:

* set the `{remove}` keyword for `geoBlocking.postalCodes.countryCode` and `geoBlocking.postalCodes` or `geoBlocking.postalCodesCsv`
* set the `{remove}` keyword only for `geoBlocking.postalCodes.countryCode`

## Deleting VODs

The same batch process used for updates also lets you remove VODs from your catalogue, using the `delete` column in your CSV.

{% stepper %}
{% step %}
In your downloaded catalogue, find the row(s) for the VOD(s) you want to remove.
{% endstep %}

{% step %}
Set the `delete` column to `true` for each of those rows.

Leave the rest of the row's values as they are — only the `delete` flag is needed to trigger removal.
{% endstep %}

{% step %}
Remove or leave any rows you're not changing

Follow the same guidance as above.
{% endstep %}

{% step %}
Save and re-upload the file

Do this as described in [Re-uploading your changes](/platform-knowledge-base/dve/batch-video-upload-via-ui/updating-batch-vods/re-uploading-your-changes.md)

{% hint style="warning" %}
Deletion is permanent. Double-check the rows you've flagged with `delete: true` before uploading — once a batch containing them is approved, those VODs cannot be recovered.
{% endhint %}

When you reach the Review and Approve step, the summary will show the number of VODs flagged for removal under **Delete**.
{% endstep %}
{% endstepper %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/dve/batch-video-upload-via-ui/updating-batch-vods/editing-your-csv.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
