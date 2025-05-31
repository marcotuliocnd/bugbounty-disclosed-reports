# RXSS Via URI Path - https://██████████/

## Report Details
- **Report ID**: 984654
- **URL**: https://hackerone.com/reports/984654
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-09-17T16:52:49.228Z
- **Disclosed**: 2021-10-18T19:26:34.911Z

## Reporter
- **Username**: 0xelkomy
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
>Hello All I Found RXSS in your OWN Website

##Steps To Reproduce
Go to This Link
``https://██████/Orders/(A(%22onerror='alert%60xElkomy%60'testabcd))/Login.aspx?ReturnUrl=/Orders``

##Browsers
I test them on Firefox and Google Chrome.

##Fix:-
Filter input on arrival
Encode data on output
Use appropriate response headers
Content Security Policy.

Regards, xElkomy

## Impact

View any information that the user is able to view. Modify any information that the user is able to modify. Initiate interactions with other application users, including malicious attacks, that will appear to originate from the initial victim user. || And I can used this for
1-Ad-Jacking
2-Session Hijacking
3-Bypassing CSRF protection
4-Crypto Mining ::::)))

## Attachments
No attachments
