# Reflected XSS in https://██████████ via "████████" parameter

## Report Details
- **Report ID**: 1095765
- **URL**: https://hackerone.com/reports/1095765
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-02-04T20:54:27.261Z
- **Disclosed**: 2021-04-02T18:48:31.884Z

## Reporter
- **Username**: nirajgautamit
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Hello Security Team,
I would like to report the XSS vulnerability on your system.
The `██████████` parameter is not escaped properly for URL encoded values.

██████

## Impact

An XSS attack allows an attacker to execute arbitrary JavaScript in the context of the attacked website and the attacked user. This can be abused to steal session cookies, perform requests in the name of the victim, or for phishing attacks.

## System Host(s)
█████████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
Visit the following POC link:
https://█████████/█████████CE399%22%3E%3C/script%3E%3Cimg%20src=x%20onerror=alert(document.domain)%3E&int_crse_eff_acad_yr=2002&int_crse_eff_term=4&sbjct_srch=true&sbjct_txt=the

## Suggested Mitigation/Remediation Actions
Sanitize the input on that parameter



## Attachments
No attachments
