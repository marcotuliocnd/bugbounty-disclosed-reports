# Stored XSS on https://apps.topcoder.com/wiki/plugins/socialbookmarking/updatebookmark.action

## Report Details
- **Report ID**: 866815
- **URL**: https://hackerone.com/reports/866815
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-05-05T22:12:43.388Z
- **Disclosed**: 2020-05-12T13:47:23.015Z

## Reporter
- **Username**: meryem0x
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: lab45

## Vulnerability Information
## Summary:
Hi :) Adding javascript url causes to stored XSS when creating bookmark.

## Steps To Reproduce:

Go to https://apps.topcoder.com/wiki/plugins/socialbookmarking/updatebookmark.action . Write `javascript:alert(document.domain)` on url input and fill other areas. After create, go `https://apps.topcoder.com/wiki/display/tcwiki/<TITLE>` and when you click the title on this page, XSS will execute.

PoC:
https://apps.topcoder.com/wiki/display/tcwiki/powerpuff_hackerone_test
{F816754}

## Impact

XSS can use to steal cookies or to run arbitrary code on victim's browser.

## Attachments
- 2020-05-06_01-05-54_ekran_g_r_nt_s_.png
