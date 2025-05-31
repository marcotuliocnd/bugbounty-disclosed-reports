# Logout CSRF

## Report Details
- **Report ID**: 223329
- **URL**: https://hackerone.com/reports/223329
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-04-24T09:08:31.928Z
- **Disclosed**: 2017-05-17T14:20:15.774Z

## Reporter
- **Username**: japz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
Hi Team,

This is a low risk but want you to know that logout on this domain `demo.weblate.org` did not protect the logout form with csrf token, therefor i can logout any user by sending this url `https://demo.webplate.org/accounts/logout/`.

Logout should have post method with a valid csrf token.

Let me know if you need more info.

Regards
Japz

## Attachments
No attachments
