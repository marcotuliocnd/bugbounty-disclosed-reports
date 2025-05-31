# Corda Server XSS ████████

## Report Details
- **Report ID**: 374057
- **URL**: https://hackerone.com/reports/374057
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-06-29T22:11:41.943Z
- **Disclosed**: 2019-12-02T19:06:16.354Z

## Reporter
- **Username**: alyssa_herrera
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**
Cord server will display the error message if something isn't allowed to be used thus allowing xss
**Description:**
/scripts/ctredirector.dll allows users to call images or files. We can use the parameter @_FILE to dictate a file or url, if it fails it'll display the url into the page. We then leverage an additional parameter named @_TEXTDESCRIPTIONEN to make the page display as a text which then allows the opportunity to trigger XSS.
## Impact
Medium
## Step-by-step Reproduction Instructions
Check the following URL in firefox
http://█████████/scripts/ctredirector.dll//?@_FILEhttp://google.com/%3Csvg/onload=confirm(document.cookie)%3E%3E@_TEXTDESCRIPTIONEN

## Product, Version, and Configuration (If applicable)
Corda Server
## Suggested Mitigation/Remediation Actions
Update corda

## Impact

An attacker can steal session cookies and conduct sophisticated phishing campaigns using this exploit

## Attachments
No attachments
