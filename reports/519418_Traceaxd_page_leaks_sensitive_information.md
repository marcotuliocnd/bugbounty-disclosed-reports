# Trace.axd page leaks sensitive information

## Report Details
- **Report ID**: 519418
- **URL**: https://hackerone.com/reports/519418
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2019-04-01T03:58:40.320Z
- **Disclosed**: 2019-08-19T12:21:03.090Z

## Reporter
- **Username**: arinerron2
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
## Summary

`Trace.axd` leaks sensitive information on `██████████` by allowing signed in users to view previous requests sent to the webserver.

## Impact

Information leaked includes (but is not limited to):
- full names
- email addresses
- social security numbers
- dates of birth
- plaintext passwords
- cookies, session tokens, and CSRF tokens
- IP addresses and headers
- application specific information (endpoints, files and directories on the filesystem, software versions, )

## Step-by-step Reproduction Instructions

1. Visit https://████████/Gateway/sso.aspx and sign in. Note that any user can create a user (and any privilege level works for this vulnerability as long as a user is signed in), so this should be considered an unauthenticated vulnerability.
2. Visit https://██████████/████/Trace.axd
3. Click on `View Details` for any request that seems interesting. You can find social security numbers by visiting any of the `/candidate_app/dspstatus.aspx` pages and then Ctrl+F'ing for `app_ssn`.

## Suggested Mitigation/Remediation Actions

Disable `Trace.axd`. https://docs.microsoft.com/en-us/previous-versions/dotnet/articles/ms972204(v=msdn.10)

## Impact

Any attacker can potentially access the following information of current or future Navy personnel:
- full names
- email addresses
- social security numbers
- dates of birth
- plaintext passwords
- cookies, session tokens, and CSRF tokens
- IP addresses and headers
- application specific information (endpoints, files and directories on the filesystem, software versions, )

## Attachments
No attachments
