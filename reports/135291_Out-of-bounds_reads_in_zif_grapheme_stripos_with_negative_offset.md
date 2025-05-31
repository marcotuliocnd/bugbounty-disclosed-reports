# Out-of-bounds reads in zif_grapheme_stripos with negative offset

## Report Details
- **Report ID**: 135291
- **URL**: https://hackerone.com/reports/135291
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-04-29T03:23:04.103Z
- **Disclosed**: 2019-10-13T18:21:26.951Z

## Reporter
- **Username**: fms
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
https://bugs.php.net/bug.php?id=72061

grapheme_stripos from the intl extension had a security issue when handling negative offsets, this allowed to read from arbitrary memory locations.

Reported to developers on 2016-04-24, fixed 2016-04-29 and released at 2016-04-28, affected PHP 5.5 , 5.6 and 7.

http://php.net/ChangeLog-5.php#5.5.35
http://php.net/ChangeLog-5.php#5.6.21
http://php.net/ChangeLog-7.php#7.0.6

## Attachments
No attachments
