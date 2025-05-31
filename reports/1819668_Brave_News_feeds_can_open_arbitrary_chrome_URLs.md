# Brave News feeds can open arbitrary chrome: URLs

## Report Details
- **Report ID**: 1819668
- **URL**: https://hackerone.com/reports/1819668
- **State**: Closed
- **Severity**: high
- **Submitted**: 2023-01-01T08:55:37.266Z
- **Disclosed**: 2023-06-22T05:50:08.953Z

## Reporter
- **Username**: nishimunea
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: brave

## Vulnerability Information
## Summary:
URL link in Brave News feeds can open arbitrary chrome: URLs.
This behavior can be exploited as a way to bypass SOP and gain access to privileged URLs.

## Products affected: 

 * 1.46.144 Chromium: 108.0.5359.128 (Official Build) （x86_64）

## Steps To Reproduce:

 * Open new tab and click customize button
 * Follow https://csrf.jp/brave/rss_chrome.php as a RSS feed of Brave News
 * Reload the tab
 * RSS feeed that name is "Access chrome: URLs" is shown on Brave News
 * Click the feed
 * `chrome://settings/resetProfileSettings?origin=userclick` is opened on the tab

## Supporting Material/References:

  * See the demonstration movie I attached

## Impact

Bypass SOP and gain access to privileged URLs.

## Attachments
- open_chrome_urls_from_brave_news_feed.mov
