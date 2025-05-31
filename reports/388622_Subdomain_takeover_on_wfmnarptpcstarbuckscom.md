# Subdomain takeover on wfmnarptpc.starbucks.com

## Report Details
- **Report ID**: 388622
- **URL**: https://hackerone.com/reports/388622
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-07-30T22:20:33.463Z
- **Disclosed**: 2018-08-09T21:09:10.902Z

## Reporter
- **Username**: 0xpatrik
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: starbucks

## Vulnerability Information
Hello,

this is pretty serious security issue in some context, so please act as fast as possible.

Overview:
One of the starbucks.com subdomains is pointing to Azure, which has unclaimed CNAME record. ANYONE is able to own starbucks.com subdomain at the moment.

This vulnerability is called subdomain takeover. You can read more about it here:

https://0xpatrik.com/subdomain-takeover-basics/

Details:
wfmnarptpc.starbucks.com has CNAME to s00149tmppcrpt.trafficmanager.net. However, s00149tmppcrpt.trafficmanager.net is not registered in Azure cloud anymore and thus can be registered by anyone. After registering the TrafficManager Profile in Azure portal, the person doing so has full control over content on wfmnarptpc.starbucks.com.

PoC:
http://wfmnarptpc.starbucks.com/poc.html

 Mitigation:
Remove the CNAME record from starbucks.com DNS zone completely.
Claim it back in Azure portal after I release it
Regards,

Patrik Hudak

## Impact

Subdomain takeover is abused for several purposes:

Malware distribution
Phishing / Spear phishing
XSS
Authentication bypass
...
List goes on and on. Since some certificate authorities (Let's Encrypt) require only domain verification, SSL certificate can be easily generated.

## Attachments
- Screen_Shot_2018-07-31_at_00.19.53.png
