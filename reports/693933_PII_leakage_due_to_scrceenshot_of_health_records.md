# PII leakage due to scrceenshot of health records

## Report Details
- **Report ID**: 693933
- **URL**: https://hackerone.com/reports/693933
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2019-09-12T19:28:02.016Z
- **Disclosed**: 2019-12-02T20:01:41.364Z

## Reporter
- **Username**: alyssa_herrera
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**
Document shows a screenshot of a medical record for a soldier 
**Description:**
One of the slides describes the CIV# and PAD DSN# along with some information relating to the soldier such as their name, the information appears to be old but could be still be an issue if they're in service
## Impact
High? maybe critical? Unsure on impact 
## Step-by-step Reproduction Instructions
Check slide 13 specifically but there's other slides that are suspect too
https://███████/wp-content/uploads/2018/12/HR_TECH_WOBC_Perform_eMILPO_Functions_eMILPO_Brief.pptx

## Product, Version, and Configuration (If applicable)
N/A
## Suggested Mitigation/Remediation Actions
Purge Doc

## Impact

An attacker could assume soldier identities and learn more about possible health information related to them

## Attachments
No attachments
