# bcpowmod accepts negative scale and corrupts _one_ definition

## Report Details
- **Report ID**: 135293
- **URL**: https://hackerone.com/reports/135293
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-04-29T03:30:19.373Z
- **Disclosed**: 2019-10-13T18:11:23.424Z

## Reporter
- **Username**: fms
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
https://bugs.php.net/bug.php?id=72093

Two issues reported on the same bug, bcpowermod accepts a negative value which also is able to corrupt the one definition and leads to memory corruption problems.

Reported to developers on 2016-04-24, fixed 2016-04-25 and released at 2016-04-28, affected PHP 5.5 , 5.6 and 7.

http://php.net/ChangeLog-5.php#5.5.35
http://php.net/ChangeLog-5.php#5.6.21
http://php.net/ChangeLog-7.php#7.0.6

## Attachments
No attachments
