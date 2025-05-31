# No email verification required when we change email from settings

## Report Details
- **Report ID**: 147182
- **URL**: https://hackerone.com/reports/147182
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-06-25T13:58:07.150Z
- **Disclosed**: 2016-07-23T17:34:22.961Z

## Reporter
- **Username**: ahsan
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: fantasytote

## Vulnerability Information
Hey, this is Ahsan Tahir!

Issue:
---------
When we try to signup with an email, it asks us for clicking a email validation link which is sent to our email, then we have to login, without clicking that link, we cannot login, but when we change email from user settings page/edit settings page, it doesn't asks us for validation..

Impact:
----------
For example, a user creates an account with his email (user@example.com) and verifies it using the link which has been sent to his email, as he/she have access to user@example.com, but next he goes  to settings and in email change mechanism, he can put any email like (president@whitehouse.gov) and no verification is required, and the user can login with that email and access his account with the email president@whitehouse.gov, and do some abusive or not good activities and the company will be blamed!

Steps To Reproduce:-
-------------------------
1. Go to sign up form.
2. Enter Any Email.
3. Create account
* The Account will be activated with any email verification!

How to fix?
-------------------
Email verification/validation should be required when a user changed email from user settings page..

I hope you'll fix it soon. :-)

Thanks,
Ahsan Tahir

## Attachments
No attachments
