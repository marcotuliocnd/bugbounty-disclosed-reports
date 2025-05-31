# PII Leak via /██████

## Report Details
- **Report ID**: 905688
- **URL**: https://hackerone.com/reports/905688
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-06-22T21:21:08.924Z
- **Disclosed**: 2021-02-18T19:11:50.422Z

## Reporter
- **Username**: un4gi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**
An attacker is able to access ServiceNow e-mail notification modules via █████/██████████. Once on this page, the attacker can click any of the notifications, select `Preview Notification`, and choose a user to view their profile data to include Full Name, rank, organization, e-mail address, physical address, and phone number.

## Step-by-step Reproduction Instructions

1. Browse to ██████ and create an account or sign in.
2. Browse to █████████/███████.
3. Click on any of the notification names. Once the notification menu appears, click `Preview Notification` in the top right corner of the screen.
4. The `████` field can now be used to query a user. Once a user is identified, the `(i)` icon can be clicked to view the users PII.
██████

## Suggested Mitigation/Remediation Actions
Restrict access to the █████ and sysevent_email_action.do modules to prevent unauthorized viewing of PII.

## Impact

An adversary can gather PII of all `███████` users via this endpoint.

## Attachments
No attachments
