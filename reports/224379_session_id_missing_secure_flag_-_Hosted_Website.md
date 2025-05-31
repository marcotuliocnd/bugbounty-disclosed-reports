# session id missing secure flag - Hosted Website

## Report Details
- **Report ID**: 224379
- **URL**: https://hackerone.com/reports/224379
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-04-27T15:17:42.858Z
- **Disclosed**: 2017-05-17T16:31:11.951Z

## Reporter
- **Username**: pavanw3b
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
Hey folks,

Looks like the `sessionid` cookie handles session id but misses `Secure` flag. Cookies without this flag will transmitted over unencrypted channel and let's the man in the middle attackers to grab the value.

### Attack Vector
- Attacker passes a http:// hosted website link
- Victim clicks the link
- Browser passes the session cookie over http
- MITIM attacker gets the value and take over the account
With the #224287, this made more simpler.

### Suggested Fix
Set the Secure flag true for the session id and any other sensitive cookies.

Example h1 reports:
https://hackerone.com/reports/58679
https://hackerone.com/reports/6877

## Attachments
- Screen_Shot_2017-04-27_at_8.40.13_PM.png
