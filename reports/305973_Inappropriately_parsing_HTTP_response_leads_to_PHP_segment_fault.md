# Inappropriately parsing HTTP response leads to PHP segment fault!

## Report Details
- **Report ID**: 305973
- **URL**: https://hackerone.com/reports/305973
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-01-17T17:29:19.969Z
- **Disclosed**: 2019-11-12T09:18:47.648Z

## Reporter
- **Username**: orange
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
## Description
-----
A NULL Pointer Deference in parsing HTTP header. It is very easy to trigger this segment fault and may be vulnerable in some scenarios.


　
## Original bug report
-----
- https://bugs.php.net/bug.php?id=75535

　
## Note
-----
- None

　
Thanks :)

## Impact

Segment fault

## Attachments
No attachments
