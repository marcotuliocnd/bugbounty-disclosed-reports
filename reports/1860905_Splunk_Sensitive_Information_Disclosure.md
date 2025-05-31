# Splunk Sensitive Information Disclosure @████████

## Report Details
- **Report ID**: 1860905
- **URL**: https://hackerone.com/reports/1860905
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-02-03T07:36:53.464Z
- **Disclosed**: 2023-02-13T11:58:00.323Z

## Reporter
- **Username**: spell1
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Hi Team,

Hope you are doing great.
I got a domain that contains Splunk Sensitive Information Disclosure @██████████
PoC:
https://███████/en-US/splunkd/__raw/services/server/info/server-info?output_mode=json
█████████

Splunk through 7.0.1 allows information disclosure by appending __raw/services/server/info/server-info?output_mode=json to a query, as demonstrated by discovering a license key.

Reference:
    - https://nvd.nist.gov/vuln/detail/CVE-2018-11409
    - https://github.com/kofa2002/splunk
    - https://www.exploit-db.com/exploits/44865/
    - http://web.archive.org/web/20211208114213/https://securitytracker.com/id/1041148

## Impact

Splunk Sensitive Information Disclosure

## System Host(s)
██████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
Open this link:
https://█████████/en-US/splunkd/__raw/services/server/info/server-info?output_mode=json

## Suggested Mitigation/Remediation Actions




## Attachments
No attachments
