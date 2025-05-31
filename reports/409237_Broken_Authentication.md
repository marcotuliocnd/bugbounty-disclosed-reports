# Broken Authentication

## Report Details
- **Report ID**: 409237
- **URL**: https://hackerone.com/reports/409237
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-09-12T22:53:21.159Z
- **Disclosed**: 2022-02-14T21:29:11.035Z

## Reporter
- **Username**: websecnl
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:** IDOR

**Description:** It is possible to access other user account by changing the parameter 'email' to another valid e-mail, i managed to guess an existing user '███████@███.com' which discloses the ███ 
Name and Surname.

## Impact
Information Disclosure

## Step-by-step Reproduction Instructions

1.Visit: https://██████
2. Register for an account
3. Follow the steps like in the attached pictures

## Product, Version, and Configuration (If applicable)
Web Application

## Suggested Mitigation/Remediation Actions
https://www.owasp.org/index.php/Insecure_Direct_Object_Reference_Prevention_Cheat_Sheet

## Impact

Information Disclosure

## Attachments
No attachments
