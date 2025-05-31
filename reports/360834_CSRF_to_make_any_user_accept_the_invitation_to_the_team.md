# CSRF to make any user accept the invitation to the team

## Report Details
- **Report ID**: 360834
- **URL**: https://hackerone.com/reports/360834
- **State**: Closed
- **Severity**: none
- **Submitted**: 2018-06-01T16:04:26.199Z
- **Disclosed**: 2018-06-02T13:03:20.245Z

## Reporter
- **Username**: albatraoz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: liberapay

## Vulnerability Information
#Description:
The victim can be tricked into accepting the invite as a normal GET request is sent while accepting the request.

#Steps to reproduce
Make an html page using the following code:
```
<a href="https://liberapay.com/test/membership/accept">click here</a>
```
Change" test" with your team mate.

## Impact

The impact is low but still it can make a user to accept the request even if he wanted not to.

## Attachments
No attachments
