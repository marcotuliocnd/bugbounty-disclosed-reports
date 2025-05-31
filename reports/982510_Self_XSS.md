# Self XSS

## Report Details
- **Report ID**: 982510
- **URL**: https://hackerone.com/reports/982510
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2020-09-15T09:58:16.788Z
- **Disclosed**: 2020-09-17T16:07:54.581Z

## Reporter
- **Username**: ahmedalahmed
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
I have found self xss in `myshopify.com/admin/apps/import-store/`
POC

1 - Go to yourstore.myshopify.com
2 - Go to settings > App -> Import [ maybe ask you for your platform select any one ]
3 -  Upload  file csv with file name payload xss "><img src=xx onerror=alert(document.domain)>

## Impact

XSS Attack

## Attachments
- xss.png
