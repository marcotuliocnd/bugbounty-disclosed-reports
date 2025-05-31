# Spamming any user from Reset Password Function

## Report Details
- **Report ID**: 223525
- **URL**: https://hackerone.com/reports/223525
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-04-24T17:59:43.823Z
- **Disclosed**: 2017-05-17T15:20:12.672Z

## Reporter
- **Username**: atruba
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
It is possible to spam any user whose email-id is known.

csrfmiddlewaretoken token can be used more than one.
Users can be spammed heavily by just Brute force attack on password reset page.

Implementtion:
Implement a Captcha.

## Attachments
No attachments
