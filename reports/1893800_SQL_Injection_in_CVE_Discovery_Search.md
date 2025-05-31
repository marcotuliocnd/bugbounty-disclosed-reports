# SQL Injection in CVE Discovery Search 

## Report Details
- **Report ID**: 1893800
- **URL**: https://hackerone.com/reports/1893800
- **State**: Closed
- **Severity**: high
- **Submitted**: 2023-03-06T17:55:10.839Z
- **Disclosed**: 2023-03-06T19:52:20.028Z

## Reporter
- **Username**: rcoleman
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**
Unsanitized user-controlled inputs in the CVE Discovery Search allow for SQL injection.

**Description:**
Search terms are split on whitespace but no additional sanitization is applied, allowing arbitrary SQL statements, such as a blind or timing-based attack. 

### Steps To Reproduce

1. Visit https://hackerone.com/intelligence/cve_discovery
2.  Enter a search term that normally returns results, plus an injection payload such as /**/AND/**/'1%'='1 and confirm that the results are still returned
3. Change the payload to /**/AND/**/'1%'='0 and confirm that no results are returned

### Optional: Your Environment (Browser version, Device, etc)

 * Chrome

### Optional: Supporting Material/References (Screenshots)
{F2211684}
{F2211685}

## Impact

Disclosure of  data in Analytics Database, including report, team, and asset data

## Attachments
- image.png
- image.png
- image.png
- image.png
