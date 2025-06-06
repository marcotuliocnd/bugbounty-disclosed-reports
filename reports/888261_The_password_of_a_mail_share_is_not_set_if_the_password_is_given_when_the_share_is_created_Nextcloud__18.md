# The password of a mail share is not set if the password is given when the share is created (Nextcloud < 18)

## Report Details
- **Report ID**: 888261
- **URL**: https://hackerone.com/reports/888261
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-06-01T10:23:36.880Z
- **Disclosed**: 2021-03-04T08:52:06.546Z

## Reporter
- **Username**: daniel_calvino_sanchez
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
- Create a new mail share with a password by using the OCS endpoint with something like:
curl -u admin:admin -X POST -H "OCS-APIRequest: true" "http://localhost/ocs/v1.php/apps/files_sharing/api/v1/shares?path=welcome.txt&shareType=4&shareWith=user@server.com&password=plainTextPassword"

- Open the share with something like:
http://localhost/index.php/s/shareToken (the "shareToken" value can be seen in the curl response)

- The shared file is shown; no password is requested to access it.

Note that a password (although an autogenerated one instead of the given one) is set if password protection is enforced (https://github.com/nextcloud/server/blob/b3f806a9497da0a7e5229e555a8f90d1c0b299de/apps/sharebymail/lib/ShareByMailProvider.php#L223) or if the share is later updated with another password (https://github.com/nextcloud/server/blob/f50bf10bec8fc1ccd834c16379ddb502972a2174/lib/private/Share20/Manager.php#L954).

This applies only to Nextcloud < 18 (the password is set for Nextcloud >= 18 with https://github.com/nextcloud/server/pull/16629, although it led to a different security issue: https://hackerone.com/reports/885041).

## Impact

An attacker would be able to access a password protected mail share with just the share token, without having to enter the password.

## Attachments
No attachments
