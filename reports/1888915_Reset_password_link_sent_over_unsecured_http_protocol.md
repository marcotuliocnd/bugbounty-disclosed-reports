# Reset password link sent over unsecured http protocol

## Report Details
- **Report ID**: 1888915
- **URL**: https://hackerone.com/reports/1888915
- **State**: Closed
- **Severity**: high
- **Submitted**: 2023-02-28T10:37:19.662Z
- **Disclosed**: 2023-05-10T08:53:31.726Z

## Reporter
- **Username**: uchihaluckycs
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mattermost

## Vulnerability Information
## Summary:
After creating the workspace, if victim clicks on forgot password then reset password link has been generated and sent over mail and that password link is unsecured http protocol.

## Steps To Reproduce:

  1. Signup to a workspace
  2. Navigate to https://h1-\*your-own-instance\*.cloud.mattermost.com/reset_password and enter signup email
  3. Check email, you will get reset passwork link. {F2201387}
  4. Copy that link paste in notepad and observe the protocol. {F2201388}

## Mitigation:
Generate reset password link with secured https protocol.

## Impact

If the victim opens the reset password link and forgot to update the password, anyone from intermediate computers through network or sniffer can reset the password.

## Attachments
- chrome_iQDUTN9H1J.png
- sublime_text_opnUofVDz2.png
