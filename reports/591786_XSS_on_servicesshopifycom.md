# XSS on services.shopify.com

## Report Details
- **Report ID**: 591786
- **URL**: https://hackerone.com/reports/591786
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-05-28T20:08:24.042Z
- **Disclosed**: 2019-06-14T18:39:04.294Z

## Reporter
- **Username**: encryptsaan123
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hy security,
 i Got a stored xss in one of your sub-domain "services.shopify.com"

steps:
1- Go to https://(your_store).myshopify.com/admin/apps/experts_marketplace/services_marketplace
2- Then Go to  All services>Marketing and sales>email marketing> Design custom email templates >click select
3- fill al the data, there will be an option for "attach file"
4: selcet a html file where the xss payloads are got stored.
5. write click on the attached file and go to that location, you will see the pop-up

## Impact

can steal cookies

## Attachments
- Untitled.png
