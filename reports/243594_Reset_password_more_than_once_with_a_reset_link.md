# Reset password more than once with a reset link

## Report Details
- **Report ID**: 243594
- **URL**: https://hackerone.com/reports/243594
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-06-27T11:16:15.416Z
- **Disclosed**: 2017-08-21T18:04:08.592Z

## Reporter
- **Username**: footstep
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
Hi,

Though passwords reset links cannot be used more than once but I found a case where one could do so.

##Reproduction Steps
1. Request a Password Reset on demo.weblate.org
2. Click the reset link in email
3. Enter a new password
4. Click `Set my password`
5. Then you'll be redirected to the login page
6. Click `reset it` again
7. Fill the email and the captcha
8. Click `Reset my Password`
9. Instead of a message to check mail, you'll be prompted with the `Password Reset form`
10. Enter a new password and set it
11. Password successfully changed again
12. Repeat from 6

Shuaib

## Attachments
No attachments
