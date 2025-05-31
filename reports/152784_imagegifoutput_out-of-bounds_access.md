# imagegif/output out-of-bounds access

## Report Details
- **Report ID**: 152784
- **URL**: https://hackerone.com/reports/152784
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-07-21T05:19:57.431Z
- **Disclosed**: 2019-10-13T18:20:54.513Z

## Reporter
- **Username**: fms
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Bug
https://bugs.php.net/bug.php?id=72519

Summary
output function from gd_gif_out.c causes out-of-bounds access of the masks array when ctx->cur_bits becomes a negative number while generating a gif file.

Reported to PHP 
2016-06-30 04:10 UTC

Patch
2016-07-19 07:47 UTC
http://git.php.net/?p=php-src.git;a=commit;h=8dc5ffa479f886fae235d4ff6391e14546a3fda9

Fixed for PHP 5.5 (security only mode), PHP 5.6, PHP 7.0
http://php.net/ChangeLog-5.php
http://php.net/ChangeLog-7.php


## Attachments
No attachments
