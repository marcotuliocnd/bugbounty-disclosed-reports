# [ addons-preview-cdn.mozilla.net ] A subdomain takeover is available via unregistered domain in Fastly

## Report Details
- **Report ID**: 2706358
- **URL**: https://hackerone.com/reports/2706358
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2024-09-08T01:13:39.169Z
- **Disclosed**: 2024-12-06T10:52:26.197Z

## Reporter
- **Username**: haveaniceday
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mozilla

## Vulnerability Information
## Summary

The domain **addons-preview-cdn.mozilla.net** will CNAME resolve to **addons.allizom.org**, which resolves within Fastly's service.  The domain **addons-preview-cdn.mozilla.net** was not registered within Fastly, which resulted in an error that says "Fastly error: unknown domain"  

After registering this domain on Fastly, I was able to serve custom content on **addons-preview-cdn.mozilla.net**.  

## Proof-of-Concept

1. Go to [http://addons-preview-cdn.mozilla.net/haveanicetakeover-poc.html](http://addons-preview-cdn.mozilla.net/haveanicetakeover-poc.html?x)

## Supporting Material

* Screenshot of [http://addons-preview-cdn.mozilla.net/haveanicetakeover-poc.html](http://addons-preview-cdn.mozilla.net/haveanicetakeover-poc.html?x) displaying custom content

## Impact

## Summary:
A subdomain takeover can be a serious issue, in which an attacker can load their own content while impersonating a targeted victim. 

This impersonation can be abused for numerous impacts, including, but not limited to:

* Cookie Stealing
* Phishing Campaigns (i.e. Stealing Credentials)
* Cross-Site Scripting (XSS)
* Authentication Bypass
* Malware Distribution

More information on the impact of subdomain takeovers can be found at: https://0xpatrik.com/subdomain-takeover-impact/

## Fix

In order to fix this bug, one only needs to remove the CNAME DNS record for **addons-preview-cdn.mozilla.net**, so that it not longer points to **addons.allizom.org**  Alternatively, the domain **addons-preview-cdn.mozilla.net** could be claimed within Fastly, in order to properly direct this domain to the correct endpoint.

If you have any questions about this report, please let me know.

Thank you,

Have a Nice Day!

## Attachments
- feeds.support.dyson.com-takeover.png
