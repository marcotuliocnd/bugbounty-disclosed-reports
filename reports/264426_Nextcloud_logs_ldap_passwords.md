# Nextcloud logs ldap passwords

## Report Details
- **Report ID**: 264426
- **URL**: https://hackerone.com/reports/264426
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-08-29T20:09:23.497Z
- **Disclosed**: 2020-01-31T14:27:11.481Z

## Reporter
- **Username**: tribut
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
When the ldap server is (temporarily) unavailable, data like the attached ends up in log files. I've replaced usernames with `XXX_USERn_XXX` and passwords with `XXX_PASSn_XXX`. It seems that at least the following are missing from `$methodsWithSensitiveParameters` in `lib/private/Log.php`:
 - `bind`
 - `areCredentialsValid`
 - `invokeLDAPMethod`
 - `checkPasswordNoLogging`

## Attachments
- nextcloud-scrubbed.txt
