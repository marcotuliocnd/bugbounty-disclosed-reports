# Out of Bounds Memory Read in exif_process_user_comment

## Report Details
- **Report ID**: 675580
- **URL**: https://hackerone.com/reports/675580
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-08-17T16:36:43.625Z
- **Disclosed**: 2020-11-09T01:49:40.092Z

## Reporter
- **Username**: sediruoksitsero
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
I have found and reported an out of bounds memory read in PHP [exif_process_user_comment]
When PHP EXIF extension is parsing EXIF information from an image, e.g. via exif_read_data() function, in PHP versions 7.1.x below 7.1.31, 7.2.x below 7.2.21 and 7.3.x below 7.3.8 it is possible to supply it with data what will cause it to read past the allocated buffer.
This has been fixed and assigned CVE-2019-11042
The bug report is here: https://bugs.php.net/bug.php?id=78256
https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11042
https://nvd.nist.gov/vuln/detail/CVE-2019-11042

## Impact

This may lead to information disclosure or crash.

## Attachments
No attachments
