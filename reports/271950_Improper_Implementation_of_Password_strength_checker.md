# Improper Implementation of Password strength checker

## Report Details
- **Report ID**: 271950
- **URL**: https://hackerone.com/reports/271950
- **State**: Closed
- **Severity**: none
- **Submitted**: 2017-09-26T12:14:55.204Z
- **Disclosed**: 2017-11-10T04:17:37.019Z

## Reporter
- **Username**: ethio
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: legalrobot

## Vulnerability Information
Hi,
I have seen Improper Implementation of Password strength checker for registration and login page. Once it suggest complex password, one can alter the password but the complexity remain the same  Its usually related to Ajax or auto-reload implementation.  

PoC
-------------------------------------
As a prof of concept see the attached picture, where the complexity says very high but with no password input. 

## Attachments
- progress6_15-06-22.png
