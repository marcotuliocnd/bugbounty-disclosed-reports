# Heap Use After Free in unserialize()

## Report Details
- **Report ID**: 261338
- **URL**: https://hackerone.com/reports/261338
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-08-18T13:24:49.512Z
- **Disclosed**: 2018-11-27T15:59:52.330Z

## Reporter
- **Username**: cy1337
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
ext/standard/var_unserializer.re in PHP 7.0.x before 7.0.21 and 7.1.x before 7.1.7 is prone to a heap use after free while unserializing untrusted data, related to the zval_get_type function in Zend/zend_types.h. Exploitation of this issue can have an unspecified impact on the integrity of PHP.

This has been fixed and assigned CVE-2017-12934.  The bug report is here: https://bugs.php.net/bug.php?id=74101

## Attachments
No attachments
