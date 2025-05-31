# No rate limit in stats api token endpoint

## Report Details
- **Report ID**: 412526
- **URL**: https://hackerone.com/reports/412526
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-09-21T17:44:18.120Z
- **Disclosed**: 2018-10-19T17:41:22.424Z

## Reporter
- **Username**: maximus-decimus-meridius
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: chaturbate

## Vulnerability Information
##Brute force on statsapi endpoint to view stats of an user##


## Steps To Reproduce:

  1.  Stats api token can be generated at https://chaturbate.com/statsapi/authtoken/
https://chaturbate.com/statsapi/?username=hackeronetestchat&token=**vulnerable**

 I've used my profile and and my token to check brute force

The  correct token returned with 200 ok status

## Impact

An attacker could view the stats of an user

## Attachments
- chaturbate1.PNG
