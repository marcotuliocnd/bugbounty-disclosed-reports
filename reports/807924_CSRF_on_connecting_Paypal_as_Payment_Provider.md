# CSRF on connecting Paypal as Payment Provider

## Report Details
- **Report ID**: 807924
- **URL**: https://hackerone.com/reports/807924
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-03-01T02:58:21.320Z
- **Disclosed**: 2020-04-10T01:54:21.635Z

## Reporter
- **Username**: ngalog
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hi,

I think there is a weak csrf protection on adding paypal as the payment provider, but the protection is not good. When user try to add paypal as payment provider, they will make this GET request

`https://h60ngalog.myshopify.com/admin/payments/complete_paypal_incontext_oauth/41?merchantId=MTU4MzAzMDUwNDowMTBmMDZkYjg1NzM0YjQ4NWVkMDk1YzQ1YWYxY2ZlNw%3D%3D&merchantIdInPayPal=5NS8DHQCFGT84&permissionsGranted=true&accountStatus=BUSINESS_ACCOUNT&consentStatus=true&productIntentID=addipmt&productIntentId=addipmt&isEmailConfirmed=true`

The `merchantId` belongs to your store only, and the base64 decoded value is `1583030504:010f06db85734b485ed095c45af1cfe7` which is obviously too long to brute force, I'll say it is a pretty good way to mitigate CSRF, however there is one catch. This value is fixed, i.e. if someone who previously was an admin of this store before, then he/she can take advantage of this fixed value for CSRF protection, and perfomr CSRF attack on victim to connect victim's payment provider to their Paypal order. Or this value is leaked somewhere, then the store owner is forever vulnerable to CSRF attack 

## Steps to reproduce
- Visit https://YOURDOMAIN.myshopify.com/admin/settings/payments, if there is already paypal account connected, disconnect it first
- Then click the link Acitivate paypal express checkout
- In the link, jot down the value of merchantId, this merchantId belongs to your store only, in order to connect your store to victim's store, you'll need this parameter, it looks like this `MTU4MzAzMDUwNDowMTBmMDZkYjg1NzM0YjQ4NWVkMDk1YzQ1YWYxY2ZlNw%3D%3D`
- Finally, visit this link with merchantId replaced with the value you got from above step (replace YOUTSUBDOMAIN and REPLACEME)

`https://YOURSUBDOMAIN.myshopify.com/admin/payments/complete_paypal_incontext_oauth/41?merchantId=REPLACEME&merchantIdInPayPal=5NS8DHQCFGT84&permissionsGranted=true&accountStatus=BUSINESS_ACCOUNT&consentStatus=true&productIntentID=addipmt&productIntentId=addipmt&isEmailConfirmed=true`

Here in `5NS8DHQCFGT84` is the attacker's paypal merchant id, so after you visit that link, you got CSRFed to connect your store to my paypal as payment provider, very similar to #807921 but different impact

## Impact

CSRFed to connect your store to my paypal as payment provider, very similar to #807921 but different impact

## Attachments
No attachments
