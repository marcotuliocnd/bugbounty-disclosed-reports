# RCE (Remote code execution) in one of DoD's websites 

## Report Details
- **Report ID**: 874924
- **URL**: https://hackerone.com/reports/874924
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-05-15T10:01:24.258Z
- **Disclosed**: 2020-07-30T17:47:50.131Z

## Reporter
- **Username**: pwn1um
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**
The targeted website is vulnerable to CVE-2017-1000486, by only running command was (whoami) to prove that the RCE exist has been run successfully on the target
**Description:**
The target uses a vulnerable version of primefaces : Primetek Primefaces 5.x, that is vulnerable to a weak encryption flaw resulting in remote code execution
## Impact
Critical
## Step-by-step Reproduction Instructions
Using the following exploit : https://github.com/pimps/CVE-2017-1000486
1. python primefaces.py████████/

## Product, Version, and Configuration (If applicable)
Primefaces 5.3.6
## Suggested Mitigation/Remediation Actions
Primefaces has to be updated to a newer version

## Impact

An attacker could execute remote codes on the target system, that could impact all of the CIA triad

## Attachments
No attachments
