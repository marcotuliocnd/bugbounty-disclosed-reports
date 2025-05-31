# Disabling context isolation, nodeIntegrationInSubFrames using an unauthorised frame.

## Report Details
- **Report ID**: 1647287
- **URL**: https://hackerone.com/reports/1647287
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-07-23T04:36:37.729Z
- **Disclosed**: 2022-08-11T23:08:15.229Z

## Reporter
- **Username**: s1r1u5
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Details can be found in the following github advisory: https://github.com/electron/electron/security/advisories/GHSA-mq8j-3h7h-p8g7

## Impact

Using a renderer exploit, context isolation and nodeIntegrationInSubFrames can be disabled, which enables an attacker to leak IPC module and communicate with the more privileged main process which might eventually lead to Remote Code Execution if there are sensitive IPC handlers on main process.

## Attachments
No attachments
