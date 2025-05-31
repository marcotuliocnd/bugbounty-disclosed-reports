# Subdomain takeover on svcgatewaydevus.starbucks.com and svcgatewayloadus.starbucks.com

## Report Details
- **Report ID**: 383564
- **URL**: https://hackerone.com/reports/383564
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2018-07-19T03:32:35.559Z
- **Disclosed**: 2018-07-23T17:45:05.475Z

## Reporter
- **Username**: blurbdust
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: starbucks

## Vulnerability Information
Hello,

This is fairly close to [this report](https://hackerone.com/reports/325336) however these are different subdomains than the one in the report.

This can be pretty serious since I can server virtually anything I want. In the 45 minutes I've held the domain I have served to 341 unique IP addresses. 

Two starbucks.com subdomains are pointed to Azure with an unclaimed CNAME record. Anyone would be able to serve content on these subdomains.

##svcgatewayloadus.starbucks.com
```
;; Server: 1.1.1.1:53
;; Size: 191
;; Unix time: 1531965036
;; ->>HEADER<<- opcode: QUERY, status: NXDOMAIN, id: 3697
;; flags: qr rd ra ; QUERY: 1, ANSWER: 1, AUTHORITY: 1, ADDITIONAL: 0

;; QUESTION SECTION:
svcgatewayloadus.starbucks.com. IN A

;; ANSWER SECTION:
svcgatewayloadus.starbucks.com. 600 IN CNAME s00197tmp0crdfulload0.trafficmanager.net.

;; AUTHORITY SECTION:
trafficmanager.net. 30 IN SOA tm1.msft.net. hostmaster.trafficmanager.net. 2003080800 900 300 2419200 30

```

##svcgatewaydevus.starbucks.com
```
;; Server: 9.9.9.9:53
;; Size: 156
;; Unix time: 1531965036
;; ->>HEADER<<- opcode: QUERY, status: NXDOMAIN, id: 47788
;; flags: qr rd ra ; QUERY: 1, ANSWER: 1, AUTHORITY: 1, ADDITIONAL: 0

;; QUESTION SECTION:
svcgatewaydevus.starbucks.com. IN A                                                                                                                                                            

;; ANSWER SECTION:
svcgatewaydevus.starbucks.com. 600 IN CNAME s00197tmp0crdfuldev0.trafficmanager.net.                                                                                                           

;; AUTHORITY SECTION:
trafficmanager.net. 30 IN SOA tm1.msft.net. hostmaster.trafficmanager.net. 2003080800 900 300 2419200 30
```

#PoC:
http://svcgatewayloadus.starbucks.com/
http://svcgatewaydevus.starbucks.com/

##Mitigation:
Remove the CNAME record from the starbucks.com DNS zone
Claim it in Azure once I release it

## Impact

Subdomain takeover can be used for several purposes:

* Malware
* Phishing / Spear phishing
* XSS
* Authentication bypass

## Attachments
No attachments
