# ByPassing the email Validation Email on Sign up process in mobile apps

## Report Details
- **Report ID**: 57764
- **URL**: https://hackerone.com/reports/57764
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2015-04-22T14:41:56.344Z
- **Disclosed**: 2016-11-28T18:13:55.836Z

## Reporter
- **Username**: kaleemgiet
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: coinbase

## Vulnerability Information
Hi,

According to the design When the new user sign up using mobile apps(android,ios).It will ask for the confirmation of the email.It will send a confirmation mail to mail id and a screen will also appear in the mobile app. The user needs to open the email in the device then the screen will Off and user will successfully login.

Bypass:

Here simply we can bypass this validation and can successfully login to the application without verifying the validation email which comes to the user.Using this the attacker can create so many spoofed accounts.

1.Sign for new user using email id and password
2.Next screen will appear saying please click on the validation which sent to proceed further
3.Here in the second screen click the back button now you will go to Login screen
4.Now login with the creds which you have given in the registration process
5.Now you will successfully login to the application
6.Here it is not asking for email verification email.

Pls follow above procedure to reproduce the issue.

Pls respond to remaining bugs which I had reported 

Thanks,
kaleem

## Attachments
No attachments
