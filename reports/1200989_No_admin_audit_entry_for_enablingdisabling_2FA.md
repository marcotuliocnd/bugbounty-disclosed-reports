# No admin audit entry for enabling/disabling 2FA

## Report Details
- **Report ID**: 1200989
- **URL**: https://hackerone.com/reports/1200989
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-05-18T13:57:33.397Z
- **Disclosed**: 2021-06-16T08:40:24.869Z

## Reporter
- **Username**: rtod
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Related to https://hackerone.com/reports/1177353
When a user enables or disables 2FA there is no entry in the audit log.

## Impact

Especially for disabling it should probably be logged there. But account security related things should be in there.

## Attachments
No attachments
