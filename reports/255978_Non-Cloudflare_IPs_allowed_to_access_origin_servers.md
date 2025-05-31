# Non-Cloudflare IPs allowed to access origin servers

## Report Details
- **Report ID**: 255978
- **URL**: https://hackerone.com/reports/255978
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-08-03T01:59:21.038Z
- **Disclosed**: 2018-02-07T21:43:45.233Z

## Reporter
- **Username**: moritz30
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: unikrn

## Vulnerability Information
**Summary:** Non-Cloudflare IPs allowed to access origin servers

**Description:** Your origin servers are not blocking access from non-Cloudflare servers. This way crawlers can find your origin servers' IPs by checking random IPs until they found your origin server(s).

What makes this especially easy are tools like censys.io (which can find your origin servers).

One of the origin server IPs I found is ███████ but there were quite a few others, too.

This attack vector can be extremely bad because with the IP found out an attacker could attack the servers by DDoS or other attacks without being stopped by CloudFlare.]


## Attachments
No attachments
