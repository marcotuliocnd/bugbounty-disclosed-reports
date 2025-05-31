# Admin audit is not properly logging unsetting of expiration date

## Report Details
- **Report ID**: 1200810
- **URL**: https://hackerone.com/reports/1200810
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-05-18T12:31:10.161Z
- **Disclosed**: 2021-07-15T19:13:34.255Z

## Reporter
- **Username**: rtod
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
In relation to https://hackerone.com/reports/1177353

1. Enable the audit log
2. Share a file
3. Set and expiration date

So far all looks good in the log

4. Unset the the expiration date.
5. See a pretty useless log line

## Impact

The audit log is used to get a full trail of the actions which is now incompletely. With possible important information.
It seems to be also listed on https://portal.nextcloud.com/article/using-the-audit-log-44.html

## Attachments
No attachments
