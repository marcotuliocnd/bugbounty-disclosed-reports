# Website vulnerable to POODLE (SSLv3) with expired certificate

## Report Details
- **Report ID**: 481632
- **URL**: https://hackerone.com/reports/481632
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-01-17T21:04:34.918Z
- **Disclosed**: 2021-04-02T18:53:00.392Z

## Reporter
- **Username**: fuomag9
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**
████████ uses insecure cipher suites (SSL V2 and SSL V3) which makes it vulnerable to many attacks, including POODLE. The ssl certificate has also expired 4 years ago.

##Impact

The POODLE attack can be used against any system or application that supports SSL 3.0 with CBC mode ciphers. This affects most current browsers and websites, but also includes any software that either references a vulnerable SSL/TLS library (e.g. OpenSSL) or implements the SSL/TLS protocol suite itself. By exploiting this vulnerability in a likely web-based scenario, an attacker can gain access to sensitive data passed within the encrypted web session, such as passwords, cookies and other authentication tokens that can then be used to gain more complete access to a website (impersonating that user, accessing database content, etc.).

## Suggested Mitigation/Remediation Actions

Disable SSL 2 and SSL 3, renew the certificate and disable weak cyphers like RC4 to further mitigate other issues.

**Sources:**
https://www.us-cert.gov/ncas/alerts/TA14-290A

## Impact

The POODLE attack can be used against any system or application that supports SSL 3.0 with CBC mode ciphers. This affects most current browsers and websites, but also includes any software that either references a vulnerable SSL/TLS library (e.g. OpenSSL) or implements the SSL/TLS protocol suite itself. By exploiting this vulnerability in a likely web-based scenario, an attacker can gain access to sensitive data passed within the encrypted web session, such as passwords, cookies and other authentication tokens that can then be used to gain more complete access to a website (impersonating that user, accessing database content, etc.).

**Example**:
 http://██████/███ would be vulnerable to this assuming the credentials were transmitted using HTTPS (which they aren't and this is a vulnerability itself).

## Attachments
No attachments
