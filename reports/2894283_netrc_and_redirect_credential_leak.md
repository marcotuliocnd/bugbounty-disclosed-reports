# netrc and redirect credential leak

## Report Details
- **Report ID**: 2894283
- **URL**: https://hackerone.com/reports/2894283
- **State**: Closed
- **Severity**: low
- **Submitted**: 2024-12-11T07:57:42.035Z
- **Disclosed**: 2025-01-15T12:17:39.258Z

## Reporter
- **Username**: nyymi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
When asked to both use a .netrc file for credentials and to follow HTTP redirects, curl could leak the password used for the first host to the followed-to host under certain circumstances.

This flaw only manifests itself if the netrc file has an entry that matches the redirect target hostname but the entry either omits just the password or omits both login and password.

## Impact

Information disclosure (password sent to the wrong host).

## Attachments
No attachments
