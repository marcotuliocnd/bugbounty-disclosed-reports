# twofactor_auth bypassable if provider fails to load

## Report Details
- **Report ID**: 317711
- **URL**: https://hackerone.com/reports/317711
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-02-20T01:00:10.407Z
- **Disclosed**: 2018-09-27T10:10:19.480Z

## Reporter
- **Username**: cyphar
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
(Just want to preface this by saying that this is probably not a significant
vulnerability, as it requires that the server either have recently been
incorrectly upgraded or otherwise misconfigured. However in the administration
of my own personal NextCloud instance I have hit this several times.)

This is a general trait of 2FA provider failures. If you enable 2FA for any
given user on NextCloud, and the 2FA provider fails to by enabled for whatever
reason (such as an upgrade which made the 2FA provider incompatible, or the 2FA
provider source code was removed or corrupted somehow) then 2FA will be
bypassable for all accounts on the system.

While this may not seem like a significant issue, since twofactor_auth
providers are not part of the main NextCloud server source, upgrading the main
server (either through the official updater app, or manually) will result in
twofactor_auth being disabled if the provider has not been updated. Thus there
is a window around upgrading the NextCloud server where an attacker can bypass
2FA.

Ultimately the solution to this problem would be to *always* require 2FA if 2FA
has been enabled, and if a provider is not available you must require that the
user enter one of their backup codes. I'm not sure how backup codes are
currently implemented, but if they're implemented in the server (rather than
individually by each 2FA provider) this should not be overly complicated to
implement.

I have only tested this with the TOTP 2FA provider, but I would be surprised if
it didn't affect all 2FA providers.

## Impact

Attackers being able to bypass 2FA means that keyloggers or other tools could
be used to steal the users' passphrase, and then the attacker could gain access
while the user would expect the attacker to require access to their 2FA token.

## Attachments
No attachments
