# SSN leak due to editable slides

## Report Details
- **Report ID**: 693943
- **URL**: https://hackerone.com/reports/693943
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2019-09-12T20:05:50.579Z
- **Disclosed**: 2020-05-14T18:09:29.111Z

## Reporter
- **Username**: alyssa_herrera
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**
A presentation slide contains a screenshot of a records brief which contains an SSN
**Description:**
The slides try to redact the PII of the records with a blue block but we can remove it by editing the slides to remove the offending blue block
## Impact
Critical 
## Step-by-step Reproduction Instructions
We can see an officer record brief, but the area with the SSN is blocked. We can make a copy of the file and edit it to remove the blue block thus allowing us to see the SSN
https://█████████/wp-content/uploads/2018/03/███████
Slide 84
███████
█████████
## Product, Version, and Configuration (If applicable)
N/A
## Suggested Mitigation/Remediation Actions

Purge Doc

## Impact

Identity theft

## Attachments
No attachments
