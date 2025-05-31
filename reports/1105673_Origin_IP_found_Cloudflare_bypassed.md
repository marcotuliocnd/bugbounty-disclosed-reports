# Origin IP found, Cloudflare bypassed

## Report Details
- **Report ID**: 1105673
- **URL**: https://hackerone.com/reports/1105673
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-02-17T15:36:35.592Z
- **Disclosed**: 2021-03-30T10:51:42.976Z

## Reporter
- **Username**: sawmj
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: cs_money

## Vulnerability Information
Greetings!, Hope Y'all good and fine.

## Summary:
I would like to report another vulnerability very Similar to my other report in #975991


Due to lack of secure design, I was able to find the origin IPs behind Cloludflare WAF.

The IPs I found belong to :

3d.cs.money

## Description:

I was able to find and access the Origin IPs behind the WAF due to lack of access control,
I could also port scan the IP 

The IP found :
51.83.253.82

## Steps To Reproduce:
simply visit:

https://51.83.253.82/

## Impact

As reported in many other submissions, Cloudflare bypasses can have a significant impact, as any adversary is now able to communicate with the origin server directly, enabling them to perform unfiltered attacks (such as denial-of-service), and data retrieval.

This attack vector can be extremely bad because with the IP found out an attacker could attack the servers by DDoS or other attacks without being stopped by CloudFlare.]

Thanks!

## Attachments
No attachments
