# Potential infinite loop in gdImageCreateFromGifCtx!

## Report Details
- **Report ID**: 305972
- **URL**: https://hackerone.com/reports/305972
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-01-17T17:27:50.375Z
- **Disclosed**: 2019-11-12T09:18:47.646Z

## Reporter
- **Username**: orange
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
## Description
-----
It is easy to trigger in web application if the web use GD as its image library.
For example, It can be triggered if a website resize the user-uploaded GIF, and **ALL** PHP version are affected!
　
## Original bug report
-----
- https://bugs.php.net/bug.php?id=75571

　
## Note
-----
- CVE-2018-5711 assigned

　
Thanks :)

## Impact

A malicious GIF can trigger an infinite loop and lead to exhausted the server resource!

## Attachments
No attachments
