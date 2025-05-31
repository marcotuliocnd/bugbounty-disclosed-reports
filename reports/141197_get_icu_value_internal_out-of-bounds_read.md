# get_icu_value_internal out-of-bounds read

## Report Details
- **Report ID**: 141197
- **URL**: https://hackerone.com/reports/141197
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-05-26T14:19:23.800Z
- **Disclosed**: 2019-10-13T18:12:26.202Z

## Reporter
- **Username**: fms
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
https://bugs.php.net/bug.php?id=72241

Absence of null character terminator causes unexpected zend_string length and leaks heap memory when using several intl functions that commonly receive user input:

- locale_canonicalize
- locale_filter_matches
- locale_lookup
- locale_parse
- locale_get_primary_language 

This affected PHP version 5.5, 5.6 and 7.0, patch released today:

http://php.net/ChangeLog-5.php#5.5.36

## Attachments
No attachments
