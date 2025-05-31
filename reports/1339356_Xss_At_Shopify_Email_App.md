# Xss At Shopify Email App

## Report Details
- **Report ID**: 1339356
- **URL**: https://hackerone.com/reports/1339356
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-09-14T13:04:40.174Z
- **Disclosed**: 2021-12-24T09:33:27.714Z

## Reporter
- **Username**: shaktiranjan867
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hello Team,
i have found a Xss on the Shopify email app, but it's a bit wired, it's not executing directly but when i am coping the code it is getting executed.

step-1:  Navigate to https://s1-aug.myshopify.com/admin/apps/shopify-email/editor/3694417
step-2:  Add the xss pay load anywhere  like subject, preview text or in the selection body section. "/><img src=x onerror=alert(document.domain)>
step-3: copy the written code

Xss will be fired.

## Impact

Code injection leads to xss

## Attachments
- recording-1631624647311.webm
