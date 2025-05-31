# Missing ownership check on remote wipe endpoint

## Report Details
- **Report ID**: 819807
- **URL**: https://hackerone.com/reports/819807
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-03-15T21:55:05.955Z
- **Disclosed**: 2020-04-19T13:15:25.770Z

## Reporter
- **Username**: hitman_47
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
On settings/user/security

You can mark a device for wipe out that does not belong to you.

Steps:

1. Create 2 accounts one for the hacker and one for the victim
2. On both accounts add devices with different names
3.  On the hacker account, while intercepting with burpsuite, select the option to wipe out a device
4.  Forward with burpsuite and in the url that looks like settings/personal/authtokens/wipe/{data-id}, change the data-id to the id of the device of the victim
5. Stop intercepting or forward again and the device of the victim will be marked for wipe out. 

Here is a video demo 
{F748890}

## Impact

Attacker can wipe out the device of another user by using the device ID

## Attachments
- IDORNextCloud.mp4
