# Open Redirect - www.shopify.com

## Report Details
- **Report ID**: 905737
- **URL**: https://hackerone.com/reports/905737
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-06-22T23:26:02.859Z
- **Disclosed**: 2020-07-14T21:15:20.708Z

## Reporter
- **Username**: zonduu
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hello Shopify team,

I found an open redirect in www.shopify.com

Link:

- `https://www.shopify.com/plus/get-cdn-asset?asset=http://evil.com/?`

**Vulnerable parameter:** `asset`

## Impact

- Open redirect that can lead to phishing and other type of attacks.

Have a good day, zonduu.

## Attachments
No attachments
