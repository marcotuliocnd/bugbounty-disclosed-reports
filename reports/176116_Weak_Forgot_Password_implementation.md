# Weak Forgot Password implementation

## Report Details
- **Report ID**: 176116
- **URL**: https://hackerone.com/reports/176116
- **State**: Closed
- **Severity**: low
- **Submitted**: 2016-10-16T09:36:26.873Z
- **Disclosed**: 2017-08-02T05:58:25.063Z

## Reporter
- **Username**: pavanw3b
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: revive_adserver

## Vulnerability Information
**"Cricetinae"** :)

###Short Description
The Forgot Password is missing a several industry best practices. I strongly believe due to the level of the access given after a successful exploitation, the implementation could have been better.

###Vulnerability Details
Referring to OWASP Standards and guidelines [https://www.owasp.org/index.php/Forgot_Password_Cheat_Sheet], I see the following risks in the Forgot Password implementation:
* Invalidate or provide an option to invalidate existing sessions after password has been reset
* Invalidate the current session and redirect to login after successful password reset.

Also consider:
* Do not allow the old the password as the new one.
* Provide an option to set up Security Questions for admin accounts.

I'm not sure about the above two points as they sound more like features rather than bugs.

### Steps to Reproduce
* Login as a admin on **Browser A** & keep it.
* Open **Browser B** (or incognito/private). Go to Password Recovery page by clicking `Forgot your password?` from the login page.
* Note the `sessionID` cookie. Enter the email address and `Proceed >`.
* Open the reset link received by email on **Browser B**. Note that the `sessionID` remained the same. Change the password. Note that the user have logged to dashboard without invalidating the current session and the `sessionID` remained the same.
* Come back to **Browser A** and note that the user session is still valid.

### Attack vector
* **Invalidating other existing session:** The `sessionID` cookie which drives everything about user accounts, is set to expire on `Session` which means until the user explicitly clicks the `Logout` or the browser/tab is closed. Thus if an attacker some how (phishing or brute force) compromised an user account, the hacked session remained the same even though the account owner resets the password or change the email address.
* **Invalidating the current session after the password recovery:** Attacker with physical access to the user's computer, leaves the Revive Adserver login page open by noting down the `sessionID`. User comes, resets the password and logged in. As the attacker knows the `sessionID`, he can use that in logging in as the user. This works even the attacker not having admin access on the system to install a keylogger and valid until the user logs out and the session is destroyed.

### Test Environment Details
Version: Latest as on Oct 16: revive-adserver-4.0.0 downloaded from the official source
Setup type: local
Browser: Firefox 47.0
OS: Mac OS X


Cheers,
Pavan


## Attachments
No attachments
