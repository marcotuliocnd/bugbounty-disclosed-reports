# CURLOPT_SSH_HOST_PUBLIC_KEY_SHA256 comparison disaster

## Report Details
- **Report ID**: 1549435
- **URL**: https://hackerone.com/reports/1549435
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-04-24T16:02:36.368Z
- **Disclosed**: 2022-04-25T10:58:34.118Z

## Reporter
- **Username**: nyymi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: curl

## Vulnerability Information
## Summary:
`CURLOPT_SSH_HOST_PUBLIC_KEY_SHA256` base64 encoded host fingerprint is compared case-insensitive by accident. This means that it is technically possible (however still difficult) to create forged ssh host key that matches in this comparison.

The bug appears to have been introduced when adding `CURLOPT_SSH_HOST_PUBLIC_KEY_SHA256`  support, and then copying the case insensitive comparison of the string for` CURLOPT_SSH_HOST_PUBLIC_KEY_MD5` (where it is appropriate since the MD5 fingerprint is a hex string).

This bug as added by commit https://github.com/curl/curl/commit/d1e7d9197b7fe417fb4d62aad5ea8f15a06d906c

## Impact

Host identify spoofing

## Attachments
No attachments
