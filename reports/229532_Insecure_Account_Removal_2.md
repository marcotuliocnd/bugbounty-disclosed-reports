# Insecure Account Removal #2

## Report Details
- **Report ID**: 229532
- **URL**: https://hackerone.com/reports/229532
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-05-18T07:08:00.927Z
- **Disclosed**: 2018-08-28T01:29:13.456Z

## Reporter
- **Username**: japz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
Hi Team,

This report is the pretty much same of my closed report here: #223355 , the difference is __[BUG#2] when a user created an account BUT did not supply the password__, therefor there is nothing to reauthenticate when deleting the account, it will successfully delete the account without supplying password because the user not yet set his/her password.

The removal of account is one of the sensitive part of a web application that needs to protect, therefor removing an account should validate the authenticity of the legitimate user.

  1. The user create a weblate account to a shared computer (office, library, cafe)
  2. The user not yet set his/her password
  3. Left the account open.
  4. Intruder came and try to delete the users account
  5. Intruder can easily delete the account because the system did not protect it by asking the password to validate that the person deleting the account is the legitimate user.

### Mitigation:

I am not sure how you are going to handle this one, because reauthentication is the solution for this, but since the user not yet set his/her password, reauthentication will not work and the account can delete successfully, please consider my suggestion below.

### Suggestion to mitigate this:

The password creation should be enforced on the registration form, that will resolved many issues regarding the login and password reset mentioned on my other report here: #229528

When the user already have password on account registration, you don't have to touch the code of the account deletion form, you can leave it as it is since the user already have password to reauthenticate.

Let me know if you need more information or if there is anything i can help with.

Regards
Japz

## Attachments
No attachments
