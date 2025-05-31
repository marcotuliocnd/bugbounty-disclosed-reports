# Persistent user tracking is possible using window.caches, by avoiding Brave Shields

## Report Details
- **Report ID**: 1668815
- **URL**: https://hackerone.com/reports/1668815
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-08-14T10:27:27.625Z
- **Disclosed**: 2023-06-22T05:50:50.921Z

## Reporter
- **Username**: nishimunea
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: brave

## Vulnerability Information
## Summary:

The recent version of iOS 15 introduced `window.caches` in WKWebView. It provides a persistent cache for web pages, and is also potentially usable for user tracking.
The current [CookieControl.js](https://github.com/brave/brave-ios/blob/development/Client/Frontend/UserContent/UserScripts/CookieControl.js) disables cookie, localStorage and sessionStorage, but it doesn't disable `window.caches`, so it allows client-side user tracking by `window.caches` even when cookie brocker is enabled.

## Products affected: 

* Brave for iOS Version 1.41.1 (22.7.27.20)
* iPhone 8 with iOS 15.6

## Steps To Reproduce:

* Enable Brave Shields and block all cookies
* Visit https://csrf.jp/2022/caches.php
* Push "Set Tracking ID" button, then your tracking ID is set to window.caches
* Push "Get Tracking ID" button, then you can confirm your tracking ID that was set above
* Close your browser and visit the above page again
* Push "Get Tracking ID" button, then you can see your tracking ID again

## Supporting Material/References:

  * Attached is a movie file that demonstrate the above steps to reproduce.

## Impact

As witten in summary, client-side user tracking by `window.caches` is possible even when cookie brocker is enabled.

## Attachments
- track_with_caches.mp4
