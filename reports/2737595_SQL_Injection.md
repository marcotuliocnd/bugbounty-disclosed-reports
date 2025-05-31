# SQL Injection

## Report Details
- **Report ID**: 2737595
- **URL**: https://hackerone.com/reports/2737595
- **State**: Closed
- **Severity**: high
- **Submitted**: 2024-09-25T08:53:00.441Z
- **Disclosed**: 2024-10-25T15:27:56.819Z

## Reporter
- **Username**: k0x
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
I discovered a Blind SQL Injection vulnerability in the application, which allows an attacker to manipulate database queries by injecting malicious input into the vulnerable parameter. Unlike regular SQL injection, blind SQL injection does not directly return data but can be exploited through true/false or time-based responses, revealing the structure and content of the database.

## References

## Impact

Blind SQL injection can be leveraged to extract sensitive information, bypass authentication, or escalate privileges by manipulating the backend SQL queries. Since the injection is blind, an attacker can use time-based, boolean-based, or out-of-band techniques to extract the data.

## System Host(s)
██████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
Run SQLMap: Use the following SQLMap command to test for SQL injection by directly specifying the vulnerable URL and the parameter:

```bash
sqlmap -u "███████" \
--technique=BT --level=5 --risk=3 --threads=10 -p 'filter[event]' \
--dbms='MySQL' --batch --current-db --random-agent
```

**-u:** Specifies the target URL.
**--technique=BT:** Tells SQLMap to use both Boolean-based (B) and Time-based (T) blind SQL injection techniques.
**--level=5:** Sets the highest level of testing, increasing the depth of testing.
**--risk=3:** Specifies a higher risk level for potentially dangerous payloads.
**--threads=10:** Increases the number of concurrent requests, speeding up the process.
**-p 'filter[event]':** Specifies that the filter[event] parameter is the target for injection.
**--dbms='MySQL':** Indicates that the target database management system is MySQL.
**--batch:** Automatically answers all questions (non-interactive mode).
**--current-db:** Attempts to retrieve the current database name.
**--random-agent:** Randomizes the User-Agent header to evade detection.

████████

## Suggested Mitigation/Remediation Actions




## Attachments
No attachments
