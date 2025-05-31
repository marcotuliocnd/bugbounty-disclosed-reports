# Emails from Grammarly missing sanitization(lack of validation?) -> HTML injection in emails

## Report Details
- **Report ID**: 404864
- **URL**: https://hackerone.com/reports/404864
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-09-03T21:06:28.515Z
- **Disclosed**: 2019-04-30T06:09:22.333Z

## Reporter
- **Username**: metnew
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: grammarly

## Vulnerability Information
**Summary:** 
Emails from Grammarly (e.g. "reset password" email) missing HTML sanitization. That leads to content spoofing in emails.

## Steps To Reproduce:

1. Go to "Profile"
2. Find reset password tab (if you're logged in using FB/Google, you won't see this menu)
3. Change email to something like: `user@mail.com` -> `user+<h1>2@mail.com`
4. Find the letter from Grammarly in your inbox, about password reset attempt.
5. `<h1>` tag is noticeable.

## Impact

Currently, the impact is miserable - content spoofing in "reset password" emails (sounds like a joke).
However, it's still a bad behavior. I guess that HTML injection through unsanitized/unvalidated input **could affect other Grammarly's email templates**.

## Attachments
- grammarly-html-in-emails.mp4
