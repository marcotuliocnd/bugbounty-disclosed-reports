# Session works after logout from Shopify account and password of online store is displayed

## Report Details
- **Report ID**: 837729
- **URL**: https://hackerone.com/reports/837729
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-04-03T04:56:50.206Z
- **Disclosed**: 2020-04-27T16:09:54.014Z

## Reporter
- **Username**: premium101
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
When a user creates a Shopify Lite Plan account, in the product creation stage when the account has not been upgraded, the store's password is enabled such that any visitor who wants to access the store is required to enter password before being granted access to view the products listed in the online store. 

When a logout request has been made and response has been received/displayed that logout is successful, session still works when
https://unctify.myshopify.com/accounts/passwords is entered in the browser url address bar; the resulting Shopify page displays the password required to enter the store which is supposed to be visible to only the admin and those who have been sent this password.

Please see the PoC attached.

## Impact

Third party can view the listed products and also exploit the user session vulnerability.

## Attachments
- Session_not_logged_out__displayed_page_password.avi
