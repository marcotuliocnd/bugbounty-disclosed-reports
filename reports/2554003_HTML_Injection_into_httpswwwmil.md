# HTML Injection into https://www.██████.mil

## Report Details
- **Report ID**: 2554003
- **URL**: https://hackerone.com/reports/2554003
- **State**: Closed
- **Severity**: low
- **Submitted**: 2024-06-17T05:11:15.073Z
- **Disclosed**: 2024-07-19T14:18:55.744Z

## Reporter
- **Username**: thpless
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
### PoC

You can use the following link:
https://www.██████.mil/search/%2522%253E%253C/form%253E%253Ch1%253EHTML%2520INJECTION%2520IS%2520POSSIBLE%2520!!!%253C/h1%253E%253C/body%253E%253C/form%253E%253C!--

## Impact

HTML injection can compromise the security and integrity of a website by allowing attackers to inject malicious HTML code, leading to unauthorized content display, data theft, or user redirection. It can result in a loss of user trust and potentially cause significant damage to a website's reputation and user base.

## System Host(s)
www.████.mil

## Affected Product(s) and Version(s)
Wordpress Website

## CVE Numbers


## Steps to Reproduce
https://www.█████████.mil/search/%2522%253E%253C/form%253E%253Ch1%253EHTML%2520INJECTION%2520IS%2520POSSIBLE%2520!!!%253C/h1%253E%253C/body%253E%253C/form%253E%253C!--

## Suggested Mitigation/Remediation Actions
Input validation and output encoding are essential to prevent HTML injection vulnerabilities.



## Attachments
No attachments
