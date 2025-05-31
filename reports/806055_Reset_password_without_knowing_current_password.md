# Reset password without knowing current password

## Report Details
- **Report ID**: 806055
- **URL**: https://hackerone.com/reports/806055
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-02-27T08:10:11.796Z
- **Disclosed**: 2020-03-25T19:58:45.521Z

## Reporter
- **Username**: naategh
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
## Description
Hi team,
I found an interesting flaw in your password recovery mechanism that can get the ability of reset password without a valid token and knowing current password. I'm going to explain it here:
In https://www.twitterflightschool.com/ domain if you try to reset your password from https://www.twitterflightschool.com/student/authentication/request_password_reset you'll get a reset password link in your email that is like:
`https://www.twitterflightschool.com/student/authentication/reset_password/<TOKEN>`
**If you logged in to your account**  your application doesn't validate token at all, Actually for reset password, we don't need a token! and just via `https://www.twitterflightschool.com/student/authentication/reset_password/` link, we can reset our password!

In this domain, On the profile page, for changing the password you should enter the current password first but using this issue it's possible to bypass this and update the password without knowing the current password.
**Note:** For abusing this issue an attacker first need to hijack victim's session because while you using `https://www.twitterflightschool.com/student/authentication/reset_password/` to change password it changes current user password, So attack scenario is limited to when an attacker successfully hijacked a victim session and hi want to update password (but he don't know current password), Hi use this issue to bypass `Change Password` in profile section and update password without knowing the current password.

## PoC
With the assumption that the victim's twitter session is 'hijacked' and in a 'logged in' state for the hacker. The below steps must be followed In order to reproduce the security vulnerability.

- Go to https://www.twitterflightschool.com/ and login to your account
- Go to https://www.twitterflightschool.com/student/authentication/reset_password/
- Enter your new password and click on `Update Password`
- It will say that `Password successfully updated`
- Now logout from your account then try to login again
- You'll get you can't login with your previous password and you should enter that password you entered in the above step

## Fix
For fixing this simply you can reject requests to `/student/authentication/reset_password/` endpoint without a valid token even while user logged in.

## Impact

An attacker after hijacking a victim session can abuse this to update the password while he doesn't know the current password, By changing the password he can block user access to his account.

Best regards,
@Naategh

## Attachments
No attachments
