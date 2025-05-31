# Reflected XSS on error page on https://apps.topcoder.com/wiki/plugins/socialbookmarking/updatebookmark.action

## Report Details
- **Report ID**: 866861
- **URL**: https://hackerone.com/reports/866861
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-05-05T23:40:24.691Z
- **Disclosed**: 2020-05-12T13:40:50.564Z

## Reporter
- **Username**: meryem0x
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: lab45

## Vulnerability Information
Hi :) 
In https://apps.topcoder.com/wiki/plugins/socialbookmarking/updatebookmark.action `bookmarkPageId` parameter expects a number value. If you add XSS payload instead of number, an error page displays with XSS.

PoC
`https://apps.topcoder.com/wiki/plugins/socialbookmarking/updatebookmark.action?bookmarkPageId="><img src=x onerror=alert(document.domain)>`
{F816846}

## Impact

XSS can use to steal cookies or to run arbitrary code on victim's browser.

## Attachments
- Screenshot_20200506-023406.png
