# libcurl: freeing stack buffer during x509 certificate parsing 

## Report Details
- **Report ID**: 2621057
- **URL**: https://hackerone.com/reports/2621057
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2024-07-24T07:11:10.367Z
- **Disclosed**: 2024-08-23T20:31:07.165Z

## Reporter
- **Username**: z2_
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Hello, I would like to report a vulnerability here, initially reported by me to the curl project.

HackerOne Report: https://hackerone.com/reports/2559516
CVE: CVE-2024-6197
Advisory: https://curl.se/docs/CVE-2024-6197.html
Severity: Medium

## Impact

By serving a specifically crafted TLS certificate, a malicious server can trigger a `free()` of a buffer located on the stack.
This can lead to a crash or to further memory corruptions.

## Attachments
No attachments
