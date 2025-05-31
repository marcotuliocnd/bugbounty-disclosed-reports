#  libssh backend CURLOPT_SSH_HOST_PUBLIC_KEY_SHA256 validation bypass

## Report Details
- **Report ID**: 1825377
- **URL**: https://hackerone.com/reports/1825377
- **State**: Closed
- **Severity**: low
- **Submitted**: 2023-01-07T01:05:51.590Z
- **Disclosed**: 2023-01-07T21:04:06.121Z

## Reporter
- **Username**: nyymi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: curl

## Vulnerability Information
## Summary:
If libcurl is built against libssh `CURLOPT_SSH_HOST_PUBLIC_KEY_SHA256` is quietly ignored. As a result a SSH connection will be established even if the SHA256 key set doesn't match.

## Steps To Reproduce:

  1. configure libcurl with libssh and build it
  2. `curl --hostpubsha256 HOSTFINGERPRINTHERE sftp://example.tld/`

Instead of  failing due to mismatching fingerprint the connection quietly continues.

While the `CURLOPT_SSH_HOST_PUBLIC_KEY_SHA256 ` documentation does mention that this option `Requires the libssh2 backend`, it is still wrong to quietly ignore the validation.

## Remediation

Change `lib/vssh/libssh.c` `myssh_is_known` to reject connection if `CURLOPT_SSH_HOST_PUBLIC_KEY_SHA256` is set, or implement sha256 fingerprint support for libssh.

## Impact

SSH host validation bypass.

## Attachments
No attachments
