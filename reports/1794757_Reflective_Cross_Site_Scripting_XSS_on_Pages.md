# Reflective Cross Site Scripting (XSS) on ███████/Pages

## Report Details
- **Report ID**: 1794757
- **URL**: https://hackerone.com/reports/1794757
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-12-06T10:49:50.780Z
- **Disclosed**: 2024-03-22T17:32:41.589Z

## Reporter
- **Username**: predatorsparrow
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
## Reflective Cross-Site Scripting (XSS)
An elevation of privilege vulnerability exists when Microsoft SharePoint Server does not properly sanitize a specially crafted web request to an affected SharePoint server. An authenticated attacker could exploit the vulnerability by sending a specially crafted request to an affected SharePoint server. 
The attacker to read content that the attacker is not authorized to read, use the victim's identity to take actions on the SharePoint site on behalf of the user, such as change permissions and delete content, and inject malicious content in the browser of the user.

## System Host(s)
https://██████████/Pages

## Affected URLs in Scope
https://█████████/Pages/default.aspx?FollowSite=0&SiteName=%27-confirm(%27XSSALERT%27)-%27

## Affected Product(s) and Version(s)
Microsoft SharePoint Foundation 2013 Service Pack 1

██████ 

References
https://msrc.microsoft.com/update-guide/vulnerability/CVE-2017-0255

## CVE Numbers
CVE-2017-0255

## Steps to Reproduce

Injecting this XSS payload containing allows a window to pop up as a result of the payload being executed.

 1. Go to- 
https://████████/Pages/default.aspx?FollowSite=0&SiteName=%27-confirm(%27XSSALERT%27)-%27


## Suggested Mitigation/Remediation Actions
Sanitize data input (to make sure the URL input does not contain any code) is loaded from well-defined endpoints. 


## Attachments
No attachments
