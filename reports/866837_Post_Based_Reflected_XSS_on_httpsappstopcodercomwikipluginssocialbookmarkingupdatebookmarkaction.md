# Post Based Reflected XSS on https://apps.topcoder.com/wiki/plugins/socialbookmarking/updatebookmark.action

## Report Details
- **Report ID**: 866837
- **URL**: https://hackerone.com/reports/866837
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-05-05T22:44:36.793Z
- **Disclosed**: 2020-05-12T13:40:05.095Z

## Reporter
- **Username**: meryem0x
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: lab45

## Vulnerability Information
## Summary:
Hi :) A post based reflected XSS occurs when creating bookmarks.

## Steps To Reproduce:
`Title` and `Labels` parameters are vulnerable to XSS on https://apps.topcoder.com/wiki/plugins/socialbookmarking/updatebookmark.action. This form uses POST request so i added HTML file below. When someone opens this html file, or we can add it into our website, XSS will execute.

{F816815}
{F816816}

## Impact

XSS can use to steal cookies or to run arbitrary code on victim's browser.

## Attachments
- xss.html
- 2020-05-06_01-38-17_ekran_g_r_nt_s_.png
- 2020-05-06_01-38-04_ekran_g_r_nt_s_.png
