# User Information leak allows user to bypass email verification.

## Report Details
- **Report ID**: 163467
- **URL**: https://hackerone.com/reports/163467
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-08-26T02:48:11.338Z
- **Disclosed**: 2016-09-12T18:47:08.559Z

## Reporter
- **Username**: cablej
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: legalrobot

## Vulnerability Information
When a user is logged on, the following is sent:

```
██████
```

This contains some sensitive information, most notably the email token. A user can use this to bypass email verification and verify any email.

In addition, the hashed password is leaked, which could present a vulnerability if a user's account is compromised without compromising the password.

## Attachments
No attachments
