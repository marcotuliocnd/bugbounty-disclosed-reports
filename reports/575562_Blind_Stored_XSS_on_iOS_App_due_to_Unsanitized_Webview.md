# Blind Stored XSS on iOS App due to Unsanitized Webview

## Report Details
- **Report ID**: 575562
- **URL**: https://hackerone.com/reports/575562
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-05-09T17:15:08.282Z
- **Disclosed**: 2020-03-07T21:54:57.092Z

## Reporter
- **Username**: n00bsec
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Hi Team!

I found a Blind XSS can executed on iOS App due to unsanitized webview. Using this issue, attacker can extract information from victim.

##Steps To Reproduce:
1. Upload malicious HTML, share to victim
2. Waiting victim to open it

{F487447}

{F487448}

HTML payload attached, don't forget to change IP Address to yours.

**Recomendation:** Disabling Javascript on Webview
**Reference:**
https://developer.apple.com/documentation/webkit/wkpreferences#//apple_ref/occ/instp/WKPreferences/javaScriptEnabled

## Impact

In this PoC, attacker can extract information from victim such as IP Address, Location, OS.

## Attachments
- nextcloud_blindxss.jpg
- nextcloud_blindxss.png
