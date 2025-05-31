# Lack of Password Confirmation When Changing Email

## Report Details
- **Report ID**: 245334
- **URL**: https://hackerone.com/reports/245334
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-07-02T13:06:15.472Z
- **Disclosed**: 2017-07-03T06:49:30.028Z

## Reporter
- **Username**: pratyushjanghel
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wakatime

## Vulnerability Information
When any user wants to change the password, current password is asked for proceeding the request. This should also be implemented on changing the email.

Attack Scenerio :  When some forget to logout from the account in a publc computer, anyone can change the email to its own and verify it. And after that using the forget password feature, it can change the password too.

Reference From : #546

Best Regards,
Pratyush Janghel

## Attachments
No attachments
