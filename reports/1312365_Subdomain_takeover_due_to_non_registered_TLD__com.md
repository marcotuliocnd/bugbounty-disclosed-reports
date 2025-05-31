# Subdomain takeover due to non registered TLD [ ██████████.█████.██████.com ]

## Report Details
- **Report ID**: 1312365
- **URL**: https://hackerone.com/reports/1312365
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-08-19T20:28:25.941Z
- **Disclosed**: 2021-08-31T16:18:38.513Z

## Reporter
- **Username**: 0xprial
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: affirm

## Vulnerability Information
## Summary:
I was looking at recent disclosed report #1297689 and I was thinking to take a look for the same issue on this asset as I love to test for subdomain takeover vulnerabilities. 

While testing I noticed a DNS entry for `███████.████.██████████.com` is CNAME `████.███████████` which's TLD is not registered yet and also not reserved for using Internal DNS Domain Name . As a result, an attacker can register for the `███` TLD to create and takeover **███████.████████.█████.com** subdomain.


## Steps To Re█████████uce:
* Check `CNAME` record of **█████.█████.██████.com** subdomain and you will see a record like below

```
0xPrial@n00b ~ % dig ████.████.████.com

; <<>> DiG 9.10.6 <<>> ██████.█████.████.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NXDOMAIN, id: 27323
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 1, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4096
;; QUESTION SECTION:
;██████.███████.████.com.	IN	A

;; ANSWER SECTION:
██████████.███████.██████.com. 300 IN	CNAME	██████████.██████████████.

;; AUTHORITY SECTION:
.			10800	IN	SOA	a.root-servers.net. nstld.verisign-grs.com. 2021081901 1800 900 604800 86400

;; Query time: 216 msec
;; SERVER: 10.0.0.1#53(10.0.0.1)
;; WHEN: Fri Aug 20 02:18:14 +06 2021
;; MSG SIZE  rcvd: 162

```
* Take a look at **CNAME** value what is `████.████████████.` domain which TLD is **████** what is not registered yet. So it's available to register and buy the domain.
* You can check already registered TLD's from this list: **http://data.iana.org/TLD/tlds-alpha-by-domain.txt**

## Supporting Material/References:
And Internal used reserved domains TLD are
* `.test`
* `.example`
* `.invalid`
* `.localhost`

## Impact

An attacker can register for **████████** TLD to take over the target subdomain by buying **██████████** domain and create `█████.███████` subdomain to serve content on **█████.█████████.█████████.com** subdomain, which can lead to malicious attacks against users. Users will see this as a valid domain of Affirm and they may share their sensitive information with an attacker.


**Reference documents:**
* https://www.itprotoday.com/active-directory/q-can-i-use-local-or-pvt-top-level-domain-tld-names-part-active-directory-ad-tree
* https://helgeklein.com/blog/2008/09/choosing-a-future-proof-internal-dns-domain-name-mission-impossible/


RECOMMENDED FIX
It looks like it was a human error while creating that subdomain record. If it was an error update that DNS record to a correct one or delete it if it's not in need.

Regards
**Prial**

## Attachments
No attachments
