# Wrong password validation message

## Report Details
- **Report ID**: 265863
- **URL**: https://hackerone.com/reports/265863
- **State**: Closed
- **Severity**: none
- **Submitted**: 2017-09-04T18:46:45.641Z
- **Disclosed**: 2017-10-04T20:44:54.742Z

## Reporter
- **Username**: ashish_r_padelkar
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: legalrobot

## Vulnerability Information
Hello,

Your password validation message seems to be contradicting with the server side validation of password field during new account sign up at `https://app.legalrobot.com/sign-in`.

When you start typing in password field, it says `Passwords must be more than 8 characters` but when you type more than 8 characters with valid combinations of letters, numbers, symbols etc, still it doesn't validate properly and it says, `Please fix this field.` even when  complexity is fair enough.

When you type in 11 characters, then only it takes password as valid.

I think you should either change the message or validate the password field properly.

Also, same problem when login !

Thanks
Ashish

## Attachments
No attachments
