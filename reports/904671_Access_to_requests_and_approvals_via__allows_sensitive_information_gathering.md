# Access to requests and approvals via /█████ allows sensitive information gathering

## Report Details
- **Report ID**: 904671
- **URL**: https://hackerone.com/reports/904671
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-06-22T06:09:37.315Z
- **Disclosed**: 2021-02-18T19:12:43.891Z

## Reporter
- **Username**: un4gi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**
An adversary is able to view/modify requests and approvals via ████████/████████.

## Step-by-step Reproduction Instructions

1. Browse to █████ and create an account or sign in.
2. Browse to ███████/██████████. You can now view current/past requests.
3. Clicking on these requests seems to allow an adversary to update/create changes/send e-mails, as well as attach files to the requests. I did not test these features as I did not want to impact existing requests, however I believe the ability to view these requests is enough of a security issue by itself as it allows an attacker to identify hardware/software specifications for NIPR/SIPR assets, as well as identifying justifications for the requests (upcoming TDYs, etc.)

## Suggested Mitigation/Remediation Actions
Restrict access to this endpoint to only allow administrators to view requests as well as allowing users to view their own requests or the requests of users in the same workgroup.

## Impact

An adversary can identify hardware/software specifications of NIPRNET/SIPRNET assets. Additionally, an adversary can gather intel based on justification requirements in the requests (upcoming TDYs, deployments, mission posture due to COVID, etc.)

## Attachments
No attachments
