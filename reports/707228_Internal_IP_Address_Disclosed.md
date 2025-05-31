# Internal IP Address Disclosed

## Report Details
- **Report ID**: 707228
- **URL**: https://hackerone.com/reports/707228
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-10-03T16:40:38.679Z
- **Disclosed**: 2020-05-14T16:58:03.203Z

## Reporter
- **Username**: ahmd_halabi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Target Url**
https://███████/███████/static/pubsite/js/main-header-dropdown.js?ver=0.87

**Summary**
Hello, I found an internal IP address disclosure in the page.

**Description:**
Extracted ip address: ████████
extracted port: ██████
place where I found it: `var logoutUrl = 'https://██████:███/█████/logout'`

## Step-by-step Reproduction Instructions

1. Navigate to the target url and search for the ip and you will find it.
█████████

## Suggested Mitigation/Remediation Actions
Avoid disclosing private ip addresses in public codes.

## Impact

Honestly there is no direct impact; however, I found that I should tell you about it in ██████e you don't know about this issue because this information can help an attacker identify other vulnerabilities or help during the exploitation of other identified vulnerabilities.

**Best Regards**

## Attachments
No attachments
