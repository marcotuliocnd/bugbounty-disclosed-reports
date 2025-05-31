# EC2 Takeover at turn.shopify.com

## Report Details
- **Report ID**: 1295497
- **URL**: https://hackerone.com/reports/1295497
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-08-09T08:45:17.644Z
- **Disclosed**: 2022-03-28T14:21:28.665Z

## Reporter
- **Username**: 0xd0m7
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
**Summary**
Hi team,
It seems that the domain **turn.shopify.com** pointed to an EC2 instance that was terminated and the DNS record wasn't updated. We managed to register a new EC2 instance with the IP that **turn.shopify.com** points to:

**Command**
```
dig turn.shopify.com
; <<>> DiG 9.11.3-1ubuntu1.13-Ubuntu <<>> turn.shopify.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 5523
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 65494
;; QUESTION SECTION:
;turn.shopify.com.		IN	A

;; ANSWER SECTION:
turn.shopify.com.	3600	IN	A	54.90.1.144

;; Query time: 17 msec
;; SERVER: 127.0.0.53#53(127.0.0.53)
;; WHEN: Mon Aug 09 10:41:14 CEST 2021
;; MSG SIZE  rcvd: 61
```

**URL**
``http://turn.shopify.com/0xd0m7``

**POC**
{F1404895}

Saved at:
``https://archive.ph/4ro3x``

## Impact

An EC2 takeover has the same impact as a subdomain takeover, instead of having a dangling CNAME there is a dangling A record. With it we are able to:
Serve phishing pages which are bound to be trusted, since there is no way of finding out that we are the owners. Besides, we could also get an SSL certificate to serve the content via HTTPS. For demonstration purposes we have only opened port 80.
Stored XSS and DoS, as shown in the PoC.
Privilege escalation: we will be checking upon submission of the report, it could be possible to use an XSS to exfiltrate personal information or take over accounts. A comment will be added if this is the case.
SSH sniffing: it'd be possible to open ports and install different services on the machine, amongst them an ssh or ftp server to capture credentials.
Malware distribution.
And many more, basically everything since we now have control over one of your domains.

## Attachments
- xss_hackerone_shopify.png
- 1.png
