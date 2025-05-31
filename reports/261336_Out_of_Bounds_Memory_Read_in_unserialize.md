# Out of Bounds Memory Read in unserialize()

## Report Details
- **Report ID**: 261336
- **URL**: https://hackerone.com/reports/261336
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-08-18T13:22:28.231Z
- **Disclosed**: 2018-11-27T15:59:52.325Z

## Reporter
- **Username**: cy1337
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
The finish_nested_data function in ext/standard/var_unserializer.re in PHP before 5.6.31, 7.0.x before 7.0.21, and 7.1.x before 7.1.7 is prone to a buffer over-read while unserializing untrusted data. Exploitation of this issue can have an unspecified impact on the integrity of PHP.

This has been fixed and assigned CVE-2017-12933 the bug report is here: https://bugs.php.net/bug.php?id=74111

## Attachments
No attachments
