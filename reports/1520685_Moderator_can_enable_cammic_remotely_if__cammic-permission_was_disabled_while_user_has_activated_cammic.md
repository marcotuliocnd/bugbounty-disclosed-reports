# Moderator can enable cam/mic remotely if  cam/mic-permission was disabled while user has activated cam/mic

## Report Details
- **Report ID**: 1520685
- **URL**: https://hackerone.com/reports/1520685
- **State**: Closed
- **Severity**: low
- **Submitted**: 2022-03-24T08:10:53.270Z
- **Disclosed**: 2022-06-09T12:42:33.695Z

## Reporter
- **Username**: michag86
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
## Summary:
[add summary of the vulnerability]

## Steps To Reproduce:

  1. Create a Call as User A (Moderator)
  2. Add User B to the call
  3. Start the call as User A
  4. User B joins the call and enables the camera
  5. User A removes all permissions for User B, cam and mic are now disabled
  6. User A grants all permissions to User B

--> now mic and cam are enabled remotely, if User B didn't disable it before removing permissions by User B

## Used Software Versions:
Nextcloud 23.0.3
spreed-App 13.0.4
nextcloud-spreed-signaling 0.4.0

## Impact

A call moderator can remotely enable user webcams, if there were enabled before removing the permissions. This is a big privacy issue.

## Attachments
No attachments
