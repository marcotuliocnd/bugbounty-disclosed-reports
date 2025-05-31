# Upload of Avatars for other Users

## Report Details
- **Report ID**: 501084
- **URL**: https://hackerone.com/reports/501084
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-02-25T15:05:48.762Z
- **Disclosed**: 2024-08-10T21:59:54.595Z

## Reporter
- **Username**: gronke
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rocket_chat

## Vulnerability Information
Unprivileged users were found being able to upload Avatar pictures under the behalf of other users.

Attackers authenticated to the API trigger the `ufsImportURL` method with a different `userId` than their own, so that the other users avatar is changed.

The effect of an exploit depends on the storage backend, but the default one coming with a development release, GridFS, is affected.

## Releases Affected:

  * [develop@5f0180d](https://github.com/RocketChat/Rocket.Chat/commit/5f0180dc1500b4e37b8320b39869babadb5d01cd)

## Steps To Reproduce (from initial installation to vulnerability):

(Add details for how we can reproduce the issue)

  1. Authenticate to the API
  2. Invoke `ufsImportURL` method pointing to other user
  3. Clear browser caches and reload page

## Supporting Material/References:

- see [packages/rocketchat-file-upload/server/lib/FileUpload.js#L210](https://github.com/RocketChat/Rocket.Chat/blob/dc2005b76d8f4e315ebed6e06126102148672e0e/packages/rocketchat-file-upload/server/lib/FileUpload.js#L210)

### Payload
```json
["{\"msg\":\"method\",\"method\":\"ufsImportURL\",\"params\":[\"https://radicallyopensecurity.com/images/ros-logo.gif\",{\"name\": \"ros.jpg\", \"extension\": \"jpg\", \"type\": \"text/plain\", \"userId\": \"<USER_ID>\"},\"Avatars\"],\"id\":\"15\"}"]
```

## Suggested mitigation

  * Properly authenticate Avatar uploads

## Impact

Any authenticated user can upload avatar pictures for any other user.

## Attachments
No attachments
