# Improper Authentication - 2FA OTP Reusable

## Report Details
- **Report ID**: 2529780
- **URL**: https://hackerone.com/reports/2529780
- **State**: Closed
- **Severity**: high
- **Submitted**: 2024-06-01T02:57:57.846Z
- **Disclosed**: 2024-07-11T14:40:48.215Z

## Reporter
- **Username**: xklepxn
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**
I found an “Improper Authentication” issue where the 2FA OTP generated by the Microsoft Authenticator app can be used for two-step verification in HackerOne. This is similar to the common issue where tokens remain usable after logout. This means that the OTP does not have an invalidation period even if the app has generated a new OTP. 

**Description:**
OTP is generated every 30 seconds. In the POC, I let the app generate three OTPs, meaning 90 seconds  passed to let the old OTP. Supposedly, the old OTP is no longer valid because a new OTP is generated. However, I was still able to use the old OTP.

### Steps To Reproduce

1.  Set up an account that has 2FA enabled
2.  Login to the account
3.  View the otp created by the Authenticator app
4. Let the app create 3x otp (it's up to you how many you want)
5. But, the otp used is the first one 

### POC 

███████

### Reference

 * https://book.hacktricks.xyz/pentesting-web/2fa-bypass

### CVSS Explaination
* ```Privileges required: HIGH``` I admit, to accomplish this attack means that the attacker already has the victim's user credential/password data (there are many ways to do this, e.g. credential stealer etc.).
* ```CIA : HIGH ``` The success of the attacker taking over the account will have an impact on confidentiality (private programs, account data, etc.), integrity (the attacker is able to control what he wants to do with the account), Availability imagine the attacker changing the email, etc. until finally the victim has no access to the account.

But the final decision on CVSS is still up to you.

## Impact

The generated otp codes are all common as in the 6-digit otp list on github, with the reusable otp loophole, this increases the probability of successful brute force otp. In other words, the loophole impacts the takeover account.

{F3317700}

## Attachments
- image.png
