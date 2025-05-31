# Exposing debug.log file leads to server full path disclosure

## Report Details
- **Report ID**: 696360
- **URL**: https://hackerone.com/reports/696360
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-09-17T10:37:40.752Z
- **Disclosed**: 2019-10-17T12:50:54.472Z

## Reporter
- **Username**: sohelahmed786
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
At the following address i have found debug.log file disclose the application full path on the server.
https://nextcloud.com/wp-content/debug.log

## Impact

The server should not expose this log file as it could help an attacker to understand the environment that may lead to further attacks.

## Attachments
No attachments
