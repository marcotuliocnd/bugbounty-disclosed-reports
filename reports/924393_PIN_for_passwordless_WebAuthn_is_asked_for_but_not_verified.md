# PIN for passwordless WebAuthn is asked for but not verified

## Report Details
- **Report ID**: 924393
- **URL**: https://hackerone.com/reports/924393
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-07-15T12:18:30.607Z
- **Disclosed**: 2020-10-28T09:19:31.956Z

## Reporter
- **Username**: dschuermann
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Nextcloud introduced WebAuthn passwordless authentication with version 19. As far as we understand, you assume that your implementation provide two-factor authentication:

"The server asking for authentication can request verification of multiple factors, so that a configured key requires the user to not just plug it in but also enter a PIN or scan a finger print." (see https://www.nitrokey.com/news/2020/what-passwordless-world-looks )

We found the same issue like in Microsoft’s implementation: userVerification is not set and the UV flag is not checked on the server. Thus, even though a FIDO2 key with a PIN is added in a user account, the PIN is not required to log in.

The full description is available in our unlisted blog post at: https://hwsecurity.dev/2020/06/webauthn-pin-bypass/

## Impact

We have a nice video in our blog post:  https://hwsecurity.dev/2020/06/webauthn-pin-bypass/

An attacker could log into the victims account without a PIN by sneaking up on the victim and using the security hardware over NFC.

## Attachments
No attachments
