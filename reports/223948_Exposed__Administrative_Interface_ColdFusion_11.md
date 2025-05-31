# Exposed ███████ Administrative Interface (ColdFusion 11)

## Report Details
- **Report ID**: 223948
- **URL**: https://hackerone.com/reports/223948
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-04-26T03:56:24.484Z
- **Disclosed**: 2019-12-02T18:54:09.011Z

## Reporter
- **Username**: jamesit
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**
The "/██████████/administrator/" directory is accessible to the public and allows an attacker to further enumerate the system and/or perform brute force attacks.

**Description:**
The ████████ website has an exposed "Administrative Interface" for ColdFusion 11, which could be useful to an attacker to perform brute force attacks and/or further version enumeration. Additionally, leaving an exposed administrative interface open to the world, increases attack surface to zero days and other advanced attacks that would exploit the ████ administrative interface, which has been stopped previously due to access restrictions.

## Impact
Low
## Step-by-step Reproduction Instructions

1) Perform directory scanning, which detects the URL using tools such as Burp Suite professional spider and/or DirSearch.
2) Visit URL - https://█████████/████/administrator/index.cfm
3) None.

## Product, Version, and Configuration (If applicable)
ColdFusion 11
https://██████/████████/administrator/index.cfm

## Suggested Mitigation/Remediation Actions
The "/█████" directory should be completely locked down to prevent unauthorised access, to ensure secure design principles are followed. This can be achieved by .htaccess password protection, or IP restrictions with IP filtering. (IP/Domain Restrictions)

## Attachments
No attachments
