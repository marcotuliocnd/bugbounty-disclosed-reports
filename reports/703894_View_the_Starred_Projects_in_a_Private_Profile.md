# View the Starred Projects in a Private Profile

## Report Details
- **Report ID**: 703894
- **URL**: https://hackerone.com/reports/703894
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-09-29T18:09:48.881Z
- **Disclosed**: 2021-02-02T14:07:50.702Z

## Reporter
- **Username**: maruthi12
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
### Summary

It is possible to view the  starred Projects in a private profile. Consider my profile for instance, https://gitlab.com/maruthi-adithya . This is a private profile and none of my account-related information should be leaked. However, https://gitlab.com/users/maruthi-adithya/starred.json exposes Starred Projects.

### Steps to reproduce

1. Login to Gitlab. Go to Settings.
2. Check "Don't display activity-related personal information on your profiles".
3. Save the Profile.
4. Now, open your profile from a private window. It will say this is a private profile. However, the above mentioned API exposes the starred projects information.

## Impact

According to the docs, https://gitlab.com/help/user/profile/index.md#private-profile, starred projects should be hidden. However, due to this API, it is getting exposed. Using this, an attacker could steal sensitive data from a private profile.

## Attachments
No attachments
