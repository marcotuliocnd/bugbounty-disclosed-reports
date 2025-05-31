# New XSS vector in ReaderMode with %READER-TITLE-NONCE%

## Report Details
- **Report ID**: 1436142
- **URL**: https://hackerone.com/reports/1436142
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2021-12-26T06:59:17.690Z
- **Disclosed**: 2023-06-22T05:51:33.965Z

## Reporter
- **Username**: nishimunea
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: brave

## Vulnerability Information
## Summary:
Previously, script execution in ReaderMode pages was prohibited by CSP. However, three months ago, [this commit](https://github.com/brave/brave-ios/pull/4209/files#diff-eaeef15a290e9e5e9bcaae784f18d874f8c932dfa3de416a5820eccd6b2d8cfbR54) partially relaxed the CSP and scripts with `nonce-%READER-TITLE-NONCE%` are now allowed to be executed. This relaxation of the CSP rule can be exploited for XSS attacks on ReaderMode pages.

Here, the attack vector is `%READER-CREDITS%` which is also [included in the ReaderMode HTML template](https://github.com/brave/brave-ios/blob/6f667506228eeff77daf4df7c9dddae22eb0ad1b/Client/Frontend/Reader/Reader.html#L18). The `%READER-CREDITS%` is replaced with the value of the `<meta name="author">` tag in the original page, but then the HTML tags are not escaped. So, when the following meta tag is embedded in the original page and the page is displayed in ReaderMode, [this Swift code](https://github.com/brave/brave-ios/blob/6f667506228eeff77daf4df7c9dddae22eb0ad1b/Client/Frontend/Reader/ReaderModeUtils.swift#L30)  replaces `%READER-TITLE-NONCE%` with the correct nonce value.
```
<meta name="author" content="Evil &lt;script nonce=%READER-TITLE-NONCE%&gt;alert(document.location);&lt;/script&gt;!--">
```

As a result, the malicious script will be executed on a page `http://localhost:6571/reader-mode?uri={uri}&uuidkey={value}`.
In Brave, all readalized pages are hosted on `http://localhost:6571`. Therefore, through this XSS, any cross-origin pages, that has been converted to ReaderMode, can be stolen by embedding an iframe and reading out them. Also, please find that the `uuidkey` is included in the URL query string. By obtaining this key, the attacker can gain access to Brave's privileged pages.

## Products affected: 

 * Brave iOS 1.31.1 and higher (including the latest Nightly)

## Steps To Reproduce:

 * Show https://csrf.jp/2021/brave/author_xss.php
 * Push reader mode button on the address bar
 * An alert dialog is shown

## Supporting Material/References:

 * See the screenshot of the alert dialog when the bug is reproduced.

## Impact

* Any cross-origin pages, that has been converted to ReaderMode, can be stolen
* Attacker can gain access to Brave's privileged pages

## Attachments
- screenshot_alert_dialog_on_reader_view.png
