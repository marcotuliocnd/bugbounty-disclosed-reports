# REGISTRATION USING FAKE EMAIL ACCOUNT

## Report Details
- **Report ID**: 361941
- **URL**: https://hackerone.com/reports/361941
- **State**: Closed
- **Severity**: none
- **Submitted**: 2018-06-05T00:35:56.219Z
- **Disclosed**: 2018-06-05T11:13:32.484Z

## Reporter
- **Username**: rootbakar___
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: liberapay

## Vulnerability Information
1. Go to page https://liberapay.com/sign-up
2. Input email address (I tried to register with some email address)
     * a@a.a
     * b@b.b
     * c@c.c
     * d@d.d
     * e@e.e
3. Select the currency you want to use
4. click "GO" button
5. Will automatically enter into account without going through the process of verification email address first


NOTE:
* Email addresses can be verified before or after a user enters the system

## Impact

Allows an attacker to flood the database with a fake account that is registered with an invalid email

## Attachments
- 2.png
- 1.png
- 3.png
- 4.png
- 5.png
