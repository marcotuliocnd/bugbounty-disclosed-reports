# No Security check at changing password and at adding mobile number which leads to account takeover and spam

## Report Details
- **Report ID**: 207552
- **URL**: https://hackerone.com/reports/207552
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-02-19T21:12:21.445Z
- **Disclosed**: 2017-02-21T20:45:12.417Z

## Reporter
- **Username**: mohith_kalyan
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: khanacademy

## Vulnerability Information
#Description

I have noticed that there is no security check at changing password. If someone gets a logged in account for 5 seconds, they are extremely likely to change the password of the account with the knowledge of the victim. also, while adding a mobile number / changing a mobile number, there is no sms / call verification which leads to spamming of any user using Khan Academy as source.

Since there is no sms verification, I could spam anyone (not necessarily khan academy user) with khan Academy notifications.


#Steps to reproduce

1. Click on the name of the profile on top right.
2. Select settings in the drop down menu.
3.  Change the password by just entering the new password, without knowing anything.
4.  Add the mobile number (if already entered, change ) of your choice, since there is no security check, they will be spammed by khan academy messages.


#Impact

Lack of security check at password change leaves a vulnerability open to attackers to change the password without knowing anything about the user.
Lack of verification of mobile while adding / changing mobile number leaves every mobile user open for spamming via Khan Academy.


#Screen shots/ References

███
F162091


## Attachments
- no_security_check_at_changing_password..PNG
