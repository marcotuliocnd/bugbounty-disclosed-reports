# Self XSS in Timeline 

## Report Details
- **Report ID**: 854299
- **URL**: https://hackerone.com/reports/854299
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2020-04-20T14:46:56.815Z
- **Disclosed**: 2020-08-25T17:04:37.224Z

## Reporter
- **Username**: ryat
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Copy the url `javascript:` XSS payload to any Timeline, then click url will trigger XSS.

{F796167}
{F796161}

I previously reported a storefront url XSS at #841361, then admin copy the url to Timeline is possibly.

## Impact

Self XSS

## Attachments
- xss.png
- url.png
