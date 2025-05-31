# Running 2 accounts with a single email #3

## Report Details
- **Report ID**: 245304
- **URL**: https://hackerone.com/reports/245304
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-07-02T10:46:46.087Z
- **Disclosed**: 2018-08-27T19:06:57.343Z

## Reporter
- **Username**: footstep
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
Following the fixes: #241608 & #224072. there's still another way round this.

##Reproduction Steps
1. Register 2 accounts (Preferably using Gmail not third party)
- Login both accounts on separate browsers
- In Browser1, navigate to https://demo.weblate.org/accounts/profile/#auth
- Add a new association with the Google third party link using the registered email address in Browser2
- Fill the Password and Add the Association
- Disconnect the email on the account initially
- Email will be changed to the new one added in (4)
- Now, both browsers have the same email address i.e 2 accounts with a single email
- Logging out any of the account and trying to login leads to a server error.

Screenshots are attached below.

Shuaib.

## Attachments
No attachments
