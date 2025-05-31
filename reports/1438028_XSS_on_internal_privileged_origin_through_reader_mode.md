# XSS on internal: privileged origin through reader mode

## Report Details
- **Report ID**: 1438028
- **URL**: https://hackerone.com/reports/1438028
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-12-30T07:48:37.001Z
- **Disclosed**: 2023-06-22T05:51:13.868Z

## Reporter
- **Username**: nishimunea
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: brave

## Vulnerability Information
## Summary:

Brave iOS has two weaknesses described below. By combining them, XSS can be achieved on the privileged origin `internal://local`.

1. Exposure of uuidKey through REFERER header
Reader mode in Brave has two HTML templates, [Reader.html](https://github.com/brave/brave-ios/blob/development/Client/Frontend/Reader/Reader.html) and [ReaderViewLoading.html](https://github.com/brave/brave-ios/blob/development/Client/Frontend/Reader/ReaderViewLoading.html). The former template defines [<meta name="referrer" content="never">](https://github.com/brave/brave-ios/blob/development/Client/Frontend/Reader/Reader.html#L10) header for preventing referrer leakage, but the latter template [does not](https://github.com/brave/brave-ios/blob/development/Client/Frontend/Reader/ReaderViewLoading.html#L8). Therefore, by opening an external page through `ReaderViewLoading.html`, the `uuidKey` contained in the Reader mode page URL is leaked.

2. XSS in SessionRestoreHandler
SessionRestoreHandler is used to restore a previously used tab, but [it does not validate an URL to be restored](https://github.com/brave/brave-ios/blob/83eb41ac922d7bd18fd311e0a4279e02cdd8e190/Client/Frontend/Browser/SessionRestoreHandler.swift#L34). Therefore, if a javascript: URL is provided, the code is executed on the `internal:` domain.

Note that the first vulnerability is not reproduced on iOS 15 because WKWebView's referrer policy has been changed to hostname only. However, according to [Apple's report in June 2021](https://developer.apple.com/support/app-store/), more than 90% of users were using iOS 14.

## Products affected: 

* Brave iOS 1.32.3 and higher (include the latest Nightly) on iOS 14.x and below

## Steps To Reproduce:

* Visit https://csrf.jp/brave/reader_uuid_leakage.php
* Open the page in Reader mode
* Long tap a hyperlink in the page and choose "Open in New Private Tab"
* Wait for several seconds and tap "Load original page"
* uuidKey in the reader mode URL is stolen through REFERER header
* Click an exploit URL in the page, then XSS is triggered on `internal://local`

## Supporting Material/References:

* xss_on_internal_origin_through_reader_mode.mov: video of the attack against the vulnerabilities
* reader_uuid_leakage.php: server-side exploit code

## Impact

* Attacker can elevate privileges to `internal:` origin

## Attachments
- xss_on_internal_origin_through_reader_mode.mov
- reader_uuid_leakage.php
