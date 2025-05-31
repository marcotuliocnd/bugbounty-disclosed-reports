# The 'Create a New Account' action is vulnerable to CSRF

## Report Details
- **Report ID**: 109810
- **URL**: https://hackerone.com/reports/109810
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-01-10T21:00:17.524Z
- **Disclosed**: 2016-07-24T03:40:39.513Z

## Reporter
- **Username**: roshanpty
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: coinbase

## Vulnerability Information
The request to create an account wallet doesn't validate if the request is originating from the user itself with the help of an anti-CSRF token. 

Step 1: Craft an HTML page with request to create a wallet in your accounts page. 
https://www.coinbase.com/accounts > New Account > Wallet

Step 2: Open the HTML page in a tab of the browser where a user is already logged in to coinbase. It can be observed that a wallet is created.

PS: In some browsers this may not work. It should be noted that it is not because the application doesn't have a proper CSRF mitigation mechanism, rather the parameter utf8 is improperly rendered.

## Attachments
- Coinbase_CSRF.html
