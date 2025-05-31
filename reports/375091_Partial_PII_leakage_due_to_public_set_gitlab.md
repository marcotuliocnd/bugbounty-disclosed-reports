# Partial PII leakage due to public set gitlab

## Report Details
- **Report ID**: 375091
- **URL**: https://hackerone.com/reports/375091
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-07-01T22:20:43.563Z
- **Disclosed**: 2019-12-02T19:06:43.878Z

## Reporter
- **Username**: alyssa_herrera
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**
 ████████ allows you to explore the repos, snippets,etc. On the snippets we find a name+icon and some code information. This shouldn't publicly exposed as an attacker may use it to perform further attacks
**Description:**
A configuration issue allows code and the name+icon of a user on the gitlab instance to leaked publicly.
## Impact
A tiny bit of PII leakage, mainly name+ personal picture. Along with a bit of code leakage
## Step-by-step Reproduction Instructions

https://█████/snippets/72
https://███/explore/snippets

## Product, Version, and Configuration (If applicable)
Gitlab
## Suggested Mitigation/Remediation Actions
Make private

## Impact

Recovery of  partial code and username+picture

## Attachments
No attachments
