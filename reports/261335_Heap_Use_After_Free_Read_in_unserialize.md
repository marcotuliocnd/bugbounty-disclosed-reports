# Heap Use After Free Read in unserialize()

## Report Details
- **Report ID**: 261335
- **URL**: https://hackerone.com/reports/261335
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-08-18T13:20:37.058Z
- **Disclosed**: 2018-11-27T15:59:52.397Z

## Reporter
- **Username**: cy1337
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
ext/standard/var_unserializer.re in PHP 7.0.x through 7.0.22 and 7.1.x through 7.1.8 is prone to a heap use after free while unserializing untrusted data, related to improper use of the hash API for key deletion in a situation with an invalid array size. Exploitation of this issue can have an unspecified impact on the integrity of PHP.

This is CVE-2017-12932 and the bug report confirming that I reported the issue is here: https://bugs.php.net/bug.php?id=74103

## Attachments
No attachments
