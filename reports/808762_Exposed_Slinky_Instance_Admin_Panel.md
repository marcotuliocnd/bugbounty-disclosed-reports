# Exposed Slinky Instance Admin Panel

## Report Details
- **Report ID**: 808762
- **URL**: https://hackerone.com/reports/808762
- **State**: Closed
- **Severity**: none
- **Submitted**: 2020-03-02T14:47:05.211Z
- **Disclosed**: 2021-01-16T06:07:40.241Z

## Reporter
- **Username**: rhynorater
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Last night the following server went from a 404 to a 200:
███████

Upon navigating to this page, I found that there was a slinky admin panel available here with the ability to change and modify URL redirection. 
```
https://slinky-server.shopifycloud.com/
```

## Impact

Ability to modify potentially trusted URL redirects

## Attachments
No attachments
