# Browser Self XSS Protection not implemented

## Report Details
- **Report ID**: 400785
- **URL**: https://hackerone.com/reports/400785
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2018-08-27T06:36:29.256Z
- **Disclosed**: 2018-09-26T11:05:58.392Z

## Reporter
- **Username**: allenaleen
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: portswigger

## Vulnerability Information
Hi

Self XSS Protection not used ,An attacker  can trick users to insert JavaScript in browser console.

A Self-XSS scam usually works by promising to help you access somebody else's account. Instead, the scammer tricks you into gaining access to your account for fraud, spam and tricking more people into a scam.

I see that you have not enabled 'Self XSS Protection ' on https://portswigger.net/ , This technique prevents user from getting tricked into injecting js themselves and allow attackers to socially engineering them..

For example, Facebook have : http://gyazo.com/3b448c200124053b60b622d0149e242d https://www.facebook.com/selfxss

But you don't have it, You should ,  to protect your  users , it prevents the users from  getting  tricked and be safe. Its a best practice every website should follow for a safer web!

This bug has been fixed by many websites including Facebook. So its strongly advised you to fix it.

[Similar fixed issue](https://hackerone.com/reports/76307)

## Impact

Users with low knowledge can be tricked to attack themselves via xss attacks.

#Ref
-  https://stackoverflow.com/questions/21692646/how-does-facebook-disable-the-browsers-integrated-developer-tools
- https://facebook.com/selfxss

Regards

## Attachments
No attachments
