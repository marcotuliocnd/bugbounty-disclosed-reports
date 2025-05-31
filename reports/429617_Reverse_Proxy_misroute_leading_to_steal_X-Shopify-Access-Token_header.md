# Reverse Proxy misroute leading to steal X-Shopify-Access-Token header

## Report Details
- **Report ID**: 429617
- **URL**: https://hackerone.com/reports/429617
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-10-27T10:16:39.287Z
- **Disclosed**: 2019-03-14T10:50:35.082Z

## Reporter
- **Username**: chaosbolt
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hello Shopify team! I found out that on /admin/api/graphql endpoint server fetches content of Host header value (${HTTP_Host} + /admin/api/graphql). If my own host was sent to server, request comes from ██████████or ██████████ (your google cloud cluster). Also I can grab all reverse proxy headers including X-Shopify-Access-Token.

example of such request in base64:

```
███
```


Also it returns response your server got on ${HTTP_Host} + /admin/api/graphql address


How to reproduce:
1. POST /admin/api/graphql with Host pointing to external website
2. As external website owner grab incoming headers.

## Impact

SSRF, X-Shopify-Access-Token leakage

## Attachments
- responseleakage.png
