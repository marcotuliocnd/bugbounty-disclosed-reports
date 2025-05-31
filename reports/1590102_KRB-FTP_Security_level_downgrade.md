# KRB-FTP: Security level downgrade

## Report Details
- **Report ID**: 1590102
- **URL**: https://hackerone.com/reports/1590102
- **State**: Closed
- **Severity**: none
- **Submitted**: 2022-06-02T20:58:34.518Z
- **Disclosed**: 2022-06-05T20:58:34.335Z

## Reporter
- **Username**: nyymi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: curl

## Vulnerability Information
## Summary:
libcurl doesn't fail the FTP connection if Kerberos authentication fails for some reason, but rather reverts back to using regular clear text password authentication.

The logic is in`lib/ftp.c` `ftp_statemachine`: https://github.com/curl/curl/blob/07a9b89fedaec60bdbc254f23f66149b31d2f8da/lib/ftp.c#L2706

This means that active attacker in a man in the middle position can downgrade any attempt to use Kerberos FTP to regular one by merely forcing the Kerberos authentication to fail.

The more secure course of action would be to fail the FTP connection if Kerberos authentication fails. If such change is not deemed necessary the current limitations should be documented.

## Steps To Reproduce:

  1. MitM the connection and make the kerberos authentication fail
  2. `curl --krb private ftp://victim.tld/`

## Impact

- Security level downgrade.

## Attachments
No attachments
