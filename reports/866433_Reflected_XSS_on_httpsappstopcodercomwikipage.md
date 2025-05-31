# Reflected XSS on https://apps.topcoder.com/wiki/page/

## Report Details
- **Report ID**: 866433
- **URL**: https://hackerone.com/reports/866433
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-05-05T13:53:05.387Z
- **Disclosed**: 2020-05-12T13:49:07.302Z

## Reporter
- **Username**: meryem0x
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: lab45

## Vulnerability Information
## Summary:

Hi :) A reflected XSS occurs on https://apps.topcoder.com/wiki/pages/doeditattachment.action when editing wiki pages attachments.

## Steps To Reproduce:

A user can add attachments on https://apps.topcoder.com/wiki/pages/viewpageattachments.action?pageId=165871793 a wiki page and can edit on https://apps.topcoder.com/wiki/pages/editattachment.action?pageId=165871793&fileName=sss.svg. If there is an error, user redirected to `doeditattachment` path with an error message. An attacker can change the filename parameter and add JS codes. When a victim opens this url, XSS will execute. 

PoC:
https://apps.topcoder.com/wiki/pages/doeditattachment.action?pageId=165871793&fileName=s%22%3E%3Cimg%20src=X%20onerror=alert(document.domain)%3Ess.svg
{F816100}

## Impact

XSS can use to steal cookies or to run arbitrary code on victim's browser.

## Attachments
- 2020-05-05_16-44-40_ekran_g_r_nt_s_.png
