# External storage app saves password for all users in the database

## Report Details
- **Report ID**: 867164
- **URL**: https://hackerone.com/reports/867164
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-05-06T13:13:40.888Z
- **Disclosed**: 2021-03-01T11:01:47.786Z

## Reporter
- **Username**: alacn1
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
External storage (files_external) app save passwords of all users to database table "oc_credentials" even when "Log-in credentials, save in database" option is not used.

It's a security risk that allow password extraction of all users.

A local system admin that has access to database and nextcloud config file could decrypt any user password.

### Steps to reproduce
1. Enable app "External storage support" (files_external).
2. Login to nextcloud.
3. User recoverable password will be saved to table "oc_credentials" at "password::logincredentials/credentials".

### Expected behaviour
Don't save user password to table "oc_credentials" unless user has a mount with "Log-in credentials, save in database" option.

### Actual behaviour
Passwords of all users is saved to table "oc_credentials" when files_external app is enabled.

### Tested with
Nextcloud 18.0.4 + External storage 1.9.0
Nextcloud 17.0.5 + External storage 1.8.0

## Impact

A local system admin could recover any user password.

## Attachments
No attachments
