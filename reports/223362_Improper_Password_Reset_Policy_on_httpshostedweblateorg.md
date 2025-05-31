# Improper Password Reset Policy on https://hosted.weblate.org/

## Report Details
- **Report ID**: 223362
- **URL**: https://hackerone.com/reports/223362
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-04-24T10:25:40.189Z
- **Disclosed**: 2017-05-17T14:08:31.105Z

## Reporter
- **Username**: mrnull1337
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
Application should not allow the user to set the last 3-5 password in terms of secure design principles. It should give a warning or provide such avoidance while user is using repetitive usage of passwords.

Repro:
1. Try to set same old password via Password Reset link.

Fix: Application should avoid user to set last history of passwords to enforce the security.

Let me know if any further info is required.

Regards,
Mr_R3boot.  

## Attachments
No attachments
