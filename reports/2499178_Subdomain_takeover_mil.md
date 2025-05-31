# Subdomain takeover ████████.mil

## Report Details
- **Report ID**: 2499178
- **URL**: https://hackerone.com/reports/2499178
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2024-05-10T13:23:09.111Z
- **Disclosed**: 2024-06-27T17:34:10.298Z

## Reporter
- **Username**: martinvw
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Description:**

The subdomain `█████.mil` is pointing to `peosol-lg.███████.`, the domain `██████` is currently available for registration as can be seen at https://www.godaddy.com/nl-nl/domainsearch/find?domainToCheck=█████

Given the rules, residency of the US, of the `us`-tld I decided not to register the domain, also I do believe the output to be enough.

## References

## Impact

Using this vulnerability an attacker can:
- host unwanted/malicious content under your domain
- receive email on subdomains mentioned above
- effectively execute cross-site scripting attacks
- in some cases, steal cookie data
- in some cases, trick password managers into filling passwords

## System Host(s)
██████████.mil

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
See the DIG output:

```
√ martinvw@denali:~/src > dig █████.mil

; <<>> DiG 9.10.6 <<>> ████.mil
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NXDOMAIN, id: 44977
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 1, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 512
;; QUESTION SECTION:
;█████████.mil.			IN	A

;; ANSWER SECTION:
██████████.mil.		3600	IN	CNAME	peosol-lg.███.

;; AUTHORITY SECTION:
us.			900	IN	SOA	a.cctld.us. admin.tldns.godaddy. 1715345748 1800 300 604800 1800

;; Query time: 166 msec
;; SERVER: 8.8.8.8#53(8.8.8.8)
;; WHEN: Fri May 10 15:06:32 CEST 2024
;; MSG SIZE  rcvd: 148
```

And the GoDaddy page: https://www.godaddy.com/nl-nl/domainsearch/find?domainToCheck=███

And whois:

```
√ martinvw@denali:~/src > whois ████████.
% IANA WHOIS server
% for more information on IANA, visit http://www.iana.org
% This query returned 1 object

refer:        whois.nic.us

domain:       US

organisation: Registry Services, LLC
address:      100 S. Mill Ave, Suite 1600
address:      Tempe AZ 85281
address:      United States of America (the)

contact:      administrative
name:         IANA Contact
organisation: Registry Services, LLC
address:      100 S. Mill Ave, Suite 1600
address:      Tempe AZ 85281
address:      United States of America (the)
phone:        +1 480 505 8800
fax-no:       +1 480 393 4275
e-mail:       iana@about.us

contact:      technical
name:         IANA Contact
organisation: Registry Services, LLC
address:      100 S. Mill Ave, Suite 1600
address:      Tempe AZ 85281
address:      United States of America (the)
phone:        +1 480 505 8800
fax-no:       +1 480 393 4275
e-mail:       iana@about.us

nserver:      B.CCTLD.US 156.154.125.70 2001:502:ad09:0:0:0:0:29
nserver:      F.CCTLD.US 2001:500:3682:0:0:0:0:11 209.173.58.70
nserver:      K.CCTLD.US 156.154.128.70 2001:503:e239:0:0:0:3:1
nserver:      W.CCTLD.US 2001:dcd:1:0:0:0:0:15 37.209.192.15
nserver:      X.CCTLD.US 2001:dcd:2:0:0:0:0:15 37.209.194.15
nserver:      Y.CCTLD.US 2001:dcd:3:0:0:0:0:15 37.209.196.15
ds-rdata:     59017 8 2 7daf469d42b5d8e5537fd4dd4b6057710e9a61f72c32eb7fb6526f52277ec2b0

whois:        whois.nic.us

status:       ACTIVE
remarks:      Registration information: http://www.nic.us

created:      1985-02-15
changed:      2024-04-16
source:       IANA

# whois.nic.us

No Data Found
URL of the ICANN Whois Inaccuracy Complaint Form: https://www.icann.org/wicf/
>>> Last update of WHOIS database: 2024-05-10T13:10:37Z <<<
```

## Suggested Mitigation/Remediation Actions
Remove CNAME record █████████.mil



## Attachments
No attachments
