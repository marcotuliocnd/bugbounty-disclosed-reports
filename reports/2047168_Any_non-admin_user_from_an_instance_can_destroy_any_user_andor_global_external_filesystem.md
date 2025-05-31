# Any (non-admin) user from an instance can destroy any (user and/or global) external filesystem

## Report Details
- **Report ID**: 2047168
- **URL**: https://hackerone.com/reports/2047168
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-07-02T15:13:30.383Z
- **Disclosed**: 2023-08-10T09:50:03.738Z

## Reporter
- **Username**: cult
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
## Summary:

There is no verification of the ownership and/or its type when deleting a user-manager external storage. 
Meaning anyone on a Nextcloud instance can destroy any (user, global) external filesystem.
The attacker does not need to have access to the external storage.
The options 'Allow users to mount external storage does not need to be enabled.

When executing the DELETE request on /apps/files_external/userstorages/<storage_id> [1], the app will:
- only check that the mount exists in database, without any condition based on the type of the storage and/or its owner [2]
- remove all data from database related to the storage based on its id. [3]

[1] https://github.com/nextcloud/server/blob/master/apps/files_external/lib/Controller/UserStoragesController.php#L234
[2]  https://github.com/nextcloud/server/blob/master/apps/files_external/lib/Service/DBConfigService.php#L67
[3] https://github.com/nextcloud/server/blob/master/apps/files_external/lib/Service/DBConfigService.php#L274


## Steps To Reproduce:

- From an admin session, create a new external storage.
- From a non-admin session, send a DELETE request to `/apps/files_external/userstorages/<storage_id>`, replace `storage_id` by the correct id (integer) of the storage.
- From an admin session, the created external storage is not listed anymore.

## Impact

Filesystem can be unmounted by anyone, I have no clue how this was not reported earlier.

## Attachments
- recording-1688310781410.webm
