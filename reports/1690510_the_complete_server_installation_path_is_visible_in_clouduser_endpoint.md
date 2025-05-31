# the complete server installation path is visible in cloud/user endpoint

## Report Details
- **Report ID**: 1690510
- **URL**: https://hackerone.com/reports/1690510
- **State**: Closed
- **Severity**: low
- **Submitted**: 2022-09-03T17:44:27.716Z
- **Disclosed**: 2023-03-30T09:14:16.107Z

## Reporter
- **Username**: bohwaz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
https://github.com/nextcloud/server/issues/33883


When doing a GET request on `/ocs/v1.php/cloud/user?format=json` the server returns user data, including one containing the full local server path:

```
            "storageLocation": "/home/bohwaz/www/tmp/nextcloud/data/bohwaz",
```

This is not a big security issue (as you need to be logged-in to get that response), but this is data that an attacker shouldn't be able to know easily.

This happens on a brand new install after using the web installer.

## Impact

Sensitive internal info

## Attachments
No attachments
