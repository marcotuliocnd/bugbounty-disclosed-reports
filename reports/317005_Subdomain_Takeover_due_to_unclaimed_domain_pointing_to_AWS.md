# Subdomain Takeover due to unclaimed domain pointing to AWS

## Report Details
- **Report ID**: 317005
- **URL**: https://hackerone.com/reports/317005
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-02-17T01:29:54.029Z
- **Disclosed**: 2019-08-26T18:58:39.212Z

## Reporter
- **Username**: zephrfish
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gsa_bbp

## Vulnerability Information
**Note: I know this is on an out of scope domain, however felt it should still be raised as it was the only subdomain of data.gov to be vulnerable.**

## Issue Details

The consultant identified that subdomain `https://18f.domains.api.data.gov/` is pointing to `dn9rrjaiux2m0.cloudfront.net` via a DNS CNAME record. When browsing to the subdomain an AWS cloudflare error is displayed.

The subdomain "https://18f.domains.api.data.gov/" was (and still is) a CNAME pointing to a AWS Cloudfront CDN server (depending on your location, the latter will resolve differently):

```
 nslookup  18f.domains.api.data.gov
Server:         213.186.33.99
Address:        213.186.33.99#53

Non-authoritative answer:
18f.domains.api.data.gov        canonical name = dn9rrjaiux2m0.cloudfront.net.
Name:   dn9rrjaiux2m0.cloudfront.net
Address: 52.85.89.116
Name:   dn9rrjaiux2m0.cloudfront.net
Address: 52.85.89.87
Name:   dn9rrjaiux2m0.cloudfront.net
Address: 52.85.89.105
Name:   dn9rrjaiux2m0.cloudfront.net
Address: 52.85.89.202
Name:   dn9rrjaiux2m0.cloudfront.net
Address: 52.85.89.145
Name:   dn9rrjaiux2m0.cloudfront.net
Address: 52.85.89.21
Name:   dn9rrjaiux2m0.cloudfront.net
Address: 52.85.89.64
Name:   dn9rrjaiux2m0.cloudfront.net
Address: 52.85.89.161
Name:   dn9rrjaiux2m0.cloudfront.net
Address: 2600:9000:2045:d000:3:f914:5e00:93a1
Name:   dn9rrjaiux2m0.cloudfront.net
Address: 2600:9000:2045:6600:3:f914:5e00:93a1
Name:   dn9rrjaiux2m0.cloudfront.net
Address: 2600:9000:2045:6400:3:f914:5e00:93a1
Name:   dn9rrjaiux2m0.cloudfront.net
Address: 2600:9000:2045:5000:3:f914:5e00:93a1
Name:   dn9rrjaiux2m0.cloudfront.net
Address: 2600:9000:2045:be00:3:f914:5e00:93a1
Name:   dn9rrjaiux2m0.cloudfront.net
Address: 2600:9000:2045:c400:3:f914:5e00:93a1
Name:   dn9rrjaiux2m0.cloudfront.net
Address: 2600:9000:2045:4400:3:f914:5e00:93a1
Name:   dn9rrjaiux2m0.cloudfront.net
Address: 2600:9000:2045:7000:3:f914:5e00:93a1

```

However, the hostname  was not claimed any more on Cloudfront, resulting in a Cloudfront error page when visiting the subdomain before the takeover.

Subsequently, a new Amazon Cloudfront CDN endpoint was created and linked to an attacker-controlled origin server. For the new Cloudfront CDN endpoint, `18f.domains.api.data.gov` was designated as hostname successfully:

{F264221}

This concluded the subdomain takeover:

{F264222}

## Risk Breakdown
- Risk: High
- Difficulty to Exploit: Medium
- CVSS3 Score: 7.7 AV:N/AC:L/PR:N/UI:N/S:C/C:L/I:L/A:L/E:P/RL:O/RC:R

## Affected URLs

- 18f.domains.api.data.gov

## Attack Scenario

1. TTS starts using a new service, eg an external Support Ticketing-service, in this case aws.
2. TTS points a subdomain to the Support Ticketing-service, eg 18f.domains.api.data.gov
3. TTS stops using this service but does not remove the subdomain redirection pointing to the ticketing system.
4. Attacker signs up for the Service and claims the domain as theirs. No verification is done by the Service Provider, and the DNS-setup is already correctly setup.
5. Attacker can now build a complete clone of the real site, add a login form, redirect the user, steal credentials (e.g. admin accounts), cookies and/or completely destroy business credibility for your company.

## Recommendation
The most effective way to remediate this issue would be to remove the DNS entry entirely however if this is not possible, consider pointing the DNS entry at a redirect of some description to prevent potential hostile take over.

## Impact

Sub-domain take over attacks can happen when a company creates a dns entry that points to a third party service, however forgets about the third party application leaving it vulnerable to be hijacked by another party. Hackers can claim subdomains with the help of external services. This attack is practically non-traceable.

## Attachments
- claimed_sub.png
- zephrfish_h1_takeover.png
