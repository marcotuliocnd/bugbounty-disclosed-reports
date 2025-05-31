# Open Redirect on Login Page of Stocky App

## Report Details
- **Report ID**: 1087189
- **URL**: https://hackerone.com/reports/1087189
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-01-26T04:31:23.806Z
- **Disclosed**: 2021-02-11T19:18:29.723Z

## Reporter
- **Username**: luc1d
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Vulnerable app is Stocky,
1. Visit login page of app with vulnerable parameter & malicious website address`(?return_to=//evil.com)` like `https://stocky.shopifyapps.com/users/login?return_to=//evil.com`
2. Then login to account
3. Open Redirect is executed

PoC Video:
{F1172071}

## Impact

Open Redirect

## Attachments
- shopify_open_redirect.mov
