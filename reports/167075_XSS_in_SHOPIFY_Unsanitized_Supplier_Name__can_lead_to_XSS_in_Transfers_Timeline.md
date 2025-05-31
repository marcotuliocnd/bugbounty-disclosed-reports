# XSS in SHOPIFY: Unsanitized Supplier Name  can lead to XSS in Transfers Timeline

## Report Details
- **Report ID**: 167075
- **URL**: https://hackerone.com/reports/167075
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-09-09T10:38:00.021Z
- **Disclosed**: 2016-09-19T16:02:32.881Z

## Reporter
- **Username**: nismo
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hello

I would like to report an XSS happening in Transfer Timeline because the Supplier Name input is not sanitized as it should!

***POC***
Set Supplier Name to "><img src=x onerror=prompt('XSS')>
Create a Transfer with multiple items and cancel on of the items.
Review the timeline
In the timeline you will see `You canceled items in a shipment from SUPPLIER NAME` which since it is unsanitized it will trigger XSS

{F118573}
{F118574}

Live XSS is here https://whitehat-3.myshopify.com/admin/transfers/11073

Hope it will be triaged and fixed



## Attachments
- xsslocation.PNG
- xsssupplier.PNG
