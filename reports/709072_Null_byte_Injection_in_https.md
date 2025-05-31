# Null byte Injection in https://████/

## Report Details
- **Report ID**: 709072
- **URL**: https://hackerone.com/reports/709072
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-10-07T15:36:44.075Z
- **Disclosed**: 2020-05-14T17:17:48.736Z

## Reporter
- **Username**: mohammedadam24
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
#Description:
Microsoft .NET Framework is prone to multiple NULL-byte injection vulnerabilities because it fails to adequately sanitize user-supplied data.

#Vulnerable URL: https://████/%2F%20This%20website%20is%20vulnerable%20to%20NULL%20BYTE%20INJECTION/

#Steps to Reproduce:
1) An attacker can exploit this issue via a browser.

The following example URI request is available:
https://███████/%2F%20This%20website%20is%20vulnerable%20to%20NULL%20BYTE%20INJECTION%00

#Mitigation: https://www.securityfocus.com/bid/24791/solution

#See Also: https://www.exploit-db.com/exploits/30281

#Proof of Concept: Screenshots attached.

## Impact

An attacker can exploit these issues to access sensitive information that may aid in further attacks; other attacks are also possible.

## Attachments
No attachments
