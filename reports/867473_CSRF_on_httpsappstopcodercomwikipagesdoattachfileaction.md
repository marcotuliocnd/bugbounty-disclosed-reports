# CSRF on https://apps.topcoder.com/wiki/pages/doattachfile.action

## Report Details
- **Report ID**: 867473
- **URL**: https://hackerone.com/reports/867473
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-05-06T22:53:20.880Z
- **Disclosed**: 2020-12-14T15:59:34.972Z

## Reporter
- **Username**: meryem0x
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: lab45

## Vulnerability Information
## Summary:
Hi :) There is a CSRF on attaching files to wiki pages.

## Steps To Reproduce:
There is no CSRF token or anything like that on https://apps.topcoder.com/wiki/pages/doattachfile.action?pageId= . I added the poc html file below. When someone opens this html file, or we can add it into our website, he/she creates an attachment unwillingly.

This file creates csrf.txt on https://apps.topcoder.com/wiki/pages/doattachfile.action?pageId=165871793

Note: This only works to signed-in users. Because unauthorized users cannot upload attachments. There is a mistake on https://apps.topcoder.com/wiki/login.action now. If you encounter an error, you can login on main site (https://accounts.topcoder.com/member) then try.

## Impact

An attacker can force other users to upload files without their knowledge.

## Attachments
- csrf.html
