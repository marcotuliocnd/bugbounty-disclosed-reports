# Blind Sql Injection in https://████

## Report Details
- **Report ID**: 2597543
- **URL**: https://hackerone.com/reports/2597543
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2024-07-11T16:44:20.127Z
- **Disclosed**: 2024-08-29T17:47:35.095Z

## Reporter
- **Username**: iamunixtz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Bug Bounty Report**

### Summary
A SQL injection vulnerability was discovered in the User-Agent parameter of the website `https://██████████/`. This vulnerability allows an attacker to inject SQL commands through the User-Agent HTTP header, potentially leading to unauthorized access to sensitive data stored in the backend database.

████

## Impact

- Successful exploitation of this vulnerability allows an attacker to execute arbitrary SQL commands on the backend database management system (MySQL >= 8.0.0, MariaDB fork).
   - Potential impact includes unauthorized access to sensitive data, manipulation of database content, and even complete compromise of the database server

## System Host(s)
███

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
1. **SQLMap Command**: 
   ```
   sqlmap --url "https://█████████/" --batch --random-agent --level 5 --risk 3
   ```

2. **Injection Point Identified**:
   ```
   Parameter: User-Agent (User-Agent)
       Type: boolean-based blind
       Title: OR boolean-based blind - WHERE or HAVING clause
       Payload: -5127 OR 2687=2687
   ```

## Suggested Mitigation/Remediation Actions
### Recommendations
- **Immediate Mitigation**: 
  - Implement input validation and parameterized queries to sanitize user inputs, especially HTTP headers like User-Agent.
  - Apply web application firewall (WAF) rules to detect and block SQL injection attempts.
  
- **Long-term Solutions**:
  - Regular security assessments and penetration testing to identify and remediate vulnerabilities.
  - Educate developers about secure coding practices, including input validation and output encoding.



## Attachments
No attachments
