# Download permissions can be changed by resharer

## Report Details
- **Report ID**: 1724016
- **URL**: https://hackerone.com/reports/1724016
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-10-06T06:49:36.814Z
- **Disclosed**: 2023-02-24T07:33:41.050Z

## Reporter
- **Username**: rullzer
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
The new feature in NC 25 to limit downloads also for internal shares is meant to force users to use secure view. So documents are watermarked and what not.

Assume a company wide share. People can share files from it to others but they can't be downloaded. For simplicity

* user1 shares a folder with reshare permissions but without download permissions to user2. Assume this is a share with ID 10
* user2 shares that folder with user3, this is a share with ID 11

This all works as expected

Now user2 simply does a PUT

```
curl -u user2:pass 'https://SERVER/ocs/v2.php/apps/files_sharing/api/v1/shares/11' -X PUT -H "OCS-APIREQUEST: true" -H 'Content-Type: application/json' --data-raw '{"permissions":"17","attributes":"[{\"scope\":\"permissions\",\"key\":\"download\",\"enabled\":true}]"}'
```

And there you go. No more pesky secure view. Just easy downloads for user3.

## Impact

Secure view for internal shares is useless if also reshare permissions are given.

## Attachments
No attachments
