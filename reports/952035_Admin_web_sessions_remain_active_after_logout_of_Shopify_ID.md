# Admin web sessions remain active after logout of Shopify ID

## Report Details
- **Report ID**: 952035
- **URL**: https://hackerone.com/reports/952035
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2020-08-05T18:59:11.102Z
- **Disclosed**: 2020-09-14T18:59:43.268Z

## Reporter
- **Username**: jaka-tingkir
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
previously on #837729 a session is still valid and the store password can be seen.

this time I report that the session is still valid despite changing the email address on the shopify account.

## summary: accounts that have changed email addresses still have permission to enter the store through another browser, so old emails can still have access to the store

## steps for reproduction
1. Change your account email (the account has handled several stores) and confirm (I use Firefox)
2. The email account has been successfully replaced
3. open another browser (chrome beta) and log in with the old email, here you are asked to enter the code from the email and you have successfully logged in the account
4. Try opening your shop and logging in with your old email (here I was directed to enter and still have full access, even after changing my email address).

please see the https://150hy.myshopify.com store (test store) and ████@wearehackerone.com and ██████+top@wearehackerone.com accounts (password = ██████████)

## Impact

access not revoke after changed email address on accounts shopify

## Attachments
No attachments
