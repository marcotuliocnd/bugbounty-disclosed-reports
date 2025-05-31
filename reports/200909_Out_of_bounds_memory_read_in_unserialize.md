# Out of bounds memory read in unserialize()

## Report Details
- **Report ID**: 200909
- **URL**: https://hackerone.com/reports/200909
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-01-24T20:38:29.185Z
- **Disclosed**: 2017-05-28T19:23:37.252Z

## Reporter
- **Username**: hanno
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
I have found and reported an out of bounds memory read in PHP:
https://bugs.php.net/bug.php?id=73825

It affected all three supported versions and has been fixed with the latest updates:
https://secure.php.net/ChangeLog-5.php#5.6.30
https://secure.php.net/ChangeLog-7.php#7.0.15
https://secure.php.net/ChangeLog-7.php#7.1.1

## Attachments
No attachments
