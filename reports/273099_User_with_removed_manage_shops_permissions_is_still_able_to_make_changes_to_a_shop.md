# User with removed manage shops permissions is still able to make changes to a shop 

## Report Details
- **Report ID**: 273099
- **URL**: https://hackerone.com/reports/273099
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-09-29T19:42:07.546Z
- **Disclosed**: 2020-06-12T14:11:14.562Z

## Reporter
- **Username**: flashdisk
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
#Description 
it has been noticed that when a partner account user with `` manage shops `` permissions installs app in the one of the managed shops he can still be able to make changes to the shop through that app although his `` manage shops `` permissions were revoked on partners.shopify.com.

#POC

1. create partners account on partners.shopify.com and add staff member with `` manage shops `` permissions.

2. create development store and login to the store with the created staff account with `` manage shops `` permissions.

3. install order printer app and access that app and press on ``manage templates`` button and create template.

4. after creating the template press on ``delete`` for the created template and intercept the request with burp, don;t send it.

5. go to https://partners.shopify.com/664398/memberships and remove `` manage shops `` permissions for the staff account.

6. send the request from step 4 and you will notice that the template was deleted although the user doesn't have `` manage shops `` permissions.

#NOTE 
I also tested this **Bulk Discounts** app and it gave me permissions to create new discount code for each order although I was missing the `` manage shops `` permissions.

#IMPACT
a partner staff member can make drastic changes to a store after revoking his permissions.

thanks. 

## Attachments
No attachments
