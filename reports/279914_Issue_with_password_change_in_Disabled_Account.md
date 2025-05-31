# Issue with password change in Disabled Account

## Report Details
- **Report ID**: 279914
- **URL**: https://hackerone.com/reports/279914
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-10-18T16:32:40.515Z
- **Disclosed**: 2017-11-16T23:24:17.010Z

## Reporter
- **Username**: 0xm1racle
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
Hello Hackerone,

**Summary:**
I have found that #38343 is not yet fully fixed, disabled user is not always gets notification about password change when a password is changed via password reset link, then such a notification is not send to the disabled user.

**Description (Include Impact):**
When a password changed in user's profile `When a password changed in user's profile` or `password reset links` for `enabled/active user` receives a notification via email containing that the password was recently changed. This is the fixed that reported in #38343. 

However, it defeats the fix in #38343 because when a password changed in `password reset links` for `disabled/inactive user` does not receive notification via email containing that password was recently changed.

__POC__ 
https://vimeo.com/214135835
password: protection

## Attachments
No attachments
