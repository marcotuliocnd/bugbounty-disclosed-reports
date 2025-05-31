# Stored XSS on new Calling plugin (spreed)

## Report Details
- **Report ID**: 190870
- **URL**: https://hackerone.com/reports/190870
- **State**: Closed
- **Severity**: high
- **Submitted**: 2016-12-13T16:47:24.296Z
- **Disclosed**: 2016-12-13T21:08:22.342Z

## Reporter
- **Username**: coolboss
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
There's a stored xss vulnerability ....

Proof Of Concept :
===============
1. Set `name` as an xss payload like `"x><img src=a onerror=alert(1)>`.
{F143238}
2. Invite people to single call room.
3. Xss will execute in IE. (It doesn't support CSP)
{F143237}

Impact :
========
Admin user can be xssed via this method if admin uses browsers like IE.

Let me know if you need help in reproducing

## Attachments
- xss.png
- name.png
