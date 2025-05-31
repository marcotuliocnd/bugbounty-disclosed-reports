# DOMXSS in redirect param

## Report Details
- **Report ID**: 361287
- **URL**: https://hackerone.com/reports/361287
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-06-03T10:03:13.734Z
- **Disclosed**: 2019-03-20T12:34:50.453Z

## Reporter
- **Username**: flamezzz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: semmle

## Vulnerability Information
#Summary
The **redirect** param can consist of a ``javascript:`` url, which results in XSS. If a victim visits a malicious URL and logs in, the attacker can perform actions on behalf of the victim.

#Steps to reproduce
1) Logout
2) Visit `` https://lgtm-com.pentesting.semmle.net/?redirect=javascript:prompt(document.domain)%2f%2f
 ``
3) Log in through email

## Impact

If a victim visits a malicious URL and logs in, the attacker can perform actions on behalf of the victim.

## Attachments
No attachments
