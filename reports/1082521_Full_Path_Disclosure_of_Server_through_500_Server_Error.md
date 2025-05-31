# Full Path Disclosure of Server through 500 Server Error

## Report Details
- **Report ID**: 1082521
- **URL**: https://hackerone.com/reports/1082521
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-01-20T15:41:43.064Z
- **Disclosed**: 2021-08-16T17:46:04.025Z

## Reporter
- **Username**: basant0x01
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: kartpay

## Vulnerability Information
Hello team,

EXPLANATION
============
I found a interesting vulnerability into your site that it unexpected disclosing the server path where the PHP files are being hosted. When application sends account verification links in email then if anyone tries to verify his account with that link at a twice then on the title of the website the whole server path is disclosing through 500 Server Error.

Vulnerable Path :
---------------
`/usr/share/ngnix/website/resources/view/auth/create_password.blade.php`


I have added a POC .

## Impact

1. Server Information Disclosure

## Attachments
- Full_Path_Disclosure.mp4
