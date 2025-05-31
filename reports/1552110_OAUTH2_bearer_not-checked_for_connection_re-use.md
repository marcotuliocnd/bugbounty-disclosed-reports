# OAUTH2 bearer not-checked for connection re-use

## Report Details
- **Report ID**: 1552110
- **URL**: https://hackerone.com/reports/1552110
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-04-27T16:16:35.698Z
- **Disclosed**: 2022-04-29T11:34:09.285Z

## Reporter
- **Username**: monnerat
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
libcurl might reuse OAUTH2-authenticated connections without properly making
sure that the connection was authenticated with the same credentials as set
for this transfer. This affects SASL-enabled protcols: SMTP(S), IMAP(S),
POP3(S) and LDAP(S) (openldap only).

libcurl maintains a pool of connections after a transfer has completed. The
pool of connections is then gone through when a new transfer is requested and
if there's a live connection available that can be reused, it is preferred
instead of creating a new one.

A connection that is successfully created and authenticated with a user name +
OAUTH2 bearer could subsequently be reused even for user + [other OAUTH2
bearer], even though that might not even be a valid bearer. This could lead to
an authenticion bypass, either by mistake or by a malicious actor.

The problem can be demontrated using an imap server supporting OAUTH2 authentication using command:

`curl 'imap://server:port/path/;MAILINDEX=1' --login-options 'AUTH=OAUTHBEARER' -u user: --oauth2-bearer validbearer --next 'imap://server:port/path/;MAILINDEX=1' --login-options 'AUTH=OAUTHBEARER' -u user: --oauth2-bearer anything`

Note:
This vulnerability has been assigned CWE-305 "Authentication Bypass by Primary Weakness" that is not selectable on the current IBB form.

## Impact

Unauthorized access.

## Attachments
No attachments
