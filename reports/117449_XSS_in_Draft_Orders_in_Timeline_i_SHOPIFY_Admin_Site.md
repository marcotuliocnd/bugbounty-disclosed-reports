# XSS in Draft Orders in Timeline i SHOPIFY Admin Site!

## Report Details
- **Report ID**: 117449
- **URL**: https://hackerone.com/reports/117449
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-02-19T16:48:32.007Z
- **Disclosed**: 2016-07-28T16:25:00.228Z

## Reporter
- **Username**: nismo
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information

1. Create an Draft with a product named "><img src=x onerror=prompt('XSSP')
2. Send the Draft to someone and complete the order.
Order is shown as Completed Drafts as order.png
3. Create a timeline and reference this Draft. As soon as you click POST you will be XSSEd (xss.png)

Thanks

## Attachments
No attachments
