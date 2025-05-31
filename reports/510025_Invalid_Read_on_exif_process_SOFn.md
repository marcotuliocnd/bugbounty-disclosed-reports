# Invalid Read on exif_process_SOFn

## Report Details
- **Report ID**: 510025
- **URL**: https://hackerone.com/reports/510025
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-03-15T08:45:38.365Z
- **Disclosed**: 2020-10-10T02:17:08.150Z

## Reporter
- **Username**: chamal
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
This  bug is present in exif_scan_thumbnail method of ext/exif/exif.c file.

Detailed description and steps to reproduce for this bug is present in bug report submitted to php.net.
Bug Report : https://bugs.php.net/bug.php?id=77540
PHP version : 7.1.26
CVE-ID : 2019-9640

## Impact

This bug may allow an attacker to read unintended data from memory.

## Attachments
No attachments
