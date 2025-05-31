# Hackers can Invite Collaborators Without 2FA on Programs Requiring 2FA

## Report Details
- **Report ID**: 2575079
- **URL**: https://hackerone.com/reports/2575079
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2024-06-26T02:41:52.672Z
- **Disclosed**: 2024-07-11T14:28:45.891Z

## Reporter
- **Username**: anish-kosaraju
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**
Hackers can invite collaborators that don't have 2FA enabled in reports sent to programs that require 2FA.

### Steps To Reproduce

1. Create a new program and enable 2FA.
2. Submit a report to that program. Create a new account without 2FA and invite that account as a collaborator to the report.
3. The new account will be able to accept the invite.

## Impact

This defeats the point of having 2FA enabled as hackers who don't have 2FA can still access the report.

## Attachments
No attachments
