# Configuration and/or source code files on uchat-staging.uberinternal.com can be viewed without OneLogin SSO Authentication 

## Report Details
- **Report ID**: 298990
- **URL**: https://hackerone.com/reports/298990
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-12-17T22:29:41.572Z
- **Disclosed**: 2017-12-26T11:03:14.669Z

## Reporter
- **Username**: gregoryvperry
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: uber

## Vulnerability Information
## Summary
Configuration file and/or source code information leakage without Uber OneLogin SSO authentication.

## Security Impact
Misconfiguration on the server results in information leakage without authentication.

## Reproduction Steps
https://uchat-staging.uberinternal.com/static/main.740f5a0b92c00e72e2e1.js

## Specifics
* http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2005-2169
* http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2005-0202
* https://www.owasp.org/index.php/Testing_for_Local_File_Inclusion

## Impact

Access to internal configuration files, system names, and source code.

## Attachments
No attachments
