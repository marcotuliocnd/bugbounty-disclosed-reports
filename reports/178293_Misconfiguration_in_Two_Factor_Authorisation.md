# Misconfiguration in Two Factor Authorisation

## Report Details
- **Report ID**: 178293
- **URL**: https://hackerone.com/reports/178293
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-10-26T21:12:21.852Z
- **Disclosed**: 2016-12-17T02:49:54.815Z

## Reporter
- **Username**: dhaval
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hey

There seems to be a weird misconfiguration which leads to bypass of two factor authorisation

#### Scenario

1. Let's assume you have setup Two Factor Authorisation with Google Authenticator

2. You now activate `Google Apps` from `Login services` at https://shop-1.myshopify.com/admin/settings/account

3. Now your try to "Sign In with Google" `https://shop-1.myshopify.com/admin/auth/login?google_apps=1`

What's weird is no two factor code is required and you directly land in Admin Panel

#### Issue

Issue here is Two Factor Authorisation is disabled as soon as you "Sign In with Google" and now you cannot even enable it because you can't see any Two Factor Authenticator Tab in Accounts

And now when you try to simple login with correct credentials you can access Admin Panel without Two Factor Code from Google Authenticator at `https://shop-1.myshopify.com/admin/auth/login`

Also there is no indication to via mail or notification that Two Factor Authorisation has been disabled when Two Factor Authorisation is disabled
While it shouldn't be disabled in the first place


## Attachments
No attachments
