# Subdomain takeover of www2.growasyouplan.com

## Report Details
- **Report ID**: 1179193
- **URL**: https://hackerone.com/reports/1179193
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-04-28T23:41:24.322Z
- **Disclosed**: 2021-05-29T19:29:40.612Z

## Reporter
- **Username**: ian
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: palo_alto_software

## Vulnerability Information
## Summary
www2.growasyouplan.com points to an AWS EC2 instance at 67.202.62.93 that no longer exists. I was able to take control of this IP address and run my own EC2 instance. I can now serve content on this domain, obtain a TLS certificate for this domain, etc.

If any customers or servers are pointing to anything within this domain, I could serve them arbitrary/malicious content. I could also use this in case your domain whitelists your own domain for OAuth, or if there are cookies scoped to the entire domain. Usually this can have a high impact.

### Proof of scope
`growasyouplan.com` is owned by the same company as `paloalto.com`.

```
% whois growasyouplan.com | grep Org
Registrant Organization: Palo Alto Software, Inc.
```

### PoC
```
% dig +short www2.growasyouplan.com
67.202.62.93

% curl www2.growasyouplan.com
<!-- hackerone.com/ian -->
```

## Impact

Subdomain takeover

## Attachments
No attachments
