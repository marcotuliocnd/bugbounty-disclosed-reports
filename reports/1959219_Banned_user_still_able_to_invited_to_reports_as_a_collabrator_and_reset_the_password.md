# Banned user still able to invited to reports as a collabrator and reset the password

## Report Details
- **Report ID**: 1959219
- **URL**: https://hackerone.com/reports/1959219
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-04-23T15:22:31.892Z
- **Disclosed**: 2023-07-06T07:37:04.971Z

## Reporter
- **Username**: light3r
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
#Description:

* The permanently banned user account can't access any account features or reports and when accessing his profile he receives 404 not found so the account seems to be not signed or not found so the permanently banned user account must be can not access any HackerOne/account features anymore or access reports, but I was able to add the permanently banned user as a collaborator In the report and reset the password without any restrictions

##Steps to reproduce:

* I created an account and send a message to the support team to permanently ban the user account 

* After the account was banned I created a new test account and sandbox program 

* I send a collaborator request to the banned account so he must be can't receive the collaborator email

* But he invited to the report as shown below:

{F2309760}

* Also I can send and reset the password

{F2309761}

{F2309769}

* Here I reset the password

{F2309773}

* Now the banned user is able to join reports as a collaborator and reset his password and this restricted to banned user

## Impact

The banned user able to join reports as a collaborator and reset his password this Is restricted due to be permanently banned from the platform and must be can't access any data or use any feature from the HackerOne platform because his account Is seems to be deleted from the platform and must be can't access anything from his account or access any data

## Attachments
- ban.png
- ban2.png
- ban3.png
- ban4.png
