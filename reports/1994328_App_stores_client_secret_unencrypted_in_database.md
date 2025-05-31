# App stores client secret unencrypted in database

## Report Details
- **Report ID**: 1994328
- **URL**: https://hackerone.com/reports/1994328
- **State**: Closed
- **Severity**: low
- **Submitted**: 2023-05-19T11:29:28.191Z
- **Disclosed**: 2023-08-23T14:56:00.746Z

## Reporter
- **Username**: rullzer
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
To identify the nextcloud server need to have the client id and the client secret.
The id is public but the secret is not. Currently this is stored in plain text in the database. Here you can't use hashing as you need the actual value. But Nextcloud should at the very least make sure that this data is properly encrypted at rest in the database.

## Impact

An attacker that obtains read only access to (a snapshot of) the database can impersonate the Nextcloud server without issues

## Attachments
No attachments
