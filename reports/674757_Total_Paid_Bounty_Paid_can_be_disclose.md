# Total Paid Bounty Paid can be disclose

## Report Details
- **Report ID**: 674757
- **URL**: https://hackerone.com/reports/674757
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-08-15T23:29:33.343Z
- **Disclosed**: 2020-02-28T17:36:38.163Z

## Reporter
- **Username**: zrachessanasz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**

Hello HackerOne Bug Bounty Team,

I noticed that HackerOne recently updated their interface. Indeed, when a hacker hover his mouse over a program, it now disclose some new information :
{F556858}
The one that interested us is "Bounties sent in the last 90 days" value

**Description:**

This new feature could potentially disclose some program information that the team isn't willing to share. Indeed, this can happen in some scenario :

1- The program is 90 days or younger and has choose to not disclose the total paid amount.
2- The program is not 90 days or younger, but an automated script is continually tracking "Bounties sent in the last 90 days" value (note that this would give an exact number since the tracking has started or a very approximate number) (inspired from report #148050)

## Impact

Total Paid Bounty Paid can be disclose

## Attachments
- H1-InfoDisclo-01.png
