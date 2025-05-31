# Add to your nextcloud endpoint is not properly protected

## Report Details
- **Report ID**: 1192144
- **URL**: https://hackerone.com/reports/1192144
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-05-11T13:56:27.069Z
- **Disclosed**: 2021-08-11T09:24:19.106Z

## Reporter
- **Username**: rtod
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
This is related to https://hackerone.com/reports/1173684

The endpoint you hit does have bruteforce protection
https://github.com/nextcloud/server/blob/master/apps/federatedfilesharing/lib/Controller/MountPublicLinkController.php#L126

But this is only triggered by finding a share that is password protected
https://github.com/nextcloud/server/blob/master/apps/federatedfilesharing/lib/Controller/MountPublicLinkController.php#L157

Or a file drop public share
https://github.com/nextcloud/server/blob/master/apps/federatedfilesharing/lib/Controller/MountPublicLinkController.php#L166

In other words this endpoint can also be used to try to brute force share tokens.

## Impact

Low just like on the other report. But should be fixed non the less.

## Attachments
No attachments
