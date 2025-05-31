# Reflected XSS in ████████████

## Report Details
- **Report ID**: 1882592
- **URL**: https://hackerone.com/reports/1882592
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-02-22T07:35:42.177Z
- **Disclosed**: 2023-04-14T17:26:48.340Z

## Reporter
- **Username**: 0xd3adc0de
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Description:**
XSS vulnerability found on one of `███████` subdomains. [ DoD scope]

After analyzing `https://████████████/` (national levee database) I found  `auth/logout.jsx` page that have `home` parameter in `GET` request.  `home` parameter vulnerable to XSS vulnerability.


Payload:
`https://█████████████████/auth/logout.jsx?home=javascript:(alert(%27XSS%20Success!%27))()`
████████


## References
https://owasp.org/www-community/attacks/xss/

## Impact

By exploiting this vulnerability an attacker can trick the users to execute XSS and steal user's cookies.
Launch advanced phishing attacks.
Execute browser-based attacks etc.

## System Host(s)
███████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
* Visit the following URL 
`https://████████████████/auth/logout.jsx?home=javascript:(alert(%27XSS%20Success!%27))()`

* click on `Click here to return to your application.`  and you will receive `XSS Success!` alert box.

## Suggested Mitigation/Remediation Actions




## Attachments
No attachments
