# Open redirect in bulk edit

## Report Details
- **Report ID**: 169759
- **URL**: https://hackerone.com/reports/169759
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-09-16T05:46:18.316Z
- **Disclosed**: 2016-12-04T12:54:10.843Z

## Reporter
- **Username**: zombiehelp54
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hi , 
I have found an open redirection issue when bulk editing resources.
#PoC:
Go to `https://<shop>.myshopify.com/admin/bulk?resource_name=Product&return_to=/..//evil.com` then click the **Close** button and you'll go to *evil.com* 

Thanks!

## Attachments
No attachments
