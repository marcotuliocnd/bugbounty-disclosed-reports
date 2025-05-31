# OAuth2 client_secret stored in plain text in the database

## Report Details
- **Report ID**: 1994324
- **URL**: https://hackerone.com/reports/1994324
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-05-19T11:22:17.241Z
- **Disclosed**: 2023-11-15T07:22:13.305Z

## Reporter
- **Username**: rullzer
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
If an attacker would obtain a dumb of the database they could read out the OAuth2 client secret trivially.
https://github.com/nextcloud/server/blob/master/apps/oauth2/lib/Controller/OauthApiController.php#L128

While I realise this is a big if it is not that hard to make sure the client secret is stored properly hashed.
Or at the very least make sure it is stored encrypted. (however non recoverable has the preference here I'd say)

## Impact

An attacker obtaining the read access to a dump of the database can trivially impersonate any OAuth2 client.

## Attachments
No attachments
