# User Enumeration when adding email to account

## Report Details
- **Report ID**: 223531
- **URL**: https://hackerone.com/reports/223531
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-04-24T18:23:39.916Z
- **Disclosed**: 2017-05-17T15:20:24.394Z

## Reporter
- **Username**: atruba
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
It is possible to find all the Register emails which can be use for spam or other purposes

csrfmiddlewaretoken token can be used more than one.
All Register Email can be found by just brute force attack.
Your web endpoint https://demo.weblate.org/accounts/email/ when changing email after login.
Implementtion:
Implement a Captcha.

## Attachments
No attachments
