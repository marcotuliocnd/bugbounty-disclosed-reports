# PII Leak via /███████

## Report Details
- **Report ID**: 904659
- **URL**: https://hackerone.com/reports/904659
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-06-22T05:21:41.931Z
- **Disclosed**: 2021-02-18T19:09:42.629Z

## Reporter
- **Username**: un4gi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**
The ██████████ website allows access to PII of all site users via faulty access control to the /██████ endpoint.

## Step-by-step Reproduction Instructions

1. Browse to ████████ and login or create an account.
2. Browse to ███████/████████. You will be able to access PII of all site users (click a username to view the PII).

## Suggested Mitigation/Remediation Actions
Restrict access to the /██████████ module to only administrative users.

## Impact

An adversary can gain access to PII of all ███████ users.

## Attachments
No attachments
