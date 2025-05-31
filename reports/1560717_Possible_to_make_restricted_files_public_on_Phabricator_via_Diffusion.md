# Possible to make restricted files public on Phabricator via Diffusion

## Report Details
- **Report ID**: 1560717
- **URL**: https://hackerone.com/reports/1560717
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2022-05-05T23:54:40.993Z
- **Disclosed**: 2022-07-29T22:37:58.052Z

## Reporter
- **Username**: dyls
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: phabricator

## Vulnerability Information
Files on Phabricator are always viewable to a user if they are attached to an object that they can view. It seems Phabricator does check if you can view a file before allowing you to a attach it. If you don't have access to the file, it will just look like this {F99999999999} in plaintext. It seems Phabricator does not do this check when creating commits in Differential repositories. This means you make a restricted file public simply by including the syntax to attach the file in the commit message which will then by synced to Phabricator, causing the file to be made public regardless of whether you had access in the first place. It is possible to find a restricted file simply by enumeration.

File "Can View" is set to Administrator:
F1718695
However the file is in the commit and viewable:
F1718696
User is not an Administrator:
F1718697

## Impact

Gain access to restricted file objects.

## Attachments
- Screenshot_(283).png
- Screenshot_(282).png
- Screenshot_(281).png
