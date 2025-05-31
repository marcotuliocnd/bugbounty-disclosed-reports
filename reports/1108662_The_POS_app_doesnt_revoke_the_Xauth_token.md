# The POS app doesn't revoke the Xauth token 

## Report Details
- **Report ID**: 1108662
- **URL**: https://hackerone.com/reports/1108662
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-02-22T11:19:14.046Z
- **Disclosed**: 2021-04-08T18:37:17.397Z

## Reporter
- **Username**: fr4via
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
It was identified that the POS android application doesn't revoke the authentication token when the user logs off from the session.  More specifically despite the fact that the app removes the entry from the shared_prefs/default_user.xml, the token remains active on the server side and may be used to validate an HTTP request. In order to reproduce the issue, follow the steps bellow:
- Connect to the POS mobile android app 
- Fetch the authentication token, from either the default_user file or from a captured HTTP request 
- Disconnect from the application 
- Use the same token to perform authenticated request in behalf of the account that was connected in the POS

## Impact

An application should always revoke an authentication token by the time that the end user choses to Log Off from a session. Keeping a token active, while the user is not aware of it imposes a big risk, since by the time that an unauthorised entity fetches it, may hijack the user's session and get full control of the store.

## Attachments
No attachments
