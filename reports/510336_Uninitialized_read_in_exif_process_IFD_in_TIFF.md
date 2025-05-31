# Uninitialized read in exif_process_IFD_in_TIFF

## Report Details
- **Report ID**: 510336
- **URL**: https://hackerone.com/reports/510336
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2019-03-15T14:21:28.872Z
- **Disclosed**: 2020-10-10T02:18:18.265Z

## Reporter
- **Username**: chamal
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
This bug can be reproduced only in 32 bit PHP builds.
This bug is present in exif_process_IFD_in_TIFF method of ext/exif/exif.c file.

Detailed description and steps to reproduce for this bug is present in bug report submitted to php.net.
Bug Report : https://bugs.php.net/bug.php?id=77509
PHP version : 7.1.26
CVE-ID : 2019-9641

## Impact

Uninitialized variables may leak data from memory.

## Attachments
No attachments
