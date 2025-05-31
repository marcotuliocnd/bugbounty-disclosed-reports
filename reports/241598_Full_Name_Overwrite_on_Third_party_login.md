# Full Name Overwrite on Third party login

## Report Details
- **Report ID**: 241598
- **URL**: https://hackerone.com/reports/241598
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-06-20T07:21:00.626Z
- **Disclosed**: 2017-08-21T17:47:12.291Z

## Reporter
- **Username**: footstep
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
##Description
After one might have logged in on a browser using the *Third party login* (Google) and have made changes to the account like the `Full name`. Making a *third party login* on another browser using the same email overwrites the `Full name` to the name on the email.

One would know he is logged in the same account because the username remains the same.

#####NOTE: This happens when you logout and make a `third party login` again. The `Full name` changes.

Shuaib.

## Attachments
No attachments
