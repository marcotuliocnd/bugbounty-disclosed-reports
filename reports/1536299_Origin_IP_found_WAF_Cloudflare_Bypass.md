# Origin IP found, WAF Cloudflare Bypass

## Report Details
- **Report ID**: 1536299
- **URL**: https://hackerone.com/reports/1536299
- **State**: Closed
- **Severity**: low
- **Submitted**: 2022-04-09T19:56:57.092Z
- **Disclosed**: 2022-05-15T10:20:52.125Z

## Reporter
- **Username**: tarun_sec
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: smtp2go

## Vulnerability Information
Description:
I have discovered that the http://172.105.190.180/login/  site exposed it's IP
which could allow bypassing of anti-DDoS mechanisms i.e you are using
Cloudflare for protection.
For Originate IP address which I found from https://search.censys.io/

By using these IP address as a resolver instead of the intended
addresses I'm able to access the service without going through the
WAF, thus I'm able to forward unfiltered payloads to the service, as
well as avoiding the common protections offered by Cloudflare, also
being able to perform crippling denial-of-service towards the origin.

Suggestion:
My recommendations fall in line with Cloudflare's own guidelines: the
Origin server must communicate exclusively with Cloudflare's IP
address ranges, otherwise--as reported in this post on Cloudflare's
blog, the protection offered by having a reverse proxy basically
becomes useless.
IP
1  172.105.190.180
2  139.162.232.147
Files Attached

## Impact

As reported in many other submissions, Cloudflare bypasses can have a
significant impact, as any adversary is now able to communicate with
the origin server directly, enabling them to perform unfiltered
attacks (such as denial-of-service), and data retrieval

## Attachments
- recording-1649534157213.webm
