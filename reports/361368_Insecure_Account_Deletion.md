# Insecure Account Deletion

## Report Details
- **Report ID**: 361368
- **URL**: https://hackerone.com/reports/361368
- **State**: Closed
- **Severity**: none
- **Submitted**: 2018-06-03T15:10:11.787Z
- **Disclosed**: 2018-06-04T10:47:41.545Z

## Reporter
- **Username**: hack2684
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: liberapay

## Vulnerability Information
Hi Team,

The removal of account is one of the sensitive part of a web application that needs to protect, therefore removing an account should validate the authenticity of the user, however i have found that when removing an account, the system did not require the user to input the account password.

Steps to reproduce:

1. go to https://liberapay.com/ and login to your account.
2. go to profile/settings.
3. you'll see the "close account" button.
4. press that button and you'll be successfully deleted your account.

Mitigation:
Put reauthentication when anyone/user is deleting an account, ask the user to input password before the completion of the account deletion.

Let me know if you need more information.

Thanks,

## Impact

Exploit Scenario:

1. The user logins to a shared computer (office, library, cafe)
2. Left the account open.
3. Intruder came and try to delete the users account
4. Intruder can easily delete the account because the system did not protect it by asking the password to validate that the person deleting the account is the real user.

## Attachments
No attachments
