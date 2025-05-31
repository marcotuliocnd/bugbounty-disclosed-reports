# It's possible to view configuration and/or source code on uchat.awscorp.uberinternal.com without 

## Report Details
- **Report ID**: 298862
- **URL**: https://hackerone.com/reports/298862
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-12-17T00:36:48.078Z
- **Disclosed**: 2017-12-26T11:02:58.464Z

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
https://uchat.awscorp.uberinternal.com/static/main.740f5a0b92c00e72e2e1.js

## Specifics
* http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2005-2169
* http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2005-0202
* https://www.owasp.org/index.php/Testing_for_Local_File_Inclusion

## Impact

Access to internal configuration files, system names, and source code.

## Attachments
No attachments
