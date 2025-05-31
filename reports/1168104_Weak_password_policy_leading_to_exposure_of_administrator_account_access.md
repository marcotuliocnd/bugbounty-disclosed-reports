# Weak password policy leading to exposure of administrator account access

## Report Details
- **Report ID**: 1168104
- **URL**: https://hackerone.com/reports/1168104
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2021-04-19T06:46:31.444Z
- **Disclosed**: 2021-05-20T14:45:10.915Z

## Reporter
- **Username**: rptl
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gsa_vdp

## Vulnerability Information
Hi,

The login endpoint https://mysmartplans.gsa.gov/Marathon/Default.aspx is having weak password policy.

During the recon, I came across a mysmartplans overview document http://www.accentimaging.com/accent/pdfs/Accent%20MySmartPlans.pdf
. In this document few users are mentioned like - rick, ban, tim etc.I tried to login user password combination of these user-names & rick wass found a valid administrator username & password.

username- rick
password -rick

This user appears to be administrator user.
Hope GSA takes necessary measures to improve user account policies.

PoC

1) Open url https://mysmartplans.gsa.gov/Marathon/Default.aspx
2) Enter username  rick password rick
3) You will be logged into user account with administrative access. You can edit, create, update users.

## Impact

Admin account compromise.

## Attachments
- Capture.JPG
