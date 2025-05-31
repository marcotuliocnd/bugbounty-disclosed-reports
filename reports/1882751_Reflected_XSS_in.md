# Reflected XSS in ██████████

## Report Details
- **Report ID**: 1882751
- **URL**: https://hackerone.com/reports/1882751
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-02-22T12:11:01.978Z
- **Disclosed**: 2023-03-24T17:26:52.240Z

## Reporter
- **Username**: 0xd3adc0de
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Description:**
XSS vulnerability found on one of `██████████` subdomains. [ DoD scope]

After analyzing `https://████████████/` (███████) I found  `path/user/NextRequestAccount.action` page that have `militarybranch` parameter in `GET` request.  `militarybranch` parameter vulnerable to XSS vulnerability.


`https://█████████████/` requires a valid user to access the contents, but the registration page is accessible to all visitors without any restrictions or credentials.
████

User should select `Military Branch` in registration page and there is reflection point! 
Modifying `militarybranch` parameter in request and set payload on it, you'll receive `XSS Success!` alert box.

Payload:
`https://████████████/path/user/NextRequestAccount.action?militarybranch=███%3CHTMl%0Aonmouseover%0A=%0Aalert(%27XSSSuccess!%27)%0Dx//&firstName=0xd3adc0de&middleName=0xd3adc0de&lastName=0xd3adc0de&email=0xd3adc0de&title=0xd3adc0de&department=&organization=&ship=0xd3adc0de&orgid=&location=`
█████

## References
https://owasp.org/www-community/attacks/xss/

## Impact

By exploiting this vulnerability an attacker can trick the users to execute XSS and steal user's cookies.
Launch advanced phishing attacks.
Execute browser-based attacks etc.

## System Host(s)
████████████████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
* Visit the following URL 
`https://████████████/path/user/NextRequestAccount.action?militarybranch=████%3CHTMl%0Aonmouseover%0A=%0Aalert(%27XSSSuccess!%27)%0Dx//&firstName=0xd3adc0de&middleName=0xd3adc0de&lastName=0xd3adc0de&email=0xd3adc0de&title=0xd3adc0de&department=&organization=&ship=0xd3adc0de&orgid=&location=` you will receive `XSS Success!` alert box.

## Suggested Mitigation/Remediation Actions




## Attachments
No attachments
