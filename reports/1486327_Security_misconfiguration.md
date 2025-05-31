# Security misconfiguration 

## Report Details
- **Report ID**: 1486327
- **URL**: https://hackerone.com/reports/1486327
- **State**: Closed
- **Severity**: high
- **Submitted**: 2022-02-20T07:42:18.460Z
- **Disclosed**: 2022-05-16T09:41:20.201Z

## Reporter
- **Username**: mr23r0
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: lemlist

## Vulnerability Information
## Description :
When we request a magic link to login into the application, and use that same link in multiple browsers, it working there isn't any limit on use of link.

Steps to reproduce :
1. go to app.lemilist.com
2. create a magic link 
3. use it to login 
4. now open another browser or incognito window
5. use that same magic link

And You'll be logged in in your account.

## Impact

If Attacker gets the magic link of user he can login into victim's account.
Account takeover.

Mitigation :
1. Add a limit to magic link and remove the magic link from database after 1 use.
2. only allow the Requester IP to login using the magic link.

## Attachments
No attachments
