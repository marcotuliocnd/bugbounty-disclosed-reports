# Take over subdomain undici.nodejs.org.cdn.cloudflare.net

## Report Details
- **Report ID**: 1763817
- **URL**: https://hackerone.com/reports/1763817
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-11-06T23:57:14.008Z
- **Disclosed**: 2023-01-11T04:07:10.952Z

## Reporter
- **Username**: algisec1337
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs

## Vulnerability Information
Hello,

this is a pretty serious security issue in some contexts, so please act as soon as possible

Summary:

I just went to undici.nodejs.org, and I've also checked the IP of the main domain it goes to cdn.cloudflare.net which means if it's not added it can be added to any github account your subdomain should be added to your account so shows the URL you selected. This vulnerability is called subdomain takeover

•Remove CNAME records from DNS zone completely

Poc
http://undici.nodejs.org.cdn.cloudflare.net/

## Impact

Subdomain takeovers are abused for several purposes:

Malware distribution
•Phishing / Spear phishing
•XSS
•Bypass authentication
•...


The list goes on and on. Since some certificate authorities (Let's Encrypt) only require domain verification, SSL certificates can be generated easily.

Regards Algisec1337

## Attachments
- 20221107_064929_edited.mp4
