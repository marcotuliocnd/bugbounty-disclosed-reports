# Out of Bounds Memory Read in php_jpg_get16

## Report Details
- **Report ID**: 665330
- **URL**: https://hackerone.com/reports/665330
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2019-08-01T05:45:21.955Z
- **Disclosed**: 2020-11-09T01:47:14.529Z

## Reporter
- **Username**: sediruoksitsero
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
I have found and reported an out of bounds memory read in PHP [php_jpg_get16]
When PHP EXIF extension is parsing EXIF information from an image, e.g. via exif_read_data() function, in PHP versions 7.1.x below 7.1.30, 7.2.x below 7.2.19 and 7.3.x below 7.3.6 it is possible to supply it with data what will cause it to read past the allocated buffer.
This has been fixed and assigned CVE-2019-11040
The bug report is here: https://bugs.php.net/bug.php?id=77988
https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11040
https://nvd.nist.gov/vuln/detail/CVE-2019-11040

## Impact

This may lead to information disclosure or crash.

## Attachments
No attachments
