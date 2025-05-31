# Monero wallet password change is confirmed when not matching

## Report Details
- **Report ID**: 803028
- **URL**: https://hackerone.com/reports/803028
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-02-24T01:54:23.945Z
- **Disclosed**: 2020-03-11T23:13:39.302Z

## Reporter
- **Username**: consistent-dream
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: monero

## Vulnerability Information
## Summary:
If you change your wallet password in gui, the confirmation does not need to match the new password.

## Releases Affected:

  * [list each version and OS of the application affected]
  * [list each version and OS of the application affected]

## Steps To Reproduce:
Open your wallet.
Go to settings.
Change wallet password.
Enter old password.
You now have prompt with two passwords.
Enter your new password in the first line.
Leaving confirmation blank press enter.
Password is changed successfully without confirmation.

## Supporting Material/References:
I have personally attempted this many times.

## Housekeeping

1. Be sure to read our policy before submitting
2. Provide an XMR address within the report if you wish to receive bounty (assuming that the report is valid)
    - PoC within a report will most likely result in more bounty than not

45vSCZ1DhEQCjXtPHzgr7m1jCkD31J9ZDCmDakuNV1Sw7mo5ywUPxVxXacJwtiBg7zdRQa4qjzy9Lg8NJdNMDdV3QH8xkPe

## Impact

User can lock themselves out of wallet.

## Attachments
No attachments
