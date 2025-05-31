# Subdomain takeover of v.zego.com

## Report Details
- **Report ID**: 1180697
- **URL**: https://hackerone.com/reports/1180697
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-04-29T23:47:33.652Z
- **Disclosed**: 2021-06-26T04:22:26.339Z

## Reporter
- **Username**: ian
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: zego

## Vulnerability Information
## Summary
v.zego.com points to an AWS EC2 instance at 52.214.138.192 that no longer exists. I was able to take control of this IP address and run my own EC2 instance. I can now serve content on this domain, obtain a TLS certificate for this domain, etc.

If any customers or servers are pointing to anything within this domain, I could serve them arbitrary/malicious content. I could also use this in case your domain whitelists your own domain for OAuth, or if there are cookies scoped to the entire domain. Usually this can have a high impact.

### PoC
```
% dig +short v.zego.com
52.214.138.192

% curl v.zego.com
<!-- hackerone.com/ian -->
```

## Impact

Subdomain takeover

## Attachments
No attachments
