# [ux.shopify.com] Subdomain takeover

## Report Details
- **Report ID**: 221631
- **URL**: https://hackerone.com/reports/221631
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-04-17T18:45:14.594Z
- **Disclosed**: 2018-10-19T13:55:29.578Z

## Reporter
- **Username**: bobrov
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
The subdomain ux.shopify.com points to domains.tumblr.com, but this subdomain is not used by anyone on Tumblr. Any user can register his blog for this subdomain.
```
ux.shopify.com.	3600	IN	CNAME	domains.tumblr.com.
```
{F176574}

As an PoC, I registered a blog for this subdomain. It is available only with the password **c7gBX6gELPFLhYOeYxQD**.

http://ux.shopify.com/

{F176578}

You need to remove the DNS entry ux.shopify.com. Or I can release this subdomain so that you can register it.

## Attachments
- Screenshot_at_22-29-52.png
- Screenshot_at_22-42-35.png
