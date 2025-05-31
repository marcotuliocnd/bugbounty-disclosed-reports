# Reflected XSS on $Any$.myshopify.com/admin

## Report Details
- **Report ID**: 422707
- **URL**: https://hackerone.com/reports/422707
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-10-11T19:25:34.947Z
- **Disclosed**: 2018-11-13T10:16:42.532Z

## Reporter
- **Username**: dr_dragon
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
# Description :
Hi,
I have found a reflected cross site scripting vulnerability in <any>.myshopify.com/admin through return_url parameter .

# Step to reproduce :
1-Go to https://<Any>.myshopify.com/admin/authenticate?return_url=javascript:alert(100)//
2-Click on reload this page
3-Xss alert message

## Impact

Xss attack in <Any>.myshopify.com/admin

## Attachments
- 1.PNG
- 2.PNG
