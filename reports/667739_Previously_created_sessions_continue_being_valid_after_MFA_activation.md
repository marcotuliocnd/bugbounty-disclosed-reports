# Previously created sessions continue being valid after MFA activation

## Report Details
- **Report ID**: 667739
- **URL**: https://hackerone.com/reports/667739
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-08-05T15:49:02.756Z
- **Disclosed**: 2019-08-19T15:25:48.612Z

## Reporter
- **Username**: brdoors3
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: grammarly

## Vulnerability Information
Hi team,

I found one issue related to your 2FA system on https://account.grammarly.com/security

POC

1 access the same account on https://account.grammarly.com in two devices
2 on device 'A' go to https://account.grammarly.com/security > complete all steps to activate the 2FA system

Now the 2FA is activated for this account

3 back to device 'B' reload the page

The session still active

## Impact

In this scenario when 2FA is activated the other sessions of the account are not invalidated.

2FA is required to login. I believe the expected and recommended behavior here is to terminate the other sessions> request a new login> request the 2FA code> so then give the account access again

## Attachments
No attachments
