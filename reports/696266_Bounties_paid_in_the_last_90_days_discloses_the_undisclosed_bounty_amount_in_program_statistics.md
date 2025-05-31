# "Bounties paid in the last 90 days" discloses the undisclosed bounty amount in program statistics

## Report Details
- **Report ID**: 696266
- **URL**: https://hackerone.com/reports/696266
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-09-17T07:06:51.386Z
- **Disclosed**: 2020-02-21T19:13:37.034Z

## Reporter
- **Username**: japz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
Hi Team,

## Summary:

I have found a bypass on this disclosed report: [Know undisclosed Bounty Amount when Bounty Statistics are enabled.](https://hackerone.com/reports/148050)

## Description:

When a program does not disclose how much bounty is paid to particular report, but if bounty statics is enabled then undisclosed Bounty Amount can be enumerated using the __"Bounties paid in the last 90 days".__

"Bounties paid in the last 90 days" is the total amount paid in the last 90 days, so by doing a basic mathematical equation, we can be able to determine the undisclosed bounty amount, below is the formula to get the undisclosed bounty amount.

__Formula__

`old` = `Old Bounties paid in the last 90 days` >> Total 90 days bounty paid
`new` = `New Bounties paid in the last 90 days` >> Everytime the 90 days bounty changes

`undisclosed amount` = `old - new`

## Mitigation:

Use the same fix you have applied in this report #148050

## Impact

Disclosing the undisclosed bounty amount for program which is not disclosing bounties in their settings.

Let me know if anything else is needed.

Regards
Japz

## Attachments
No attachments
