# user can bypass password enforcement when federated sharing is enabled

## Report Details
- **Report ID**: 838510
- **URL**: https://hackerone.com/reports/838510
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2020-04-03T21:34:58.933Z
- **Disclosed**: 2022-06-01T13:52:58.109Z

## Reporter
- **Username**: michag86
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
If the admin forces password for link shares and federated shares are enabled, users can bypass this enforcement. Tested with Nextcloud 18.0.3

Steps to reproduce:
 - enable password enforcement for link shares as admin
 - as user1 create a link share with password
 - open the link share in a separate browser session and enter the password
 - use "add to your nextcloud" and add the file to another nextcloud or the same nextcloud with another user.
 - login as user1, now there is a new link share without password protection. The gui shows that password is enforced, but the link has no password protection
 - copy the new created link

Additional information:
I think the problem is, that if the share is added by "add to your nextcloud", the wrong share_type is set. federated shares normally use the value 6, but the value 3 is set.

Additional problem:
Users can bruteforce link-ids. okay this is something that takes a long time because of 62^15 combinations. But if a forced password is used, every try is protected by the brute-force protection. Just testing links isn't protected by the bruteforce protection I think. Maybe someone just gets read access to the database (or a backup of this). In this case all federated shares are leaked.

So, if password is forced for link shares, enabling federated shares will lower the security level.

Why is there no additional password or public/private-keypair used for establishing and accessing federated shares?

## Impact

This is something that can be used by registered users to bypass the sharing policy.
An attacker that gets read access to the database can access all federated shares.

## Attachments
- share-settings.png
