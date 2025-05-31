# Insecure Account Removal

## Report Details
- **Report ID**: 223355
- **URL**: https://hackerone.com/reports/223355
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-04-24T10:09:41.069Z
- **Disclosed**: 2017-05-17T14:15:35.554Z

## Reporter
- **Username**: japz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
Hi Team,

The removal of account is one of the sensitive part of a web application that needs to protect, therefor removing an account should validate the authenticity of the legitimate user, however i have found that when removing an account, the system did not require the user to input the account password.

### Scenario

  1. The user logins to a shared computer (office, library, cafe) 
  2. Left the account open.
  3. Intruder came and try to delete the users account
  4. Intruder can easily delete the account because the system did not protect it by asking the password to validate that the person deleting the account is the legitimate user.

### Mitigation:

Put reauthentication when anyone/user is deleting an account, ask the user to input password before the completion of the account deletion.

Let me know if you need more information.

Regards
Japz

## Attachments
No attachments
