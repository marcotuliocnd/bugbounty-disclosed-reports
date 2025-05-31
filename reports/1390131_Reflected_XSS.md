# Reflected XSS

## Report Details
- **Report ID**: 1390131
- **URL**: https://hackerone.com/reports/1390131
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-11-02T22:49:12.055Z
- **Disclosed**: 2023-01-06T19:14:56.813Z

## Reporter
- **Username**: f6x
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Description:**
Hi i found a XSS at a new IP Address (ssl points to ███hostname)


https://███████/WebPuff5.4/Login?signIn=Sign%20In&password=g00dPa%24%24w0rD&url=login.jsp%27%22()%26%25%3Cacx%3E%3CScRiPt%20%3Ealert(9868)%3C/ScRiPt%3E&username=tMtFQiRt

## References
https://owasp.org/www-community/attacks/xss/

## Impact

With the help of xss a hacker or attacker can perform social engineering on users by redirecting them from real website to fake one. hacker can steal their cookies and download a malware on their system, and there are many more attacking scenarios a skilled attacker can perform with xss.

## System Host(s)
███████████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
click here and a alert will popup https://█████/WebPuff5.4/Login?signIn=Sign%20In&password=g00dPa%24%24w0rD&url=login.jsp%27%22()%26%25%3Cacx%3E%3CScRiPt%20%3Ealert(9868)%3C/ScRiPt%3E&username=tMtFQiRt

## Suggested Mitigation/Remediation Actions
Sanitize special character in the url



## Attachments
No attachments
