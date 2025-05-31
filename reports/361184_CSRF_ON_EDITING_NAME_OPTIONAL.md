# CSRF ON EDITING NAME (OPTIONAL)

## Report Details
- **Report ID**: 361184
- **URL**: https://hackerone.com/reports/361184
- **State**: Closed
- **Severity**: none
- **Submitted**: 2018-06-02T20:48:29.577Z
- **Disclosed**: 2018-06-04T11:49:17.355Z

## Reporter
- **Username**: rootbakar___
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: liberapay

## Vulnerability Information
Allows an attacker to change one's account information in this case ie information from "Name (Optional)". Attackers can change the information without having to login to victim account or without having to login but only by using CSRF technique. I tried changing the "Name (Optional)" information to "YOU HAVE BEEN HACKED".

For reproduce stages I attach in the url https://www.youtube.com/watch?v=aDMd5cjAHZI

potential url with csrf attack https://liberapay.com/talaohu28/edit/username


Regards,
LahatalePutih

## Impact

Change other people's information without having to login

## Attachments
- before.png
- csrf.png
- after.png
