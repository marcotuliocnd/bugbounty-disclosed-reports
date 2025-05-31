# PII Leak via /████████

## Report Details
- **Report ID**: 905679
- **URL**: https://hackerone.com/reports/905679
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-06-22T21:00:02.410Z
- **Disclosed**: 2021-02-18T19:10:51.200Z

## Reporter
- **Username**: un4gi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**
An attacker is able to view PII (Full name/address/e-mail/phone) of all website users via █████████/████████

## Step-by-step Reproduction Instructions

1. Browse to ████ and login or create an account.
2. Browse to ████/███████
3. Begin typing a name in the `Select User` field, and click the `(i)` icon on the right side of the field to view the users data.
██████

## Suggested Mitigation/Remediation Actions
Restrict access to this endpoint to administrative roles.

## Impact

An adversary can gather PII of all `█████████` users via this endpoint.

## Attachments
No attachments
