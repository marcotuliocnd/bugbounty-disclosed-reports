# User with read-only access to a share can gain write access to sub-folders in the share

## Report Details
- **Report ID**: 619484
- **URL**: https://hackerone.com/reports/619484
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-06-19T04:50:02.608Z
- **Disclosed**: 2020-03-01T13:36:11.620Z

## Reporter
- **Username**: phil-davis
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
user0 creates folders /test and /test/sub
user0 creates file /test/sub/file.txt
user0 shares folder /test with user1 with read+share permissions (17)
user1 receives the folder /test and can read-download /test/sub/file.txt - good
user1 creates a link share of /test/sub - it has permissions 1 (read-only) - good
user1 uses the sharing API to escalate the permissions of the link share, e.g.
```
curl --user user1:user1 "http://172.17.0.1:8081/ocs/v1.php/apps/files_sharing/api/v1/shares/3" -H "OCS-APIRequest: true"  -X PUT --data 'permissions=15'
```
Now browse to the link, e.g. my link was http://172.17.0.1:8081/index.php/s/t9dfm6K57yo6a9r

From the link, anyone (in this case user1, who has knowledge of the link) can create/change/delete files.
e.g. delete file.txt and then upload other files, or some different file.txt

Now login as user0. 

user0 sees that the content of /test/sub has been changed. But they only gave read and share permissions to user1. They never gave any create-change-delete permissions to anyone.

## Impact

A user who has shared some folder(s) read-only can have the content of sub-folders modified by a user who has received the read-only share.

Here is a realistic use case where this public link share permissions bump will be a real issue:

1) the organisation shares read-only a folder to almost everybody. In that folder are sub-folders that have files that have, for example, organisation policy documents (`Policy/Finance` `Policy/HR` etc folders)
2) just 1 user `bob`'s password/authentication details are compromised, or `bob` is malicious himself
3) the attacker `bob` makes a read-only public link share of each sub-folder
4) the attacker `bob` increases the permissions of the public link share to read-write-delete
5) the attacker `bob` browses to the public link share, deletes all the real policy documents and uploads different ones...

Now everybody else in the organisation sees different documents in the (supposedly) read-only share.

## Attachments
No attachments
