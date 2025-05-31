# select_colors write out-of-bounds

## Report Details
- **Report ID**: 161189
- **URL**: https://hackerone.com/reports/161189
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-08-19T02:49:28.093Z
- **Disclosed**: 2019-10-31T06:16:34.902Z

## Reporter
- **Username**: fms
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Upstream Bug
---
2016-07-28 06:38 UTC
https://bugs.php.net/bug.php?id=72697

Summary
--
Type mismatch parameters between ncolors and colorsWanted parameters at zif_imagetruecolortopalette and php_gd_gdImageTrueColorToPalette, ncolors is a 64 bit integer and colorsWanted is 32 bits, ncolors' value 0x1000000000000000 becomes 0 inside php_gd_gdImageTrueColorToPalette. Later, select_colors will not allocate enough memory and writes out of bounds.

Patch
--
2016-08-10 07:01 UTC
http://git.php.net/?p=php-src.git;a=commit;h=4d76676101f8814520ea988e42b3bda54eb9e255

Fixed for PHP 5.6.25, PHP 7.0.10
--
http://php.net/ChangeLog-5.php
http://php.net/ChangeLog-7.php#7.0.10

## Attachments
No attachments
