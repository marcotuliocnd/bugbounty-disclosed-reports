# Brew bootstrap process is insecure

## Report Details
- **Report ID**: 1166535
- **URL**: https://hackerone.com/reports/1166535
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-04-16T15:03:16.577Z
- **Disclosed**: 2021-04-30T12:15:42.999Z

## Reporter
- **Username**: nightwatch-cybersecurity
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: homebrew

## Vulnerability Information
The process described in this page is not secure - no checksum / PGP signature is published and there is no way to check the download is
legit:
https://brew.sh/

"/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)""

This can lead to supply chain attacks such as the one that just happened here:
https://about.codecov.io/security-update/

This can lead to two possible attacks:
1. Supply chain attacks if the script is modified on the server.
2. Injection attacks if the TLS connections are compromised.

## Impact

For brew, a checksum and a way to check it should be provided, and security information should be added to the webpage referenced above. This way users can check the downloads.

## Attachments
No attachments
