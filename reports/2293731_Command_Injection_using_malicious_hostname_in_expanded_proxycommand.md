# Command Injection using malicious hostname in expanded proxycommand

## Report Details
- **Report ID**: 2293731
- **URL**: https://hackerone.com/reports/2293731
- **State**: Closed
- **Severity**: low
- **Submitted**: 2023-12-20T22:05:47.557Z
- **Disclosed**: 2024-02-28T16:28:01.972Z

## Reporter
- **Username**: vx01
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Using the ProxyCommand or the ProxyJump feature enables users to exploit
unchecked hostname syntax on the client, which enables to inject malicious code
into the command of the above-mentioned features through the hostname parameter.

User interaction is required to exploit this issue.

Advisory from libssh: https://www.libssh.org/security/advisories/CVE-2023-6004.txt

Advisory from OpenSSH which also suffered from this flaw: https://www.openssh.com/txt/release-9.6

## Impact

Code execution via malicious input hostname or other tokens

## Attachments
No attachments
