# Subdomain takeover on 'de-headless.staging.gymshark.com'

## Report Details
- **Report ID**: 1711890
- **URL**: https://hackerone.com/reports/1711890
- **State**: Closed
- **Severity**: high
- **Submitted**: 2022-09-26T00:49:59.598Z
- **Disclosed**: 2022-10-27T11:14:05.926Z

## Reporter
- **Username**: a-p0c
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gymshark

## Vulnerability Information
The Gymshark subdomain https://de-headless.staging.gymshark.com/ was pointing to an unclaimed Shopify site. Because of this an attacker could claim this subdomain, via Shopify, and serve their own content.

This is extremely dangerous as an attacker could serve any malicious content on this domain such as malware, domain defacement, phishing campaigns etc. 

Also, phishing victims wouldn't be able to identify the maliciousness of a potential phishing campaign because it would be from a valid Gymshark subdomain.

**Note:** *I have temporarily claimed this domain for PoC and have password protected the site to reduce unnecessary impact to others. I am happy to remove this protection if you require further takeover evidence*.

## Remediation
- Remove the CNAME record for Shopify on 'de-headless.staging.gymshark.com'.
- I can release 'de-headless.staging.gymshark.com' for reclaim if needed.

## PoC Link
https://de-headless.staging.gymshark.com/

## PoC Evidence
{F1954064}
{F1954066}
{F1954069}
{F1954070}

Thanks, A-p0c

## Impact

If an attacker controlled https://de-headless.staging.gymshark.com/ they could host any malicious content they wanted, such as malware, defacement, a convincing phishing campaign

## Attachments
- image.png
- image.png
- GymsharkSubdomainTakeover_Evidence.mp4
- image.png
