# Bypassing 2FA with conventional session management - open.rocket.chat

## Report Details
- **Report ID**: 1701378
- **URL**: https://hackerone.com/reports/1701378
- **State**: Closed
- **Severity**: low
- **Submitted**: 2022-09-15T17:32:22.802Z
- **Disclosed**: 2024-08-10T19:08:18.213Z

## Reporter
- **Username**: hackeriron1
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rocket_chat

## Vulnerability Information
**Summary:**
Hii Team,

I have found a vulnerability in open.rocket.chat and I able to bypass 2FA by Email confirmation link.
In this case, attackers use the email confirmation link because, often, 2FA is not implemented on the system’s login page after a email confirmation.

## Releases Affected:

https://open.rocket.chat

## Steps To Reproduce:

Attack scenario :
1). Sign up with email.
2). add 2FA.
3). Go to account change email  (Email verification will be sent to victim email).
4). Attacker able to login with email verification link without 2FA code.

## Supporting Material/References:
same vulnerability was in Instagram but via password reset.
https://infosecwriteups.com/how-i-couldve-bypassed-the-2fa-security-of-instagram-once-again-43c05cc9b755

## Suggested mitigation
Do not direct login after email confirmed. 

##POC Video
███

I hope you will understand 
If you need more info, I will provide you.

## Impact

Using this method, attackers can bypass the two-factor authentication in open.rocket.chat where the architecture of the site or platform makes it possible.

## Attachments
No attachments
