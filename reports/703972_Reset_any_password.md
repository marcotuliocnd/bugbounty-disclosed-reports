# Reset any password

## Report Details
- **Report ID**: 703972
- **URL**: https://hackerone.com/reports/703972
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-09-29T21:45:27.602Z
- **Disclosed**: 2021-03-31T01:58:17.733Z

## Reporter
- **Username**: pdaa
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: pixiv

## Vulnerability Information
## Summary:

When I try to reset the password, the verification code of the mailbox is 6 digits, and there is no limit on the number of submissions, so I can reset the password of any user.

## Steps To Reproduce:
1.input the email  [reset password url](https://www.pixiv.net/reminder.php).
{F595146}
click  the "submit" button
{F595147}
input the email verification code and try to guess the verification code, but I won’t be able to continue using it after I try it a few times.

{F595148}

2.After trying, I found that there was no such submission restriction when the password was reset in the third step.

Repeat the above steps, the only difference is that you need to enter the correct verification code.

{F595160}
It can be seen that when we reset the password in the last step, the verification code will still be sent, that is, the verification code will be sent to the server for validity verification in the last step, and the verification code of the last step is not limited by the number of submissions. In other words, we can guess the verification code.

I wrote a python script to verify the vulnerability, you only need to enter the following parameters to verify the vulnerability.

parameter：tt code_id code phpsession

python: {F595166}
video: {F595172}

## Supporting Material/References:
none

  * [attachment / reference]

## Impact

Reset any user's password

## Attachments
- 0.png
- 1.png
- 2.png
- 3.png
- poc.py
- 4.mp4
