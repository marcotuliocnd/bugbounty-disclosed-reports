# inviting collaborator using email disclose the hackerone account related to the user

## Report Details
- **Report ID**: 2045722
- **URL**: https://hackerone.com/reports/2045722
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-07-01T08:17:14.208Z
- **Disclosed**: 2024-09-19T12:09:03.982Z

## Reporter
- **Username**: raymatp
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
##Summary
The new hackerone collaborator features allows users to disclose hackerone account related to a user without any interaction from the invitee

##Description
In the old hackerone collaborator feature, if you invite a collaborator using an email, the related account to that email wont be disclosed up until the user accepts the invite. However, in the new collaborator feature, if you invite a collaborator using email, it would automatically resolves to the hackerone account related to the email address.

##Steps to reproduce
1. In a report that allows collaborator invite, click manage collaborators.
2. add your dummy account as a collaborator using email address then click save

████

3. After saving, check the participants and notice that instead of a pending invite to an email address, it was already resolved to the hackerone account related to the email

{F2458957}

## Impact

disclosing hackerone account related to an email. This can be used to enumerate hackerone users using email address

## Attachments
- pending_collaborator.png
