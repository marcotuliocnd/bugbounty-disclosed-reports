# The password recovery let users know whether an email address exists or not in the website

## Report Details
- **Report ID**: 681468
- **URL**: https://hackerone.com/reports/681468
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2019-08-25T00:03:13.241Z
- **Disclosed**: 2019-11-22T17:51:03.959Z

## Reporter
- **Username**: guilhermesilva
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
URL: https://apps.nextcloud.com/password/reset/

I have tried to recover the password for some emails:

test@test.com (exists)
teste@teste.com.br (does not exists)

After I clicked the "reset my password"'s button, the website informed that the email did not exist.

## Impact

This is a bad practice, and it is an invitation to brute force emails that possibly exist in the domain @nextcloud.com.

By using a wordlist of common passwords, it is possible to guess a combination of email/password of an administrator account.

## Attachments
No attachments
