# Previously created sessions continue being valid after MFA activation

## Report Details
- **Report ID**: 1185479
- **URL**: https://hackerone.com/reports/1185479
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-05-06T04:27:53.123Z
- **Disclosed**: 2021-05-18T16:04:45.514Z

## Reporter
- **Username**: benjamin-mauss
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: cs_money

## Vulnerability Information
## Summary:
Hi, team.
This is the same issue of #667739. Please take a look.

I found one issue related to your 2FA system on https://cs.money/security/

## Steps To Reproduce:

1. access the same account on https://cs.money/ in two devices
1. on device 'A' go to https://cs.money/security/ > complete all steps to activate the 2FA system
1. Now the 2FA is activated for this account
1. back to device 'B' reload the page
1. The session still active

## Impact

In this scenario when 2FA is activated the other sessions of the account are not invalidated.
2FA is required to login. I believe the expected and recommended behavior here is to terminate the other sessions> request a new login> request the 2FA code> so then give the account access again

## Attachments
No attachments
