# Password of failed (2FA) login attempt is stored in log

## Report Details
- **Report ID**: 244092
- **URL**: https://hackerone.com/reports/244092
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-06-28T19:13:38.872Z
- **Disclosed**: 2020-03-01T14:10:53.113Z

## Reporter
- **Username**: maprambo
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
If I try to log in on Webdav with my usual Nextcloud password, it doesn't work due to 2FA. I need an application password.

The password of a failed login attempt by any user is stored plain text in the log:
`[...]OCA\\\\DAV\\\\Connector\\\\Sabre\\\\Auth->validateUserPass('matthes', '***THE_PASSWORD***')[...]`

Even though the login attempt failed, the password is the right password. I am using two factor, but still, the password may not be leaked to anyone. It may also be used for other websites or services, like LDAP. And you can disable 2FA and still use the same password. The log is in some cases visible to multiple people, may it be admins (but who shouldn't have access to the user data) or if the file is just sent to someone else for debugging.

## Attachments
No attachments
