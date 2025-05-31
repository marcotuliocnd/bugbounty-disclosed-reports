# RXSS - https://███/

## Report Details
- **Report ID**: 864091
- **URL**: https://hackerone.com/reports/864091
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-05-01T15:16:50.460Z
- **Disclosed**: 2021-03-11T20:50:50.933Z

## Reporter
- **Username**: 0xelkomy
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
>Hello All I Found RXSS in your OWN Website


##Steps:-
Add Payload XSS To /████?view=

##Example:-
https://████/█████████?view=%3Cscript%3Ealert(%22xElkomy%22)%3C/script%3E

##Payloads:-
Any payloads XSS

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
