# Staff without Manage Themes permissions can update themes

## Report Details
- **Report ID**: 1550400
- **URL**: https://hackerone.com/reports/1550400
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-04-25T16:01:16.986Z
- **Disclosed**: 2024-01-23T18:10:59.189Z

## Reporter
- **Username**: harshdranjan
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hey team,
as per https://help.shopify.com/en/partners/dashboard/account-access#store-access only people with **Manage themes** can View and edit the theme listing, and **upload a new version to the Shopify Theme Store** but **Manage public listings** 	can only Manage apps, themes, and experts listings. not **upload a new version to the Shopify Theme Store** but when a **Owner** gives his **STAFF** permission of **Manage public listings** , he is able to **upload a new version to the Shopify Theme Store** by just going to the https://themes.shopify.com/services/v2/themes/submission/new


## Shops Used to Test:
https://partners.shopify.com/2450201/


## Steps To Reproduce:

1. **owner** invites the **STAFF** with **Manage public listings** and **STAFF** accept it and Login.
2. Now he goes to https://partners.shopify.com/2450201/themes but he won't have access to it so he directly went to "https://themes.shopify.com/services/v2/themes/submission/new"

███████
3. and now he can Uploads a Theme file from the Partner side

and if these are wrong , let me know if there is any detailed version of Permission on Partners.shopify.com as **Manage public listings** is confusing to me a little because of my previous and this report.
## Supporting Material:
Attached

## Impact

Permission mis-configuration ,**STAFF** with **Manage public listings** permission can Upload Theme which is a feature for **Manage themes**

## Attachments
No attachments
