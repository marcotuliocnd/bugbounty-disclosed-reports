# Default page exposes admin functions and all metods and classes available. on https://██████/█████/dwr/index.html

## Report Details
- **Report ID**: 214800
- **URL**: https://hackerone.com/reports/214800
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-03-20T05:51:12.764Z
- **Disclosed**: 2019-12-02T18:44:29.580Z

## Reporter
- **Username**: daveysec
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**
https://████/██████/dwr/index.html is a default installation page of DWR engine that exposes all classes and methods available to the user.

**Description:**
https://█████████/██████████/dwr/index.html is a default installation page of DWR engine that exposes all classes and methods available to the user. This include test methods and classes as well as admin functions. Some of these I have found to be vulnerable to issues like SQL injection and XSS since they may not have had the same attention as other functions that were expected to be in production.

**Source**
http://gerionsecurity.com/2012/09/experiences-in-pentesting-dwr/

## Impact
Attacker easily discovering and abusing actions they should not be able to use or know about. Abusing information to find issues like SQL injection on poorly implemented functions that are not expected to be publicly available.

## Step-by-step Reproduction Instructions

1.visit https://██████/████/dwr/index.html
2.You can now view and execute all the methods and classes available to this application included test and admin functionality.

## Product, Version, and Configuration (If applicable)
Current version of Firefox.

## Suggested Mitigation/Remediation Actions
delete or restrict access to this default page. Remove or restrict access to test and admin functionality that are unneeded.

## Attachments
No attachments
