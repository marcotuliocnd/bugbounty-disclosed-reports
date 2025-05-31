# 4 severe remote + several minor OpenVPN vulnerabilities

## Report Details
- **Report ID**: 242579
- **URL**: https://hackerone.com/reports/242579
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-06-23T10:58:19.459Z
- **Disclosed**: 2019-10-14T00:24:28.052Z

## Reporter
- **Username**: guido
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
CVE-2017-7521 Remote server crashes/double-free/memory leaks in certificate processing
CVE-2017-7520 Remote (including MITM) client crash, data leak
CVE-2017-7508 Remote server crash (forced assertion failure)
CVE-2017-7522 Crash mbed TLS/PolarSSL-based server
(no cve) Remote/mitm Null-pointer dereference in establish_http_proxy_passthru()
(no cve) Stack buffer overflow if long –tls-cipher is given
(no cve) Remote (including MITM) client stack buffer corruption

https://community.openvpn.net/openvpn/wiki/VulnerabilitiesFixedInOpenVPN243
https://guidovranken.wordpress.com/2017/06/21/the-openvpn-post-audit-bug-bonanza/

## Attachments
No attachments
