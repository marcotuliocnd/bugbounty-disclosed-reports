# Stored XSS on activity

## Report Details
- **Report ID**: 391390
- **URL**: https://hackerone.com/reports/391390
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-08-07T17:31:29.764Z
- **Disclosed**: 2018-08-14T20:29:30.810Z

## Reporter
- **Username**: shazadsadiq
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hi security team members,

#Description
I found a store xss on the activity which allows an attacker to steal admin account cookies.

#Step to reproduce
1-Create store
2- Add a member in a store
3- Member can choose any name 
4- So change the any member name with hunter"><svg/onload=alert(2)>
5- Now on admain account make changes 
6- That will create activity with attacker malicious payload

#POC
Please see the below image
{F329469}
Let me know if more information is needed to my end.
Best Regards,
Shahzad

## Impact

An attacker(staff member) can takeover admin account.

## Attachments
- Untitled.png
