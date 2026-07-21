> For the complete documentation index, see [llms.txt](https://docs.onvesper.com/platform-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.onvesper.com/platform-knowledge-base/consumer-experience/theming-and-customisation/iconography.md).

# Iconography

There are multiple types of iconography in the Vesper application suite.

1. Application icons and branding set when apps are built
2. Custom icons in [Menu items](/platform-knowledge-base/back-office/administration/menu-items.md) shown in the menus and home pages
3. Other iconography used for other CTAs (buttons) throughout the apps

Starting in Q4 2025, Vesper is introducing the capability to customise the iconography used for the last item in the list: CTA iconography can now be customised according to your own branding or preferences.

Making these changes requires working with your account manager, see below for details on the specs you will need to adhere to, and the options available.

{% hint style="info" %}
Note that mobile applications require a re-build whenever iconography controlled by the icon store is updated. Work with your account manager to schedule that re-build. In some select/extreme circumstances it may be possible to submit an OTA patch if there is an urgent need.
{% endhint %}

### Specifications

If you wish to customise any icons on the platform, you will need to provide multiple icons to account for state, and device.

For each icon you will need to provide:

**Description**: The Name of the icon, plus any translations in your supported languages&#x20;

**Alt Text**: Accessibility labels / alt text for icons, plus any translations in your supported languages

**Recommended Size**: 28px x 28px recommended

Then, a set of assets for each platform, as defined below)

<table><thead><tr><th>Web (SVG format)</th><th width="174.40625">Mobile (SVG format)</th><th>TV (SVG format***)</th><th>Roku (PNG format)</th></tr></thead><tbody><tr><td>Normal state</td><td>Normal state</td><td>Normal state</td><td>Normal state</td></tr><tr><td>Hover state</td><td>-</td><td>Hover state**</td><td>Hover state**</td></tr><tr><td>Selected state*</td><td>Selected state*</td><td>Selected state*</td><td>Selected state*</td></tr></tbody></table>

\* Selected state only applies to certain icons, see the list below

\*\* Hover state refers to the "focused" state on TV/Roku

\*\*\* Ensure there is no styling or CSS in vectors/SVGs provided for TV, as these cannot be rendered

### Iconography options

The following list explains each icon which is available for customisation and it's purpose in the Vesper apps

With the exception of the numbered cards icons for Top 10 (see specs in the table below) - all icons are recommended size of 28x28px

You do not need to provide all of these icons if you only wish to update one! If you chose not to customise an icon, your Vesper realm will continue to receive the default icons.

{% hint style="info" %}
If there's an icon you want to customise that is not on this list, let your Account manager know. The Vesper product team plans to expand the available icons in future iterations
{% endhint %}

{% hint style="danger" %}
At time of publishing, icon store is in **BETA.** Some of the icons below may not be available on all platforms or may not yet have been made available for customisation. If you're interested in changing a particular icon, enquire and test with your account manager.
{% endhint %}

