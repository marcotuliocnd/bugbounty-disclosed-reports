# xml_parse_into_struct segmentation fault

## Report Details
- **Report ID**: 135294
- **URL**: https://hackerone.com/reports/135294
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-04-29T03:38:30.259Z
- **Disclosed**: 2019-10-13T18:06:53.554Z

## Reporter
- **Username**: fms
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
https://bugs.php.net/bug.php?id=72099

Invalid memory access while parsing XML input using xml_parse_into_struct, parser->level wasn't being checked and then used as an offset parser->ltags[parser->level-1].

Reported to developers on 2016-04-25, fixed 2016-04-25 and released at 2016-04-28, affected PHP 5.5 , 5.6 and 7.

http://php.net/ChangeLog-5.php#5.5.35
http://php.net/ChangeLog-5.php#5.6.21
http://php.net/ChangeLog-7.php#7.0.6

## Attachments
No attachments
