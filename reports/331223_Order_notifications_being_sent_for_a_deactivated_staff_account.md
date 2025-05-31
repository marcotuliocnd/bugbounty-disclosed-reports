# Order notifications being sent for a deactivated staff account

## Report Details
- **Report ID**: 331223
- **URL**: https://hackerone.com/reports/331223
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-03-29T21:38:50.768Z
- **Disclosed**: 2018-04-12T08:20:21.139Z

## Reporter
- **Username**: newbie_101
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hi,

Steps to reproduce :
-

- Have a staff account with settings permission
- The staff account can go to notifications & add himself so as to get new order notifications
- Now,deactivate the staff account via the admin.
- Create a new order,you shall see that the staff still receives the order notification via email.
- This happens because the account still exists,but if staff deleted , then there is no account,hence no email) so no notification.

## Impact

- Info disclosure about a customer of a store the staff account cant have access to.

## Attachments
No attachments
