# Subdomain takeover of images.crossinstall.com

## Report Details
- **Report ID**: 1406335
- **URL**: https://hackerone.com/reports/1406335
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-11-21T03:12:47.609Z
- **Disclosed**: 2022-01-05T19:58:27.163Z

## Reporter
- **Username**: ian
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
## Summary
images.crossinstall.com points to an AWS S3 bucket that no longer exists. I was able to take control of this bucket and put my own content onto it. I can now serve content on this domain, obtain a TLS certificate for this domain, etc.

If any customers or servers are pointing to anything within this domain, I could serve them arbitrary/malicious content. I could also use this in case your domain whitelists your own domain for OAuth, or if there are cookies scoped to the entire domain. Usually this can have a high impact.

## PoC
Visit images.crossinstall.com/index.html; an HTML comment with my username is present.

```
% dig images.crossinstall.com +short
assets.crossinstall.com.s3.amazonaws.com.
s3-1-w.amazonaws.com.
s3-w.us-east-1.amazonaws.com.
52.217.103.180

% curl images.crossinstall.com/index.html
<!-- hackerone/ian bugcrowd/iangcarroll -->

% whois crossinstall.com | grep Org
Registrant Organization: Twitter, Inc.
Admin Organization: Twitter, Inc.
Tech Organization: Twitter, Inc.
```

## Impact

Subdomain takeover

## Attachments
No attachments
