# Reauthentication for changing password bypass

## Report Details
- **Report ID**: 642886
- **URL**: https://hackerone.com/reports/642886
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-07-14T11:55:54.888Z
- **Disclosed**: 2020-12-23T10:16:00.179Z

## Reporter
- **Username**: viber
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: liberapay

## Vulnerability Information
Hello There
So Libra Pay has this security system because of which if a malicious user tries to change the password of a logged in account, whether by session hijack or anything else he will be asked to re-enter the password before he can change it. 
But this loop hole I found in the system using which he/she can change it without even knowing the old password. How? 
Here is the reproduction steps:

Step 1. Go to accounts settings. 
Step 2. Add an email address to the email which we have access to(Remember adding an email doesn't require you to re-enter password but changing password does) 
Step 3. Confirm the email address. 
Step 4. Make it primary email. (Even this doesn't require you to re-enter password)
Step 5. Now we can change the password by reseting it through the new ema

I have checked for this in several other platforms as well but most of them were smart enough to ask me for entering password before I could change or add email address. May be you can implement the same.

Thank you.
Baibhav Anand Jha.
Security Researcher.

## Impact

A malicious user will be able to change the password without knowing the old password.

## Attachments
No attachments
