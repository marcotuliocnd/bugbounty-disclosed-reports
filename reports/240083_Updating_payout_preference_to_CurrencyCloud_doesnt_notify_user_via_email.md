# Updating payout preference to CurrencyCloud doesn't notify user via email

## Report Details
- **Report ID**: 240083
- **URL**: https://hackerone.com/reports/240083
- **State**: Closed
- **Severity**: none
- **Submitted**: 2017-06-15T04:56:28.889Z
- **Disclosed**: 2018-01-31T02:05:10.071Z

## Reporter
- **Username**: dr_dragon
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
When change payment method in user's payments, then a notification about 
Change payment method is sent to the user (email).

However, user not always gets a notification about change payment method - when change payment method via add payout method on Payout Methods, then such a notification is not send to the user (email).

Also,
when user try to change payment method , they were asked to verify the request by entering hackerone password. for the same reason a verification should be there on add payout method.




## Attachments
No attachments
