# Subdomain Takeover in http://genghis-cdn.shopify.io/ pointing to Fastly 

## Report Details
- **Report ID**: 165309
- **URL**: https://hackerone.com/reports/165309
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-09-02T15:25:15.655Z
- **Disclosed**: 2016-09-06T15:46:49.314Z

## Reporter
- **Username**: peroni
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hi,

I've found a Shopifu cdn domain here which had an instance of fastly setup but did not remove the dns record when the service was cancelled. a subdomain takeover similar to that of https://hackerone.com/reports/32825 could be possible.

Vulnerable URL: http://genghis-cdn.shopify.io

Page Response: 
```
Fastly error: unknown domain: genghis-cdn.shopify.io. Please check that this domain has been added to a service.
```

Which indicate that this domain is point to fastly but there is no app in fastly with that name allowing anyone to claim it.
The subdomain "http://genghis-cdn.shopify.io/" is currently pointing to Fastly (shopify-e.map.fastly.net), but is not registered to a service. 

```
$ host genghis-cdn.shopify.io
genghis-cdn.shopify.io is an alias for shopify-e.map.fastly.net.
shopify-e.map.fastly.net is an alias for prod.shopify-e.map.fastlylb.net.
prod.shopify-e.map.fastlylb.net has address 151.101.60.108
```


Thanks!

## Attachments
No attachments
