# Subdomain takeover of ████.jitsi.net

## Report Details
- **Report ID**: 1197013
- **URL**: https://hackerone.com/reports/1197013
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-05-14T06:14:10.099Z
- **Disclosed**: 2021-05-14T17:35:31.575Z

## Reporter
- **Username**: ian
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: 8x8-bounty

## Vulnerability Information
## Summary
█████.jitsi.net points to an AWS EC2 instance at 18.195.93.116 that no longer exists. I was able to take control of this IP address and run my own EC2 instance. I can now serve content on this domain, obtain a TLS certificate for this domain, etc.

If any customers or servers are pointing to anything within this domain, I could serve them arbitrary/malicious content. I could also use this in case your domain whitelists your own domain for OAuth, or if there are cookies scoped to the entire domain. Usually this can have a high impact.

```
% dig +short ██████.jitsi.net
18.195.93.116

% curl ██████████.jitsi.net
<!-- hackerone.com/ian -->
```

## Impact

Subdomain takeover

## Attachments
No attachments
