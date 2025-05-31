# Federated share accepting/declining is not logged in audit log

## Report Details
- **Report ID**: 1200815
- **URL**: https://hackerone.com/reports/1200815
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-05-18T12:34:55.501Z
- **Disclosed**: 2022-09-03T06:12:07.191Z

## Reporter
- **Username**: rtod
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
In relation to https://hackerone.com/reports/1177353

1. Enable the audit log
2. Share a file to a federated user
3. So far all looks good in the log
4. the recipient checks either accepts or declines the share
5.  There is no line regarding this in the logs.

## Impact

The audit log is used to get a full trail of the actions which is now incompletely. With possible important information.
It seems to be also listed on https://portal.nextcloud.com/article/using-the-audit-log-44.html
From my point of view a declined share is unshared again.

## Attachments
No attachments
