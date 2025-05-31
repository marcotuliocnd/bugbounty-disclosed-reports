# External Storage - WebDAV - New user has access to storage from deleted user (same user-ID)

## Report Details
- **Report ID**: 549831
- **URL**: https://hackerone.com/reports/549831
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2019-04-28T18:30:08.036Z
- **Disclosed**: 2021-02-14T16:24:44.764Z

## Reporter
- **Username**: sanmue
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
* Delete existing user account "user3"
* Create new user account "user3"

Also reported on https://github.com/nextcloud/server/issues/15258

## Impact

Newly created user with same user-id of a deleted user has access to the configured external webdav storage from the deleted user.

## Attachments
- oc_external_mounts.png
- oc_external_config.png
- user3_external-storage-config.png
