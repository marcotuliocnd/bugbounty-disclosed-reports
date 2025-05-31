# JWT audience claim is not verified

## Report Details
- **Report ID**: 1889161
- **URL**: https://hackerone.com/reports/1889161
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2023-02-28T18:06:26.575Z
- **Disclosed**: 2023-04-16T18:43:01.524Z

## Reporter
- **Username**: farcaller
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
All versions of Argo CD starting with v1.8.2 are vulnerable to an improper authorization bug causing the API to accept certain invalid tokens.

OIDC providers include an aud (audience) claim in signed tokens. The value of that claim specifies the intended audience(s) of the token (i.e. the service or services which are meant to accept the token). Argo CD does validate that the token was signed by Argo CD's configured OIDC provider. But Argo CD does not validate the audience claim, so it will accept tokens that are not intended for Argo CD.

## Impact

If Argo CD's configured OIDC provider also serves other audiences (for example, a file storage service), then Argo CD will accept a token intended for one of those other audiences. Argo CD will grant the user privileges based on the token's groups claim, even though those groups were not intended to be used by Argo CD.

This bug also increases the blast radius of a stolen token. If an attacker steals a valid token for a different audience, they can use it to access Argo CD.

## Attachments
No attachments
