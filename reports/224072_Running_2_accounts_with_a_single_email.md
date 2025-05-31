# Running 2 accounts with a single email

## Report Details
- **Report ID**: 224072
- **URL**: https://hackerone.com/reports/224072
- **State**: Closed
- **Severity**: none
- **Submitted**: 2017-04-26T14:48:05.355Z
- **Disclosed**: 2017-05-18T07:58:05.815Z

## Reporter
- **Username**: footstep
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
Hi,

While testing, I found a logic flaw which made me to make two accounts with a single email

###Reproduction Steps
- You need 3 emails (Gmail to be precise)
- Register 2 accounts with 2 different emails
- On account 1, add a new email (3rd email) using the Google Auth
- Then delete the previous email
- add a new email (3rd email) using the Google Auth
- Logout and Login, you'll see one with email and other with Google logo
- Delete the  one with Google logo (Auth) leaving the other
- Navigate to https://myaccount.google.com/permissions and remove `Weblate`
- Do the same on account 2 preferably in another browser without the last step (*Navigate....*)
- Now 2 accounts have one email.
- Logout and login (account 2) and you'll see a message like below

{F179708}

Regards,
Shuaib

## Attachments
- Weblate_Error.png
