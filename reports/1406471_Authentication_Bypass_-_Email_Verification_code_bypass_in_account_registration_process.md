# Authentication Bypass - Email Verification code bypass in account registration process.

## Report Details
- **Report ID**: 1406471
- **URL**: https://hackerone.com/reports/1406471
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2021-11-21T12:51:08.871Z
- **Disclosed**: 2021-12-07T18:57:19.042Z

## Reporter
- **Username**: anas_44
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: upchieve

## Vulnerability Information
Hi Team,

I was able to bypass Email Verification code in account registration process.

Summary :
Authentication Bypass is a dangerous vulnerability, which is found in Web-Applications. An Attackers can bypass the control mechanisms which are used by the underlying web application like Email verification, OTP, Captcha, 2FA, etc. An Attacker can perform a  complete Account takeover of Victim.

Severity :   High / Critical

Complexity : Easy 

From : Remote / External

Steps to Reproduce:

1- First visit your website "https://hackers.upchieve.org" and request for the sign up.
2- In the second step, choose either you want to register as an academic coach or need an academic coach.
3- In the third step, enter your email and create a password.
4- In the fourth step, enter name and mobile phone, then sign up.
5- Then request for verification code on email.
6- Enter wrong verification code and intercept request using Burp suite.
7- After intercepting the request, I changed the status from "False" to "True".
          {"status":false to "status":true}
8- Boom!! Verification code bypassed.
9- Finally, the account was created with the wrong verification code.


Proof of Concept : 
For better understanding, I have attached screenshots and videos after intercepting the request from Burp Suite.

Recommendations :
The application should protect the sensitive actions and validate the verification process of the web application. Restrict the user for any malicious behavior. 

References:
https://hackerone.com/reports/1040047
https://hackerone.com/reports/57764
https://medium.com/@AGNIHACKERS/otp-bypass-through-response-manipulation-beeb467359d8

## Impact

An Adversary can carry out Auth Bypass attack and perform an Account Take Over. An attacker can succeed in the account takeover of any user without any privileges.

## Attachments
- Email_Verification_bypass.mp4
- Status-False.PNG
- Status-True.PNG
