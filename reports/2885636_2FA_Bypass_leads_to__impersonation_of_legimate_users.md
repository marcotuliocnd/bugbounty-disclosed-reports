# 2FA Bypass leads to  impersonation of legimate users

## Report Details
- **Report ID**: 2885636
- **URL**: https://hackerone.com/reports/2885636
- **State**: Closed
- **Severity**: high
- **Submitted**: 2024-12-06T07:48:31.063Z
- **Disclosed**: 2025-03-14T15:30:23.950Z

## Reporter
- **Username**: duk33d
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: drugs_com

## Vulnerability Information
## Summary:
Hello team,
I have discovered a logic flaw in the authentication system that allows an attacker (User A) to impersonate a legitimate user (User B) who has not yet registered. By abusing the email change functionality and bypassing 2FA, the attacker can retain access to the account until the legitimate user resets their password.

## Steps to re-produce
1. Go to https://www.drugs.com/account/register/ and create an account using an email you own.

██████

2. Complete OTP verification and select "Trust this device for 1 month". This gives you a valid session that does not require 2FA for one month.

3. Go to https://www.drugs.com/account/details/ and change the email to the victim's email (User B)
   - Now, the attacker has a valid session associated with User B's email for one month, bypassing 2FA.

███

4. Log out and log back in to confirm that the application doesn't prompt for OTP.

### To maintain this bypass indefinitely (until the original user resets the password):
1. Change the email back to the attacker's email.

2. Re-verify the new email by completing OTP verification and selecting "Trust this device for 1 month".
3. Change the email back to the victim's email (or any other arbitrary email).

By repeating this process, the attacker can retain access without triggering 2FA.
Note that the platform only notifying the attacker to activate the account , but not Terminating the session after the email has changed successfully 

## From victim POV
1. Go to Sign Up page 
2. try to Sign up with the victim's email
3. Note that  the platform says that email's already used (while the original Owner of the email didn't  create the account) 

███████

## Impact

## Summary:

1. ** Loss of Trust:** Users will lose confidence in the platform's security if they learn attackers had  impersonated them.

2. **Impersonation Risk:** Attackers can impersonate legitimate users and interact with the platform.

3. **Email Ownership Not Protected:** The platform fails to verify the original owner of the email, allowing attackers to use it.

## Attachments
No attachments
