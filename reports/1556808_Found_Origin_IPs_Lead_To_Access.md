# Found Origin IP's Lead To Access ████

## Report Details
- **Report ID**: 1556808
- **URL**: https://hackerone.com/reports/1556808
- **State**: Closed
- **Severity**: low
- **Submitted**: 2022-05-02T20:03:07.428Z
- **Disclosed**: 2022-10-14T14:28:10.096Z

## Reporter
- **Username**: ibrahim0936356
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Discovered that the ██████ site exposed its Non-Cloudflare IP which could allow bypassing of anti-DDoS mechanisms.
Your origin servers are not blocking access from non-Cloudflare servers.This way crawlers can find your origin servers' IPs by checking random IPs until they found your origin server(s).
What makes this especially easy are tools like shodan.io(which can find your origin servers).

## Impact

This attack vector can be extremely bad because with the IP found out an attacker could attack the servers by DDoS or other attacks without being stopped by CloudFlare.

## System Host(s)
████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
Visit these link:
https://www.shodan.io/search?query=hostname%3A████+200

IP:
-███

## Suggested Mitigation/Remediation Actions




## Attachments
No attachments