<table data-full-width="true"><thead><tr><th width="120.84375">Icon</th><th width="111.8203125">Default Description</th><th width="195.03515625">Purpose</th><th width="146.17578125">Selected State?</th><th>Platforms</th><th>Example</th></tr></thead><tbody><tr><td>Account</td><td>Account</td><td>Shown on menu</td><td>N</td><td>Web</td><td><div><figure><img src="/files/60NIIDsI4mpQlbECGMQd" alt=""><figcaption></figcaption></figure></div></td></tr><tr><td>AddToWatchlist</td><td>Add to watchlist</td><td>Allows adding to watchlist</td><td>N</td><td>Mobile, TV, Web</td><td><div><figure><img src="/files/sUQoDkXUVqdocPA5DJ8o" alt=""><figcaption></figcaption></figure></div></td></tr><tr><td>AddedToWatchlist</td><td>Remove from watchlist</td><td>Allows removing from watchlist</td><td>N</td><td>Mobile, TV, Web</td><td><div><figure><img src="/files/99Fn9QPk3QE2XM8IUzOJ" alt=""><figcaption></figcaption></figure></div></td></tr><tr><td>Apple</td><td>Continue with Apple</td><td>Vesper SSO sign in with Apple</td><td>N</td><td>Web</td><td><div><figure><img src="/files/KAK3QojDsNiB4X8tGdRE" alt=""><figcaption></figcaption></figure></div></td></tr><tr><td>ArrowDown</td><td>Down</td><td>Used to indicate a dropdown of expandable information</td><td>?</td><td>Mobile</td><td><div><figure><img src="/files/4xmyvVxvHdTKvl7NqNWm" alt=""><figcaption></figcaption></figure></div></td></tr><tr><td>Browse</td><td>On Demand</td><td>The browse section default icon in menus</td><td>?</td><td></td><td><div><figure><img src="/files/77Bh3NoAcbEEZt8kTlZf" alt=""><figcaption></figcaption></figure></div></td></tr><tr><td>Burger</td><td>Burger</td><td>Menu icon used for "burger" menu</td><td>?</td><td>Mobile, Web</td><td><div><figure><img src="/files/E3AJ7P93DDXhG4Uxxe7V" alt=""><figcaption></figcaption></figure></div></td></tr><tr><td>Calendar</td><td>Calendar</td><td>Icon used when users want to add live events to their calendar on mobile app</td><td></td><td></td><td><div><figure><img src="/files/oiseUpXSJlpsbLsqOpYS" alt=""><figcaption></figcaption></figure></div></td></tr><tr><td>Close</td><td>Close</td><td>Close/dismiss icon to exit states or popups</td><td>N</td><td>Mobile, Web, TV</td><td><div><figure><img src="/files/aYtTElWRSIj7Be4P9zIv" alt=""><figcaption></figcaption></figure></div></td></tr><tr><td>CardPosition_X_Default*</td><td>Card position X - Default card</td><td>16:9 representation of the numbers for top 10 feature<br><br>105x200px recommended</td><td>N</td><td></td><td><div><figure><img src="/files/OlGf6tlKtX7v8rko2vf9" alt=""><figcaption></figcaption></figure></div></td></tr><tr><td>CardPosition_X_Poster*</td><td>Card position X - Poster card</td><td>Poster representation of the numbers for top 10 feature<br><br>160x360px recommended</td><td>N</td><td></td><td><div><figure><img src="/files/Wk6DPQFiSlTYoZsBhDCt" alt=""><figcaption></figcaption></figure></div></td></tr><tr><td>CheckCircle</td><td>Checkbox rounded filled</td><td>Used in managing downloaded content on mobile app</td><td>Y</td><td></td><td><div><figure><img src="/files/xiR0c2Bbivd6jKVvrjTj" alt=""><figcaption></figcaption></figure></div></td></tr><tr><td>Email</td><td>Continue with Email</td><td>Vesper SSO: when registering with an e-mail address</td><td>N</td><td></td><td><div><figure><img src="/files/P9XVPOJOI5cQekybOGcv" alt=""><figcaption></figcaption></figure></div></td></tr><tr><td>Eye</td><td>Reveal</td><td>Show/hide password</td><td>?</td><td></td><td><div><figure><img src="/files/VGrJGuvdrPZ7nh6mvNTc" alt=""><figcaption></figcaption></figure></div></td></tr><tr><td>Filter</td><td>Filter</td><td>Shown on Vesper Search page</td><td>?</td><td></td><td><div><figure><img src="/files/lP2d7BjOhXV3EOgiNKWY" alt=""><figcaption></figcaption></figure></div></td></tr><tr><td>Home</td><td>Home</td><td>Default Home icon on menus</td><td>?</td><td></td><td><div><figure><img src="/files/lRBu83qOIgR4CBgAJllH" alt=""><figcaption></figcaption></figure></div></td></tr><tr><td>Lock</td><td>Lock</td><td>Icon shown over content which is locked behind paywalls</td><td></td><td></td><td>Not yet available</td></tr><tr><td>Play</td><td>Play</td><td>Play icon used on CTAs for interstitial pages</td><td>N</td><td>Mobile, TV, Web</td><td><div><figure><img src="/files/m0ZeaL49exYAC3RK1WSl" alt=""><figcaption></figcaption></figure></div></td></tr><tr><td>Restart</td><td>Restart</td><td>Watch from start CTA for interstitial pages</td><td>N</td><td></td><td><div><figure><img src="/files/WY7VoJhNrVjvKYv9wMg8" alt=""><figcaption></figcaption></figure></div></td></tr><tr><td>Search</td><td>Search</td><td>Default search icon</td><td>N</td><td></td><td><div><figure><img src="/files/Mm5atHC4AWGBGloFCe9F" alt=""><figcaption></figcaption></figure></div></td></tr><tr><td>Sort</td><td>Sort</td><td>Shown on Vesper Search page</td><td></td><td></td><td><div><figure><img src="/files/YHKVGsSRxFhL8qhFF6QO" alt=""><figcaption></figcaption></figure></div></td></tr><tr><td>Share</td><td>Share</td><td>Share CTA for interstitial pages</td><td>N</td><td></td><td><div><figure><img src="/files/lSFQcLZmxBVNLy7agu1X" alt=""><figcaption></figcaption></figure></div></td></tr></tbody></table>

\*If customising the top 10 feature numbers, you will need to provide all numbers, 1-10

Tip: you might want to switch this documentation space/page to "dark mode" at the bottom right of the page to better see the default icons above!


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.onvesper.com/platform-knowledge-base/consumer-experience/theming-and-customisation/iconography.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
