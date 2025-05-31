# Subdomain takeover on svcgatewayus.starbucks.com

## Report Details
- **Report ID**: 325336
- **URL**: https://hackerone.com/reports/325336
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2018-03-13T02:01:15.805Z
- **Disclosed**: 2018-06-25T18:59:58.915Z

## Reporter
- **Username**: 0xpatrik
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: starbucks

## Vulnerability Information
Hello,

this is pretty serious security issue in some context, so please act as fast as possible.

### Overview:

One of the starbucks.com subdomains is pointing to Azure, which has unclaimed CNAME record. ANYONE is able to own starbucks.com subdomain at the moment.

This vulnerability is called subdomain takeover. You can read more about it here:

* https://blog.sweepatic.com/subdomain-takeover-principles/
* https://hackerone.com/reports/32825
* https://hackerone.com/reports/175070
* https://hackerone.com/reports/172137

### Details:

svcgatewayus.starbucks.com has CNAME to s00197tmp0crdfulprod0.trafficmanager.net which has CNAME to 1fd05821-7501-40de-9e44-17235e7ab48b.cloudapp.net. However, 1fd05821-7501-40de-9e44-17235e7ab48b.cloudapp.net is not registered in Azure cloud anymore and thus can be registered by anyone. After registering the Cloud App in Azure portal, the person doing so has full control over content on svcgatewayus.starbucks.com.

### PoC:

http://svcgatewayus.starbucks.com

### Mitigation:

* Remove the CNAME record from starbucks.com DNS zone completely.
* Claim it back in Azure portal after I release it

Regards,

Patrik Hudak

## Impact

Subdomain takeover is abused for several purposes:

* Malware distribution
* Phishing / Spear phishing
* XSS
* Authentication bypass
* ...

List goes on and on. Since some certificate authorities (Let's Encrypt) require only domain verification, SSL certificate can be easily generated.

## Attachments
No attachments
