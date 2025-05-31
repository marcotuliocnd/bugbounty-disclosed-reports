# Password Policy Bypass

## Report Details
- **Report ID**: 213767
- **URL**: https://hackerone.com/reports/213767
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-03-15T19:12:09.828Z
- **Disclosed**: 2017-08-28T06:14:15.929Z

## Reporter
- **Username**: r0h17
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: legalrobot

## Vulnerability Information
Hi LegalRobot team,

I noticed that there is a strong Password policy enforced on login page which only allows passwords with 8 or more characters and they need to be a combination of Capital letters, small letters, and numbers/special characters.
However i found that i am able to bypass this Password policy when trying to change password and set a very weak password on account.

I have attached steps to reproduce the issue (set the character 'a' as password) in document, please take a look at it.

Alternatively, i can give you credentials for my account which has password set to 123

## Attachments
- LegalRobot_PasswordPolicy_Bypass.docx
