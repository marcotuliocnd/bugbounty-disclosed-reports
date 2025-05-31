# Out of Bounds Memory Read in exif_scan_thumbnail

## Report Details
- **Report ID**: 675578
- **URL**: https://hackerone.com/reports/675578
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-08-17T16:33:30.569Z
- **Disclosed**: 2020-11-09T01:49:45.909Z

## Reporter
- **Username**: sediruoksitsero
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
I have found and reported an out of bounds memory read in PHP [exif_scan_thumbnail]
When PHP EXIF extension is parsing EXIF information from an image, e.g. via exif_read_data() function, in PHP versions 7.1.x below 7.1.31, 7.2.x below 7.2.21 and 7.3.x below 7.3.8 it is possible to supply it with data what will cause it to read past the allocated buffer.
This has been fixed and assigned CVE-2019-11041
The bug report is here: https://bugs.php.net/bug.php?id=78222
https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11041
https://nvd.nist.gov/vuln/detail/CVE-2019-11041

## Impact

This may lead to information disclosure or crash.

## Attachments
No attachments
