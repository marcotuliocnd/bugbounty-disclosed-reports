# CSRF Token Bypass in Account Deletion

## Report Details
- **Report ID**: 182487
- **URL**: https://hackerone.com/reports/182487
- **State**: Closed
- **Severity**: low
- **Submitted**: 2016-11-16T11:14:50.871Z
- **Disclosed**: 2017-04-20T16:50:53.899Z

## Reporter
- **Username**: 7h0r4pp4n
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
The authentication token `authenticity_token` used in the POST request for deleting an account can be bypassed, by replacing the same with a token generated for deleting another account. This way, a self submitting form can be used to delete another user's account as long as he/she's logged in.

**Steps to Reproduce:**
1. Create an account and copy the POST request for deleting it.

```
POST /users HTTP/1.1
Host: gitlab.com
Referer: https://gitlab.com/profile/account
Cookie: _gitlab_session=1staccount_cookie;
Content-Type: application/x-www-form-urlencoded

_method=delete&authenticity_token=auth_1staccount
```
2. Create another account and send the above request after replacing the `_gitlab_session` cookie with that of the new one.  The `authenticity_token` remains the same as that of the first account.
3. Send the request and the new account gets deleted.

I have not explored all possible scenarios like different IP addresses or something. But the above situation, where I used accounts created using emails from a temporary email address generator, was reproduced multiple times.

## Attachments
No attachments
