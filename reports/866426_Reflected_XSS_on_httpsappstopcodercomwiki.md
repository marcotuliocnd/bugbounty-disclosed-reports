# Reflected XSS on https://apps.topcoder.com/wiki/

## Report Details
- **Report ID**: 866426
- **URL**: https://hackerone.com/reports/866426
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-05-05T13:41:27.348Z
- **Disclosed**: 2020-05-12T13:48:28.035Z

## Reporter
- **Username**: meryem0x
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: lab45

## Vulnerability Information
## Summary:
Hi :)  A reflected XSS occurs on https://apps.topcoder.com/wiki/plugins/tinymce/wysiwyg-insertlink.action when creating wiki pages.

## Steps To Reproduce:

A user can create wiki page on https://apps.topcoder.com/wiki/pages/createpage.action?spaceKey=tcwiki. A url can be inserted this page. When you click `Insert/Edit url` https://apps.topcoder.com/wiki/plugins/tinymce/wysiwyg-insertlink.action?draftType=page&spaceKey=tcwiki&currentspace=tcwiki&formname=createpageform&fieldname=wysiwygcontent&alias= page opens. You can change `alias` parameter and add `tooltip` parameter with JS codes. If a victim opens this url, XSS will execute. 

PoC:
https://apps.topcoder.com/wiki/plugins/tinymce/wysiwyg-insertlink.action?draftType=page&spaceKey=tcwiki&currentspace=tcwiki&formname=createpageform&fieldname=wysiwygcontent&alias=as%22%3E%3Cimg%20src=x%20onerror=alert(document.domain)%3E&tooltip=as%22%3E%3Cimg%20src=X%20onerror=alert(document.cookie)%3E

{F816079}
{F816080}

## Impact

XSS can use to steal cookies or to run arbitrary code on victim's browser.

## Attachments
- document_cookie.png
- document_domain.png
