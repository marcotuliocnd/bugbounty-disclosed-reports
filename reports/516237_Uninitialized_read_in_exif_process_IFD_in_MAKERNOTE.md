# Uninitialized read in exif_process_IFD_in_MAKERNOTE

## Report Details
- **Report ID**: 516237
- **URL**: https://hackerone.com/reports/516237
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-03-27T03:18:50.881Z
- **Disclosed**: 2020-10-10T02:17:45.672Z

## Reporter
- **Username**: chamal
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
This bug is present in exif_process_IFD_in_MAKERNOTE method of ext/exif/exif.c file.

Detailed description and steps to reproduce for this bug is present in bug report submitted to php.net.
Bug Report : https://bugs.php.net/bug.php?id=77563
PHP version : 7.1.26
CVE-ID : 2019-9638

## Impact

Uninitialized data may leak data from memory.

## Attachments
No attachments
