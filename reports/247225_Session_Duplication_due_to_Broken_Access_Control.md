# Session Duplication due to Broken Access Control

## Report Details
- **Report ID**: 247225
- **URL**: https://hackerone.com/reports/247225
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-07-08T15:42:40.205Z
- **Disclosed**: 2017-07-10T07:33:51.921Z

## Reporter
- **Username**: anurag98
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wakatime

## Vulnerability Information
Due to improper validation of user before generating an API-KEY and improper measures taken at the time of password reset, it is possible to generate a parallel session at the attacker's end.

Proof of concept video is attached to confirm the vulnerability and to demonstrate the Impact of this _logical_ bug.

Steps to Reproduce
=============
Attacker
---------
- Create an account with victims email.
- Download the coding platforms and get API-KEY.
- He can code from the platforms using the victims API-key.

Victim
-------
- User fails to create an account, due to email already registered and does a password reset.
- Downloads the coding platform and get API-KEY.
- He codes using API-KEY.

It is possible for the Attacker and Victim, for coding at the same time, which will be shown at the dashboard. Attacker can reduce the difficulty and can damage the reputation of the coder.

 Impact
=====

__Attacker can brute-force email and register multiple account on wakatime to get API-Key of many users.__
 
Improper rank calculation.

Session duplication by the attacker



## Attachments
- My_Movie1.wmv
