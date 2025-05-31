# Trusted server shared secret stored unencrypted in the database

## Report Details
- **Report ID**: 1173670
- **URL**: https://hackerone.com/reports/1173670
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-04-24T09:43:55.072Z
- **Disclosed**: 2021-06-16T08:56:40.781Z

## Reporter
- **Username**: rtod
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
The attack vector here is that somebody gets their hands on your database.

When two servers have added each other as trusted server they exchange  shared secret token. With this token they can sync down each other user lists.

However it seems that this token is stored in plain text in the `oc_trusted_servers` table.
This seems especially odd since you do store credentials for external storage encrypted in the database. Simply encrypting the shared secret in the database would help.

## Impact

If the database of a system is compromised the attacker can easily obtain the token of any trusted server. And keep syncing down the address book with that.

## Attachments
No attachments
