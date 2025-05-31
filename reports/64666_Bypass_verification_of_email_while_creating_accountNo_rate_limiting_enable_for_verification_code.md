# Bypass verification of email while creating account(No rate limiting enable for verification code)

## Report Details
- **Report ID**: 64666
- **URL**: https://hackerone.com/reports/64666
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2015-05-29T19:53:43.315Z
- **Disclosed**: 2016-08-25T22:59:21.848Z

## Reporter
- **Username**: indoappsec
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: maplogin

## Vulnerability Information
Hi Team,

Bug type : Authentication bypass(Missing rate limiting)

Description : While creating a account user needs to enter a email id and verification has been sent to his email ID.It is a 4 digits code.But there is no rate limiting enable while checking the verification on server side.So basically Any one can use account by any email ID in the world.

Exploite : 
1.Attacker creates a account with victim's email ID Ex: victim@gmail.com
2.Now he doesn't know the verification code.Attacker will start brute force attack to get the correct verification code.Once Attacker gets the verification code,He will be able to use the Email id of victim on Maplogin account.


Solution : Enable rate limiting on verifying the code (Ex: User can try only 10 times after that he's blocked for sometime)

This is a critical authentication issue,kindly look into it asap.

Regards !

## Attachments
No attachments
