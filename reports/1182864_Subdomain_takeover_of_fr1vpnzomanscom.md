# Subdomain takeover of fr1.vpn.zomans.com

## Report Details
- **Report ID**: 1182864
- **URL**: https://hackerone.com/reports/1182864
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-05-03T08:00:51.175Z
- **Disclosed**: 2021-09-17T05:50:51.808Z

## Reporter
- **Username**: ian
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: zomato

## Vulnerability Information
## Summary
fr1.vpn.zomans.com points to an AWS EC2 instance at 52.47.57.107 that no longer exists. I was able to take control of this IP address and run my own EC2 instance. I can now serve content on this domain, obtain a TLS certificate for this domain, etc.

If any customers or servers are pointing to anything within this domain, I could serve them arbitrary/malicious content. I could also use this in case your domain whitelists your own domain for OAuth, or if there are cookies scoped to the entire domain. Usually this can have a high impact.

Since the risk of employee phishing here is pretty high, along with the risk of existing clients connecting to this server, I think it qualifies as a High per your policy:
> Subdomain Takeover - on a domain that sees heavy traffic or would be a convincing candidate for a phishing attack

### PoC
```
% dig +short fr1.vpn.zomans.com
52.47.57.107

% curl fr1.vpn.zomans.com
<!-- hackerone.com/ian -->
```

## Impact

Subdomain takeover

## Attachments
No attachments
