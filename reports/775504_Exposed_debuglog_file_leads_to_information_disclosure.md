# Exposed debug.log file leads to information disclosure

## Report Details
- **Report ID**: 775504
- **URL**: https://hackerone.com/reports/775504
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-01-15T12:44:07.843Z
- **Disclosed**: 2020-01-15T22:53:37.716Z

## Reporter
- **Username**: muhammaddaffa
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mariadb

## Vulnerability Information
At the following address i have found debug.log file disclose the application full path on the server. And there is database username too in debug.log

http://mariadb.org/wp-content/debug.log

## Impact

Information disclosure

## Attachments
No attachments
