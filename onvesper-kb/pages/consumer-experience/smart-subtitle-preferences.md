> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/consumer-experience/smart-subtitle-preferences.md).

# Smart Subtitle Preferences

## What are Smart Subtitle Preferences?

By default on Vesper, viewers set one subtitle preference that applies everywhere, regardless of what language the content's audio is in. With Smart Subtitle Preferences, the platform instead remembers a separate subtitle choice for each audio language a viewer watches in.

The original system introduces friction to the experience for content catalogues that have content with multiple language audio tracks, as users will be forced to change subtitles settings during playback e.g. a user selects "English US" as their subtitles preference and prefer this for watching Spanish audio content, but need to manually turn subtitles off for English audio content during playback every time.

This is remedied by Smart Subtitle Preferences. For example, a bilingual viewer could have subtitles automatically appear in Spanish whenever they watch Spanish-language content, while English-language content plays with subtitles off without the viewer ever having to set this up manually.

In summary your viewers get a more personalized, less repetitive subtitle experience: fewer manual adjustments, subtitles that consistently match their habits for each language, and a seamless experience whether they're moving between devices or between on-demand and live content.

## How does it work?

<figure><img src="/files/o39ovg1ZQuQ0o4VKosHB" alt=""><figcaption></figcaption></figure>

For each [Profiles](/platform-knowledge-base/consumer-experience/profiles.md) the Vesper platform maintains a ranked list of subtitle preferences keyed by audio language (please note: if your realm does not utilise profiles today, this is just the default account experience). The player consults the ranking for the current audio language when playback starts.

{% hint style="success" %}
To enable Smart Subtitle Preferences, please reach out to your Account Manager
{% endhint %}

| <h4><em><strong>Mode</strong></em></h4> | <h4><em><strong>What it means for end users</strong></em></h4>                                                                                                                    |
| --------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Disabled** (default)                  | Classic single subtitle preference. The user sets one preferred subtitle language in Account Preferences and/or the player; it applies across all content languages. No learning. |
| **Enabled**                             | Smarter Subtitle Preferences is on for everyone on your realm. No user action required; the platform learns and applies automatically.                                            |
| **User opt-in required**                | Smarter Subtitle Preferences is available, but each profile chooses to turn it on (or off) via a toggle in Account Preferences.                                                   |

### **Learning from behaviour** <a href="#id-2.2-learning-from-behaviour" id="id-2.2-learning-from-behaviour"></a>

* A **manual save** in Account Preferences applies immediately as rank #1 for the relevant audio language key.
* When a user changes the subtitle track during playback, that choice silently updates the ranking for that audio language. Frequent choices rise to the top and, over time, override earlier manual saves.
* A preference is only stored when it results from a user interaction with the player. If the system could not have shown a subtitle (e.g. the preferred language isn't available in the asset), no preference is recorded, because the user took no real decision.
  * For example, a viewer's stored preference is Arabic, and their display language is also Arabic. They land on a title with English audio, and no Arabic subtitles are available for that title. Because Arabic subtitles simply couldn't have been shown (they don't exist in that asset), the viewer never had a genuine choice to make; so their preferences stay exactly as they were. The system does not silently downgrade or overwrite their Arabic preference just because it wasn't available this one time.

### **How a selection re-ranks the list**

When the user picks a subtitle, the selected track moves above the first preference in the stored list that is present in the current asset for the currently playing audio language. For example:

*Stored preference*: `Spanish subs → German subs → English subs`; asset has `German subs, English subs`. User selects **English subs** → reference is **German** (first stored preference available in the asset), so English is inserted before it: `Spanish → English → German`.

*Stored preference*: `Spanish subs → French subs`; asset has only `English` audio language. User selects **English** **subs**→ none of the stored preferences exist in the asset, so English is appended: `Spanish → French → English`.

### **Auto-selection at playback start**

On playback start, for the current audio language, the player walks the stored preferences in rank order and selects the first preferred subtitle track that exists in the stream. If none of the preferred subtitles are present, it falls back to Off. Viewers are never shown something they did not choose.

### **Audio switching mid-session**

In a multilingual session, when the user switches audio language, the subtitle preference for the new audio language is automatically applied as part of the switch.

### **Subtitle variants are independent**

[Subtitle Variants](/platform-knowledge-base/dve/video/subtitles/subtitle-variants.md) — e.g. English, English CC, English SDH — are ranked separately.

* For audio languages, regional variants are treated as the same language: English UK (en\_UK) and English US (en\_US) audio both map to "English".
* For subtitles, regional variants are stored and ranked separately: English UK (en\_UK) and English US (en\_US) subtitles are distinct.
* A [Profiles](/platform-knowledge-base/consumer-experience/profiles.md) can hold a preference for both a specific variant (English UK) and a general language (English).

### **"Off" and unselect logic**

It's worth highlighting that `off` is a valid subtitle reference that can be included in the ranking. Where `off` is selected for a given audio language it supersedes the currently showing subtitle. Important note: any subtitles that are not available in that asset are not affected.

Example:

* VOD asset has `en_US` and `en_USCC` subtitles with Spanish audio.
* Profile has a Spanish audio subtitle ranking of `es_ES`->`en_US`->`en_USCC`&#x20;
* Playback begins, en\_US is selected (first available ranked subtitle on the asset)
* User selects `off`&#x20;
* Ranking for Spanish audio updated to `es_ES` ->`off`->`en_US`->`en_USCC`&#x20;

`es_ES` ranking is unaffected for Spanish audio as it was not available in the VOD asset where `off` was added to the ranking, which also effectively Unselects en\_US for future viewing sessions on Spanish audio. If this is repeated on a VOD asset with `es_ES` subtitles and Spanish audio, `off` becomes the default behaviour as the top ranked subtitle preference.

### FAQs & More Detail

#### **VOD and Live**

Behaviour is consistent across both VOD and live content. For live streams that expose only base language codes (e.g. `eng`), auto-selection matches by base language; a preference stored as `en_US` from VOD will match an `eng` live subtitle track when no region-specific code is available, while still respecting unselect logic.

#### **TV system subtitle setting at OS level (e.g. Samsung)** <a href="#id-2.10-tv-system-subtitle-setting-e.g.-samsung" id="id-2.10-tv-system-subtitle-setting-e.g.-samsung"></a>

On TV platforms that expose a device-level subtitle setting:

* If the system setting is **On**, the player still follows the profile's stored preference order for the current audio language. If there is no stored preference, or a preference exists but no matching track is in the stream, the result is **Off** regardless of the TV setting.
* If the system setting is **Off**, normal preference logic applies (stored preference if present, otherwise Off).

#### **Cross device syncing**

Because preferences are tied to the viewer's [Profiles](/platform-knowledge-base/consumer-experience/profiles.md) rather than a single device, a choice made while watching on mobile carries over automatically to smart TVs, web, and other supported devices.

#### Forced subtitles

Forced subtitles are not affected by ranking nor do they affect rankings. They are always displayed for any audio language that they are configured for.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/consumer-experience/smart-subtitle-preferences.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
