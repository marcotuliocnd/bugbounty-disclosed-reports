# XSS on Brave Today through custom RSS feed

## Report Details
- **Report ID**: 1184379
- **URL**: https://hackerone.com/reports/1184379
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-05-04T23:26:23.616Z
- **Disclosed**: 2023-06-22T05:51:53.264Z

## Reporter
- **Username**: nishimunea
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: brave

## Vulnerability Information
## Summary:

Two months ago, the [custom RSS feed feature](https://github.com/brave/brave-ios/pull/3317) was introduced to Brave Today on Brave iOS.

This feature allows to add any RSS feed to Brave Today, and the registered feed entries are shown in a tab with a hyperlink to the original article URL.
Then, Brave iOS doesn't restrict the URL scheme of the original article link, which can cause XSS weakness through `javascript:` URL.

Here is a demonstration RSS feed of this attack.
https://csrf.jp/brave/rss.php

This RSS feed contains `javascript:alert(document.domain)` in an entry tag like this.
```
<entry>
  <title>XSS</title>
  <link rel="alternate" type="text/html" href="javascript:alert(document.domain)" />
  <content type="html"><![CDATA[<img src="https://csrf.jp/test.png">]]></content>
</entry>
```
When user taps the entry on Brave Today, an alert dialog is shown on `http://localhost:65XX`.

## Products affected: 

 * Brave iOS current Nightly build

## Steps To Reproduce:

 * Open "Settings"
 * Tap "Brave Today" in Settings menu
 * Tap "Add Source"
 * Type "https://csrf.jp/brave/rss.php" and tap "Search"
 * RSS feed, that name is PoC, is found, then tap "Add"
 * Enable PoC feed
 * Close the Settings menu and open a new tab
 * Enable Brave Today, then you can find an article entry that name is "XSS"
 * Tap the article, then an alert dialog is shown

## Supporting Material/References:

  * See attached movie file for the demonstration

## Impact

As written in summary, XSS is possible on `http://localhost:65XX`.
Note that `http://localhost:65XX` should be considered as a privileged domain that hosts Brave's internal features such as reader-view, error-pages and so on.

## Attachments
- xss_on_localhost_through_brave_today_rss.mov
