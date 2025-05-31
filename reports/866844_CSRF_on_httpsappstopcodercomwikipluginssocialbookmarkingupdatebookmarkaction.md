# CSRF on https://apps.topcoder.com/wiki/plugins/socialbookmarking/updatebookmark.action

## Report Details
- **Report ID**: 866844
- **URL**: https://hackerone.com/reports/866844
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-05-05T23:02:01.775Z
- **Disclosed**: 2020-05-12T13:37:58.750Z

## Reporter
- **Username**: meryem0x
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: lab45

## Vulnerability Information
## Summary:
Hi :) There is a CSRF on creating bookmarks form.

## Steps To Reproduce:

There is no CSRF token or anything like that on https://apps.topcoder.com/wiki/plugins/socialbookmarking/updatebookmark.action. I added the poc html file below. When someone opens this html file, or we can add it into our website, he/she creates a bookmark unwillingly.

## Impact

An attacker can force other users to create a bookmark without their knowledge.

## Attachments
- csrf.html
