# No expiration of session ID after Password change

## Report Details
- **Report ID**: 223327
- **URL**: https://hackerone.com/reports/223327
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-04-24T09:05:25.522Z
- **Disclosed**: 2017-05-17T14:24:34.729Z

## Reporter
- **Username**: str33
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
If an user changes his password, the session persists and new session ID won't be created.

POC - 
1. Make any request and capture it using any proxy (burp)
2. Go to account settings and change the password.
3. Replay the captured request by changing any parameter(username or fullname)
4. You get a response saying our profile settings was updated.
5. When we view our profile, we can actually see that the changes have taken place.

Impact-
This has a fairly moderate impact as the session credentials are still in use even after password change.

## Attachments
No attachments
