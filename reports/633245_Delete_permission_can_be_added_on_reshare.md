# Delete permission can be added on reshare

## Report Details
- **Report ID**: 633245
- **URL**: https://hackerone.com/reports/633245
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-07-01T16:12:45.510Z
- **Disclosed**: 2019-09-03T13:14:41.352Z

## Reporter
- **Username**: phil-davis
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
user0 creates folder /test
user0 creates file /test/file.txt
user0 shares folder /test with user1 with read+share permissions (17)
user1 receives the folder /test and can read-download /test/file.txt but not delete - good
user1 uses the sharing API to share folder /test with user2, and specifies read(1)+reshare(16)+delete(8)=permissions 25 e.g.

curl --user user1:user1 "http://172.17.0.1:8081/ocs/v1.php/apps/files_sharing/api/v1/shares" -H "OCS-APIRequest: true"  -X POST --data 'path=/test&shareType=0&shareWith=user2&permissions=25'

user2 deletes /test/file.txt

curl --user user2:user2 "http://172.17.0.1:8081/remote.php/dav/files/user2/test/file.txt" -H "OCS-APIRequest: true" -X DELETE

or with the webUI.

This seems to be a side-effect of https://github.com/nextcloud/server/blob/master/lib/private/Files/View.php#L1389 

```
			if ($mount instanceof MoveableMount && $internalPath === '') {
				$data['permissions'] |= \OCP\Constants::PERMISSION_DELETE;
			}
```
which seems to be there so that a user that receives a share gets "implied delete" access to the share "root" so that they can unshare. (They cannot really delete the whole received share, when they "delete" they are actually just "unsharing". But when they reshare on to `user2` then this "implied delete" is able to be passed on.

The problem also happens if user1 shares with a group, and adds the delete permission. Users in the group can delete files. user1 can share with a group that they are already a member of. That gives user1 delete access to the files in the folder.

## Impact

A malicious user can reshare any received share, adding the delete permission to the reshare. Thus giving themselves (if they are in the group) or the end-user the ability to delete files of the first user.

The scenario works with current server master. I guess it will work with 16.* release...

## Attachments
No attachments
